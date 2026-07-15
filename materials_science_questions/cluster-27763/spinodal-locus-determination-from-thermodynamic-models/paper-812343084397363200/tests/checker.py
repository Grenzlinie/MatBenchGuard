import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.stats import pearsonr

def _find_row_by_field(rows, field, target, eps=1e-4):
    target = float(target)
    for row in rows:
        diff = abs(float(row[field]) - target)
        if diff < eps:
            return row
    return None

def _compute_max_slope_change(rows, h_col, val_col):
    """Return maximum absolute slope change between consecutive intervals."""
    arr = np.array([(float(r[h_col]), float(r[val_col])) for r in rows])
    arr = arr[arr[:,0].argsort()]
    if len(arr) < 3:
        return 0.0
    slopes = np.diff(arr[:,1]) / np.diff(arr[:,0])
    if len(slopes) < 2:
        return 0.0
    slope_changes = np.abs(np.diff(slopes))
    return float(np.max(slope_changes))


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


# === block: score_0 (check id='check_free_energy') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    r_xi_large = params['r_xi_large']
    r_xi_small = params['r_xi_small']
    jump_thresh = params['max_slope_change_jump_threshold']
    smooth_thresh = params['max_slope_change_smooth_threshold']
    min_pts = params.get('min_points_required', 10)

    rows_large = [r for r in artifact if abs(float(r['r_xi']) - r_xi_large) < 1e-6]
    rows_small = [r for r in artifact if abs(float(r['r_xi']) - r_xi_small) < 1e-6]

    score_large = 0.0
    score_small = 0.0

    if len(rows_large) >= min_pts:
        max_sc = _compute_max_slope_change(rows_large, 'h_xi', 'excess_free_energy')
        if max_sc > jump_thresh:
            score_large = 1.0

    if len(rows_small) >= min_pts:
        max_sc = _compute_max_slope_change(rows_small, 'h_xi', 'excess_free_energy')
        if max_sc < smooth_thresh:
            score_small = 1.0

    return 0.5 * score_large + 0.5 * score_small


# === block: score_1 (check id='check_binodal') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    ref_points = params['reference_points']
    tol_large = params['tolerance_large_r']
    tol_small = params['tolerance_small_r']
    small_thresh = params['small_r_threshold']
    eps = params.get('r_matching_eps', 1e-4)

    if not ref_points:
        return 0.0

    scores = []
    for pt in ref_points:
        r_lambda_target = float(pt['r_lambda'])
        ref_h = float(pt['h_lambda'])
        match = _find_row_by_field(artifact, 'r_lambda', r_lambda_target, eps)
        if match is None:
            scores.append(0.0)
            continue
        sub_h = float(match['h_lambda'])
        tol = tol_small if r_lambda_target <= small_thresh else tol_large
        if abs(sub_h - ref_h) <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)

    return float(np.mean(scores)) if scores else 0.0


# === block: score_2 (check id='check_force') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    r_xi_large = params['r_xi_large']
    r_xi_small = params['r_xi_small']
    linear_corr_thresh = params['linear_corr_threshold']
    zero_thresh = params['zero_force_abs_threshold']
    smooth_max_sc = params['smooth_max_slope_change']
    jump_thresh = params.get('slope_change_jump_threshold', 5.0)

    rows_large = [r for r in artifact if abs(float(r['r_xi']) - r_xi_large) < 1e-6]
    rows_small = [r for r in artifact if abs(float(r['r_xi']) - r_xi_small) < 1e-6]

    score_large = 0.0
    if len(rows_large) >= 5:
        arr = np.array([(float(r['h_xi']), float(r['force_scaled'])) for r in rows_large])
        arr = arr[arr[:,0].argsort()]
        # detect jump via slope changes
        h_vals = arr[:,0]
        f_vals = arr[:,1]
        if len(arr) >= 4:
            slopes = np.diff(f_vals) / np.clip(np.diff(h_vals), 1e-12, None)
            sc = np.abs(np.diff(slopes))
            jump_idx = None
            for i in range(len(sc)):
                if sc[i] > jump_thresh:
                    jump_idx = i + 2  # point after the high slope change
                    break
            if jump_idx is not None and jump_idx >= 2:
                # data before jump
                pre_h = h_vals[:jump_idx]
                pre_f = f_vals[:jump_idx]
                if len(pre_h) >= 4:
                    corr, _ = pearsonr(pre_h, pre_f)
                    if abs(corr) >= linear_corr_thresh:
                        # check that force after jump is near zero
                        post_f = f_vals[jump_idx:]
                        if len(post_f) > 0 and np.max(np.abs(post_f)) <= zero_thresh:
                            score_large = 1.0

    score_small = 0.0
    if len(rows_small) >= 5:
        max_sc = _compute_max_slope_change(rows_small, 'h_xi', 'force_scaled')
        if max_sc < smooth_max_sc:
            score_small = 1.0

    return 0.5 * score_large + 0.5 * score_small


_SCORERS = {
    'check_free_energy': score_0,
    'check_binodal': score_1,
    'check_force': score_2,
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
