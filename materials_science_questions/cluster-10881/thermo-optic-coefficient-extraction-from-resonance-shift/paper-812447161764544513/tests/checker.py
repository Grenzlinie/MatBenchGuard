import os
import json
import csv

# === author imports / helpers ===
import json
import os
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
    outputs_dir = '/app/outputs'
    ctx = {}
    fitted_path = os.path.join(outputs_dir, 'fitted_angles.json')
    if os.path.exists(fitted_path):
        with open(fitted_path) as f:
            ctx['fitted'] = json.load(f)
    acc_path = os.path.join(outputs_dir, 'acceptance_ratio.json')
    if os.path.exists(acc_path):
        with open(acc_path) as f:
            ctx['acceptance'] = json.load(f)
    lin_path = os.path.join(outputs_dir, 'linear_regression_slope.json')
    if os.path.exists(lin_path):
        with open(lin_path) as f:
            ctx['linreg'] = json.load(f)
    return ctx


# === block: score_0 (check id='s2') ===
def score_0(artifact, step, ctx):
    artifact = artifact
    ref_angles = step.get('reference_angles_rad')
    tol = step.get('tolerance_rad', 5e-5)
    if not isinstance(artifact, dict) or 'D_rad' not in artifact:
        return 0.0
    D = artifact['D_rad']
    if not isinstance(D, list) or len(D) != len(ref_angles):
        return 0.0
    for a, ref in zip(D, ref_angles):
        if abs(a - ref) > tol:
            return 0.0
    return 1.0


# === block: score_1 (check id='s3') ===
def score_1(artifact, step, ctx):
    fitted = ctx.get('fitted')
    if fitted is None or 'T_C' not in fitted or 'D_rad' not in fitted:
        return 0.0
    T = fitted['T_C']
    D = fitted['D_rad']
    if not (isinstance(T, list) and isinstance(D, list)) or len(T) != len(D) or len(T) < 2:
        return 0.0
    n = len(T)
    sum_t = sum(T)
    sum_d = sum(D)
    sum_td = sum(t*d for t,d in zip(T,D))
    sum_t2 = sum(t*t for t in T)
    denom = n*sum_t2 - sum_t*sum_t
    if denom == 0:
        return 0.0
    slope = (n*sum_td - sum_t*sum_d) / denom
    target = step.get('target_slope_rad_per_C', 2.60e-5)
    tol = step.get('slope_tolerance_abs', 2e-6)
    return 1.0 if abs(slope - target) <= tol else 0.0


# === block: score_2 (check id='s6') ===
def score_2(artifact, step, ctx):
    acc = ctx.get('acceptance')
    if acc is None or 'Delta_theta_L_mrad_cm' not in acc or 'Delta_T_L_C_cm' not in acc:
        return 0.0
    dthL = acc['Delta_theta_L_mrad_cm']
    dTL = acc['Delta_T_L_C_cm']
    if not isinstance(dthL, (int, float)) or not isinstance(dTL, (int, float)) or dTL == 0:
        return 0.0
    ratio = (dthL / dTL) * 1e-3
    # compare ratio to paper
    ratio_target = step.get('target_ratio_rad_per_C', 2.46e-5)
    ratio_tol = step.get('ratio_tolerance_abs', 1.5e-6)
    ratio_score = 1.0 if abs(ratio - ratio_target) <= ratio_tol else 0.0
    # recompute slope for consistency check
    fitted = ctx.get('fitted')
    slope = None
    if fitted and 'T_C' in fitted and 'D_rad' in fitted:
        T = fitted['T_C']
        D = fitted['D_rad']
        if isinstance(T, list) and isinstance(D, list) and len(T) == len(D) and len(T) >= 2:
            n = len(T)
            sum_t = sum(T)
            sum_d = sum(D)
            sum_td = sum(t*d for t,d in zip(T,D))
            sum_t2 = sum(t*t for t in T)
            denom = n*sum_t2 - sum_t*sum_t
            if denom != 0:
                slope = (n*sum_td - sum_t*sum_d) / denom
    consistency_score = 0.0
    if slope is not None and ratio != 0:
        rel_diff = abs(slope - ratio) / abs(ratio)
        max_rel = step.get('max_relative_diff_slope_ratio', 0.06)
        consistency_score = 1.0 if rel_diff <= max_rel else 0.0
    # weight sub-components: 0.7 ratio match, 0.3 consistency
    return 0.7 * ratio_score + 0.3 * consistency_score


_SCORERS = {
    's2': score_0,
    's3': score_1,
    's6': score_2,
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
