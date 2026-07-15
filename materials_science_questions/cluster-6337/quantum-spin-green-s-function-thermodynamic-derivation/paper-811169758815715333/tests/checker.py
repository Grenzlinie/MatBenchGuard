import os
import json
import csv

# === author imports / helpers ===
import os, csv, json, math

def fit_exponent(pairs):
    """pairs: [(logN, logE)]; returns slope (positive exponent) of logE vs logN"""
    n = len(pairs)
    if n < 3:
        return None
    sum_x = sum(p[0] for p in pairs)
    sum_y = sum(p[1] for p in pairs)
    sum_xy = sum(p[0]*p[1] for p in pairs)
    sum_x2 = sum(p[0]*p[0] for p in pairs)
    denom = n*sum_x2 - sum_x*sum_x
    if abs(denom) < 1e-12:
        return None
    slope = (n*sum_xy - sum_x*sum_y) / denom
    # slope of log10(error) vs log10(N) is negative; exponent = -slope
    return -slope

def method_exponents(csv_rows, min_n=50):
    """returns dict method->exponent"""
    grouped = {}
    for row in csv_rows:
        m = row['method'].strip()
        N = float(row.get('N_theta','0'))
        err = float(row.get('relative_error','0') or row.get('errorbar','0'))
        if err <= 0 or N < min_n:
            continue
        grouped.setdefault(m, []).append((N, err))
    exponents = {}
    for method, pts in grouped.items():
        pts.sort(key=lambda x: x[0])
        log_pairs = [(math.log10(p[0]), math.log10(p[1])) for p in pts]
        exp = fit_exponent(log_pairs)
        if exp is not None:
            exponents[method] = exp
    return exponents


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
    path = os.path.join(outputs_dir, 'fig2a_errorbar_data.csv')
    ctx = {}
    if os.path.exists(path):
        with open(path, newline='') as f:
            rows = list(csv.DictReader(f))
        exp = method_exponents(rows, min_n=50)
        ctx['fig2a_exponents'] = exp
    else:
        ctx['fig2a_exponents'] = {}
    return ctx


# === block: score_0 (check id='fig1_convergence') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    thr = step.get('method_thresholds', {})
    exp = method_exponents(artifact, min_n=50)
    if not exp:
        return 0.0
    method_scores = {}
    for m, vals in thr.items():
        e = exp.get(m)
        if e is None:
            method_scores[m] = 0.0
            continue
        low, high = vals['low'], vals['high']
        if low <= e <= high:
            method_scores[m] = 1.0
        elif e < low:
            method_scores[m] = max(0.0, e / low)
        else:
            method_scores[m] = max(0.0, 1.0 - (e - high) / (high*0.1 + 0.01))
    average = sum(method_scores.values()) / max(1, len(method_scores))
    trend_ok = 1.0
    if 'PR' in exp and 'QR' in exp and 'grid' in exp:
        if exp['QR'] - exp['PR'] < step.get('min_difference', 0.15) or exp['grid'] - exp['PR'] < step.get('min_difference', 0.15):
            trend_ok = 0.0
    tw = float(step.get('trend_weight', 0.5))
    return (1-tw)*average + tw*trend_ok


# === block: score_1 (check id='fig2a_convergence') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    thr = step.get('method_thresholds', {})
    exp = method_exponents(artifact, min_n=50)
    if not exp:
        return 0.0
    method_scores = {}
    for m, vals in thr.items():
        e = exp.get(m)
        if e is None:
            method_scores[m] = 0.0
            continue
        low, high = vals['low'], vals['high']
        if low <= e <= high:
            method_scores[m] = 1.0
        elif e < low:
            method_scores[m] = max(0.0, e / low)
        else:
            method_scores[m] = max(0.0, 1.0 - (e - high) / (high*0.1 + 0.01))
    average = sum(method_scores.values()) / max(1, len(method_scores))
    trend_ok = 1.0
    if 'PR' in exp and 'QR' in exp and 'grid' in exp:
        if exp['QR'] - exp['PR'] < step.get('min_difference', 0.20) or exp['grid'] - exp['PR'] < step.get('min_difference', 0.20):
            trend_ok = 0.0
    tw = float(step.get('trend_weight', 0.5))
    return (1-tw)*average + tw*trend_ok


# === block: score_2 (check id='fitted_slopes_consistency') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    ref = ctx.get('fig2a_exponents', {})
    if not ref:
        return 0.0
    methods = ['QR','PR','grid']
    tol = float(step.get('tolerance_abs', 0.015))
    scores = []
    for m in methods:
        v = artifact.get(m)
        e = ref.get(m)
        if e is None or not isinstance(v, (int, float)):
            scores.append(0.0)
        else:
            diff = abs(float(v) - e)
            scores.append(1.0 if diff <= tol else 0.0)
    return sum(scores) / len(scores)


_SCORERS = {
    'fig1_convergence': score_0,
    'fig2a_convergence': score_1,
    'fitted_slopes_consistency': score_2,
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
