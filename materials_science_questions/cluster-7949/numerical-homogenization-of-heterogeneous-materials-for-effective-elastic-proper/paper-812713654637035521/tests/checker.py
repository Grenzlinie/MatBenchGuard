import os
import json
import csv

# === author imports / helpers ===
import csv
import numpy as np
from scipy.optimize import fsolve

# ---------- Powers' hydration model ----------
def powers_volumes(wc, alpha, rho_a=3.13, kappa_w=1.31, kappa_h=2.13):
    denom = 1.0 + rho_a * wc
    f_a = (1.0 - alpha) / denom
    f_h = kappa_h * alpha / denom
    f_cp = (rho_a * wc + (1.0 - kappa_h) * alpha) / denom
    phi = f_cp / (f_cp + f_h) if (f_cp + f_h) > 0 else 0.0
    return f_a, f_h, f_cp, phi

def alpha_max_external(wc, rho_a=3.13, kappa_h=2.13):
    if wc <= (kappa_h - 1.0) / rho_a:
        return (rho_a * wc) / (kappa_h - 1.0)
    else:
        return 1.0

# ---------- Hill/Eshelby helpers for elasticity ----------
def eshelby_helpers(nu, omega):
    import math
    if omega == 1.0:
        g = 2.0 / 3.0
    elif omega > 1.0:
        g = math.acosh(omega) / (omega * math.sqrt(omega * omega - 1.0))
    else:
        g = math.acos(omega) / (omega * math.sqrt(1.0 - omega * omega))
    denom = 2.0 * (omega * omega - 1.0)
    F0 = omega * omega * (1.0 - g) / denom
    F1 = omega * omega * ((2.0 * omega * omega + 1.0) * g - 3.0) / (8.0 * (omega * omega - 1.0) ** 2)
    return F0, F1

def walpole_inverse(L):
    # L is list of 6 Walpole components
    L1, L2, L3, L4, L5, L6 = L
    Delta = L1 * L2 - 2.0 * L5 * L6
    inv1 = L2 / Delta if Delta != 0 else 0.0
    inv2 = L1 / Delta if Delta != 0 else 0.0
    inv3 = 1.0 / L3 if L3 != 0 else 0.0
    inv4 = 1.0 / L4 if L4 != 0 else 0.0
    inv5 = -L5 / Delta if Delta != 0 else 0.0
    inv6 = -L6 / Delta if Delta != 0 else 0.0
    return [inv1, inv2, inv3, inv4, inv5, inv6]

# ---------- self-consistent elasticity for hydrate foam ----------
def elastic_sc_residual(vars, f_h, f_p, k_h, mu_h, omega_h, omega_p):
    k_sc, mu_sc = vars
    if k_sc <= 0 or mu_sc <= 0:
        return [1e6, 1e6]
    nu_sc = (3.0 * k_sc - 2.0 * mu_sc) / (2.0 * (3.0 * k_sc + mu_sc))
    residual_k = 0.0
    residual_mu = 0.0
    for f_i, k_i, mu_i, omega_i in [(f_h, k_h, mu_h, omega_h), (f_p, 0.0, 0.0, omega_p)]:
        # compute Eshelby tensor S in matrix (k_sc, mu_sc) for spheroid omega_i
        F0, F1 = eshelby_helpers(nu_sc, omega_i)
        # S'_ components from Eq A.12
        S1p = F0 + 2.0 * F1
        S2p = (1.0 - nu_sc) * (1.0 - 2.0 * F0) + 4.0 * F1
        S3p = (1.5 - 2.0 * nu_sc) * F0 + F1
        S4p = (1.0 - nu_sc) * (1.0 - F0) - 4.0 * F1
        S5p = nu_sc * (1.0 - 2.0 * F0) - 2.0 * F1
        S6p = nu_sc * F0 - 2.0 * F1
        # true S = S' / (1 - nu_sc)
        den = 1.0 - nu_sc
        S = [S1p/den, S2p/den, S3p/den, S4p/den, S5p/den, S6p/den]
        # relative stiffness ratios
        kr = k_i / k_sc if k_sc != 0 else 0.0
        mur = mu_i / mu_sc if mu_sc != 0 else 0.0
        # D = C_i:C_sc^{-1} - I
        D = [2.0/3.0*(kr-1) + 2.0/3.0*(mur-1), 1.0/3.0*(kr-1) + 4.0/3.0*(mur-1),
             (mur-1), (mur-1), 1.0/3.0*(kr-1) - 2.0/3.0*(mur-1), 1.0/3.0*(kr-1) - 2.0/3.0*(mur-1)]
        # I + S : D
        I_SD = [1.0 + S[0]*D[0] + 2.0*S[5]*D[4],   # c=1
                1.0 + S[1]*D[1] + 2.0*S[4]*D[5],   # c=2
                1.0 + S[2]*D[2],                    # c=3
                1.0 + S[3]*D[3],                    # c=4
                S[4]*D[0] + S[1]*D[5],              # c=5
                S[5]*D[1] + S[0]*D[4]]              # c=6
        A_i = walpole_inverse(I_SD)
        # average over orientation: a_i, b_i using (A.11)
        a_i = (2.0/3.0 * A_i[0] + 2.0/3.0 * A_i[1] + 0.0*A_i[2] + 0.0*A_i[3] + 2.0/3.0*A_i[4] + 2.0/3.0*A_i[5])
        b_i = (2.0/15.0 * A_i[0] - 2.0/15.0 * A_i[1] + 2.0/5.0*A_i[2] + 2.0/5.0*A_i[3] - 2.0/15.0*A_i[4] + 2.0/15.0*A_i[5])
        residual_k += f_i * (k_i - k_sc) * a_i
        residual_mu += f_i * (mu_i - mu_sc) * b_i
    return [residual_k, residual_mu]

def foam_elastic_moduli(f_h, f_cp, E_h=25.3, nu_h=0.29, omega_h=0.013, omega_cp=6):
    k_h = E_h / (3.0 * (1.0 - 2.0 * nu_h))
    mu_h = E_h / (2.0 * (1.0 + nu_h))
    # initial guess: Voigt bound
    f_total = f_h + f_cp
    if f_total == 0:
        return 0.0, 0.0
    phi = f_cp / f_total
    k_voigt = (1.0 - phi) * k_h + phi * 0.0
    mu_voigt = (1.0 - phi) * mu_h + phi * 0.0
    if k_voigt <= 0:
        k_voigt = 1e-6
    if mu_voigt <= 0:
        mu_voigt = 1e-6
    try:
        sol = fsolve(elastic_sc_residual, [k_voigt, mu_voigt], args=(1.0-phi, phi, k_h, mu_h, omega_h, omega_cp), maxfev=2000, xtol=1e-12)
        k_f, mu_f = sol
        if k_f <= 0 or mu_f <= 0:
            return 0.0, 0.0
        return k_f, mu_f
    except:
        return 0.0, 0.0

# ---------- Mori-Tanaka for paste elasticity ----------
def cement_elastic_moduli(f_a, k_f, mu_f, E_a=135.0, nu_a=0.3):
    k_a = E_a / (3.0 * (1.0 - 2.0 * nu_a))
    mu_a = E_a / (2.0 * (1.0 + nu_a))
    # Eshelby tensor for sphere in matrix (k_f, mu_f)
    alpha_f = (3.0 * k_f) / (3.0 * k_f + 4.0 * mu_f) if (k_f > 0 or mu_f > 0) else 0.0
    beta_f = (6.0 / 5.0) * (k_f + 2.0 * mu_f) / (3.0 * k_f + 4.0 * mu_f) if (k_f > 0 or mu_f > 0) else 0.0
    k_cement = k_f * (1.0 + f_a * (k_a - k_f) / (k_f + (1.0 - f_a) * alpha_f * (k_a - k_f)))
    mu_cement = mu_f * (1.0 + f_a * (mu_a - mu_f) / (mu_f + (1.0 - f_a) * beta_f * (mu_a - mu_f)))
    return k_cement, mu_cement

def young_modulus(k, mu):
    if k <= 0 or mu <= 0:
        return 0.0
    return 9.0 * k * mu / (3.0 * k + mu)

# ---------- self-consistent diffusion for hydrate foam ----------
def foam_diffusivity(phi, D_h, D_cp, omega_h, omega_cp):
    # phi = porosity (f_cp/(f_cp+f_h))
    # construct quartic coefficients from Eq A.6
    f1 = 1.0 - phi  # hydrates
    f2 = phi        # pores
    D1 = D_h
    D2 = D_cp
    # m_c: m1=1/3, m2=2/3
    m1 = 1.0/3.0
    m2 = 2.0/3.0
    # helper to compute S_c (c=1,2) for given omega
    def S_components(omega):
        import math
        if omega == 1.0:
            S1 = 1.0/3.0
            S2 = 1.0/3.0
        else:
            if omega > 1.0:
                g = math.acosh(omega) / (omega * math.sqrt(omega*omega - 1.0))
            else:
                g = math.acos(omega) / (omega * math.sqrt(1.0 - omega*omega))
            S2 = (omega*omega) / (omega*omega - 1.0) * (1.0 - g) / 2.0
            S1 = 1.0 - 2.0 * S2
        return S1, S2
    S1_h, S2_h = S_components(omega_h)
    S1_p, S2_p = S_components(omega_cp)
    # Build polynomial a D_sc^4 + b D_sc^3 + ...
    # sum_{i} f_i (D_i - D) * [ m1/(D + S1_i (D_i-D)) + m2/(D + S2_i (D_i-D)) ] = 0
    # Expand analytically to get coefficients; we can compute by evaluating at several D and fit, or use symbolic.
    # For simplicity, we define function f(D) and find root via fsolve.
    def func(D):
        if D <= 0:
            return -1e6
        total = 0.0
        for fi, Di, S1, S2 in [(f1,D1,S1_h,S2_h), (f2,D2,S1_p,S2_p)]:
            diff = Di - D
            term = fi * diff * ( m1/(D + S1 * diff) + m2/(D + S2 * diff) )
            total += term
        return total
    # initial guess: weighted harmonic/arithmetic
    D_init = f1*D1 + f2*D2
    try:
        sol = fsolve(func, D_init, xtol=1e-12, maxfev=2000)
        D_f = sol[0]
        return max(D_f, 0.0)
    except:
        return 0.0

# ---------- Mori-Tanaka for paste diffusion ----------
def cement_diffusivity(f_a, D_f):
    if f_a >= 1.0:
        return 0.0
    return (1.0 - f_a) / (1.0 + f_a / 2.0) * D_f

# ---------- computing reference curves ----------
def compute_youngs_curve(wc=0.4, alphas=None):
    rho_a=3.13; kappa_w=1.31; kappa_h=2.13
    E_h=25.3; nu_h=0.29; omega_h=0.013; omega_cp=6
    E_a=135.0; nu_a=0.3
    ref = {}
    for alpha in alphas:
        f_a, f_h, f_cp, phi = powers_volumes(wc, alpha, rho_a, kappa_w, kappa_h)
        if f_h + f_cp == 0:
            ref[alpha] = 0.0
            continue
        k_f, mu_f = foam_elastic_moduli(f_h, f_cp, E_h, nu_h, omega_h, omega_cp)
        if k_f <= 0 or mu_f <= 0:
            ref[alpha] = 0.0
            continue
        k_p, mu_p = cement_elastic_moduli(f_a, k_f, mu_f, E_a, nu_a)
        ref[alpha] = young_modulus(k_p, mu_p)
    return ref

def compute_diff_curve(wcs):
    D_h = 5.04e-4  # D_h/D_bulk
    D_cp = 1.0
    omega_h = 0.013; omega_cp = 6
    rho_a=3.13; kappa_w=1.31; kappa_h=2.13
    ref = {}
    for wc in wcs:
        alpha_max = alpha_max_external(wc, rho_a, kappa_h)
        f_a, f_h, f_cp, phi = powers_volumes(wc, alpha_max, rho_a, kappa_w, kappa_h)
        if f_h + f_cp == 0:
            ref[wc] = 0.0
            continue
        D_f = foam_diffusivity(phi, D_h, D_cp, omega_h, omega_cp)
        D_cement = cement_diffusivity(f_a, D_f)
        ref[wc] = D_cement
    return ref


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
    params_youngs = spec['steps'][0]['params']
    params_diff = spec['steps'][1]['params']
    ctx = {}
    ctx['youngs_ref'] = compute_youngs_curve(wc=0.4, alphas=params_youngs['x_sample_points'])
    ctx['diff_ref'] = compute_diff_curve(wcs=params_diff['x_sample_points'])
    return ctx


# === block: score_0 (check id='youngs_modulus_curve') ===
def score_0(artifact, step, ctx):
    if artifact is None or len(artifact)==0:
        return 0.0
    xs = np.array([float(row[step['params']['x_column']]) for row in artifact])
    ys = np.array([float(row[step['params']['y_column']]) for row in artifact])
    sort_idx = np.argsort(xs)
    xs = xs[sort_idx]
    ys = ys[sort_idx]
    ref = ctx['youngs_ref']
    tol = step['params']['tolerance']
    max_err = 0.0
    for x0 in step['params']['x_sample_points']:
        if x0 < xs[0] or x0 > xs[-1]:
            return 0.0
        y_agent = np.interp(x0, xs, ys)
        y_ref = ref.get(x0, 0.0)
        if y_ref == 0.0:
            continue
        err = abs(y_agent - y_ref) / abs(y_ref)
        if err > max_err:
            max_err = err
    if max_err <= tol:
        return 1.0
    else:
        limit = step['params'].get('max_acceptable_error', 0.5)
        score = max(0.0, 1.0 - (max_err - tol) / (limit - tol))
        return score


# === block: score_1 (check id='diffusivity_curve') ===
def score_1(artifact, step, ctx):
    if artifact is None or len(artifact)==0:
        return 0.0
    xs = np.array([float(row[step['params']['x_column']]) for row in artifact])
    ys = np.array([float(row[step['params']['y_column']]) for row in artifact])
    sort_idx = np.argsort(xs)
    xs = xs[sort_idx]
    ys = ys[sort_idx]
    ref = ctx['diff_ref']
    tol = step['params']['tolerance']
    max_err = 0.0
    for x0 in step['params']['x_sample_points']:
        if x0 < xs[0] or x0 > xs[-1]:
            return 0.0
        y_agent = np.interp(x0, xs, ys)
        y_ref = ref.get(x0, 0.0)
        if y_ref == 0.0:
            continue
        err = abs(y_agent - y_ref) / abs(y_ref)
        if err > max_err:
            max_err = err
    if max_err <= tol:
        return 1.0
    else:
        limit = step['params'].get('max_acceptable_error', 0.5)
        score = max(0.0, 1.0 - (max_err - tol) / (limit - tol))
        return score


_SCORERS = {
    'youngs_modulus_curve': score_0,
    'diffusivity_curve': score_1,
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
