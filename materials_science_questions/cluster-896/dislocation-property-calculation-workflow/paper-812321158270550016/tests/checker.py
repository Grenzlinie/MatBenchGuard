import os
import json
import csv

# === author imports / helpers ===
import cmath
import math
import numpy as np

def _conformal_zeta(z, m):
    """Map physical z to zeta-plane using ω(ζ)=ζ+m/ζ with R=1."""
    disc = z * z - 4.0 * m
    sqrt_disc = cmath.sqrt(disc)
    r1 = (z + sqrt_disc) / 2.0
    r2 = (z - sqrt_disc) / 2.0
    if abs(r1) > abs(r2):
        return r1
    return r2


def _eval_unperturbed(zeta, zeta0, m, kappa1):
    """Evaluate unperturbed potentials φ_*, ψ_* and first derivatives at zeta."""
    pi = math.pi
    gamma = complex(0.0, -1.0) / (pi * (kappa1 + 1.0))
    conj_gamma = gamma.conjugate()
    R = 1.0

    # common factors
    A = zeta - zeta0
    B = zeta - m / zeta0
    den_log = A * B / zeta

    # φ_*
    phi_star = R * gamma * cmath.log(den_log)

    # φ_*'
    dphi_star = R * gamma * (1.0 / A + 1.0 / B - 1.0 / zeta)

    # ψ_*  (Eq (1))
    term1 = R * conj_gamma * cmath.log(den_log)
    num2 = zeta * (1.0 / zeta + m * zeta - zeta0.conjugate() - m / zeta0.conjugate())
    den2 = A * B
    term2 = R * gamma * num2 / den2
    psi_star = term1 + term2

    # ψ_*'  (differentiate term1 + term2)
    dterm1 = R * conj_gamma * (1.0 / A + 1.0 / B - 1.0 / zeta)
    dnum = 2.0 * m * zeta - zeta0.conjugate() - m / zeta0.conjugate()
    dden = 2.0 * zeta - (zeta0 + m / zeta0)
    dterm2 = R * gamma * (dnum * den2 - num2 * dden) / (den2 * den2)
    dpsi_star = dterm1 + dterm2

    return phi_star, dphi_star, psi_star, dpsi_star


def _solve_coefficients(m, Gamma, kappa1, kappa2, zeta0, z0, kmax=15):
    """Solve for perturbative series coefficients a_k,b_k(,c_k,d_k)."""
    rho0 = abs(zeta0)
    if abs(m) < 1e-12:
        rho_b = 0.0
    else:
        rho_b = math.sqrt(abs(m))
    if rho_b < 1e-10:
        rho_b = 1e-10

    npnt = 8 * kmax
    theta = np.linspace(0.0, 2.0 * math.pi, npnt, endpoint=False)
    zeta_pts = rho_b * np.exp(1j * theta)

    # evaluate unperturbed quantities at collocation points
    phi_star = np.empty(npnt, dtype=np.complex128)
    dphi_star = np.empty(npnt, dtype=np.complex128)
    psi_star = np.empty(npnt, dtype=np.complex128)
    dpsi_star = np.empty(npnt, dtype=np.complex128)
    for i, zeta in enumerate(zeta_pts):
        phi_star[i], dphi_star[i], psi_star[i], dpsi_star[i] = _eval_unperturbed(
            zeta, zeta0, m, kappa1
        )

    R = 1.0
    omega_arr = R * (zeta_pts + m / zeta_pts)
    omega_p_arr = R * (1.0 - m / (zeta_pts * zeta_pts))

    # helper to add contribution of one unknown (real+imag) to two rows
    def add_contrib(A, row_start, col_re, col_im, P, Q):
        # contribution to complex residual = P*a + Q*conj(a)
        # = (P+Q)*x_re + i*(P-Q)*x_im
        E_re = P + Q
        E_im = 1j * (P - Q)
        A[row_start, col_re] += E_re.real
        A[row_start, col_im] += E_im.real
        A[row_start + 1, col_re] += E_re.imag
        A[row_start + 1, col_im] += E_im.imag

    if Gamma < 1e-12:
        # hole: traction free -> L1 = 0
        nunk = 4 * kmax
        A = np.zeros((2 * npnt, nunk))
        rhs = np.zeros(2 * npnt)
        for i in range(npnt):
            zeta = zeta_pts[i]
            omega = omega_arr[i]
            omega_p = omega_p_arr[i]
            # a_k columns at 4k-4 (real), 4k-3 (imag), b_k at 4k-2, 4k-1
            for k in range(1, kmax + 1):
                z_inv_k = zeta ** (-k)
                z_inv_kp1 = zeta ** (-k - 1)
                z_conj_inv_kp1 = (zeta.conjugate()) ** (-k - 1)
                z_conj_inv_k = (zeta.conjugate()) ** (-k)
                col_a_re = (k - 1) * 4
                col_a_im = col_a_re + 1
                col_b_re = col_a_re + 2
                col_b_im = col_a_re + 3
                row_start = 2 * i
                # a_k: P = ζ^{-k}, Q = -k (ω/ω') ζ^{-k-1}¯
                P_a = z_inv_k
                Q_a = -k * (omega / omega_p) * z_conj_inv_kp1
                add_contrib(A, row_start, col_a_re, col_a_im, P_a, Q_a)
                # b_k: P = 0, Q = ζ^{-k}¯
                P_b = 0.0 + 0.0j
                Q_b = z_conj_inv_k
                add_contrib(A, row_start, col_b_re, col_b_im, P_b, Q_b)

            rhs_cmplx = -(phi_star[i] + (omega / omega_p) * dphi_star[i].conjugate() + psi_star[i].conjugate())
            rhs[row_start] = rhs_cmplx.real
            rhs[row_start + 1] = rhs_cmplx.imag

        coeff, _, _, _ = np.linalg.lstsq(A, rhs, rcond=None)
        a_k = [coeff[k * 4] + 1j * coeff[k * 4 + 1] for k in range(kmax)]
        b_k = [coeff[k * 4 + 2] + 1j * coeff[k * 4 + 3] for k in range(kmax)]
        return a_k, b_k, [0j] * kmax, [0j] * kmax

    elif Gamma > 1e8:
        # rigid: zero displacement -> L2 = 0
        nunk = 4 * kmax
        A = np.zeros((2 * npnt, nunk))
        rhs = np.zeros(2 * npnt)
        for i in range(npnt):
            zeta = zeta_pts[i]
            omega = omega_arr[i]
            omega_p = omega_p_arr[i]
            for k in range(1, kmax + 1):
                z_inv_k = zeta ** (-k)
                z_inv_kp1 = zeta ** (-k - 1)
                z_conj_inv_kp1 = (zeta.conjugate()) ** (-k - 1)
                z_conj_inv_k = (zeta.conjugate()) ** (-k)
                col_a_re = (k - 1) * 4
                col_a_im = col_a_re + 1
                col_b_re = col_a_re + 2
                col_b_im = col_a_re + 3
                row_start = 2 * i
                # a_k in L2: P = κ1 ζ^{-k}, Q = +k (ω/ω') ζ^{-k-1}¯
                P_a = kappa1 * z_inv_k
                Q_a = k * (omega / omega_p) * z_conj_inv_kp1
                add_contrib(A, row_start, col_a_re, col_a_im, P_a, Q_a)
                # b_k: P=0, Q = -ζ^{-k}¯
                P_b = 0.0 + 0.0j
                Q_b = -z_conj_inv_k
                add_contrib(A, row_start, col_b_re, col_b_im, P_b, Q_b)

            rhs_cmplx = -(kappa1 * phi_star[i] - (omega / omega_p) * dphi_star[i].conjugate() - psi_star[i].conjugate())
            rhs[row_start] = rhs_cmplx.real
            rhs[row_start + 1] = rhs_cmplx.imag

        coeff, _, _, _ = np.linalg.lstsq(A, rhs, rcond=None)
        a_k = [coeff[k * 4] + 1j * coeff[k * 4 + 1] for k in range(kmax)]
        b_k = [coeff[k * 4 + 2] + 1j * coeff[k * 4 + 3] for k in range(kmax)]
        return a_k, b_k, [0j] * kmax, [0j] * kmax

    else:
        # general bimaterial
        invGamma = 1.0 / Gamma
        nunk = 8 * kmax
        A = np.zeros((4 * npnt, nunk))
        rhs = np.zeros(4 * npnt)
        for i in range(npnt):
            zeta = zeta_pts[i]
            omega = omega_arr[i]
            omega_p = omega_p_arr[i]
            for k in range(1, kmax + 1):
                z_inv_k = zeta ** (-k)
                z_inv_kp1 = zeta ** (-k - 1)
                z_pos_k = zeta ** k
                z_pos_km1 = zeta ** (k - 1)
                z_conj_inv_kp1 = (zeta.conjugate()) ** (-k - 1)
                z_conj_inv_k = (zeta.conjugate()) ** (-k)
                z_conj_pos_km1 = (zeta.conjugate()) ** (k - 1)
                z_conj_pos_k = (zeta.conjugate()) ** k
                base = (k - 1) * 8
                # a_k (p_k)
                col_a_re = base
                col_a_im = base + 1
                # b_k (q_k)
                col_b_re = base + 2
                col_b_im = base + 3
                # c_k
                col_c_re = base + 4
                col_c_im = base + 5
                # d_k
                col_d_re = base + 6
                col_d_im = base + 7

                # Traction equation (L1): rows row_start = 4*i, +1
                row1 = 4 * i
                # a_k in L1
                P_a_L1 = z_inv_k
                Q_a_L1 = -k * (omega / omega_p) * z_conj_inv_kp1
                add_contrib(A, row1, col_a_re, col_a_im, P_a_L1, Q_a_L1)
                # b_k in L1
                P_b_L1 = 0.0 + 0.0j
                Q_b_L1 = z_conj_inv_k
                add_contrib(A, row1, col_b_re, col_b_im, P_b_L1, Q_b_L1)
                # c_k in L1
                P_c_L1 = -z_pos_k
                Q_c_L1 = -k * (omega / omega_p) * z_conj_pos_km1
                add_contrib(A, row1, col_c_re, col_c_im, P_c_L1, Q_c_L1)
                # d_k in L1
                P_d_L1 = 0.0 + 0.0j
                Q_d_L1 = -z_conj_pos_k
                add_contrib(A, row1, col_d_re, col_d_im, P_d_L1, Q_d_L1)

                # Displacement equation (L2): rows row2 = 4*i+2
                row2 = 4 * i + 2
                # a_k in L2
                P_a_L2 = kappa1 * z_inv_k
                Q_a_L2 = k * (omega / omega_p) * z_conj_inv_kp1
                add_contrib(A, row2, col_a_re, col_a_im, P_a_L2, Q_a_L2)
                # b_k in L2
                P_b_L2 = 0.0 + 0.0j
                Q_b_L2 = -z_conj_inv_k
                add_contrib(A, row2, col_b_re, col_b_im, P_b_L2, Q_b_L2)
                # c_k in L2
                P_c_L2 = -(kappa2 * invGamma) * z_pos_k
                Q_c_L2 = k * invGamma * (omega / omega_p) * z_conj_pos_km1
                add_contrib(A, row2, col_c_re, col_c_im, P_c_L2, Q_c_L2)
                # d_k in L2
                P_d_L2 = 0.0 + 0.0j
                Q_d_L2 = invGamma * z_conj_pos_k
                add_contrib(A, row2, col_d_re, col_d_im, P_d_L2, Q_d_L2)

            # rhs for L1
            rhs_cmplx_L1 = -(phi_star[i] + (omega / omega_p) * dphi_star[i].conjugate() + psi_star[i].conjugate())
            rhs[4 * i] = rhs_cmplx_L1.real
            rhs[4 * i + 1] = rhs_cmplx_L1.imag
            # rhs for L2
            rhs_cmplx_L2 = -(kappa1 * phi_star[i] - (omega / omega_p) * dphi_star[i].conjugate() - psi_star[i].conjugate())
            rhs[4 * i + 2] = rhs_cmplx_L2.real
            rhs[4 * i + 3] = rhs_cmplx_L2.imag

        coeff, _, _, _ = np.linalg.lstsq(A, rhs, rcond=None)
        a_k = [coeff[k * 8] + 1j * coeff[k * 8 + 1] for k in range(kmax)]
        b_k = [coeff[k * 8 + 2] + 1j * coeff[k * 8 + 3] for k in range(kmax)]
        c_k = [coeff[k * 8 + 4] + 1j * coeff[k * 8 + 5] for k in range(kmax)]
        d_k = [coeff[k * 8 + 6] + 1j * coeff[k * 8 + 7] for k in range(kmax)]
        return a_k, b_k, c_k, d_k


def compute_Fg_reference(m, Gamma, nu1, nu2, r0_over_R, phi0_deg):
    """Compute dimensionless glide force via series solution."""
    kappa1 = 3.0 - 4.0 * nu1
    kappa2 = 3.0 - 4.0 * nu2
    phi0 = math.radians(phi0_deg)
    z0 = r0_over_R * cmath.exp(1j * phi0)
    zeta0 = _conformal_zeta(z0, m)

    kmax = 15
    a_k, b_k, _, _ = _solve_coefficients(m, Gamma, kappa1, kappa2, zeta0, z0, kmax)

    # Peach-Koehler evaluation
    R = 1.0
    zeta = zeta0
    omega = R * (zeta + m / zeta)
    omega_p = R * (1.0 - m / (zeta * zeta))
    omega_pp = 2.0 * m / (zeta ** 3)

    dphi_p = 0.0j
    dpsi_p = 0.0j
    d2phi_p = 0.0j
    for k in range(1, kmax + 1):
        dphi_p += -k * a_k[k - 1] * (zeta ** (-k - 1))
        dpsi_p += -k * b_k[k - 1] * (zeta ** (-k - 1))
        d2phi_p += k * (k + 1) * a_k[k - 1] * (zeta ** (-k - 2))

    Phi_p = dphi_p / omega_p
    Phi_p_prime = (d2phi_p * omega_p - dphi_p * omega_pp) / (omega_p * omega_p)

    pi = math.pi
    gamma = complex(0.0, -1.0) / (pi * (kappa1 + 1.0))
    conj_gamma = gamma.conjugate()

    term1 = (Phi_p + Phi_p.conjugate()) / gamma
    term2 = (omega.conjugate() * Phi_p_prime + dpsi_p) / (conj_gamma * omega_p)
    expr = term1 + term2
    Fg = expr.real
    return Fg


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
    def prepare(outputs_dir, spec):
        return {}


# === block: score_0 (check id='step_03_glide_force') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import csv
        import os
        import math
        # artifact is list of dicts from csv.DictReader
        if not artifact:
            return 0.0
        required = ['m','Gamma','nu1','nu2','r0_over_R','phi0_deg','Fg']
        if not all(col in artifact[0] for col in required):
            return 0.0
        tol = step.get('tolerance_relative', 1e-4)
        total = 0.0
        n = 0
        for row in artifact:
            try:
                m = float(row['m'])
                Gamma = float(row['Gamma'])
                nu1 = float(row['nu1'])
                nu2 = float(row['nu2'])
                r0_over_R = float(row['r0_over_R'])
                phi0_deg = float(row['phi0_deg'])
                Fg_agent = float(row['Fg'])
            except (ValueError, TypeError):
                continue
            Fg_ref = compute_Fg_reference(m, Gamma, nu1, nu2, r0_over_R, phi0_deg)
            denom = max(abs(Fg_ref), 1e-12)
            rel_err = abs(Fg_agent - Fg_ref) / denom
            if rel_err <= tol:
                total += 1.0
            elif rel_err <= 10.0 * tol:
                total += 0.5
            # else zero
            n += 1
        if n == 0:
            return 0.0
        return total / n


_SCORERS = {
    'step_03_glide_force': score_0,
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
