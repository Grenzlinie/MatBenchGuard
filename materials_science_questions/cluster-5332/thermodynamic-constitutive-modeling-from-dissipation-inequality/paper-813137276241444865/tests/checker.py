import os
import json
import csv

# === author imports / helpers ===
import csv, math, os

def interpolate_from_dicts(rows, xcol, ycol, x):
    pts = [(float(r[xcol]), float(r[ycol])) for r in rows]
    pts.sort(key=lambda p: p[0])
    if not pts:
        raise ValueError("No data")
    for i, (xc, yc) in enumerate(pts):
        if xc == x:
            return yc
        if xc > x:
            if i == 0:
                if len(pts) >= 2:
                    x1, y1 = pts[0]
                    x2, y2 = pts[1]
                    if x2 != x1:
                        return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
                    else:
                        return y1
                else:
                    return yc
            else:
                x0, y0 = pts[i-1]
                x1, y1 = pts[i]
                if x1 == x0:
                    return y0
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    if len(pts) >= 2:
        xm1, ym1 = pts[-2]
        xm2, ym2 = pts[-1]
        if xm2 != xm1:
            return ym1 + (ym2 - ym1) * (x - xm1) / (xm2 - xm1)
        else:
            return ym2
    return pts[-1][1]


def score_curve_deviation(rows, xcol, ycol, points, tolerance):
    scores = []
    for (xp, yp_gold) in points:
        yp = interpolate_from_dicts(rows, xcol, ycol, xp)
        diff = abs(yp - yp_gold)
        if diff <= tolerance:
            scores.append(1.0)
        else:
            score = max(0.0, 1.0 - (diff - tolerance) / tolerance)
            scores.append(score)
    return sum(scores) / len(scores) if scores else 0.0


def get_peak_xy(rows, xcol, ycol):
    best = None
    best_y = -float('inf')
    for r in rows:
        xv = float(r[xcol])
        yv = float(r[ycol])
        if yv > best_y:
            best_y = yv
            best = (xv, yv)
    return best


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
    local_path = os.path.join(outputs_dir, 'step_01_ld_local.csv')
    gradient_path = os.path.join(outputs_dir, 'step_02_ld_gradient.csv')
    temp_path = os.path.join(outputs_dir, 'step_03_temp_time_center.csv')
    ctx = {}
    if os.path.exists(local_path):
        with open(local_path, newline='') as f:
            reader = csv.DictReader(f)
            ctx['local'] = list(reader)
    if os.path.exists(gradient_path):
        with open(gradient_path, newline='') as f:
            reader = csv.DictReader(f)
            ctx['gradient'] = list(reader)
    if os.path.exists(temp_path):
        with open(temp_path, newline='') as f:
            reader = csv.DictReader(f)
            ctx['temperature'] = list(reader)
    return ctx


# === block: score_0 (check id='step_01_ld_local') ===
def score_0(artifact, step, ctx):
    params = step['params']
    return score_curve_deviation(artifact, params['x_column'], params['y_column'], params['points'], params['tolerance'])


# === block: score_1 (check id='step_02_ld_gradient') ===
def score_1(artifact, step, ctx):
    params = step['params']
    dev_score = score_curve_deviation(artifact, params['x_column'], params['y_column'], params['points'], params['tolerance'])
    local_rows = ctx.get('local')
    grad_rows = artifact
    struct_score = 1.0
    if local_rows and grad_rows:
        local_peak = get_peak_xy(local_rows, 'displacement_mm', 'load_kN')
        grad_peak = get_peak_xy(grad_rows, 'displacement_mm', 'load_kN')
        if local_peak is None or grad_peak is None:
            struct_score = 0.0
        elif not (grad_peak[1] < local_peak[1] and grad_peak[0] > local_peak[0]):
            struct_score = 0.0
    else:
        struct_score = 0.0
    return 0.7 * dev_score + 0.3 * struct_score


# === block: score_2 (check id='step_03_temp_time_center') ===
def score_2(artifact, step, ctx):
    params = step['params']
    return score_curve_deviation(artifact, params['x_column'], params['y_column'], params['points'], params['tolerance'])


_SCORERS = {
    'step_01_ld_local': score_0,
    'step_02_ld_gradient': score_1,
    'step_03_temp_time_center': score_2,
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
