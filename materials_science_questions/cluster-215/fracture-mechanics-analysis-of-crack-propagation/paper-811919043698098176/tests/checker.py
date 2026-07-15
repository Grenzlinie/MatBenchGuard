import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os

def r1(varsigma, lam):
    s = (1+varsigma)
    t = math.sqrt((1-varsigma)**2 + 4*lam**2)
    denom = s - t
    if denom == 0:
        return float('inf')
    return s / denom

def compute_typeI_max(varsigma, lam, sign_sigma12, R22, sigma_I_f):
    # orientation beta according to Eq.6
    if lam == 0 and varsigma > 1:
        beta_opt = math.pi/2
    else:
        if sign_sigma12 > 0:
            beta_opt = 3*math.pi/4 - 0.5*math.atan2(varsigma-1, 2*lam)
        elif sign_sigma12 < 0:
            beta_opt = math.pi/4 - 0.5*math.atan2(varsigma-1, 2*lam)
        else:
            beta_opt = math.pi/2
    # maximum normal tensile stress σ_{I,t}^max  (with σ22_max = 1.0)
    sigma22_max = 1.0
    sigma22_min = R22 * sigma22_max
    sqrtD = math.sqrt((1-varsigma)**2 + 4*lam**2)
    coeff_plus = (varsigma+1)/2 + sqrtD
    coeff_minus = (varsigma+1)/2 - sqrtD
    # r1 factor for case discrimination (Eq.7a)
    denom = 1+varsigma - sqrtD
    if denom == 0:
        r1_val = float('inf')
    else:
        r1_val = (1+varsigma + sqrtD) / denom
    lam2 = lam**2
    if R22 < 1:
        if r1_val <= R22 < 1:
            sigma_max = coeff_plus * sigma22_max
        else:   # R22 < r1_val
            if varsigma > lam2:
                sigma_max = coeff_plus * sigma22_max
            else:
                sigma_max = coeff_plus * sigma22_min
    elif R22 > 1:
        if varsigma > lam2:
            sigma_max = 0.0
        else:
            sigma_max = coeff_minus * sigma22_min
    else:   # R22 == 1
        sigma_max = coeff_plus * sigma22_max
        if sigma_max < 0:
            sigma_max = 0.0
    if sigma_max < 0:
        sigma_max = 0.0
    sigma_eq = sigma_max / sigma_I_f if sigma_I_f > 0 else 0.0
    return sigma_eq, beta_opt

def compute_typeII_max(lam, R22, sigma_II_f, tau_II_f):
    lam2 = lam**2
    tau_f = tau_II_f
    sigma_f = sigma_II_f
    # simplified gamma rule (Eq.17) because tau_f > sigma_f
    threshold = -2 * math.sqrt(tau_f**2 + (lam*sigma_f)**2) / ((1+lam2)*sigma_f)
    if (lam2 < 1 and 1 > R22 > threshold) or lam2 >= 1:
        gamma_opt = math.pi/2
    else:
        gamma_opt = 0.5 * math.acos(-lam2)
    sin_g = math.sin(gamma_opt)
    cos_g = math.cos(gamma_opt)
    def eff_s22(s22):
        if s22 > 0:
            term1 = (sin_g**4) / (sigma_f**2)
            term2 = (lam2 * sin_g**2 + sin_g**2 * cos_g**2) / (tau_f**2)
            return s22 * math.sqrt(term1 + term2)
        else:
            return abs(s22 * sin_g) / tau_f * math.sqrt(lam2 + cos_g**2)
    sig_max = max(eff_s22(1.0), eff_s22(R22))
    return sig_max, gamma_opt


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
    return {
        'strengths': {'sigma_I_f': 980, 'sigma_II_f': 48, 'tau_II_f': 70},
        'conditions': spec.get('conditions', []),
        'tol_angle': spec.get('steps', [{}])[0].get('tolerance_angle', 0.001),
        'tol_rel': spec.get('steps', [{}])[0].get('tolerance_stress_rel', 0.01),
        'tol_abs': spec.get('steps', [{}])[0].get('tolerance_stress_abs', 0.01),
    }


# === block: score_0 (check id='critical_plane_prediction') ===
def score_0(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    if not rows:
        return 0.0
    lookup = {}
    for r in rows:
        cid = r.get('condition_id', '').strip()
        if cid:
            lookup[cid] = r

    conds = ctx['conditions']
    tol_a = ctx['tol_angle']
    tol_r = ctx['tol_rel']
    tol_a_stress = ctx['tol_abs']

    sigma_I_f = ctx['strengths']['sigma_I_f']
    sigma_II_f = ctx['strengths']['sigma_II_f']
    tau_II_f = ctx['strengths']['tau_II_f']

    total = len(conds)
    if total == 0:
        return 1.0

    pass_cnt = 0
    for c in conds:
        cid = c['id']
        row = lookup.get(cid)
        if not row:
            continue
        lam = c['lam']
        varsigma = c['varsigma']
        R22 = c['R22']
        sign = c['sign_sigma12']

        # compute gold
        sigmaI_eq, beta_I = compute_typeI_max(varsigma, lam, sign, R22, sigma_I_f)
        sigmaII_eq, gamma_II = compute_typeII_max(lam, R22, sigma_II_f, tau_II_f)
        gamma_I = math.pi/2
        beta_II = 0.0

        if sigmaI_eq > sigmaII_eq:
            gold_type = 'I'
            gold_beta = beta_I
            gold_gamma = gamma_I
            gold_sigmaI = sigmaI_eq
            gold_sigmaII = sigmaII_eq
        else:
            gold_type = 'II'
            gold_beta = beta_II
            gold_gamma = gamma_II
            gold_sigmaI = sigmaI_eq
            gold_sigmaII = sigmaII_eq

        try:
            a_type = str(row.get('critical_plane_type', '')).strip()
            a_beta = float(row.get('beta_c', 0))
            a_gamma = float(row.get('gamma_c', 0))
            a_sigmaI = float(row.get('max_sigma_I_eq', 0))
            a_sigmaII = float(row.get('max_sigma_II_eq', 0))
        except (ValueError, TypeError):
            continue

        if a_type != gold_type:
            continue
        if abs(a_beta - gold_beta) > tol_a or abs(a_gamma - gold_gamma) > tol_a:
            continue
        def ok(val, gold):
            if gold == 0:
                return abs(val) <= tol_a_stress
            err = abs(val - gold) / abs(gold)
            return err <= tol_r or abs(val - gold) <= tol_a_stress
        if not ok(a_sigmaI, gold_sigmaI) or not ok(a_sigmaII, gold_sigmaII):
            continue
        pass_cnt += 1

    return pass_cnt / total


_SCORERS = {
    'critical_plane_prediction': score_0,
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
