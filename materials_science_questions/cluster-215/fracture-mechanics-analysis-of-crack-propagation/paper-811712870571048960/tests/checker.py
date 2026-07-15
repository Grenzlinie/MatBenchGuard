import os
import json
import csv

# === author imports / helpers ===
import math
import numpy as np

def A_alpha(a):
    return 0.378770 * a + 0.111251 * math.sin(2*a) - 0.004847 * math.sin(4*a) + 0.000241 * math.sin(6*a)

def B_alpha(a):
    term = 0.779825 * a + 0.190716 * math.sin(2*a) - 0.008309 * math.sin(4*a) + 0.000474 * math.sin(6*a)
    sa = math.sin(a)
    ca = math.cos(a)
    poly = 0.047833 + 0.018857 * sa**2 + 0.009834 * sa**4 + 0.005564 * sa**6 + 0.003158 * sa**8 + 0.001664 * sa**10
    return term - sa * ca * poly

def f_alpha(a):
    sa = math.sin(a)
    ca = math.cos(a)
    s = math.sqrt(1 - (11/12)*sa*sa)
    num = 1 + math.sqrt(11/12)
    den = math.sqrt(11/12)*ca + s
    ln_part = math.log(num/den)
    return (1.0 / (sa*sa)) * (1 - ca*s + (1.0/math.sqrt(132)) * ln_part)

def compute_criterion(alpha_rad, reduction_percent, m, beta):
    if reduction_percent >= 100.0:
        reduction_percent = 99.9
    if reduction_percent <= 0.0:
        reduction_percent = 0.001
    rf_r0 = math.sqrt(1 - reduction_percent/100.0)
    r0_rf = 1.0 / rf_r0
    ln_rf = math.log(rf_r0)
    a = alpha_rad
    sa = math.sin(a)
    ca = math.cos(a)
    f = f_alpha(a)
    A = A_alpha(a)
    B = B_alpha(a)
    term1 = math.sqrt(3) * sa * f * (1 - rf_r0 + 2*ln_rf)
    term2 = 2*math.sqrt(3) * ((rf_r0 - 1)*A - B*ln_rf)
    term3 = r0_rf + 1 + ln_rf - 2*a/sa
    term4 = m * ca * (1 - rf_r0 + ln_rf)
    
    sqrt_t = math.sqrt(1 - (11/12)*sa*sa)
    inv_sa = 1.0 / sa
    inv_sqrt12 = 1.0 / math.sqrt(12)
    inv_sqrt3 = 1.0 / math.sqrt(3)
    asin_arg = math.sqrt(11/12)*sa
    asin_val = math.asin(asin_arg)
    ln_cos = math.log(ca) if ca > 0 else -1e10
    ln_sinp1 = math.log(sa + 1)
    
    b_termA = inv_sqrt3 * inv_sa * (5/math.sqrt(11)) * asin_val * (2*ln_rf + 1 - rf_r0)
    b_termB = (1/11) * sqrt_t * (2*ln_rf + 3*(1 - rf_r0))
    b_termC = -(13/12) * ln_rf**2
    b_termD = inv_sqrt3 * sa * ln_rf**2
    b_termE = -(math.sqrt(3)/2) * sa * (rf_r0 - 1) * ln_rf
    b_termF = (38/33) * ln_rf
    b_termG = (1/2)*(73/33) - (35/33)*rf_r0 + (1/2)*(13/3)*r0_rf + (1/2)*(7/3)*rf_r0*ln_rf
    
    inner_ln = (sqrt_t - inv_sqrt12) / (1 - inv_sqrt12)
    b_termH = inv_sqrt3 * math.log(inner_ln) * ln_rf if inner_ln > 0 else 0.0
    
    b_termI = -0.5 * inv_sqrt3 * ln_cos * (2*ln_rf + ln_rf**2)
    b_termJ = 0.5 * inv_sqrt3 * ln_sinp1 * ln_rf**2
    
    inner2 = sqrt_t + inv_sqrt12 * sa
    b_termK = inv_sqrt3 * inv_sa * math.log(inner2) * (2*ln_rf + 1 - rf_r0) if inner2 > 0 else 0.0
    
    b_termL = inv_sqrt3 * inv_sa * ln_cos * (ln_rf**2 - rf_r0*ln_rf - ln_rf + rf_r0 - 1)
    
    m_term = -0.5*(11/12)*ln_rf**2 - (1 - (5/12)*rf_r0)*ln_rf - (7/12)*(1 - rf_r0)
    b_termM = (2*m / sqrt_t) * m_term if sqrt_t > 0 else 0.0
    
    b_termN = (5/12) * sa**2 * ln_rf**2
    b_termO = sa**2 * ((11/12 - (1/3)*rf_r0)*ln_rf - (7/12)*(1 - rf_r0))
    
    beta_sum = (b_termA + b_termB + b_termC + b_termD + b_termE + b_termF
                + b_termG + b_termH + b_termI + b_termJ + b_termK + b_termL
                + b_termM + b_termN + b_termO)
    lhs = term1 + term2 + term3 + term4 + beta * beta_sum
    return lhs


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
    required_pairs = []
    test_alphas_deg = []
    tol = 0.05
    for step in spec['steps']:
        if step['id'] == 'recompute':
            required_pairs = step['params']['required_pairs']
            test_alphas_deg = step['params']['test_alphas_deg']
            tol = step['params']['tolerance_abs']
    return {'required_pairs': required_pairs, 'test_alphas_deg': test_alphas_deg, 'tol': tol}


# === block: score_0 (check id='shape') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    required = {'alpha_deg', 'reduction_percent', 'm', 'beta'}
    if not required.issubset(artifact[0].keys()):
        return 0.0
    return 1.0


# === block: score_1 (check id='coverage') ===
def score_1(artifact, step, ctx):
    required_pairs = step['params']['required_pairs']
    min_span = step['params']['min_alpha_span']
    total = len(required_pairs)
    if total == 0:
        return 1.0
    passed = 0
    for pair in required_pairs:
        m_val = pair['m']
        b_val = pair['beta']
        rows = [r for r in artifact if float(r['m']) == m_val and float(r['beta']) == b_val]
        if not rows:
            continue
        alphas = [float(r['alpha_deg']) for r in rows]
        if max(alphas) - min(alphas) >= min_span:
            passed += 1
    return passed / total


# === block: score_2 (check id='recompute') ===
def score_2(artifact, step, ctx):
    required_pairs = ctx['required_pairs']
    test_alphas = ctx['test_alphas_deg']
    tol = ctx['tol']
    if not required_pairs or not test_alphas:
        return 0.0
    pair_scores = []
    for pair in required_pairs:
        m_val = pair['m']
        b_val = pair['beta']
        rows = [r for r in artifact if float(r['m']) == m_val and float(r['beta']) == b_val]
        if len(rows) < 2:
            pair_scores.append(0.0)
            continue
        data = sorted(rows, key=lambda r: float(r['alpha_deg']))
        alphas = np.array([float(r['alpha_deg']) for r in data])
        r_percents = np.array([float(r['reduction_percent']) for r in data])
        min_a, max_a = np.min(alphas), np.max(alphas)
        num = len(test_alphas)
        passed = 0
        for ta in test_alphas:
            if ta < min_a or ta > max_a:
                continue
            interp_r = np.interp(ta, alphas, r_percents)
            if interp_r < 0 or interp_r > 100:
                interp_r = max(0, min(100, interp_r))
            lhs = compute_criterion(math.radians(ta), interp_r, m_val, b_val)
            if abs(lhs) < tol:
                passed += 1
        if num > 0:
            pair_scores.append(passed / num)
        else:
            pair_scores.append(0.0)
    if not pair_scores:
        return 0.0
    return sum(pair_scores) / len(pair_scores)


_SCORERS = {
    'shape': score_0,
    'coverage': score_1,
    'recompute': score_2,
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
