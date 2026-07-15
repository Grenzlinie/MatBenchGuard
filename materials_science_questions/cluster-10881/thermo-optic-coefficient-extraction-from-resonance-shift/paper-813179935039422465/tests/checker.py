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
    ctx = {"steady": spec["steps"][0]["target"] if "steps" in spec else spec["checks"][0]["target"]}


# === block: score_0 (check id='steady_state_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or not all(c in rows[0] for c in ('toroid_type','pump_power_mW','temperature_K','shift_pm')):
        return 0.0
    target = step.get('target', {})
    std = target.get('standard', {})
    ret = target.get('re-etched', {})
    trend = target.get('trend', {})

    import math

    def mean(vals):
        return sum(vals) / len(vals) if vals else 0.0

    def fit_linear(x, y):
        n = len(x)
        if n < 2:
            return None, None
        sx = sum(x)
        sy = sum(y)
        sx2 = sum(xi*xi for xi in x)
        sxy = sum(xi*yi for xi, yi in zip(x, y))
        denom = n*sx2 - sx*sx
        if abs(denom) < 1e-12:
            return None, None
        a = (sy*sx2 - sx*sxy) / denom
        b = (n*sxy - sx*sy) / denom
        return a, b

    def solve_3x3(A, b):
        n = 3
        M = [row[:] + [b[i]] for i, row in enumerate(A)]
        for i in range(n):
            max_row = i
            max_val = abs(M[i][i])
            for k in range(i+1, n):
                if abs(M[k][i]) > max_val:
                    max_val = abs(M[k][i])
                    max_row = k
            if max_val < 1e-12:
                return None
            if max_row != i:
                M[i], M[max_row] = M[max_row], M[i]
            piv = M[i][i]
            for j in range(i, n+1):
                M[i][j] /= piv
            for k in range(n):
                if k != i:
                    factor = M[k][i]
                    for j in range(i, n+1):
                        M[k][j] -= factor * M[i][j]
        return [M[i][n] for i in range(n)]

    def fit_quadratic(x, y):
        n = len(x)
        if n < 3:
            return None, None, None
        s0 = n
        s1 = sum(x)
        s2 = sum(xi*xi for xi in x)
        s3 = sum(xi*xi*xi for xi in x)
        s4 = sum(xi*xi*xi*xi for xi in x)
        r0 = sum(y)
        r1 = sum(xi*yi for xi, yi in zip(x, y))
        r2 = sum(xi*xi*yi for xi, yi in zip(x, y))
        M = [[s0, s1, s2], [s1, s2, s3], [s2, s3, s4]]
        rhs = [r0, r1, r2]
        try:
            coeffs = solve_3x3(M, rhs)
            if coeffs is None:
                return None, None, None
            return coeffs[0], coeffs[1], coeffs[2]
        except:
            return None, None, None

    def r2_score(y_true, y_pred):
        y_mean = mean(y_true)
        ss_res = sum((ty - py)**2 for ty, py in zip(y_true, y_pred))
        ss_tot = sum((ty - y_mean)**2 for ty in y_true)
        if ss_tot < 1e-12:
            return 0.0
        return 1.0 - ss_res / ss_tot

    # helper to find row by exact power match
    def get_row(ttype, power):
        for r in rows:
            try:
                p = float(r['pump_power_mW'])
                if r['toroid_type'].strip().lower() == ttype and abs(p - power) < 1e-6:
                    return float(r['shift_pm']), float(r['temperature_K'])
            except:
                pass
        return None, None

    # power point checks
    powers = [4.2, 12.7]
    power_items = []
    for toroid, cfg in [('standard', std), ('re-etched', ret)]:
        for p in powers:
            s, t = get_row(toroid, p)
            if s is None or t is None:
                power_items.append(0.0)
                continue
            s_gold = cfg['shifts'].get(str(p))
            t_gold = cfg['temps'].get(str(p))
            s_tol = cfg['tolerances'].get('shift_rel', 0.10) * abs(s_gold) if s_gold else 0
            t_tol = cfg['tolerances'].get('temp_abs', 5.0)
            score = 1.0 if (abs(s - s_gold) <= s_tol) and (abs(t - t_gold) <= t_tol) else 0.0
            power_items.append(score)
    power_checks = sum(power_items) / len(power_items) if power_items else 0.0

    # trend checks
    def get_toroid_data(ttype):
        xs, ys = [], []
        for r in rows:
            if r['toroid_type'].strip().lower() == ttype:
                try:
                    xs.append(float(r['pump_power_mW']))
                    ys.append(float(r['shift_pm']))
                except:
                    pass
        return xs, ys

    std_x, std_y = get_toroid_data('standard')
    ret_x, ret_y = get_toroid_data('re-etched')

    std_linear_ok = 0.0
    if len(std_x) > 2:
        a, b = fit_linear(std_x, std_y)
        if a is not None:
            y_pred = [a + b*xi for xi in std_x]
            r2 = r2_score(std_y, y_pred)
            if r2 >= trend.get('standard_linear_r2', 0.95):
                std_linear_ok = 1.0

    ret_quadratic_ok = 0.0
    if len(ret_x) > 3:
        a1, b1 = fit_linear(ret_x, ret_y)
        a2, b2, c2 = fit_quadratic(ret_x, ret_y)
        if a1 is not None and a2 is not None and b2 is not None and c2 is not None:
            pred_lin = [a1 + b1*xi for xi in ret_x]
            pred_quad = [a2 + b2*xi + c2*xi*xi for xi in ret_x]
            r2_linear = r2_score(ret_y, pred_lin)
            r2_quad = r2_score(ret_y, pred_quad)
            n = len(ret_x)
            adj_linear = 1.0 - (1.0 - r2_linear) * (n-1) / (n-2) if n > 2 else r2_linear
            adj_quad = 1.0 - (1.0 - r2_quad) * (n-1) / (n-3) if n > 3 else r2_quad
            diff = adj_quad - adj_linear
            if diff >= trend.get('re-etched_quadratic_vs_linear_adj_r2_diff', 0.05):
                ret_quadratic_ok = 1.0

    trend_score = (std_linear_ok + ret_quadratic_ok) / 2.0

    # combine
    shape_ok = 1.0 if rows else 0.0
    raw = 0.1*shape_ok + 0.5*power_checks + 0.4*trend_score
    return min(max(raw, 0.0), 1.0)


# === block: score_1 (check id='cutoff_frequency_check') ===
def score_1(artifact, step, ctx):
    val_str = artifact.strip() if isinstance(artifact, str) else str(artifact)
    try:
        val = float(val_str.strip())
    except:
        return 0.0
    target = step.get('target', {})
    ref = target.get('value', 5000.0)
    tol = target.get('tolerance', 1000.0)
    return 1.0 if abs(val - ref) <= tol else 0.0


_SCORERS = {
    'steady_state_check': score_0,
    'cutoff_frequency_check': score_1,
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
