import os
import json
import csv

# === author imports / helpers ===
import math
import json
import csv

def _bisect(f, a, b, tol=1e-8, maxiter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(maxiter):
        c = (a + b) / 2.0
        fc = f(c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2.0


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
    # Physical constants and material parameters (all publicly declared)
    k_B = 1.380649e-16   # erg/K
    mu_B = 9.274e-21      # erg/G
    B0 = 1.5e12           # erg/cm^3
    n = 2.4e22            # cm^{-3}
    gamma = 2e-13         # erg
    epsilon = -5e-10      # erg
    Tc0 = 121.0           # K
    s = 0.5               # spin
    GPa_to_erg_cm3 = 1e10

    ctx = dict(k_B=k_B, mu_B=mu_B, B0=B0, n=n, gamma=gamma, epsilon=epsilon, Tc0=Tc0, s=s, GPa_to_erg_cm3=GPa_to_erg_cm3)
    return ctx


# === block: score_0 (check id='step_compute_b') ===
def score_0(artifact, step, ctx):
    import math

    try:
        rows = artifact   # list of dicts
        P_list = []
        B_submitted = []
        for row in rows:
            P_list.append(float(row['pressure_GPa']))
            B_submitted.append(float(row['B_value']))
    except Exception:
        return 0.0

    # helper functions using ctx
    k_B = ctx['k_B']
    B0 = ctx['B0']
    n = ctx['n']
    gamma = ctx['gamma']
    epsilon = ctx['epsilon']
    Tc0 = ctx['Tc0']
    GPa_to_erg_cm3 = ctx['GPa_to_erg_cm3']

    def Tc(P_erg):
        term1 = - (gamma / (2 * k_B * B0)) * P_erg
        term2 = + (epsilon / (12 * k_B * B0**2)) * P_erg**2
        return Tc0 + term1 + term2

    def B_at_Tc(P_GPa):
        P_erg = P_GPa * GPa_to_erg_cm3
        Tc_ = Tc(P_erg)
        gamma_star = gamma - epsilon * P_erg / (3 * B0)
        B_val = 1.0/3.0 - (n / (8 * k_B * Tc_ * B0)) * (gamma_star**2)
        return B_val

    scores = []
    tol = 0.03
    for P, B_sub in zip(P_list, B_submitted):
        B_exp = B_at_Tc(P)
        score_i = max(0.0, 1.0 - abs(B_sub - B_exp)/tol)
        scores.append(score_i)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_1 (check id='step_tricritical') ===
def score_1(artifact, step, ctx):
    import math

    try:
        P_sub = float(artifact['P_t_GPa'])
        T_sub = float(artifact['T_t_K'])
    except Exception:
        return 0.0

    k_B = ctx['k_B']
    B0 = ctx['B0']
    n = ctx['n']
    gamma = ctx['gamma']
    epsilon = ctx['epsilon']
    Tc0 = ctx['Tc0']
    GPa_to_erg_cm3 = ctx['GPa_to_erg_cm3']

    def Tc(P_erg):
        term1 = - (gamma / (2 * k_B * B0)) * P_erg
        term2 = + (epsilon / (12 * k_B * B0**2)) * P_erg**2
        return Tc0 + term1 + term2

    def B_at_Tc(P_GPa):
        P_erg = P_GPa * GPa_to_erg_cm3
        Tc_ = Tc(P_erg)
        gamma_star = gamma - epsilon * P_erg / (3 * B0)
        B_val = 1.0/3.0 - (n / (8 * k_B * Tc_ * B0)) * (gamma_star**2)
        return B_val

    # Use the top-level _bisect instead of scipy.optimize.bisect
    try:
        P_t_ref = _bisect(lambda p: B_at_Tc(p), 0.0, 5.0, tol=1e-8)
        T_t_ref = Tc(P_t_ref * GPa_to_erg_cm3)
    except Exception:
        return 0.0

    err_P = abs(P_sub - P_t_ref) / (0.05 * P_t_ref)   # 5% relative tolerance
    err_T = abs(T_sub - T_t_ref) / (0.05 * T_t_ref)
    score_P = max(0.0, 1.0 - err_P)
    score_T = max(0.0, 1.0 - err_T)
    return min(score_P, score_T)


# === block: score_2 (check id='step_wing_critical') ===
def score_2(artifact, step, ctx):
    import math

    try:
        T_sub = float(artifact['T_cr_K'])
        H_sub = float(artifact['H_cr_T'])
        m_sub = float(artifact['m_cr'])
    except Exception:
        return 0.0

    k_B = ctx['k_B']
    mu_B = ctx['mu_B']
    B0 = ctx['B0']
    n = ctx['n']
    gamma = ctx['gamma']
    epsilon = ctx['epsilon']
    Tc0 = ctx['Tc0']
    GPa_to_erg_cm3 = ctx['GPa_to_erg_cm3']

    P_GPa = 1.4
    P_erg = P_GPa * GPa_to_erg_cm3

    # Tc(P)
    def Tc(P_erg):
        term1 = - (gamma / (2 * k_B * B0)) * P_erg
        term2 = + (epsilon / (12 * k_B * B0**2)) * P_erg**2
        return Tc0 + term1 + term2

    Tc_P = Tc(P_erg)

    # B(T) and C(T)
    def B_T(T):
        gamma_star = gamma - epsilon * P_erg / (3 * B0)
        return 1.0/3.0 * (Tc_P/T)**3 - (n / (8 * k_B * T * B0)) * (gamma_star**2)

    def C_T(T):
        gamma_star = gamma - epsilon * P_erg / (3 * B0)
        t = Tc_P / T
        return (1.0/8.0)*(n/(k_B*T*B0))*(t**2)*gamma_star**2 - (1.0/64.0)*(n**2*epsilon/(k_B*T*B0**2))*gamma_star**2 - (2.0/15.0)*t**5

    def f(T):
        A = (T - Tc_P)/T
        B = B_T(T)
        C = C_T(T)
        return A - (9.0/20.0)*(B**2)/C

    try:
        from scipy.optimize import bisect
        T_cr_ref = bisect(f, Tc_P + 0.1, 200.0, xtol=1e-8)
    except Exception:
        return 0.0

    B_cr = B_T(T_cr_ref)
    C_cr = C_T(T_cr_ref)
    m_cr_ref = math.sqrt( -3.0/10.0 * B_cr / C_cr )
    h_cr_ref = (6.0/25.0)*(B_cr**2 / C_cr) * m_cr_ref
    H_cr_Oe = (k_B * T_cr_ref / mu_B) * h_cr_ref   # Oe (mu_B in erg/G)
    H_cr_T_ref = H_cr_Oe / 1e4                    # convert to Tesla

    err_T = abs(T_sub - T_cr_ref) / (0.1 * T_cr_ref)
    err_H = abs(H_sub - H_cr_T_ref) / (0.1 * H_cr_T_ref)
    err_m = abs(m_sub - m_cr_ref) / (0.15 * m_cr_ref)
    score_T = max(0.0, 1.0 - err_T)
    score_H = max(0.0, 1.0 - err_H)
    score_m = max(0.0, 1.0 - err_m)
    return (score_T + score_H + score_m) / 3.0


_SCORERS = {
    'step_compute_b': score_0,
    'step_tricritical': score_1,
    'step_wing_critical': score_2,
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
