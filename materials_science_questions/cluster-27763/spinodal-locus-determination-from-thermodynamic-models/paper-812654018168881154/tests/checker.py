import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.interpolate import interp1d


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
    gold_points = []
    for step in spec.get('steps', []):
        if step['id'] == 'effective_exponents':
            gold_points = step.get('gold_points', [])
            break
    return {'gold_points': gold_points}


# === block: score_0 (check id='effective_exponents') ===
def score_0(artifact, step, ctx):
    scored=0.0
    if not artifact:
        return 0.0
    gold_pts = ctx.get('gold_points', [])
    if not gold_pts:
        return 1.0
    # Build lookup from artifact: group by gamma_r3, exponent_type, collect t and value arrays
    from collections import defaultdict
    data = defaultdict(list)
    for row in artifact:
        try:
            gr = float(row['gamma_r3'])
            tt = float(row['t'])
            et = row['exponent_type'].strip()
            ev = float(row['exponent_value'])
        except (KeyError, ValueError):
            continue
        key = (gr, et)
        data[key].append((tt, ev))
    # Sort and create interpolation functions for each key
    interp_fns = {}
    for key, pts in data.items():
        if len(pts) < 2:
            continue
        pts_sorted = sorted(pts, key=lambda x: x[0])
        ts = np.array([p[0] for p in pts_sorted])
        vs = np.array([p[1] for p in pts_sorted])
        interp_fns[key] = interp1d(ts, vs, kind='linear', bounds_error=False, fill_value=np.nan)

    point_scores = []
    tol_rel = 0.07
    tol_abs = 0.05
    for gp in gold_pts:
        key = (gp['gamma_r3'], gp['exponent_type'])
        fn = interp_fns.get(key)
        if fn is None:
            point_scores.append(0.0)
            continue
        try:
            eval_at = fn(gp['t'])
            if np.isnan(eval_at):
                point_scores.append(0.0)
                continue
            err = abs(eval_at - gp['value'])
            # relative error with a floor
            denom = max(abs(gp['value']), 1e-6)
            rel_err = err / denom
            if err <= tol_abs or rel_err <= tol_rel:
                point_scores.append(1.0)
            else:
                # partial credit based on how far beyond tolerance
                extra = max(0.0, rel_err - tol_rel)
                score = max(0.0, 1.0 - extra / tol_rel)  # linear decay
                point_scores.append(score)
        except Exception:
            point_scores.append(0.0)
    if point_scores:
        scored = float(np.mean(point_scores))
    else:
        scored = 1.0
    return scored


# === block: score_1 (check id='scaled_eos') ===
def score_1(artifact, step, ctx):
    scored = 0.0
    if not artifact or len(artifact) < 3:
        return 0.0
    delta_target = step.get('delta_target', 5.0)
    delta_tol = step.get('delta_tolerance', 0.8)
    # Collect supercritical isotherm points
    super_rows = []
    for row in artifact:
        if row.get('temperature_type', '').strip().lower() == 'supercritical':
            try:
                t_val = float(row['t'])
                x = float(row['x'])
                y = float(row['y'])
                super_rows.append((t_val, x, y))
            except (KeyError, ValueError):
                continue
    if not super_rows:
        return 0.0
    # Group by t (isotherm) and compute log-log slope between consecutive large x points
    # Only consider x > 10 to be in the asymptotic regime
    large_x_rows = [r for r in super_rows if r[1] > 10.0]
    if len(large_x_rows) < 3:
        return 0.0
    # For each isotherm, compute successive point slopes
    slopes = []
    from math import log
    large_x_sorted = sorted(large_x_rows, key=lambda r: (r[0], r[1]))  # group by t then x
    current_t = None
    current_pts = []
    for t, x, y in large_x_sorted:
        if current_t is None:
            current_t = t
        if t != current_t:
            # compute slopes within the group
            if len(current_pts) >= 2:
                for i in range(1, len(current_pts)):
                    x1, y1 = current_pts[i-1]
                    x2, y2 = current_pts[i]
                    if x2 <= x1: continue
                    slope = (log(y2) - log(y1)) / (log(x2) - log(x1))
                    slopes.append(slope)
            current_t = t
            current_pts = [(x, y)]
        else:
            current_pts.append((x, y))
    # Process last group
    if current_pts and len(current_pts) >= 2:
        for i in range(1, len(current_pts)):
            x1, y1 = current_pts[i-1]
            x2, y2 = current_pts[i]
            if x2 <= x1: continue
            slope = (log(y2) - log(y1)) / (log(x2) - log(x1))
            slopes.append(slope)
    if not slopes:
        return 0.0
    avg_slope = np.mean(slopes)
    err = abs(avg_slope - delta_target)
    if err <= delta_tol / 3.0:  # within first third of tolerance -> full credit
        scored = 1.0
    else:
        # linear decay from 1 to 0 as err goes from delta_tol/3 to delta_tol
        score = max(0.0, 1.0 - (err - delta_tol/3.0) / (delta_tol * 2.0/3.0))
        scored = score
    return scored


_SCORERS = {
    'effective_exponents': score_0,
    'scaled_eos': score_1,
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
