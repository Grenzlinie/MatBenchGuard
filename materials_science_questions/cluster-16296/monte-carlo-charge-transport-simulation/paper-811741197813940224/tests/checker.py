import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    # InAs parameters
    m_e0 = 9.10938356e-31          # kg
    e_charge = 1.602176634e-19      # C
    eps0 = 8.854187817e-12         # F/m
    kappa = 15.15                  # relative permittivity
    c_light = 2.99792458e8         # m/s

    m_e_Gamma = 0.022 * m_e0
    m_h = 0.60 * m_e0
    alpha_Gamma_eV = 2.2           # eV^-1
    alpha_Gamma_SI = alpha_Gamma_eV / e_charge  # J^-1

    Eg_eV = 0.355
    n_eq_cm3 = 2e16                # cm^-3
    n_eq_m3 = n_eq_cm3 * 1e6       # m^-3
    m_eq = m_e_Gamma               # equilibrium electrons in Gamma valley

    # Absorption coefficient table (hm : alpha_um)
    alpha_dict_um = {
        0.50: 0.7, 0.70: 1.0, 1.00: 2.0, 1.20: 3.0, 1.40: 5.6,
        1.50: 6.6, 1.55: 7.0, 1.60: 7.5, 1.70: 8.5, 1.80: 9.7,
        1.90: 11.0, 2.00: 13.0
    }
    alpha_hv_keys = sorted(alpha_dict_um.keys())

    def get_alpha_um(hv):
        if hv <= alpha_hv_keys[0]:
            return alpha_dict_um[alpha_hv_keys[0]]
        if hv >= alpha_hv_keys[-1]:
            return alpha_dict_um[alpha_hv_keys[-1]]
        for i in range(len(alpha_hv_keys)-1):
            hv1, hv2 = alpha_hv_keys[i], alpha_hv_keys[i+1]
            if hv1 <= hv <= hv2:
                a1, a2 = alpha_dict_um[hv1], alpha_dict_um[hv2]
                return a1 + (a2-a1)*(hv-hv1)/(hv2-hv1)
        return 0.0

    def gamma_of_hv(hv_eV):
        if hv_eV <= 1.2:
            return 1.7e12
        elif hv_eV >= 1.55:
            return 3.3e12
        else:
            return 1.7e12 + (3.3e12-1.7e12)*(hv_eV-1.2)/(1.55-1.2)

    def compute_e_eV(hv_eV):
        dE = hv_eV - Eg_eV
        if dE <= 0:
            return 0.0
        num = 2 * dE * m_h
        den = (m_e_Gamma + m_h + math.sqrt((m_e_Gamma+m_h)**2 + 4*alpha_Gamma_eV*dE*m_e_Gamma*m_h))
        return num / den

    def v_te2(epsilon_e_J):
        a = alpha_Gamma_SI * epsilon_e_J
        return (2 * epsilon_e_J / (3 * m_e_Gamma)) * (1 + a) / (1 + 4*a*(1 + a))

    def effective_mass_e0(epsilon_e_J):
        a = alpha_Gamma_SI * epsilon_e_J
        return m_e_Gamma * 3 * ((1 + 4*a*(1+a))**1.5) / (3 + 8*a*(1+a))

    def W_THz_formula(n_exc_m3, gamma, v_t2, m_star):
        # Eq. 24
        factor = 4 * kappa * eps0 * m_star * v_t2 / e_charge  # Note: This factor differs from Eq. 24 because Eq. 24 has different pre-factor.
        # Actually Eq. 24 as written: W = (e^2 n_exc^2 v_t^4 (omega_exc^2 - gamma^2/4)^{3/2}) / (6 pi kappa c^3 omega_exc^4) * F(p)
        # We'll compute exactly.
        omega_exc_sq = e_charge**2 * n_exc_m3 / (kappa * eps0 * m_star)
        omega_eq_sq = e_charge**2 * n_eq_m3 / (kappa * eps0 * m_eq)
    
        rad = omega_exc_sq - gamma**2 / 4.0
        if rad <= 0:
            return 0.0
        omega_exc = math.sqrt(omega_exc_sq)
        gamma_term = math.sqrt(rad)
        p = gamma / gamma_term
        p2 = p * p
        # bracket F(p)
        # handle p->0: arctan(1/p) etc blow up, but the expression has limit.
        if p < 1e-12:
            # limit: F = (4/3) * (pi/2 - pi/2? Actually limit as p->0: 2 arctan(1/p) - arctan(2/p) -> 2*(pi/2) - (pi/2) = pi/2; other terms vanish.
            # So F = (4/3)*pi/2 = 2*pi/3.
            F = 2 * math.pi / 3.0
        else:
            term_arctan = 2 * math.atan(1.0/p) - math.atan(2.0/p)
            term1 = (4.0/3.0 - p2) * term_arctan
            term2 = (2.0*p - p**3/2.0) * math.log(p)
            term3 = (p**3/3.0 - 2.0*p) * math.log(p2 + 1)
            term4 = (p - p**3/12.0) * math.log(p2 + 4)
            F = term1 + term2 + term3 + term4
    
        v_t4 = v_t2 * v_t2
        num = e_charge**2 * (n_exc_m3**2) * v_t4 * (rad**1.5)
        den = 6 * math.pi * kappa * c_light**3 * (omega_exc_sq**2)   # omega_exc^4 = (omega_exc_sq)^2
        W = num / den * F
    
        # Verify with Eq. 24's pre-factor: They had e^2 n_exc^2 v_t^4 (omega_exc^2 - gamma^2/4)^(3/2) / (6πκ c^3 ω_exc^4) * [...].
        # So correct.
        return W

    # Build gold data
    hv_list = [0.5 + 0.1*i for i in range(16)]   # 0.5 .. 2.0
    gold_data = {}
    for hv in hv_list:
        hv = round(hv, 1)
        eps_e_eV = compute_e_eV(hv)
        eps_e_J = eps_e_eV * e_charge
        v_te2_val = v_te2(eps_e_J)
        me0_val = effective_mass_e0(eps_e_J)
        m_star_val = 1.0 / (1.0/me0_val + 1.0/m_h)
        eps_h_eV = (hv - Eg_eV) - eps_e_eV
        eps_h_J = max(eps_h_eV, 0.0) * e_charge
        v_th2_val = 2 * eps_h_J / (3 * m_h)
        v_t2_val = v_te2_val - v_th2_val
        if v_t2_val < 0:
            v_t2_val = 0.0
        gamma = gamma_of_hv(hv)
        alpha_um = get_alpha_um(hv)
        alpha_cm = alpha_um * 1e4      # cm^-1
        for I_p in [1e13, 1e14]:
            n_exc_cm3 = alpha_cm * I_p
            n_exc_m3 = n_exc_cm3 * 1e6
            W = W_THz_formula(n_exc_m3, gamma, v_t2_val, m_star_val)
            gold_data[(hv, I_p)] = W

    return {"gold_data": gold_data, "hv_list": hv_list}


# === block: score_0 (check id='recompute_WTHz') ===
def score_0(artifact, step, ctx):
    tol = step.get('params', {}).get('tolerance_rel', 0.05)
    rows = artifact
    gold = ctx['gold_data']
    scores = []
    for r in rows:
        try:
            hv = round(float(r['photon_energy_eV']), 1)
            fluence = float(r['fluence_cm-2'])
            W_agent = float(r['W_THz_J'])
        except (KeyError, ValueError):
            scores.append(0.0)
            continue
        key = (hv, fluence)
        if key not in gold:
            scores.append(0.0)
            continue
        W_gold = gold[key]
        if abs(W_gold) < 1e-30:
            scores.append(1.0 if abs(W_agent) < 1e-30 else 0.0)
            continue
        rel_err = abs(W_agent - W_gold) / abs(W_gold)
        scores.append(1.0 if rel_err <= tol else 0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='scaling_exponent') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    thresh = params.get('low_energy_threshold_eV', 1.5)
    low_min = params.get('low_exp_min', 1.5)
    low_max = params.get('low_exp_max', 2.0)
    high_max = params.get('high_exp_max', 1.0)

    rows = artifact
    # build dict hv -> (W13, W14)
    from collections import defaultdict
    hv_flu = defaultdict(dict)
    for r in rows:
        try:
            hv = round(float(r['photon_energy_eV']), 1)
            flu = float(r['fluence_cm-2'])
            w = float(r['W_THz_J'])
        except (KeyError, ValueError):
            continue
        hv_flu[hv][flu] = w

    valid_count = 0
    pass_count = 0
    for hv, d in hv_flu.items():
        if 1e13 not in d or 1e14 not in d:
            continue
        w1 = d[1e13]
        w2 = d[1e14]
        if w1 <= 0 or w2 <= 0:
            continue
        valid_count += 1
        k = math.log(w2/w1) / math.log(10.0)
        if hv < thresh:
            if low_min <= k <= low_max:
                pass_count += 1
        else:
            if k < high_max:
                pass_count += 1
    if valid_count == 0:
        return 0.0
    return pass_count / valid_count


_SCORERS = {
    'recompute_WTHz': score_0,
    'scaling_exponent': score_1,
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
