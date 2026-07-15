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


# === block: score_0 (check id='step_01_ds_values') ===
def score_0(artifact, step, ctx):
    import csv, math

    target = step['target']
    tol = step['tolerance']
    scoring = step.get('scoring', {'D_c_Ds_weight':0.8, 'D_s_weight':0.2})

    # artifact is list of dicts (CSV rows)
    rows = artifact
    temps = {}
    for row in rows:
        t_val = row.get('temperature')
        if t_val is not None:
            try:
                t = float(str(t_val).strip())
                temps[t] = row
            except:
                pass

    if 85.0 not in temps or 100.0 not in temps:
        return 0.0

    row85 = temps[85.0]
    row100 = temps[100.0]

    def score_value(val, ref, rel_tol):
        if val is None or val == '':
            return 0.0
        try:
            v = float(val)
        except:
            return 0.0
        if ref == 0:
            return 1.0 if v == 0 else 0.0
        rel_err = abs(v - ref) / abs(ref)
        if rel_err <= rel_tol:
            return 1.0
        decay = 0.5
        return max(0.0, 1.0 - (rel_err - rel_tol) / decay)

    # D_c/D_s scores
    Dc85 = score_value(row85.get('D_c_Ds_char_func'), target['85K']['D_c_Ds_char_func'], tol['D_c_Ds_relative'])
    Dc100 = score_value(row100.get('D_c_Ds_char_func'), target['100K']['D_c_Ds_char_func'], tol['D_c_Ds_relative'])
    dc_score = (Dc85 + Dc100) / 2

    # D_s sanity score (average over both columns for both temperatures)
    ds_score = 0.0
    count = 0
    for row in [row85, row100]:
        temp_key = f"{int(float(row['temperature']))}K"
        ref = target[temp_key]['D_s_ref']
        for col in ['D_s_VACF','D_s_MSD']:
            if col in row:
                ds_score += score_value(row.get(col), ref, tol['D_s_relative'])
                count += 1
    if count > 0:
        ds_score = ds_score / count
    else:
        ds_score = 0.0

    weighted = scoring['D_c_Ds_weight'] * dc_score + scoring['D_s_weight'] * ds_score
    return max(0.0, min(1.0, weighted))


# === block: score_1 (check id='step_02_spinodal_binodal') ===
def score_1(artifact, step, ctx):
    import math

    text = artifact.strip()
    lines = text.splitlines()
    if len(lines) < 2:
        return 0.0

    try:
        Ts = float(lines[0].strip())
        Tb = float(lines[1].strip())
    except:
        return 0.0

    ref = step['target']
    abs_tol = step['tolerance']['abs']
    decay = step['scoring']['decay_range']

    def score_temp(val, ref_val):
        diff = abs(val - ref_val)
        if diff <= abs_tol:
            return 1.0
        return max(0.0, 1.0 - (diff - abs_tol) / decay)

    s_s = score_temp(Ts, ref['T_s'])
    s_b = score_temp(Tb, ref['T_b'])
    return (s_s + s_b) / 2


_SCORERS = {
    'step_01_ds_values': score_0,
    'step_02_spinodal_binodal': score_1,
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
