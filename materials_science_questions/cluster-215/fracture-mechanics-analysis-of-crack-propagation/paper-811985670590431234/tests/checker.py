import os
import json
import csv

# === author imports / helpers ===
import csv
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
    step = spec['steps'][0]
    return step.get('gold', {})


# === block: score_0 (check id='stress_curve_score') ===
def score_0(artifact, step, ctx):
    rows = list(csv.DictReader(open(os.path.join('/app/outputs', step.get('output_file', 'stress_curve.csv')).replace('\\', '/'), newline='', encoding='utf-8-sig')))
    if not rows or 'x_over_l' not in rows[0] or 'stress_normalized' not in rows[0]:
        return 0.0

    try:
        xs = [float(r['x_over_l']) for r in rows]
        ys = [float(r['stress_normalized']) for r in rows]
    except (ValueError, KeyError):
        return 0.0

    if len(rows) < 200:
        return 0.0
    x_min = min(xs)
    x_max = max(xs)
    if x_min > -2.0 or x_max < 2.0:
        return 0.0

    # sort by x (ensure monotonic for interpolation)
    _pairs = sorted(zip(xs, ys), key=lambda p: p[0])
    xs_sorted = [p[0] for p in _pairs]
    ys_sorted = [p[1] for p in _pairs]

    # ---- pure-python linear interpolation ----
    def _interp(x_target, x_vals, y_vals):
        if x_target <= x_vals[0]:
            return y_vals[0]
        if x_target >= x_vals[-1]:
            return y_vals[-1]
        for i in range(len(x_vals) - 1):
            if x_vals[i] <= x_target <= x_vals[i + 1]:
                x1, x2 = x_vals[i], x_vals[i + 1]
                y1, y2 = y_vals[i], y_vals[i + 1]
                if x2 == x1:
                    return (y1 + y2) / 2.0
                return y1 + (x_target - x1) * (y2 - y1) / (x2 - x1)
        # fallback (should not happen with sorted x)
        return y_vals[-1]

    tip_stress = _interp(1.0, xs_sorted, ys_sorted)

    # maximum stress and its location (pure python)
    max_idx = 0
    max_stress = ys_sorted[0]
    max_x = xs_sorted[0]
    for i, (x_val, y_val) in enumerate(zip(xs_sorted, ys_sorted)):
        if y_val > max_stress:
            max_stress = y_val
            max_x = x_val
            max_idx = i

    gold = ctx
    tol = float(gold.get('tolerance', 0.2))
    target_tip = float(gold.get('tip_stress', 0.6))
    target_max = float(gold.get('max_stress', 0.7))
    target_loc = float(gold.get('max_location', 1.2))

    err_tip = abs(tip_stress - target_tip)
    err_max = abs(max_stress - target_max)
    err_loc = abs(max_x - target_loc)

    score_tip = max(0.0, 1.0 - err_tip / tol)
    score_max = max(0.0, 1.0 - err_max / tol)
    score_loc = max(0.0, 1.0 - err_loc / tol)

    return round((score_tip + score_max + score_loc) / 3.0, 4)


_SCORERS = {
    'stress_curve_score': score_0,
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
