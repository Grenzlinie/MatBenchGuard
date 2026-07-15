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
     beta = 0.025
     gold_A = 35.93
     gold_exp = -2.0
     ctx = {'beta': beta, 'gold_A': gold_A, 'gold_exp': gold_exp}
     return ctx


# === block: score_0 (check id='sim_2d') ===
def score_0(artifact, step, ctx):
    import math
    from collections import defaultdict

    def linear_regression(x_vals, y_vals):
        """Compute slope and intercept with R^2 for y = slope*x + intercept."""
        n = len(x_vals)
        if n < 2:
            return None, None, None
        mean_x = sum(x_vals)/n
        mean_y = sum(y_vals)/n
        num = sum((x-mean_x)*(y-mean_y) for x,y in zip(x_vals, y_vals))
        den = sum((x-mean_x)**2 for x in x_vals)
        if den == 0:
            return None, None, None
        slope = num/den
        intercept = mean_y - slope*mean_x
        ss_res = sum((y - (slope*x + intercept))**2 for x,y in zip(x_vals, y_vals))
        ss_tot = sum((y-mean_y)**2 for y in y_vals)
        r2 = 1 - (ss_res/ss_tot) if ss_tot != 0 else 0.0
        return slope, intercept, r2

    if artifact is None or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    rows = []
    try:
        for r in artifact:
            a0 = float(r['a0_over_lG'])
            cr = float(r['Cr'])
            act = int(r['activated'])
            rows.append((a0, cr, act))
    except Exception:
        return 0.0
    if len(rows) == 0:
        return 0.0

    # Determine activation boundary: for each unique Cr, find the minimum a0/lG that activates
    act_by_cr = defaultdict(list)
    for a0, cr, act in rows:
        if act == 1:
            act_by_cr[cr].append(a0)
    threshold_points = []
    for cr, a0s in act_by_cr.items():
        min_a0 = min(a0s)
        threshold_points.append((cr, min_a0))

    if len(threshold_points) < 3:
        return 0.0

    # Filter intermediate regime (a0 between 500 and 10000) for power-law fit
    filtered = [(cr, a0) for cr, a0 in threshold_points if 500.0 <= a0 <= 10000.0]
    if len(filtered) < 3:
        # use all threshold points if not enough in range
        filtered = threshold_points
    if len(filtered) < 3:
        return 0.0

    log_cr = [math.log(cr) for cr, a0 in filtered]
    log_a0 = [math.log(a0) for _, a0 in filtered]
    slope, intercept, r2 = linear_regression(log_cr, log_a0)
    if slope is None:
        return 0.0
    p = slope
    # a0_min/lG = A (beta Cr)^p  ->  log(a0_min) = log(A) + p*log(beta) + p*log(Cr)
    # intercept = log(A) + p*log(beta)  -> A = exp(intercept - p*log(beta))
    beta = ctx['beta']
    try:
        A_fit = math.exp(intercept - p * math.log(beta))
    except:
        A_fit = None

    # Score exponent: within [-2.5, -1.5] gives score, maximum at -2
    exp_range = step.get('config', {}).get('exponent_range', [-2.5, -1.5])
    exp_score = 0.0
    if exp_range[0] <= p <= exp_range[1]:
        exp_score = max(0.0, 1.0 - abs(p - ctx['gold_exp']) / (exp_range[1] - ctx['gold_exp']))
    elif p < exp_range[0]:
        exp_score = max(0.0, (p - exp_range[0]) / (ctx['gold_exp'] - exp_range[0]))
    else:
        exp_score = max(0.0, (exp_range[1] - p) / (exp_range[1] - ctx['gold_exp']))

    # Score A: relative tolerance 25%
    tol_A = step.get('config', {}).get('A_tolerance_relative', 0.25)
    A_score = 0.0
    if A_fit is not None:
        A_score = max(0.0, 1.0 - abs(A_fit - ctx['gold_A']) / (tol_A * ctx['gold_A']))

    # Regime I: for a0/lG > 10000 and Cr < 10, all must be 0
    regime_I_ok = True
    regime_I_count = 0
    for a0, cr, act in rows:
        if a0 > 10000.0 and cr < 10.0:
            regime_I_count += 1
            if act != 0:
                regime_I_ok = False
                break
    regime_I_score = 1.0 if regime_I_ok else 0.0
    if regime_I_count == 0:
        regime_I_score = 0.0  # no test points

    # Regime III: for a0/lG < 500, all must be 0 regardless of Cr
    regime_III_ok = True
    regime_III_count = 0
    for a0, cr, act in rows:
        if a0 < 500.0:
            regime_III_count += 1
            if act != 0:
                regime_III_ok = False
                break
    regime_III_score = 1.0 if regime_III_ok else 0.0
    if regime_III_count == 0:
        regime_III_score = 0.0

    # Weighted combination
    score = 0.5 * (0.5*exp_score + 0.5*A_score) + 0.25 * regime_I_score + 0.25 * regime_III_score
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='fit_powerlaw') ===
def score_1(artifact, step, ctx):
    import math, os, json

    json_path = '/app/outputs/power_law_fit.json'
    if not os.path.exists(json_path):
        return 0.0
    try:
        with open(json_path) as f:
            data = json.load(f)
    except Exception:
        return 0.0

    required = ['A', 'exponent', 'R_squared', 'fitting_range_min_a0_over_lG', 'fitting_range_max_a0_over_lG', 'observed_R3_constant_a0min']
    if not all(k in data for k in required):
        return 0.0

    # Gold references
    gold_exp = ctx['gold_exp']
    gold_A = ctx['gold_A']
    config = step.get('config', {})
    exp_tol = config.get('exponent_tolerance', 0.5)
    A_tol_rel = config.get('A_tolerance_relative', 0.25)
    rsq_min = config.get('R_squared_min', 0.95)

    # Exponent score: linear around gold_exp within tolerance
    p = data['exponent']
    exp_score = max(0.0, 1.0 - abs(p - gold_exp) / exp_tol)

    # A score: relative error
    A = data['A']
    A_score = max(0.0, 1.0 - abs(A - gold_A) / (gold_A * A_tol_rel))

    # R_squared score
    rsq = data['R_squared']
    if rsq < 0:
        rsq_score = 0.0
    else:
        rsq_score = min(1.0, rsq / rsq_min)

    # Consistency with CSV if available (optional, low weight)
    csv_path = '/app/outputs/activation_diagram.csv'
    csv_consistency = 1.0
    if os.path.exists(csv_path):
        try:
            import csv
            rows = []
            with open(csv_path, newline='') as f:
                reader = csv.DictReader(f)
                for r in reader:
                    rows.append((float(r['a0_over_lG']), float(r['Cr']), int(r['activated'])))
            # recompute threshold
            from collections import defaultdict
            act_by_cr = defaultdict(list)
            for a0, cr, act in rows:
                if act == 1:
                    act_by_cr[cr].append(a0)
            threshold = [(cr, min(a0s)) for cr, a0s in act_by_cr.items()]
            # use the same intermediate range as the agent reported
            min_range = data.get('fitting_range_min_a0_over_lG', 500.0)
            max_range = data.get('fitting_range_max_a0_over_lG', 10000.0)
            filtered = [(cr, a0) for cr, a0 in threshold if min_range <= a0 <= max_range]
            if len(filtered) >= 3:
                log_cr = [math.log(cr) for cr, a0 in filtered]
                log_a0 = [math.log(a0) for a0 in filtered]
                # simple linear regression
                n = len(log_cr)
                mx = sum(log_cr)/n
                my = sum(log_a0)/n
                sxy = sum((x-mx)*(y-my) for x,y in zip(log_cr, log_a0))
                sxx = sum((x-mx)**2 for x in log_cr)
                if sxx != 0:
                    slope = sxy / sxx
                    intercept = my - slope*mx
                    # check that slope is within 25% of exponent from CSV
                    if abs(slope - p) / max(abs(p), 1e-6) > 0.25:
                        csv_consistency = 0.0
        except Exception:
            csv_consistency = 1.0  # ignore errors

    # Combine scores (weighted average)
    score = 0.35*exp_score + 0.35*A_score + 0.2*rsq_score + 0.1*csv_consistency
    return min(1.0, max(0.0, score))


_SCORERS = {
    'sim_2d': score_0,
    'fit_powerlaw': score_1,
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
