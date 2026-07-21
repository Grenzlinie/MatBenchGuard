import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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
    def find_peak(csv_path):
        max_rate = -float('inf')
        peak_T = None
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                T = float(row['temperature'])
                rate = float(row['desorption_rate'])
                if rate > max_rate:
                    max_rate = rate
                    peak_T = T
        return peak_T

    co_peak = find_peak(os.path.join(outputs_dir, 'tpd_co.csv'))
    ni_peak = find_peak(os.path.join(outputs_dir, 'tpd_ni.csv'))

    peak_json = None
    peak_json_path = os.path.join(outputs_dir, 'peak_temperatures.json')
    if os.path.exists(peak_json_path):
        with open(peak_json_path) as f:
            peak_json = json.load(f)

    return {'co_peak': co_peak, 'ni_peak': ni_peak, 'peak_json': peak_json}


# === block: score_0 (check id='recompute_co_peak') ===
def score_0(artifact, step, ctx):
    co = ctx.get('co_peak')
    if co is None: return 0.0
    target = step.get('target', 720.0)
    tol = step.get('tolerance', 30.0)
    err = abs(co - target)
    if err <= tol: return 1.0
    return max(0.0, 1.0 - (err - tol) / tol)


# === block: score_1 (check id='recompute_ni_peak') ===
def score_1(artifact, step, ctx):
    ni = ctx.get('ni_peak')
    if ni is None: return 0.0
    target = step.get('target', 640.0)
    tol = step.get('tolerance', 30.0)
    err = abs(ni - target)
    if err <= tol: return 1.0
    return max(0.0, 1.0 - (err - tol) / tol)


# === block: score_2 (check id='co_ni_order') ===
def score_2(artifact, step, ctx):
    co = ctx.get('co_peak')
    ni = ctx.get('ni_peak')
    if co is None or ni is None: return 0.0
    return 1.0 if co > ni else 0.0


# === block: score_3 (check id='site_analysis_co') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, dict): return 0.0
    required = ['fcc','hcp','step_110','step_100','edge']
    for site in required:
        if site not in artifact: return 0.0
        info = artifact[site]
        if not isinstance(info, dict): return 0.0
        occ = info.get('average_occupation')
        rate = info.get('average_association_rate')
        if not isinstance(occ, (int, float)) or not (0.0 <= occ <= 1.0): return 0.0
        if not isinstance(rate, (int, float)) or rate < 0.0: return 0.0
    return 1.0


# === block: score_4 (check id='site_analysis_ni') ===
def score_4(artifact, step, ctx):
    if not isinstance(artifact, dict): return 0.0
    required = ['fcc','hcp','step_110','step_100','edge']
    for site in required:
        if site not in artifact: return 0.0
        info = artifact[site]
        if not isinstance(info, dict): return 0.0
        occ = info.get('average_occupation')
        rate = info.get('average_association_rate')
        if not isinstance(occ, (int, float)) or not (0.0 <= occ <= 1.0): return 0.0
        if not isinstance(rate, (int, float)) or rate < 0.0: return 0.0
    return 1.0


# === block: score_5 (check id='peak_consistency') ===
def score_5(artifact, step, ctx):
    pj = ctx.get('peak_json')
    if not isinstance(pj, dict): return 0.0
    co_c = ctx.get('co_peak')
    ni_c = ctx.get('ni_peak')
    if co_c is None or ni_c is None: return 0.0
    co_j = pj.get('co_peak_T')
    ni_j = pj.get('ni_peak_T')
    if not isinstance(co_j, (int, float)) or not isinstance(ni_j, (int, float)): return 0.0
    tol = step.get('tolerance', 0.001)
    if abs(co_j - co_c) <= tol and abs(ni_j - ni_c) <= tol: return 1.0
    return 0.0


_SCORERS = {
    'recompute_co_peak': score_0,
    'recompute_ni_peak': score_1,
    'co_ni_order': score_2,
    'site_analysis_co': score_3,
    'site_analysis_ni': score_4,
    'peak_consistency': score_5,
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
