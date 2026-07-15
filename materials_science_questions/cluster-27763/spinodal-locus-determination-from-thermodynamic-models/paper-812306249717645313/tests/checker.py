import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict

def _compute_slope_score(artifact, predicted, tol, qcol):
    rows = [r for r in artifact if r.get('Delta_H') and r.get(qcol) and float(r['Delta_H'])>0 and float(r[qcol])>0]
    if not rows:
        return 0.0
    groups = defaultdict(list)
    for r in rows:
        R_val = int(r['R'])
        groups[R_val].append((float(r['Delta_H']), float(r[qcol])))
    slopes = {}
    for R_val, pts in groups.items():
        if len(pts) < 3:
            continue
        xs = [math.log10(p[0]) for p in pts]
        ys = [math.log10(p[1]) for p in pts]
        n = len(xs)
        sumx = sum(xs)
        sumy = sum(ys)
        sumx2 = sum(xi * xi for xi in xs)
        sumxy = sum(xi * yi for xi, yi in zip(xs, ys))
        denom = n * sumx2 - sumx * sumx
        if denom == 0.0:
            continue
        slopes[R_val] = (n * sumxy - sumx * sumy) / denom
    if not slopes:
        return 0.0
    errors = {R_val: abs(slopes[R_val] - predicted) for R_val in slopes}
    r25 = 25
    if r25 in errors:
        err25 = errors[r25]
        if err25 <= tol:
            r25_score = 1.0
        elif err25 <= 2*tol:
            r25_score = 0.5
        else:
            r25_score = 0.0
    else:
        r25_score = 0.0
    rsorted = sorted(slopes.keys())
    errors_list = [errors[r] for r in rsorted]
    monotonic = all(errors_list[i] >= errors_list[i+1] for i in range(len(errors_list)-1))
    if monotonic:
        conv_score = 1.0
    elif rsorted and rsorted[0] in errors and rsorted[-1] in errors and errors[rsorted[-1]] < errors[rsorted[0]]:
        conv_score = 0.5
    else:
        conv_score = 0.0
    return 0.5 * r25_score + 0.5 * conv_score


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


# === block: score_0 (check id='chi_qs_slope') ===
def score_0(artifact, step, ctx):
    import math
    from collections import defaultdict

    # Return 0 if artifact is missing or unusable
    if not artifact:
        return 0.0

    # Filter valid rows
    rows = [r for r in artifact if r.get('Delta_H') and r.get('chi_qs') and float(r['Delta_H']) > 0 and float(r['chi_qs']) > 0]
    if not rows:
        return 0.0

    # Group by R
    groups = defaultdict(list)
    for r in rows:
        R_val = int(r['R'])
        groups[R_val].append((float(r['Delta_H']), float(r['chi_qs'])))

    # Compute per-R slopes with pure Python linear regression on log10 values
    slopes = {}
    for R_val, pts in groups.items():
        if len(pts) < 3:
            continue
        xs = [math.log10(p[0]) for p in pts]
        ys = [math.log10(p[1]) for p in pts]
        n = len(xs)
        sumx = sum(xs)
        sumy = sum(ys)
        sumx2 = sum(xi * xi for xi in xs)
        sumxy = sum(xi * yi for xi, yi in zip(xs, ys))
        denom = n * sumx2 - sumx * sumx
        if denom == 0.0:
            continue
        slopes[R_val] = (n * sumxy - sumx * sumy) / denom

    if not slopes:
        return 0.0

    # Predicted slope and tolerance from step config
    predicted = step['predicted_slope']
    tol = step['tolerance_abs']

    # Errors per R
    errors = {R_val: abs(slopes[R_val] - predicted) for R_val in slopes}

    # Score for R=25 within tolerance window
    r25 = 25
    if r25 in errors:
        err25 = errors[r25]
        if err25 <= tol:
            r25_score = 1.0
        elif err25 <= 2 * tol:
            r25_score = 0.5
        else:
            r25_score = 0.0
    else:
        r25_score = 0.0

    # Monotonic convergence: errors should decrease as R increases
    rsorted = sorted(slopes.keys())
    errors_list = [errors[r] for r in rsorted]
    monotonic = all(errors_list[i] >= errors_list[i+1] for i in range(len(errors_list)-1))
    if monotonic:
        conv_score = 1.0
    elif rsorted and rsorted[0] in errors and rsorted[-1] in errors and errors[rsorted[-1]] < errors[rsorted[0]]:
        conv_score = 0.5
    else:
        conv_score = 0.0

    # Combined score (equal weight)
    return 0.5 * r25_score + 0.5 * conv_score


# === block: score_1 (check id='mean_cluster_size_slope') ===
def score_1(artifact, step, ctx):
    return _compute_slope_score(artifact, step['predicted_slope'], step['tolerance_abs'], 'mean_cluster_size')


# === block: score_2 (check id='droplet_radius_slope') ===
def score_2(artifact, step, ctx):
    return _compute_slope_score(artifact, step['predicted_slope'], step['tolerance_abs'], 'radius_of_gyration_over_R')


# === block: score_3 (check id='droplet_mass_slope') ===
def score_3(artifact, step, ctx):
    return _compute_slope_score(artifact, step['predicted_slope'], step['tolerance_abs'], 'mass')


_SCORERS = {
    'chi_qs_slope': score_0,
    'mean_cluster_size_slope': score_1,
    'droplet_radius_slope': score_2,
    'droplet_mass_slope': score_3,
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
