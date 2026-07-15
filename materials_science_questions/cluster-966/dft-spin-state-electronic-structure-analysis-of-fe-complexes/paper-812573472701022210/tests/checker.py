import os
import json
import csv

# === author imports / helpers ===
import math, csv, json


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
    ctx = {}
    for step in spec['steps']:
        sid = step.get('id')
        if sid == 'soc_curve_b1':
            ctx['soc_check'] = step.get('params', {})
        elif sid == 'pop_evolution':
            ctx['pop_check'] = step.get('params', {})
    return ctx


# === block: score_0 (check id='soc_curve_b1') ===
def score_0(artifact, step, ctx):
    params = ctx.get('soc_check', {})
    points = params.get('check_points', [])
    z_max = params.get('z1_max_allowed', 30.0)
    R_col = 'R'
    b1_col = 'b1'
    z_cols = ['z1_real', 'z1_imag', 'z1_star_real', 'z1_star_imag']
    rows = artifact
    data_R = []
    data_b1 = []
    max_z = 0.0
    for row in rows:
        try:
            r = float(row[R_col])
            b = float(row[b1_col])
            data_R.append(r)
            data_b1.append(b)
            for zc in z_cols:
                zv = abs(float(row.get(zc, 0)))
                if zv > max_z:
                    max_z = zv
        except (ValueError, TypeError, KeyError):
            continue
    if not data_R:
        return 0.0
    passed = 0
    total = len(points)
    for pt in points:
        target_R = pt['R']
        target_val = pt['target']
        tol = pt['tol']
        # find nearest R
        idx = min(range(len(data_R)), key=lambda i: abs(data_R[i] - target_R))
        if abs(data_b1[idx] - target_val) <= tol:
            passed += 1
    z_pass = 1.0 if max_z <= z_max else 0.0
    score = (passed + z_pass) / (total + 1)
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='pop_evolution') ===
def score_1(artifact, step, ctx):
    params = ctx.get('pop_check', {})
    rows = artifact
    time_col = 'time_ps'
    sing_col = 'pop_singlet'
    trip_col = 'pop_triplet_total'
    quint_col = 'pop_quintet_total'
    sept_col = 'pop_septet_total'
    times = []
    sings = []
    quints = []
    septs = []
    for row in rows:
        try:
            t = float(row[time_col])
            s = float(row[sing_col])
            q = float(row[quint_col])
            sp = float(row[sept_col])
            times.append(t)
            sings.append(s)
            quints.append(q)
            septs.append(sp)
        except (ValueError, TypeError, KeyError):
            continue
    if not times:
        return 0.0
    peak_idx = max(range(len(sings)), key=lambda i: sings[i])
    peak_time = times[peak_idx]
    peak_val = sings[peak_idx]

    peak_time_ok = 1.0 if params['peak_time_min'] <= peak_time <= params['peak_time_max'] else 0.0
    peak_val_ok = 1.0 if params['peak_value_min'] <= peak_val <= params['peak_value_max'] else 0.0

    quint_ok = 1.0
    for q in quints:
        if q < params['quintet_low'] or q > params['quintet_high']:
            quint_ok = 0.0
            break

    sept_ok = 1.0
    for s in septs:
        if s < params['septet_low'] or s > params['septet_high']:
            sept_ok = 0.0
            break

    score = (peak_time_ok + peak_val_ok + quint_ok + sept_ok) / 4.0
    return score


_SCORERS = {
    'soc_curve_b1': score_0,
    'pop_evolution': score_1,
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
