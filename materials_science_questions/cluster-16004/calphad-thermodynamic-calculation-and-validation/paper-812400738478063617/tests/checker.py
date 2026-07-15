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
    ctx = {'expected_fcc': [], 'expected_liquid': []}
    for step in spec['steps']:
        if step['id'] == 'fcc_accuracy':
            ctx['expected_fcc'] = step.get('expected_points', [])
        elif step['id'] == 'liquid_accuracy':
            ctx['expected_liquid'] = step.get('expected_points', [])
    return ctx


# === block: score_0 (check id='fcc_accuracy') ===
def score_0(artifact, step, ctx):
    import math

    # --- Thermodynamic constants and functions for fcc (C-Fe-Ni) ---
    R = 8.31448

    def G_gra(T):
        """Gibbs energy of graphite per mole C (J/mol), SER."""
        return (-17369 + 170.73*T - 24.3*T*math.log(T) - 4.723e-4*T*T
                + 2562600/T - 2.643e8/(T*T) + 1.2e10/(T*T*T))

    def G_fe_va_fcc(T):
        """Gibbs energy of fcc Fe:Va per formula unit (J/mol), T < 1811 K."""
        return (-237.57 + 132.416*T - 24.6643*T*math.log(T)
                - 3.75752e-3*T*T - 5.89269e-8*T**3 + 77358.5/T)

    def G_ni_va_fcc(T):
        """Gibbs energy of fcc Ni:Va per formula unit (J/mol), T < 1728 K."""
        return (-5179.159 + 117.854*T - 22.096*T*math.log(T) - 4.8407e-3*T*T)

    def G_fe_c_fcc(T):
        return G_fe_va_fcc(T) + G_gra(T) + 77207 - 15.877*T

    def G_ni_c_fcc(T):
        return G_ni_va_fcc(T) + G_gra(T) + 45000 + 1.88*T

    def L_Fe_Va_C():
        return -34671

    def L_Ni_Fe_Va_0(T):
        return -12054.355 + 3.27413*T

    def L_Ni_Fe_Va_1(T):
        return 11082.1315 - 4.45077*T

    def L_Ni_Fe_Va_2():
        return -725.805174

    def L_Ni_Fe_C_0(T):
        return 49074 - 7.32*T

    def L_Ni_Fe_C_1():
        return -25800

    def G_mag(y_Fe, y_Ni, y_Va, y_C, T):
        """Magnetic contribution G_mo in J/mol of formula unit."""
        Tc = -201*y_Fe + 633*y_Ni + y_Fe*y_Ni*y_Va*(2133 - 682*(y_Fe - y_Ni))
        if Tc <= 0:
            return 0.0
        B = (-2.1*y_Fe + 0.52*y_Ni
             + y_Fe*y_Ni*y_Va*(9.55 + 7.23*(y_Fe - y_Ni)
                               + 5.93*(y_Fe - y_Ni)**2 + 6.18*(y_Fe - y_Ni)**3))
        # safeguard against log of non-positive
        if B <= -1:
            return 0.0
        t = T / Tc
        if t < 1:
            f = (1.0 - 0.86034*t**(-1) - 0.1745*t**3
                 - 7.755e-3*t**9 - 1.745e-3*t**15)
        else:
            f = (-4.269e-2*t**(-5) - 1.355e-3*t**(-15) - 2.846e-4*t**(-25))
        return R * T * math.log(B + 1.0) * f

    def G_fcc_total(y_Fe, y_Ni, y_C, T):
        """Total Gibbs energy per formula unit (Fe,Ni)_1(C,Va)_1 (J/mol)."""
        y_Va = 1.0 - y_C
        # reference + compound end-members
        G = (y_Ni*y_Va*G_ni_va_fcc(T) + y_Ni*y_C*G_ni_c_fcc(T)
             + y_Fe*y_Va*G_fe_va_fcc(T) + y_Fe*y_C*G_fe_c_fcc(T))
        # ideal mixing
        ideal = y_Ni*math.log(y_Ni) + y_Fe*math.log(y_Fe)  # first sublattice
        ideal += y_C*math.log(y_C) + y_Va*math.log(y_Va)   # second sublattice
        G += R * T * ideal
        # excess sublattice interactions
        # Fe,Ni interaction on first sublattice with C and Va
        L_Ni_Fe_Va = (L_Ni_Fe_Va_0(T) + L_Ni_Fe_Va_1(T)*(y_Fe - y_Ni)
                      + L_Ni_Fe_Va_2()*(y_Fe - y_Ni)**2)
        L_Ni_Fe_C = (L_Ni_Fe_C_0(T) + L_Ni_Fe_C_1()*(y_Fe - y_Ni))
        G += y_Ni*y_Fe*(y_C * L_Ni_Fe_C + y_Va * L_Ni_Fe_Va)
        # Va,C interaction on second sublattice with Fe and Ni
        # L_Fe:Va,C given; assume L_Ni:Va,C = 0
        G += y_Va*y_C*(y_Fe * L_Fe_Va_C() + y_Ni * 0.0)
        # magnetic contribution
        G += G_mag(y_Fe, y_Ni, y_Va, y_C, T)
        return G

    def compute_a_C(y_Fe, y_Ni, y_C, T):
        """Compute carbon activity in fcc phase at given site fractions and T."""
        h = 1e-6
        y_C_plus = y_C + h
        y_C_minus = y_C - h
        if y_C_minus < 0:
            y_C_minus = 0.0
        G_plus = G_fcc_total(y_Fe, y_Ni, y_C_plus, T)
        G_minus = G_fcc_total(y_Fe, y_Ni, y_C_minus, T)
        # chemical potential of C per mole of C
        mu_C = (G_plus - G_minus) / (y_C_plus - y_C_minus) if y_C_plus != y_C_minus else 0.0
        # activity a_C = exp((mu_C - G_gra) / (RT))
        G_gra_T = G_gra(T)
        return math.exp((mu_C - G_gra_T) / (R * T))

    # --- Scoring logic ---
    points = ctx.get('expected_fcc', [])
    tolerance_rel = step.get('tolerance_rel', 0.01)
    if not points:
        return 0.0

    matched = 0.0
    for pt in points:
        target_T = 1273.0
        target_x_Ni = pt['x_Ni']
        target_x_C = pt['x_C']
        # mole fractions sum to 1; compute x_Fe
        x_Fe = 1.0 - target_x_Ni - target_x_C
        if x_Fe < -1e-12:
            continue  # invalid
        # convert to site fractions
        denom = 1.0 - target_x_C
        if denom <= 0:
            continue
        y_Fe = x_Fe / denom
        y_Ni = target_x_Ni / denom
        y_C = target_x_C / denom
        # compute expected activity from paper's model
        try:
            expected_a = compute_a_C(y_Fe, y_Ni, y_C, target_T)
        except Exception:
            expected_a = 0.0
        # find agent's value
        found = None
        for row in artifact:
            try:
                T = float(row['T'])
                x_Ni = float(row['x_Ni'])
                x_C = float(row['x_C'])
                if abs(T - target_T) < 1e-6 and abs(x_Ni - target_x_Ni) < 1e-9 and abs(x_C - target_x_C) < 1e-9:
                    found = float(row['a_C'])
                    break
            except (KeyError, ValueError):
                continue
        if found is not None and expected_a > 1e-12:
            rel_err = abs(found - expected_a) / expected_a
            if rel_err <= tolerance_rel:
                matched += 1.0
            else:
                matched += max(0.0, 1.0 - (rel_err - tolerance_rel) / tolerance_rel)
        elif found is not None and expected_a <= 1e-12:
            # if expected nearly zero, accept if found also nearly zero
            if abs(found) < 1e-12:
                matched += 1.0

    return matched / len(points)


# === block: score_1 (check id='liquid_accuracy') ===
def score_1(artifact, step, ctx):
    import math

    # --- Thermodynamic constants and functions for liquid C-Fe-Ni ---
    R = 8.31448
    T_target = 1823.0

    def G_gra(T):
        """Gibbs energy of graphite per mole C (J/mol), SER."""
        return (-17369 + 170.73*T - 24.3*T*math.log(T) - 4.723e-4*T*T
                + 2562600/T - 2.643e8/(T*T) + 1.2e10/(T*T*T))

    # Liquid pure-element Gibbs energies (high-T expressions for Fe and Ni at 1823 K)
    def G_C_liq(T):
        return (100000 + 146.1*T - 24.3*T*math.log(T) - 4.723e-4*T*T
                + 2562600/T - 2.643e8/(T*T) + 1.2e10/(T*T*T))

    def G_Fe_liq(T):
        # above 1811 K
        return -10839.7 + 291.302*T - 46*T*math.log(T)

    def G_Ni_liq(T):
        # above 1728 K
        return -9549.775 + 268.598*T - 43.1*T*math.log(T)

    # Binary interaction parameters
    def L0_FeC(T):   return -124320 + 28.5*T
    def L1_FeC():     return 19300
    def L2_FeC(T):    return 49260 - 19*T
    def L0_NiC(T):   return -110160 + 34.6*T
    def L0_FeNi(T):  return -18378.86 + 6.03912*T
    def L1_FeNi(T):  return 9228.1 - 3.54642*T

    def excess_liq(x_C, x_Fe, x_Ni, T):
        """Excess Gibbs energy per mole of atoms (J/mol)."""
        # Fe-C binary (Redlich-Kister up to k=2)
        d_FeC = (x_Fe - x_C)
        ex = x_Fe * x_C * (L0_FeC(T) + L1_FeC()*d_FeC + L2_FeC(T)*d_FeC*d_FeC)
        # Ni-C binary (only k=0)
        ex += x_Ni * x_C * L0_NiC(T)
        # Fe-Ni binary (k=0,1)
        d_FeNi = (x_Fe - x_Ni)
        ex += x_Fe * x_Ni * (L0_FeNi(T) + L1_FeNi(T)*d_FeNi)
        # ternary term
        L_ternary = 122200 - 58.8*T - 30000*(x_Fe - x_Ni)
        ex += x_C * x_Fe * x_Ni * L_ternary
        return ex

    def G_liq_molar(x_C, x_Fe, x_Ni, T):
        """Total Gibbs energy per mole of atoms."""
        G = (x_C*G_C_liq(T) + x_Fe*G_Fe_liq(T) + x_Ni*G_Ni_liq(T))
        # ideal mixing
        if x_C > 0: G += x_C * math.log(x_C)
        if x_Fe > 0: G += x_Fe * math.log(x_Fe)
        if x_Ni > 0: G += x_Ni * math.log(x_Ni)
        G *= R * T
        G += excess_liq(x_C, x_Fe, x_Ni, T)
        return G

    def mu_C_from_composition(x_C, x_Ni, T):
        """Chemical potential of carbon via finite difference of extensive G."""
        x_Fe = 1.0 - x_C - x_Ni
        if x_Fe < -1e-12:
            return None
        base_Ntotal = 1.0
        N_C = x_C * base_Ntotal
        N_Fe = x_Fe * base_Ntotal
        N_Ni = x_Ni * base_Ntotal
        eps = 1e-6
        def Gext(N_C, N_Fe, N_Ni, T):
            tot = N_C + N_Fe + N_Ni
            xc = N_C / tot
            xf = N_Fe / tot
            xn = N_Ni / tot
            return tot * G_liq_molar(xc, xf, xn, T)
        G0 = Gext(N_C, N_Fe, N_Ni, T)
        Gp = Gext(N_C + eps, N_Fe, N_Ni, T)
        return (Gp - G0) / eps

    def solve_x_C_saturated(x_Ni, T):
        """Bisection solve for x_C s.t. mu_C == G_gra."""
        Ggra = G_gra(T)
        lo = 0.0
        hi = 1.0 - x_Ni - 1e-9
        if hi <= lo:
            return 0.0
        # ensure sign change: mu_C(lo) <= Ggra and mu_C(hi) >= Ggra (should be decreasing/increasing?)
        # Typically solubility increases with temperature, so at given x_Ni high x_C has high mu_C.
        mu_lo = mu_C_from_composition(lo, x_Ni, T)
        if mu_lo is None: return 0.0
        if mu_lo >= Ggra:
            return lo
        mu_hi = mu_C_from_composition(hi, x_Ni, T)
        if mu_hi is None or mu_hi <= Ggra:
            return hi if mu_hi is not None else 0.0
        for _ in range(100):
            mid = (lo + hi) / 2.0
            mu_mid = mu_C_from_composition(mid, x_Ni, T)
            if mu_mid is None:
                hi = mid
                continue
            diff = mu_mid - Ggra
            if abs(diff) < 1e-8:
                return mid
            if diff > 0:
                hi = mid
            else:
                lo = mid
        return (lo + hi) / 2.0

    # --- Scoring logic ---
    points = ctx.get('expected_liquid', [])
    tolerance_rel = step.get('tolerance_rel', 0.01)
    if not points:
        return 0.0

    matched = 0.0
    for pt in points:
        target_x_Ni = pt['x_Ni_liquid']
        # Compute expected solubility from paper's model
        expected = solve_x_C_saturated(target_x_Ni, T_target)
        if expected <= 1e-12:
            # fallback to 0 if model yields zero
            expected = 0.0
        # Find agent's value
        found = None
        for row in artifact:
            try:
                T = float(row['T'])
                x_Ni = float(row['x_Ni_liquid'])
                x_C = float(row['x_C_saturated'])
                if abs(T - T_target) < 1e-6 and abs(x_Ni - target_x_Ni) < 1e-9:
                    found = float(row['x_C_saturated'])
                    break
            except (KeyError, ValueError):
                continue
        if found is not None and expected > 1e-12:
            rel_err = abs(found - expected) / expected
            if rel_err <= tolerance_rel:
                matched += 1.0
            else:
                matched += max(0.0, 1.0 - (rel_err - tolerance_rel) / tolerance_rel)
        elif found is not None and expected <= 1e-12:
            if abs(found) < 1e-12:
                matched += 1.0

    return matched / len(points)


_SCORERS = {
    'fcc_accuracy': score_0,
    'liquid_accuracy': score_1,
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
