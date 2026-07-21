import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import itertools

def compute_expected():
    # ---------- parameters ----------
    sigma0 = 1.0e8
    epsilon0 = 8.854187817e-12
    epsilon = 10.0 * epsilon0
    q = 1.602176634e-19
    Omega = 1.0e-29
    gamma = 1.0e-12
    a_D = 1.0e-7
    lam = 1.0e3
    v = 0.9
    delta = 1.0e-6
    Gamma_s = 1.0e3 * a_D
    K_I = 1.0e6
    K_II = 1.0e6
    # vectors
    n = [1.0/math.sqrt(3.0)] * 3
    m = [1.0/math.sqrt(2.0), -1.0/math.sqrt(2.0), 0.0]
    e = m[:]  # same as m
    # sound
    omega = 1.0e6
    tau_sigma = 1.0e-3
    rho = 5.0e3
    ct = 3.0e3
    C11 = 1.2e11
    C12 = 0.6e11
    C44 = 0.6e11

    pi = math.pi
    beta = math.sqrt(1.0 - v*v)
    v_sq = v*v
    v_sqrt = math.sqrt(v)
    v_sqrt3 = v**1.5

    sqrt_lambda_delta_aD = math.sqrt(lam * delta * a_D)
    delta_over_lambda_aD = delta / (lam * a_D)

    # triple contraction for shock front
    triple_cont = 6.0 * gamma * n[0]*n[1]*n[2]

    exp = {}

    # ---------- shock wave ----------
    Q_shock_dilat = sigma0 * (epsilon * Omega) / (12.0 * pi * q)
    Q_shock_piezo = sigma0 * triple_cont
    exp['Q_shock_dilat'] = Q_shock_dilat
    exp['Q_shock_piezo'] = Q_shock_piezo
    exp['Q_shock_total'] = Q_shock_dilat + Q_shock_piezo

    D_shock_dilat = sigma0 * (epsilon * Omega) / (12.0 * pi * q)
    D_shock_piezo = sigma0 * lam * a_D * triple_cont
    exp['D_shock_dilat'] = D_shock_dilat
    exp['D_shock_piezo'] = D_shock_piezo
    exp['D_shock_total'] = D_shock_dilat + D_shock_piezo

    # ---------- crack: common----------
    epsilon_Omega_over_4pi_q = (epsilon * Omega) / (4.0 * pi * q)

    term1_I = (3.0 * v_sq * K_I) / (5.0 * beta * math.sqrt(2.0*pi*delta))
    term1_II = (3.0 * v_sq * K_II) / (5.0 * beta * math.sqrt(2.0*pi*delta))

    # mode I dilatational
    Q_I_dilat = epsilon_Omega_over_4pi_q * term1_I * (
        1.0 + (5.0/24.0) * v_sqrt * sqrt_lambda_delta_aD / Gamma_s
    )
    D1_I_dilat = epsilon_Omega_over_4pi_q * term1_I * lam * a_D * (
        v + (5.0/21.0)*v_sqrt3*sqrt_lambda_delta_aD/Gamma_s - (50.0/21.0)*delta_over_lambda_aD
    )
    exp['Q_I_dilat'] = Q_I_dilat
    exp['D1_I_dilat'] = D1_I_dilat

    # ---------- gamma_j coefficients ----------
    def compute_gamma_j(n, m, A, B, C, D, E, F, beta):
        total = 0.0
        for lam, mu, nu in itertools.product([0,1,2], repeat=3):
            if lam == mu or mu == nu or lam == nu:
                continue
            # all distinct → gamma non-zero
            gamma_val = gamma
            term = (n[lam]*n[mu]*n[nu]*A
                    + n[lam]*m[mu]*m[nu]*B
                    + m[lam]*n[mu]*m[nu]*C
                    + beta*(m[lam]*n[mu]*n[nu]*D
                            + m[lam]*m[mu]*m[nu]*E
                            + n[lam]*n[mu]*m[nu]*F))
            total += gamma_val * term
        return total

    # constants table
    gamma0_I = compute_gamma_j(n, m, 8.0/21.0, -2.0, -8.0/21.0, 0.0, 0.0, 0.0, beta)
    gamma1_I = compute_gamma_j(n, m, -8.0/15.0, -12.0/15.0, 8.0/15.0, 0.0, 0.0, 0.0, beta)
    gamma2_I = compute_gamma_j(n, m, 0.0, 0.0, 0.0, -16.0/15.0, -8.0/15.0, -16.0/15.0, beta)
    gamma0_II = compute_gamma_j(n, m, 0.0, 0.0, 0.0, 6.0/7.0, 8.0/21.0, 8.0/21.0, beta)
    gamma1_II = compute_gamma_j(n, m, 0.0, 0.0, 0.0, -44.0/15.0, -8.0/15.0, -8.0/15.0, beta)
    gamma2_II = compute_gamma_j(n, m, 16.0/15.0, -8.0/15.0, -16.0/15.0, 0.0, 0.0, 0.0, beta)

    # piezoelectric common factors
    termQ_I = a_D * math.sqrt(a_D*lam) * v_sqrt * K_I / (beta * 2.0*math.sqrt(2.0*pi))
    termQ_II = a_D * math.sqrt(a_D*lam) * v_sqrt * (-K_II) / (beta * 2.0*math.sqrt(2.0*pi))
    termD_common = (a_D*lam)**(3.0/2.0) * v_sqrt3
    factor_D_I = K_I / (beta * 2.0*math.sqrt(2.0*pi))
    factor_D_II = -K_II / (beta * 2.0*math.sqrt(2.0*pi))
    denom_D2 = (1.0 - v_sq) * 2.0*math.sqrt(2.0*pi)

    # mode I piezo
    Q_I_piezo = gamma0_I * termQ_I
    D1_I_piezo = (gamma0_I + gamma1_I) * termD_common * factor_D_I
    D2_I_piezo = gamma2_I * termD_common * K_I / denom_D2
    exp['Q_I_piezo'] = Q_I_piezo
    exp['D1_I_piezo'] = D1_I_piezo
    exp['D2_I_piezo'] = D2_I_piezo
    exp['Q_I_total'] = Q_I_dilat + Q_I_piezo
    exp['D1_I_total'] = D1_I_dilat + D1_I_piezo
    exp['D2_I_total'] = D2_I_piezo  # D2_I has no dilatational

    # mode II piezo
    Q_II_piezo = gamma0_II * termQ_II
    # D1_II has no piezoelectric, total from dilatational
    D2_II_piezo = gamma2_II * termD_common * (-K_II) / denom_D2
    exp['Q_II_piezo'] = Q_II_piezo
    exp['Q_II_total'] = Q_II_piezo  # no dilatational
    exp['D2_II_piezo'] = D2_II_piezo

    # mode II dilatational D1 (analogous to D1_I_dilat with K_II)
    D1_II_dilat = epsilon_Omega_over_4pi_q * term1_II * lam * a_D * (
        v + (5.0/21.0)*v_sqrt3*sqrt_lambda_delta_aD/Gamma_s - (50.0/21.0)*delta_over_lambda_aD
    )
    exp['D1_II_dilat'] = D1_II_dilat
    exp['D1_II_total'] = D1_II_dilat

    # D2_II_dilat
    D2_II_dilat = - epsilon_Omega_over_4pi_q * (
        (10.0 * v_sq * K_II * lam * a_D) / ((1.0 - v_sq) * math.sqrt(2.0*pi*delta))
    ) * ( delta_over_lambda_aD + (1.0/3.0) * v_sqrt * sqrt_lambda_delta_aD / Gamma_s )
    exp['D2_II_dilat'] = D2_II_dilat
    exp['D2_II_total'] = D2_II_dilat + D2_II_piezo

    # ---------- sound absorption ----------
    # elastic tensor contraction: S^{mu,nu} = sum_{alpha,beta} Lambda^{mu,nu;alpha,beta} n_alpha e_beta
    # Lambda only non-zero for: mu=nu=alpha=beta -> C11; mu=nu != alpha=beta (both same) -> C12; mu=alpha != nu=beta or mu=beta != nu=alpha -> C44.
    S = [[0.0]*3 for _ in range(3)]
    for mu in range(3):
        for nu in range(3):
            for alpha in range(3):
                for beta in range(3):
                    val = 0.0
                    if mu == nu and alpha == beta:
                        val = C11 if mu == alpha else C12
                    elif (mu == alpha and nu == beta) or (mu == beta and nu == alpha):
                        if mu != nu:
                            val = C44
                    S[mu][nu] += val * n[alpha] * e[beta]

    # piezocontraction
    num_abs_sq = 0.0
    for lam, mu, nu in itertools.product([0,1,2], repeat=3):
        if lam == mu or mu == nu or lam == nu:
            continue
        gamma_val = gamma
        num_abs_sq += gamma_val * n[lam] * S[mu][nu]
    num_abs_sq = abs(num_abs_sq)**2

    denom = rho * ct**3 * omega**2 * tau_sigma**2 + (1.0 + omega**2 * tau_sigma**2 / lam**2)**2
    exp['gamma_t'] = 2.0 * omega**2 * tau_sigma * num_abs_sq / denom

    return exp


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
    import csv
    import os
    import math

    # load artifact
    csv_path = os.path.join(outputs_dir, 'results.csv')
    if not os.path.exists(csv_path):
        return {}
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    # build lookup
    agent_values = {}
    for row in rows:
        q = row.get('quantity', '').strip()
        try:
            agent_values[q] = float(row.get('value', 0))
        except (ValueError, TypeError):
            agent_values[q] = None

    expected = compute_expected()  # from imports
    return {'expected': expected, 'agent': agent_values}


# === block: score_0 (check id='Q_shock_dilat') ===
def score_0(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_1 (check id='Q_shock_piezo') ===
def score_1(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_2 (check id='Q_shock_total') ===
def score_2(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_3 (check id='D_shock_dilat') ===
def score_3(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_4 (check id='D_shock_piezo') ===
def score_4(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_5 (check id='D_shock_total') ===
def score_5(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_6 (check id='Q_I_dilat') ===
def score_6(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_7 (check id='Q_I_piezo') ===
def score_7(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_8 (check id='Q_I_total') ===
def score_8(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_9 (check id='D1_I_dilat') ===
def score_9(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_10 (check id='D1_I_piezo') ===
def score_10(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_11 (check id='D1_I_total') ===
def score_11(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_12 (check id='D2_I_piezo') ===
def score_12(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_13 (check id='D2_I_total') ===
def score_13(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_14 (check id='Q_II_piezo') ===
def score_14(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_15 (check id='Q_II_total') ===
def score_15(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_16 (check id='D1_II_dilat') ===
def score_16(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_17 (check id='D1_II_total') ===
def score_17(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_18 (check id='D2_II_dilat') ===
def score_18(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_19 (check id='D2_II_piezo') ===
def score_19(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_20 (check id='D2_II_total') ===
def score_20(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


# === block: score_21 (check id='gamma_t') ===
def score_21(artifact, step, ctx):
    q = step['id']
    exp = ctx.get('expected', {}).get(q, None)
    agt = ctx.get('agent', {}).get(q, None)
    if exp is None or agt is None:
        return 0.0
    rel_tol = 1e-6
    abs_tol = 1e-12
    if abs(exp) < abs_tol:
        return 1.0 if abs(agt - exp) < abs_tol else 0.0
    else:
        return 1.0 if abs(agt - exp) / abs(exp) <= rel_tol else 0.0


_SCORERS = {
    'Q_shock_dilat': score_0,
    'Q_shock_piezo': score_1,
    'Q_shock_total': score_2,
    'D_shock_dilat': score_3,
    'D_shock_piezo': score_4,
    'D_shock_total': score_5,
    'Q_I_dilat': score_6,
    'Q_I_piezo': score_7,
    'Q_I_total': score_8,
    'D1_I_dilat': score_9,
    'D1_I_piezo': score_10,
    'D1_I_total': score_11,
    'D2_I_piezo': score_12,
    'D2_I_total': score_13,
    'Q_II_piezo': score_14,
    'Q_II_total': score_15,
    'D1_II_dilat': score_16,
    'D1_II_total': score_17,
    'D2_II_dilat': score_18,
    'D2_II_piezo': score_19,
    'D2_II_total': score_20,
    'gamma_t': score_21,
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
