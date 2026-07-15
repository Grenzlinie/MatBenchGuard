import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='zero_sound_spinodal') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # dict
    checks = step.get('checks', {})
    scores = []
    for field, params in checks.items():
        val = artifact.get(field)
        if val is None:
            scores.append(0.0)
            continue
        target = params['target']
        tol = params.get('tol', 0)
        error = abs(val - target)
        if error <= tol:
            scores.append(1.0)
        else:
            excess = error - tol
            if target == 0.0:
                # for c1: if not near zero, zero credit
                scores.append(0.0)
            else:
                # decay with a range of 50.0 beyond tolerance
                score = max(0.0, 1.0 - excess / 50.0)
                scores.append(score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='critical_radius_scaling') ===
def score_1(artifact, step, ctx):
    rows = artifact  # list of dicts
    pc = step['config']['pressure_column']
    rc_col = step['config']['radius_column']
    dp_target = step['config']['target_dp']
    rc_target = step['config']['target_rc']
    rc_tol = step['config']['rc_tol']
    exp_target = step['config']['exponent_target']
    exp_tol = step['config']['exponent_tol']
    max_rc_dev = step['config']['max_rc_deviation']

    # Find row with pressure_offset close to dp_target
    point_row = None
    for r in rows:
        try:
            dp_val = float(r[pc])
        except (ValueError, KeyError):
            continue
        if abs(dp_val - dp_target) < 1e-6:
            point_row = r
            break
    if point_row is None:
        return 0.0

    # Point check
    try:
        rc_val = float(point_row[rc_col])
    except (ValueError, KeyError):
        return 0.0
    error_rc = abs(rc_val - rc_target)
    if error_rc <= rc_tol:
        point_score = 1.0
    else:
        excess = error_rc - rc_tol
        decay_range = max_rc_dev - rc_tol
        point_score = max(0.0, 1.0 - excess / decay_range) if decay_range > 0 else 0.0

    # Power-law fit (log-log linear regression)
    dps = []
    rcs = []
    for r in rows:
        try:
            d = float(r[pc])
            rv = float(r[rc_col])
            if d <= 0 or rv <= 0:
                continue
            dps.append(math.log(d))
            rcs.append(math.log(rv))
        except (ValueError, KeyError):
            continue
    n = len(dps)
    if n < 2:
        return 0.0
    sum_lx = sum(dps)
    sum_ly = sum(rcs)
    sum_lx2 = sum(x*x for x in dps)
    sum_lxly = sum(dps[i] * rcs[i] for i in range(n))
    denom = n * sum_lx2 - sum_lx * sum_lx
    if abs(denom) < 1e-12:
        return 0.0
    b = (n * sum_lxly - sum_lx * sum_ly) / denom
    error_exp = abs(b - exp_target)
    if error_exp <= exp_tol:
        exp_score = 1.0
    else:
        excess_exp = error_exp - exp_tol
        exp_score = max(0.0, 1.0 - excess_exp / 0.2)  # decay range 0.2

    return (point_score + exp_score) / 2.0


_SCORERS = {
    'zero_sound_spinodal': score_0,
    'critical_radius_scaling': score_1,
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
