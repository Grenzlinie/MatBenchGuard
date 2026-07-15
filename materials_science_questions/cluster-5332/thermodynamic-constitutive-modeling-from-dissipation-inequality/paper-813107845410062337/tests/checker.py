import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import numpy as np

# 5-point Gauss-Legendre nodes and weights (order 5)
GAUSS_NODES = np.array([-0.906179845938664, -0.538469310105683, 0.0, 0.538469310105683, 0.906179845938664])
GAUSS_WEIGHTS = np.array([0.236926885056189, 0.478628670499366, 0.568888888888889, 0.478628670499366, 0.236926885056189])

def gauss_quad_5(fn, a, b):
    mid = 0.5*(b + a)
    half_len = 0.5*(b - a)
    return half_len * np.sum(GAUSS_WEIGHTS * fn(mid + half_len*GAUSS_NODES))

# material constants
mu_e = 0.1      # MPa
alpha_e = 30.0
m_e = 1.0       # T^2
mu0 = 4e-7 * math.pi  # N/A^2
c2_val = 0.5 * mu0
Theta0 = 293.0  # K
A_i_mm = 10.0   # mm

def compute_params(row):
    lambda_i = float(row['lambda_i'])
    lambda_z = float(row['lambda_z'])
    zeta = float(row['zeta'])
    c = float(row['c'])
    Theta_e = float(row['Theta_e'])
    A_e = zeta * A_i_mm
    a_i = lambda_i * A_i_mm
    a_e_sq = a_i**2 + (A_e**2 - A_i_mm**2)/lambda_z
    a_e = math.sqrt(a_e_sq)
    b = A_i_mm**2 - lambda_z * a_i**2
    k2 = (Theta_e - Theta0) / (math.log(a_e) - math.log(a_i))
    k1 = (Theta0*math.log(a_e) - Theta_e*math.log(a_i)) / (math.log(a_e) - math.log(a_i))
    return lambda_i, lambda_z, zeta, c, Theta_e, a_i, a_e, b, k1, k2

def R2(r, lambda_z, b):
    return lambda_z * r**2 + b

def I4(r, lambda_z, b, c):
    return c**2 / R2(r, lambda_z, b)

def Omega1(r, k1, k2, lambda_z, b, c):
    theta = k1 + k2*math.log(r)
    a = alpha_e * math.tanh(I4(r, lambda_z, b, c)/m_e)
    return (theta/Theta0) * (mu_e/4) * (1.0 + a)

def lambda_r(r, lambda_z, b):
    R = math.sqrt(R2(r, lambda_z, b))
    return r / R

def compute_pressure(lambda_i, lambda_z, a_i, a_e, b, k1, k2, c, zeta):
    lam_i = lambda_i
    lam_e = a_e/(zeta * A_i_mm)
    term1 = (mu_e/(2*Theta0)) * k1 * ( (1.0/lambda_z)*math.log(lam_i/lam_e) - (1.0/(2*lambda_z**2))*(1.0/lam_i**2 - 1.0/lam_e**2) )
    term2_integral = (mu_e/(2*Theta0)) * k2 * gauss_quad_5(lambda r: r*math.log(r)/(lambda_z*r**2 + b), a_i, a_e)
    term2_anal = (mu_e/(2*Theta0)) * k2 * (
        (1.0/(2*lambda_z))*(math.log(a_e)**2 - math.log(a_i)**2) -
        (b/(lambda_z**2))*((math.log(a_e)/(2*a_e**2)) - (math.log(a_i)/(2*a_i**2)) + (1.0/4)*(a_e**-2 - a_i**-2))
    )
    term2 = term2_integral - term2_anal
    def term3_integrand(r):
        lam = lambda_r(r, lambda_z, b)
        return (k1/r) * alpha_e * math.tanh(I4(r, lambda_z, b, c)/m_e) * (lam**2 / (lambda_z*r**2 + b))
    term3 = (mu_e/(2*Theta0)) * gauss_quad_5(term3_integrand, a_i, a_e)
    def term4_integrand(r):
        lam = lambda_r(r, lambda_z, b)
        return (k2*math.log(r)/r) * alpha_e * math.tanh(I4(r, lambda_z, b, c)/m_e) * (lam**2 / (lambda_z*r**2 + b))
    term4 = (mu_e/(2*Theta0)) * gauss_quad_5(term4_integrand, a_i, a_e)
    def term5_integrand(r):
        lam = lambda_r(r, lambda_z, b)
        return (k1/r) * alpha_e * math.tanh(I4(r, lambda_z, b, c)/m_e) * ((lambda_z*r**2 + b)/(lambda_z**2 * r**2))
    term5 = (mu_e/(2*Theta0)) * gauss_quad_5(term5_integrand, a_i, a_e)
    def term6_integrand(r):
        lam = lambda_r(r, lambda_z, b)
        return (k2*math.log(r)/r) * alpha_e * math.tanh(I4(r, lambda_z, b, c)/m_e) * ((lambda_z*r**2 + b)/(lambda_z**2 * r**2))
    term6 = (mu_e/(2*Theta0)) * gauss_quad_5(term6_integrand, a_i, a_e)
    P1 = term1 + term2 + term3 + term4 - term5 - term6
    P2 = (0.5 * mu0 * c**2 * (1.0 - k1/Theta0) * (1.0/a_i**2 - 1.0/a_e**2)
          - (k2 * c**2 * mu0 / (4*Theta0)) * (a_i**-2 - a_e**-2)
          + (k2 * c**2 * mu0 / (2*Theta0)) * (math.log(a_e)/a_e**2 - math.log(a_i)/a_i**2) )
    return P1 + P2

def compute_normal_force(lambda_i, lambda_z, a_i, a_e, b, k1, k2, c, P):
    N1_force = math.pi * a_i**2 * P
    def integrand_N2(r):
        lam = lambda_r(r, lambda_z, b)
        return r * (2*lambda_z**2 - 1.0/(lam**2 * lambda_z**2) - lam**2) * Omega1(r, k1, k2, lambda_z, b, c)
    N2_force = 2 * math.pi * gauss_quad_5(integrand_N2, a_i, a_e)
    N3_force = mu0 * math.pi * c**2 * (
        (k1/Theta0 - lambda_z**(-2))*math.log(a_e/a_i)
        + (k2/(2*Theta0))*(math.log(a_e)**2 - math.log(a_i)**2)
    )
    N_force = N1_force + N2_force + N3_force
    return N_force / (math.pi * A_i_mm**2)

def compute_torque(lambda_z, zeta, c, Theta_e, tau, a_i, a_e, k1, k2):
    b = 0.0
    term_a = (k1/4)*(a_e**4 - a_i**4)
    term_b = (k2/16)*(a_e**4*(4*math.log(a_e)-1) - a_i**4*(4*math.log(a_i)-1))
    M1 = (mu_e * math.pi * tau * lambda_z**2 / Theta0) * (term_a + term_b)
    def integrand_M2(r):
        return k1 * r**2 * alpha_e * math.tanh(c**2 / (lambda_z * r**2 + b))
    M2 = (mu_e * math.pi * tau * lambda_z**2 / Theta0) * gauss_quad_5(integrand_M2, a_i, a_e)
    def integrand_M3(r):
        return k2 * r**2 * math.log(r) * alpha_e * math.tanh(c**2 / (lambda_z * r**2 + b))
    M3 = (mu_e * math.pi * tau * lambda_z**2 / Theta0) * gauss_quad_5(integrand_M3, a_i, a_e)
    M_Nmm = M1 + M2 + M3
    return M_Nmm / 1000.0


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
    return {}


# === block: score_0 (check id='step_02_bvp1') ===
def score_0(artifact, step, ctx):
    def gauss_quad_5_scalar(fn, a, b):
        nodes = [-0.906179845938664, -0.538469310105683, 0.0, 0.538469310105683, 0.906179845938664]
        weights = [0.236926885056189, 0.478628670499366, 0.568888888888889, 0.478628670499366, 0.236926885056189]
        mid = 0.5*(b + a)
        half_len = 0.5*(b - a)
        s = 0.0
        for i in range(5):
            s += weights[i] * fn(mid + half_len * nodes[i])
        return half_len * s

    def compute_pressure_local(lambda_i, lambda_z, a_i, a_e, b, k1, k2, c, zeta):
        lam_i = lambda_i
        lam_e = a_e/(zeta * A_i_mm)
        term1 = (mu_e/(2*Theta0)) * k1 * ( (1.0/lambda_z)*math.log(lam_i/lam_e) - (1.0/(2*lambda_z**2))*(1.0/lam_i**2 - 1.0/lam_e**2) )
        term2_integral = (mu_e/(2*Theta0)) * k2 * gauss_quad_5_scalar(lambda r: r*math.log(r)/(lambda_z*r**2 + b), a_i, a_e)
        term2_anal = (mu_e/(2*Theta0)) * k2 * (
            (1.0/(2*lambda_z))*(math.log(a_e)**2 - math.log(a_i)**2) -
            (b/(lambda_z**2))*((math.log(a_e)/(2*a_e**2)) - (math.log(a_i)/(2*a_i**2)) + (1.0/4)*(a_e**-2 - a_i**-2))
        )
        term2 = term2_integral - term2_anal
        def term3_integrand(r):
            lam = r / math.sqrt(lambda_z*r**2 + b)
            return (k1/r) * alpha_e * math.tanh((c**2 / (lambda_z*r**2 + b))/m_e) * (lam**2 / (lambda_z*r**2 + b))
        term3 = (mu_e/(2*Theta0)) * gauss_quad_5_scalar(term3_integrand, a_i, a_e)
        def term4_integrand(r):
            lam = r / math.sqrt(lambda_z*r**2 + b)
            return (k2*math.log(r)/r) * alpha_e * math.tanh((c**2 / (lambda_z*r**2 + b))/m_e) * (lam**2 / (lambda_z*r**2 + b))
        term4 = (mu_e/(2*Theta0)) * gauss_quad_5_scalar(term4_integrand, a_i, a_e)
        def term5_integrand(r):
            lam = r / math.sqrt(lambda_z*r**2 + b)
            return (k1/r) * alpha_e * math.tanh((c**2 / (lambda_z*r**2 + b))/m_e) * ((lambda_z*r**2 + b)/(lambda_z**2 * r**2))
        term5 = (mu_e/(2*Theta0)) * gauss_quad_5_scalar(term5_integrand, a_i, a_e)
        def term6_integrand(r):
            lam = r / math.sqrt(lambda_z*r**2 + b)
            return (k2*math.log(r)/r) * alpha_e * math.tanh((c**2 / (lambda_z*r**2 + b))/m_e) * ((lambda_z*r**2 + b)/(lambda_z**2 * r**2))
        term6 = (mu_e/(2*Theta0)) * gauss_quad_5_scalar(term6_integrand, a_i, a_e)
        P1 = term1 + term2 + term3 + term4 - term5 - term6
        P2 = (0.5 * mu0 * c**2 * (1.0 - k1/Theta0) * (1.0/a_i**2 - 1.0/a_e**2)
              - (k2 * c**2 * mu0 / (4*Theta0)) * (a_i**-2 - a_e**-2)
              + (k2 * c**2 * mu0 / (2*Theta0)) * (math.log(a_e)/a_e**2 - math.log(a_i)/a_i**2) )
        return P1 + P2

    def compute_normal_force_local(lambda_i, lambda_z, a_i, a_e, b, k1, k2, c, P, zeta):
        N1_force = math.pi * a_i**2 * P
        def integrand_N2(r):
            lam = r / math.sqrt(lambda_z*r**2 + b)
            theta = k1 + k2*math.log(r)
            a = alpha_e * math.tanh((c**2 / (lambda_z*r**2 + b))/m_e)
            Omega1_val = (theta/Theta0) * (mu_e/4) * (1.0 + a)
            return r * (2*lambda_z**2 - 1.0/(lam**2 * lambda_z**2) - lam**2) * Omega1_val
        N2_force = 2 * math.pi * gauss_quad_5_scalar(integrand_N2, a_i, a_e)
        N3_force = mu0 * math.pi * c**2 * (
            (k1/Theta0 - lambda_z**(-2))*math.log(a_e/a_i)
            + (k2/(2*Theta0))*(math.log(a_e)**2 - math.log(a_i)**2)
        )
        N_force = N1_force + N2_force + N3_force
        return N_force / (math.pi * A_i_mm**2)

    rows = artifact
    tol_rtol = step.get('tolerance_relative', 0.01)
    tol_atol = step.get('tolerance_absolute', 1e-8)
    score_sum = 0.0
    for row in rows:
        lambda_i, lambda_z, zeta, c, Theta_e, a_i, a_e, b, k1, k2 = compute_params(row)
        P_exp = compute_pressure_local(lambda_i, lambda_z, a_i, a_e, b, k1, k2, c, zeta)
        N_exp = compute_normal_force_local(lambda_i, lambda_z, a_i, a_e, b, k1, k2, c, P_exp, zeta)
        P_ag = float(row['P'])
        N_ag = float(row['N'])
        err_P = abs(P_ag - P_exp) / max(abs(P_exp), tol_atol)
        err_N = abs(N_ag - N_exp) / max(abs(N_exp), tol_atol)
        if err_P <= tol_rtol and err_N <= tol_rtol:
            score_sum += 1.0
    if rows:
        return score_sum / len(rows)
    else:
        return 0.0


# === block: score_1 (check id='step_03_bvp2') ===
def score_1(artifact, step, ctx):
    rows = artifact
    tol_rtol = step.get('tolerance_relative', 0.01)
    tol_atol = step.get('tolerance_absolute', 1e-8)
    score_sum = 0.0
    for row in rows:
        lambda_z = float(row['lambda_z'])
        zeta = float(row['zeta'])
        c = float(row['c'])
        Theta_e = float(row['Theta_e'])
        tau = float(row['tau'])
        A_e = zeta * A_i_mm
        a_i = A_i_mm / math.sqrt(lambda_z)
        a_e = A_e / math.sqrt(lambda_z)
        k2 = (Theta_e - Theta0) / (math.log(a_e) - math.log(a_i))
        k1 = (Theta0*math.log(a_e) - Theta_e*math.log(a_i)) / (math.log(a_e) - math.log(a_i))
        M_exp = compute_torque(lambda_z, zeta, c, Theta_e, tau, a_i, a_e, k1, k2)
        M_ag = float(row['M'])
        err_M = abs(M_ag - M_exp) / max(abs(M_exp), tol_atol)
        if err_M <= tol_rtol:
            score_sum += 1.0
    if rows:
        return score_sum / len(rows)
    else:
        return 0.0


_SCORERS = {
    'step_02_bvp1': score_0,
    'step_03_bvp2': score_1,
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
