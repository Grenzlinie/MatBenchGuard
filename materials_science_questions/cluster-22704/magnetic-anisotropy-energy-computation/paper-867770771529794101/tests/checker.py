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


# === block: score_0 (check id='mae_curve') ===
def score_0(artifact, step, ctx):
    import math

    # hidden gold values (derived from paper Fig. 4d and known MAE at half-filling)
    REF_SLOPE = 0.064          # meV per meV
    TOL_SLOPE = 0.0064         # ±10 %
    REF_INTERCEPT = 0.15       # meV
    TOL_INTERCEPT = 1.0        # meV
    REF_MAE_EPS4 = 6.9         # meV, at epsilon_d = -4 eV
    TOL_MAE_EPS4 = 0.5         # meV

    # --- helpers ---
    eps = 1e-12

    def lin_reg(xs, ys):
        """slope, intercept of y ~ x + const"""
        n = len(xs)
        if n < 2:
            return 0.0, 0.0
        mx = sum(xs) / n
        my = sum(ys) / n
        sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        sxx = sum((x - mx) ** 2 for x in xs)
        if sxx < eps:
            return 0.0, my
        slope = sxy / sxx
        intercept = my - slope * mx
        return slope, intercept

    def clamp_score(error, tol):
        return max(0.0, 1.0 - error / tol)

    # --- extract data ---
    rows = artifact  # list of dicts
    # collect (peak_position, MAE) for peak < 100 meV  and (epsilon_d, MAE)
    peak_vals = []
    mae_vals = []
    best_eps4_mae = None
    best_eps4_dist = float('inf')

    for row in rows:
        try:
            eps_d = float(row['epsilon_d'])
            pp = float(row['peak_position'])
            mae = float(row['MAE'])
        except Exception:
            continue

        # nearest to epsilon_d = -4.0 eV
        d = abs(eps_d - (-4.0))
        if d < best_eps4_dist:
            best_eps4_dist = d
            best_eps4_mae = mae

        # collect points for regression: peak > 0 and < 100 (strictly)
        if 0.0 < pp < 100.0:
            peak_vals.append(pp)
            mae_vals.append(mae)

    # --- score regression ---
    if len(peak_vals) < 2:
        slope_score = 0.0
        intercept_score = 0.0
    else:
        slope, intercept = lin_reg(peak_vals, mae_vals)
        slope_error = abs(slope - REF_SLOPE)
        intercept_error = abs(intercept - REF_INTERCEPT)
        slope_score = clamp_score(slope_error, TOL_SLOPE)
        intercept_score = clamp_score(intercept_error, TOL_INTERCEPT)

    # --- score MAE at epsilon_d = -4 eV ---
    if best_eps4_mae is None:
        eps4_score = 0.0
    else:
        eps4_error = abs(best_eps4_mae - REF_MAE_EPS4)
        eps4_score = clamp_score(eps4_error, TOL_MAE_EPS4)

    # equal weight to the three sub-checks
    score = (slope_score + intercept_score + eps4_score) / 3.0
    return score


# === block: score_1 (check id='occupancy_curve') ===
def score_1(artifact, step, ctx):
    import math
    refs = step['reference_points']
    tol = step.get('tolerance_abs', 0.1)
    data = {}
    for row in artifact:
        try:
            ed = float(row['epsilon_d'])
            nd = float(row['occupancy_Nd'])
            data[ed] = nd
        except:
            continue
    if not data:
        return 0.0
    ed_list = sorted(data.keys())
    scores = []
    for ref in refs:
        target_ed = ref['epsilon_d']
        ref_nd = ref['occupancy_Nd']
        best_ed = min(ed_list, key=lambda x: abs(x - target_ed))
        error = abs(data[best_ed] - ref_nd)
        point_score = max(0.0, 1.0 - error / tol)
        scores.append(point_score)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'mae_curve': score_0,
    'occupancy_curve': score_1,
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
