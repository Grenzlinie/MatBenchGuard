import os
import json
import csv

# === author imports / helpers ===
import json
import math
import os


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
    spec = json.load(open('/tests/grading_spec.json'))
    steps = spec.get('steps', spec.get('checks', []))
    ctx = {}
    for s in steps:
        sid = s['id']
        if sid == 'ef_sweep':
            ctx['ef_gold'] = s['gold_points']
            ctx['ef_tol'] = s['tolerance_rel']
        elif sid == 'u_sweep':
            ctx['u_gold'] = s['gold_points']
            ctx['u_tol'] = s['tolerance_rel']
        elif sid == 'ef_curve':
            ctx['ef_ref_csv'] = s['reference_csv']
            ctx['ef_ref_param_name'] = s['ref_param_name']
            ctx['ef_ref_param_value'] = s['ref_param_value']
            ctx['ef_curve_tol'] = s['tolerance_rel']
        elif sid == 'u_curve':
            ctx['u_ref_csv'] = s['reference_csv']
            ctx['u_ref_param_name'] = s['ref_param_name']
            ctx['u_ref_param_value'] = s['ref_param_value']
            ctx['u_curve_tol'] = s['tolerance_rel']
    return ctx


# === block: score_0 (check id='ef_curve') ===
def score_0(artifact, step, ctx):
    artifact = json.load(open(os.path.join('/app/outputs', 'transmittance_curve_ef.json')))
    time = artifact['time']
    trans = artifact['transmittance']
    if len(time) < 3 or len(trans) != len(time):
        return 0.0
    final_t = trans[-1]
    t10 = 0.1 * final_t
    t90 = 0.9 * final_t
    t_10_idx = next(i for i, v in enumerate(trans) if v >= t10)
    t_90_idx = next(i for i, v in enumerate(trans) if v >= t90)
    if t_90_idx <= t_10_idx:
        return 0.0
    rt_recomputed = (time[t_90_idx] - time[t_10_idx]) * 1000  # to ms
    # read CSV
    csv_path = os.path.join('/app/outputs', ctx['ef_ref_csv'])
    rows = []
    with open(csv_path, newline='') as f:
        import csv
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    
    if not rows:
        return 0.0
    # find matching row
    target_ef = ctx['ef_ref_param_value']
    target_name = ctx['ef_ref_param_name']
    row = None
    for r in rows:
        val = float(r[target_name])
        if abs(val - target_ef) <= 1e-13:
            row = r
            break
    if row is None:
        return 0.0
    csv_rt = float(row['response_time (ms)'])
    rel_err = abs(rt_recomputed - csv_rt) / max(1e-6, csv_rt)
    tol = ctx['ef_curve_tol']
    if rel_err <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (rel_err - tol) / (5 * tol))


# === block: score_1 (check id='u_curve') ===
def score_1(artifact, step, ctx):
    artifact = json.load(open(os.path.join('/app/outputs', 'transmittance_curve_u.json')))
    time = artifact['time']
    trans = artifact['transmittance']
    if len(time) < 3 or len(trans) != len(time):
        return 0.0
    final_t = trans[-1]
    t10 = 0.1 * final_t
    t90 = 0.9 * final_t
    t_10_idx = next(i for i, v in enumerate(trans) if v >= t10)
    t_90_idx = next(i for i, v in enumerate(trans) if v >= t90)
    if t_90_idx <= t_10_idx:
        return 0.0
    rt_recomputed = (time[t_90_idx] - time[t_10_idx]) * 1000
    csv_path = os.path.join('/app/outputs', ctx['u_ref_csv'])
    rows = []
    with open(csv_path, newline='') as f:
        import csv
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    if not rows:
        return 0.0
    target_u = ctx['u_ref_param_value']
    target_name = ctx['u_ref_param_name']
    row = None
    for r in rows:
        val = float(r[target_name])
        if abs(val - target_u) <= 1e-6:
            row = r
            break
    if row is None:
        return 0.0
    csv_rt = float(row['response_time (ms)'])
    rel_err = abs(rt_recomputed - csv_rt) / max(1e-6, csv_rt)
    tol = ctx['u_curve_tol']
    if rel_err <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (rel_err - tol) / (5 * tol))


# === block: score_2 (check id='ef_sweep') ===
def score_2(artifact, step, ctx):
    import csv
    import os
    csv_path = os.path.join('/app/outputs', 'response_time_ef.csv')
    if not os.path.exists(csv_path):
        return 0.0
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        return 0.0
    golds = ctx['ef_gold']
    tol = ctx['ef_tol']
    passed = 0
    for g in golds:
        target_ef = g['ef']
        target_rt = g['response_time_ms']
        found = False
        for r in rows:
            ef_val = float(r['ef (C/m)'])
            if abs(ef_val - target_ef) <= 1e-13:
                rt_val = float(r['response_time (ms)'])
                if rt_val <= 0:
                    break
                rel_err = abs(rt_val - target_rt) / max(1e-6, target_rt)
                if rel_err <= tol:
                    found = True
                break
        if found:
            passed += 1
    return passed / len(golds) if golds else 0.0


# === block: score_3 (check id='u_sweep') ===
def score_3(artifact, step, ctx):
    import csv
    import os
    csv_path = os.path.join('/app/outputs', 'response_time_u.csv')
    if not os.path.exists(csv_path):
        return 0.0
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        return 0.0
    golds = ctx['u_gold']
    tol = ctx['u_tol']
    passed = 0
    for g in golds:
        target_u = g['u']
        target_rt = g['response_time_ms']
        found = False
        for r in rows:
            u_val = float(r['u'])
            if abs(u_val - target_u) <= 1e-6:
                rt_val = float(r['response_time (ms)'])
                if rt_val <= 0:
                    break
                rel_err = abs(rt_val - target_rt) / max(1e-6, target_rt)
                if rel_err <= tol:
                    found = True
                break
        if found:
            passed += 1
    return passed / len(golds) if golds else 0.0


_SCORERS = {
    'ef_curve': score_0,
    'u_curve': score_1,
    'ef_sweep': score_2,
    'u_sweep': score_3,
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
