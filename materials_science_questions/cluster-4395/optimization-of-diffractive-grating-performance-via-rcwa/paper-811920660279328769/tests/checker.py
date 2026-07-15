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
    return {'derived_half_contrast_depth_20nm': None}


# === block: score_0 (check id='contrast_20nm') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows: return 0.0
    depth_key = 'depth_nm'
    contrast_key = 'contrast'
    depths = []
    contrasts = []
    for r in rows:
        try:
            d = float(r[depth_key])
            c = float(r[contrast_key])
            depths.append(d)
            contrasts.append(c)
        except: continue
    if not depths: return 0.0
    pairs = sorted(zip(depths, contrasts), key=lambda x: x[0])
    depths = [p[0] for p in pairs]
    contrasts = [p[1] for p in pairs]
    params = step.get('params', {})
    contrast_min_c0 = params.get('contrast_min_at_exit', 0.5)
    depth_max_min = params.get('depth_max_min', 100)
    step_max = params.get('step_max', 2.0)
    score = 0.0
    if depths and min(depths) <= 1e-9 and max(depths) >= depth_max_min:
        max_step = max(depths[i+1] - depths[i] for i in range(len(depths)-1)) if len(depths) > 1 else 0
        if max_step <= step_max:
            score += 0.3
    c0 = None
    for d, c in zip(depths, contrasts):
        if abs(d) < 1e-9:
            c0 = c
            break
    if c0 is not None and c0 > contrast_min_c0:
        score += 0.7
    half_contrast = None
    for i, c in enumerate(contrasts):
        if c < 0.5:
            if i == 0:
                half_contrast = depths[i]
            else:
                d0, d1 = depths[i-1], depths[i]
                c0i, c1 = contrasts[i-1], contrasts[i]
                if c1 != c0i:
                    half_contrast = d0 + (0.5 - c0i) / (c1 - c0i) * (d1 - d0)
                else:
                    half_contrast = depths[i]
            break
    ctx['derived_half_contrast_depth_20nm'] = half_contrast
    return min(1.0, score)


# === block: score_1 (check id='half_contrast_depths') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows: return 0.0
    depths = {}
    for r in rows:
        try:
            p = int(r['period_nm'])
            d = float(r['half_contrast_depth_nm'])
            depths[p] = d
        except: continue
    params = step.get('params', {})
    refs = params.get('reference_depths', {})
    tols = params.get('tolerances', {})
    expected_periods = {200, 140, 80, 20}
    score = 0.0
    if expected_periods.issubset(set(depths.keys())):
        for period in expected_periods:
            val = depths[period]
            ref = refs.get(str(period))
            if ref is None: continue
            tol = tols.get(str(period), 5.0)
            if abs(val - ref) <= tol:
                score += 0.1
    periods = sorted(depths.keys())
    values = [depths[p] for p in periods]
    n = len(periods)
    if n >= 2:
        sum_x = sum(periods)
        sum_y = sum(values)
        sum_xy = sum(x*y for x,y in zip(periods, values))
        sum_x2 = sum(x*x for x in periods)
        denom = n*sum_x2 - sum_x*sum_x
        if denom != 0:
            slope = (n*sum_xy - sum_x*sum_y) / denom
            intercept = (sum_y - slope*sum_x)/n
            y_mean = sum_y/n
            ss_res = sum((y - (slope*x + intercept))**2 for x,y in zip(periods, values))
            ss_tot = sum((y - y_mean)**2 for y in values)
            r2 = 1 - ss_res/ss_tot if ss_tot != 0 else 1.0
        else:
            slope = 0
            r2 = 0
        if r2 >= params.get('r2_min', 0.95):
            score += 0.25
        if params.get('slope_min', 0.1) <= slope <= params.get('slope_max', 0.3):
            score += 0.15
    derived = ctx.get('derived_half_contrast_depth_20nm')
    if derived is not None and 20 in depths:
        if abs(depths[20] - derived) <= params.get('consistency_tol', 0.5):
            score += 0.2
    return min(1.0, score)


_SCORERS = {
    'contrast_20nm': score_0,
    'half_contrast_depths': score_1,
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
