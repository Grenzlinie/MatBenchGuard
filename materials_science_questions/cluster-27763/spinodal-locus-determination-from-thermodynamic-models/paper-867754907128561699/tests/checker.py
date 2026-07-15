import os
import json
import csv

# === author imports / helpers ===
# no heavy imports at module level; scorers manage their own imports


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
    gold_by_id = {step['id']: step for step in spec.get('steps', [])}


# === block: score_0 (check id='equilibrium_densities') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    step = ctx['gold_by_id'].get('equilibrium_densities', {})
    gold = step.get('gold', {})
    target_temp = gold.get('temperature', 0.85)
    tol_temp = 0.01
    best_row = None
    for row in artifact:
        try:
            t = float(row.get('reduced_temperature', None))
            if abs(t - target_temp) <= tol_temp:
                best_row = row
                break
        except (ValueError, TypeError):
            continue
    if best_row is None:
        return 0.0
    liq = float(best_row['liquid_density'])
    gas = float(best_row['gas_density'])
    gold_liq = gold.get('liquid', 1.804)
    gold_gas = gold.get('gas', 0.319)
    tol = step.get('tolerance_abs', 0.05)
    score_liq = max(0.0, 1.0 - abs(liq - gold_liq) / tol)
    score_gas = max(0.0, 1.0 - abs(gas - gold_gas) / tol)
    return 0.5 * score_liq + 0.5 * score_gas


# === block: score_1 (check id='laplace_verification') ===
def score_1(artifact, step, ctx):
    import numpy as np
    step = ctx['gold_by_id'].get('laplace_verification', {})
    rc = step.get('recompute_config', {})
    slope_range = rc.get('check_slope_range', [0.9, 1.1])
    r2_min = rc.get('check_r_squared_min', 0.95)
    if not isinstance(artifact, list) or len(artifact) < 3:
        return 0.0
    alpha_rs = []
    delta_ps = []
    for row in artifact:
        try:
            R = float(row['drop_radius'])
            inside = float(row['inside_pressure'])
            outside = float(row['outside_pressure'])
            alpha = float(row['surface_tension_coefficient'])
            if R <= 0 or alpha <= 0:
                continue
            alpha_r = alpha / R
            dp = inside - outside
            alpha_rs.append(alpha_r)
            delta_ps.append(dp)
        except (ValueError, KeyError):
            continue
    if len(alpha_rs) < 3:
        return 0.0
    alpha_rs = np.array(alpha_rs)
    delta_ps = np.array(delta_ps)
    A = np.vstack([alpha_rs, np.ones(len(alpha_rs))]).T
    slope, intercept = np.linalg.lstsq(A, delta_ps, rcond=None)[0]
    residuals = delta_ps - (slope * alpha_rs + intercept)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((delta_ps - np.mean(delta_ps))**2)
    r_squared = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    score_slope = 1.0 if slope_range[0] <= slope <= slope_range[1] else 0.0
    score_r2 = 1.0 if r_squared >= r2_min else 0.5 if r_squared >= 0.9 else 0.0
    return 0.6 * score_slope + 0.4 * score_r2


# === block: score_2 (check id='domain_growth') ===
def score_2(artifact, step, ctx):
    import numpy as np
    step = ctx['gold_by_id'].get('domain_growth', {})
    gold_exp = step.get('gold_exponent', 0.70)
    tol = step.get('tolerance', 0.05)
    filter_range = step.get('recompute_config', {}).get('filter_range', [20, 128])
    if not isinstance(artifact, list) or len(artifact) < 4:
        return 0.0
    times = []
    sizes = []
    for row in artifact:
        try:
            t = float(row['time'])
            d = float(row['domain_size'])
            if filter_range[0] <= d <= filter_range[1]:
                times.append(t)
                sizes.append(d)
        except (ValueError, KeyError):
            continue
    if len(times) < 3:
        return 0.0
    log_t = np.log(times)
    log_d = np.log(sizes)
    A = np.vstack([log_t, np.ones(len(times))]).T
    n, log_A = np.linalg.lstsq(A, log_d, rcond=None)[0]
    return max(0.0, 1.0 - abs(n - gold_exp) / tol)


# === block: score_3 (check id='growth_exponent') ===
def score_3(artifact, step, ctx):
    step = ctx['gold_by_id'].get('growth_exponent', {})
    gold = step.get('gold', 0.70)
    tol = step.get('tolerance_abs', 0.05)
    try:
        val = float(artifact.strip())
    except (ValueError, AttributeError):
        return 0.0
    return max(0.0, 1.0 - abs(val - gold) / tol)


_SCORERS = {
    'equilibrium_densities': score_0,
    'laplace_verification': score_1,
    'domain_growth': score_2,
    'growth_exponent': score_3,
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
