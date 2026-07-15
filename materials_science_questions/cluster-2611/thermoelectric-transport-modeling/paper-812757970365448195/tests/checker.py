import os
import json
import csv


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
    return {}


# === block: score_0 (check id='sigma_monotonic') ===
def score_0(artifact, step, ctx):
    rows = artifact

    def check_monotonic(phase):
        phase_rows = [r for r in rows if r.get('phase','') == phase]
        if len(phase_rows) < 2:
            return 0.0
        phase_rows.sort(key=lambda r: float(r['carrier_concentration']))
        sigmas = [float(r['electrical_conductivity']) for r in phase_rows]
        for i in range(1, len(sigmas)):
            if sigmas[i] < sigmas[i-1] - 1e-12:
                return 0.0
        return 1.0

    score_w = check_monotonic('W')
    score_h = check_monotonic('H')
    return (score_w + score_h) / 2.0


# === block: score_1 (check id='sigma_ordering') ===
def score_1(artifact, step, ctx):
    rows = artifact
    w_map = {}
    h_map = {}
    for r in rows:
        phase = r.get('phase','')
        n = float(r['carrier_concentration'])
        sigma = float(r['electrical_conductivity'])
        if phase == 'W':
            w_map[n] = sigma
        elif phase == 'H':
            h_map[n] = sigma
    if not w_map:
        return 0.0
    for n, sigma_w in w_map.items():
        candidates = [(abs(nh - n), nh, sigma_h) for nh, sigma_h in h_map.items()]
        if not candidates:
            return 0.0
        diff, nh, sigma_h = min(candidates, key=lambda x: x[0])
        if diff / max(1.0, n) > 0.01:
            return 0.0
        if sigma_h <= sigma_w:
            return 0.0
    return 1.0


# === block: score_2 (check id='pf_ordering') ===
def score_2(artifact, step, ctx):
    rows = artifact
    w_pf = {}
    h_pf = {}
    for r in rows:
        phase = r.get('phase','')
        n = float(r['carrier_concentration'])
        pf = float(r['power_factor'])
        if phase == 'W':
            w_pf[n] = pf
        elif phase == 'H':
            h_pf[n] = pf
    if not w_pf:
        return 0.0
    count = 0
    total = len(w_pf)
    for n, pf_w in w_pf.items():
        candidates = [(abs(nh - n), nh, pf_h) for nh, pf_h in h_pf.items()]
        if not candidates:
            continue
        diff, nh, pf_h = min(candidates, key=lambda x: x[0])
        if diff / max(1.0, n) > 0.01:
            continue
        if pf_h > pf_w:
            count += 1
    fraction = count / total
    if fraction >= 0.8:
        return 1.0
    return fraction / 0.8


# === block: score_3 (check id='zt_ordering') ===
def score_3(artifact, step, ctx):
    rows = artifact
    cutoff = 1.5e19
    w_zt = {}
    h_zt = {}
    for r in rows:
        n = float(r['carrier_concentration'])
        if n > cutoff + 1e-12:
            continue
        phase = r.get('phase','')
        zt = float(r['ZT'])
        if phase == 'W':
            w_zt[n] = zt
        elif phase == 'H':
            h_zt[n] = zt
    if not w_zt:
        return 0.0
    for n, zt_w in w_zt.items():
        candidates = [(abs(nh - n), nh, zt_h) for nh, zt_h in h_zt.items() if nh <= cutoff + 1e-12]
        if not candidates:
            return 0.0
        diff, nh, zt_h = min(candidates, key=lambda x: x[0])
        if diff / max(1.0, n) > 0.01:
            return 0.0
        if zt_h <= zt_w:
            return 0.0
    return 1.0


# === block: score_4 (check id='zt_temp_ordering') ===
def score_4(artifact, step, ctx):
    rows = artifact
    for r in rows:
        if float(r.get('ZT_H', 0)) <= float(r.get('ZT_W', 0)):
            return 0.0
    return 1.0


# === block: score_5 (check id='ratio_temp_gt1') ===
def score_5(artifact, step, ctx):
    rows = artifact
    for r in rows:
        if float(r.get('ratio', 0)) <= 1.0:
            return 0.0
    return 1.0


# === block: score_6 (check id='ratio_inc') ===
def score_6(artifact, step, ctx):
    rows = artifact
    vals = {}
    for r in rows:
        T = int(float(r.get('temperature', 0)))
        ratio = float(r.get('ratio', 0))
        vals[T] = ratio
    if 300 not in vals or 1000 not in vals:
        return 0.0
    if vals[1000] > vals[300]:
        return 1.0
    return 0.0


_SCORERS = {
    'sigma_monotonic': score_0,
    'sigma_ordering': score_1,
    'pf_ordering': score_2,
    'zt_ordering': score_3,
    'zt_temp_ordering': score_4,
    'ratio_temp_gt1': score_5,
    'ratio_inc': score_6,
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
