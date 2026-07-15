import os
import json
import csv

# === author imports / helpers ===
import csv, math


import os as _ff_os
import json as _ff_json


def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract']."""
    spec_path = "/tests/grading_spec.json"
    if not _ff_os.path.exists(spec_path):
        return []
    with open(spec_path) as _f:
        _spec = _ff_json.load(_f)
    contract = _spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = _ff_os.path.join(out_dir, base)
        if not _ff_os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        if fmt == "json":
            try:
                data = _ff_json.load(open(path))
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": invalid JSON (" + str(exc) + ")")
                continue
            required = schema.get("required", {})
            fields = required.keys() if isinstance(required, dict) else (required or [])
            if isinstance(data, dict):
                for field in fields:
                    if field not in data:
                        violations.append(base + ": missing JSON field '" + str(field) + "'")
        elif fmt in ("csv", "tsv"):
            import csv as _ff_csv
            delim = "\t" if fmt == "tsv" else ","
            try:
                with open(path, newline="") as _f:
                    cols = set((_ff_csv.reader(_f, delimiter=delim).__next__() or []))
            except StopIteration:
                cols = set()
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations


def _ff_contract_gate():
    """Zero the reward and exit if the submission violates the output_contract shape."""
    violations = _ff_validate_output_contract()
    if not violations:
        return
    _ff_os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        _ff_json.dump({"output_contract_violations": violations}, _f, indent=2)
    raise SystemExit(0)


def load_artifact(path):
    if not path or not os.path.exists(path):
        return None
    if path.endswith(".json"):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:  # noqa: BLE001
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    return {
        'delta72': 0.72, 'delta65': 0.65, 'delta57': 0.57,
        'topo_gold': {'0.72': 'CEP', '0.65': 'triple point + tricritical', '0.57': 'tricritical only'},
        'jump_threshold': 0.05,
        'peak_ranges': [(0.0, 0.2), (0.2, 0.5), (0.5, 0.8)]
    }


# === block: score_0 (check id='coex_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    by_delta = {}
    for r in rows:
        d = float(r['delta'])
        by_delta.setdefault(d, []).append(r)

    def check_delta72(rows):
        if not rows:
            return 0.0
        sorted_rows = sorted(rows, key=lambda x: float(x['temperature']))
        temps = [float(r['temperature']) for r in sorted_rows]
        rho_v = [float(r['rho_vapour']) for r in sorted_rows]
        rho_l = [float(r['rho_liquid']) for r in sorted_rows]
        # monotonicity
        inc_v = all(rho_v[i] <= rho_v[i+1] + 1e-6 for i in range(len(rho_v)-1))
        dec_l = all(rho_l[i] >= rho_l[i+1] - 1e-6 for i in range(len(rho_l)-1))
        mono_score = (0.5 if inc_v else 0.0) + (0.5 if dec_l else 0.0)
        # crossing with lambda line
        diffs = []
        for r in sorted_rows:
            lam_str = r.get('rho_lambda_line', '').strip()
            if lam_str:
                diffs.append(float(r['rho_liquid']) - float(lam_str))
        crossing = 0.0
        if diffs and max(diffs) > 0 and min(diffs) < 0:
            crossing = 1.0
        elif diffs and (max(diffs) <= 0 or min(diffs) >= 0):
            crossing = 0.3  # partial if no crossing but lambda exists
        return 0.5 * mono_score + 0.5 * crossing

    def check_delta65(rows):
        if not rows:
            return 0.0
        sorted_rows = sorted(rows, key=lambda x: float(x['temperature']))
        rho_l = [float(r['rho_liquid']) for r in sorted_rows]
        # jump indicating triple point
        jump_found = False
        for i in range(len(rho_l)-1):
            if abs(rho_l[i+1] - rho_l[i]) > 0.05:
                jump_found = True
                break
        jump_score = 1.0 if jump_found else 0.0
        # lambda line crossing
        diffs = []
        for r in sorted_rows:
            lam_str = r.get('rho_lambda_line', '').strip()
            if lam_str:
                diffs.append(float(r['rho_liquid']) - float(lam_str))
        crossing = 0.0
        if diffs and max(diffs) > 0 and min(diffs) < 0:
            crossing = 1.0
        elif diffs:
            crossing = 0.3
        return 0.6 * jump_score + 0.4 * crossing

    score72 = check_delta72(by_delta.get(0.72, []))
    score65 = check_delta65(by_delta.get(0.65, []))
    return 0.5 * score72 + 0.5 * score65


# === block: score_1 (check id='spinodal_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    delta = 0.57
    group = [r for r in rows if abs(float(r['delta']) - delta) < 1e-6]
    if not group:
        return 0.0
    num_valid = 0
    for r in group:
        try:
            s1 = float(r['S1'])
            s2 = float(r['S2'])
            s3 = float(r['S3'])
            hbl = float(r['hidden_binodal_rho_liquid'])
            hbv = float(r['hidden_binodal_rho_vapour'])
        except (ValueError, TypeError):
            continue
        if s1 < s2 < s3 and 0 <= s1 <= 1 and 0 <= s2 <= 1 and 0 <= s3 <= 1:
            if hbl > hbv and 0 <= hbv <= 1 and 0 <= hbl <= 1:
                num_valid += 1
    return min(1.0, num_valid / max(1, len(group)))


# === block: score_2 (check id='topology_check') ===
def score_2(artifact, step, ctx):
    expected = ctx['topo_gold']
    lines = [l.strip() for l in artifact.splitlines() if l.strip()]
    present = {}
    for line in lines:
        if line.startswith('δ=') or line.startswith('δ='):
            parts = line.split(':')
            if len(parts) == 2:
                key = parts[0].split('=')[1].strip()
                label = parts[1].strip()
                present[key] = label
    matched = 0
    for d, lab in expected.items():
        if d in present and present[d] == lab:
            matched += 1
    return matched / len(expected)


# === block: score_3 (check id='mc_dist_check') ===
def score_3(artifact, step, ctx):
    density = [float(r['density_bin']) for r in artifact]
    prob = [float(r['probability']) for r in artifact]
    n = len(density)
    if n < 3:
        return 0.0
    peaks = []
    for i in range(1, n-1):
        if prob[i] > prob[i-1] and prob[i] > prob[i+1] and prob[i] > 1e-4:
            peaks.append(density[i])
    found_in = 0
    ranges = ctx['peak_ranges']
    for (lo, hi) in ranges:
        for p in peaks:
            if lo <= p <= hi:
                found_in += 1
                break
    return found_in / 3.0


_SCORERS = {
    'coex_check': score_0,
    'spinodal_check': score_1,
    'topology_check': score_2,
    'mc_dist_check': score_3,
}


def _step_id(step, index):
    sid = str(step.get("id", "")).strip()
    if sid:
        return sid
    output = str(step.get("output_file", "")).split("/")[-1].rsplit(".", 1)[0]
    kind = str(step.get("kind") or step.get("metric") or "score").strip()
    base = "_".join(part for part in (output, kind) if part).strip("_")
    return base or ("check_" + str(index))


def main():
    _ff_contract_gate()
    with open("/tests/grading_spec.json") as f:
        spec = json.load(f)
    outputs_dir = "/app/outputs"
    ctx = prepare(outputs_dir, spec)
    steps = spec.get("steps", spec.get("checks", [])) or []
    breakdown = {}
    total = 0.0
    for index, step in enumerate(steps):
        sid = _step_id(step, index)
        output_file = str(step.get("output_file", "")).split("/")[-1]
        weight = float(step.get("weight", 0.0))
        artifact = load_artifact(os.path.join(outputs_dir, output_file)) if output_file else None
        fn = _SCORERS.get(sid)
        if fn is None:
            score = 0.0
        else:
            try:
                score = float(fn(artifact, step, ctx))
            except Exception as exc:  # noqa: BLE001
                score = 0.0
                breakdown.setdefault("_errors", {})[sid] = repr(exc)
        score = max(0.0, min(1.0, score))
        breakdown[sid or output_file] = {"score": score, "weight": weight}
        total += score * weight
    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(round(total, 6)))
    with open("/logs/verifier/breakdown.json", "w") as f:
        json.dump(breakdown, f, indent=2)


if __name__ == "__main__":
    main()
