import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.special import erfc

# Helper functions for Ewald summation

def compute_H(x):
    """Compute the 3x3 Hessian matrix H_{γ,γ'}(x) for a vector x of shape (3,)"""
    r = np.linalg.norm(x)
    if r < 1e-12:
        return np.diag([0.0, 0.0, 0.0])  # not used for self-term; self-term handled separately
    xx = x[:, None] * x[None, :] / (r**2)
    delta = np.eye(3)
    # Eq. A3
    erfc_r = erfc(r)
    term1 = (3.0 / r**3 * erfc_r + 2.0 / np.sqrt(np.pi) * (3.0 / r**2 + 2.0) * np.exp(-r**2))
    term2 = (1.0 / r**3 * erfc_r + 2.0 / np.sqrt(np.pi) * (1.0 / r**2) * np.exp(-r**2))
    H = xx * term1 - delta * term2
    return H

def compute_H0():
    """Self-term for l=l', k=k'"""
    return np.eye(3) * (4.0 / (3.0 * np.sqrt(np.pi)))

def compute_coulomb_cartesian(q):
    """q: Cartesian reduced wave vector (units of 2π/a), shape (3,)
       Returns 15x15 symmetric matrix of Coulomb coefficients C_{k,k',γ,γ'}"""
    a = 1.0
    v_a = a**3
    Y = 2.1  # dimensionless Y * a^2
    # Atom fractional coordinates (basis positions within unit cell)
    frac_positions = np.array([
        [0.0, 0.0, 0.0],     # A (0)
        [0.5, 0.5, 0.5],     # B (1)
        [0.5, 0.5, 0.0],     # O1 (2)
        [0.5, 0.0, 0.5],     # O2 (3)
        [0.0, 0.5, 0.5]      # O3 (4)
    ])  # 5 atoms
    cart_positions = frac_positions * a
    nat = 5
    # Real-space summation range
    n_max = 5
    # Reciprocal lattice vectors (2π * integer vector)
    b_vecs = [2.0*np.pi*np.array([h,k,l]) for h in range(-n_max, n_max+1)
              for k in range(-n_max, n_max+1) for l in range(-n_max, n_max+1)]
    # Build matrix
    C = np.zeros((nat*3, nat*3), dtype=complex)
    for i, pos_i in enumerate(cart_positions):
        for j, pos_j in enumerate(cart_positions):
            delta_x = pos_i - pos_j
            # Reciprocal sum part of Q
            sum_rec = np.zeros((3,3), dtype=complex)
            for tau_vec in b_vecs:
                tau_plus_q = tau_vec + q
                norm_sq = np.dot(tau_plus_q, tau_plus_q)
                if norm_sq < 1e-12:
                    continue
                gamma = tau_plus_q[:, None] * tau_plus_q[None, :] / norm_sq
                factor = np.exp(-norm_sq / (4.0*Y)) * np.exp(1j * np.dot(tau_vec, delta_x))
                sum_rec += gamma * factor
            # First term of Q (analytic)
            norm_q_sq = np.dot(q, q)
            if norm_q_sq < 1e-12:
                # Handle q=0 limit: use small epsilon approximation
                q_small = np.array([1e-6, 1e-6, 0.0]) * 2.0*np.pi
                norm_q_sq_small = np.dot(q_small, q_small)
                gamma_q = q_small[:, None] * q_small[None, :] / norm_q_sq_small
                exp_term = np.exp(-norm_q_sq_small / (4.0*Y))
            else:
                gamma_q = q[:, None] * q[None, :] / norm_q_sq
                exp_term = np.exp(-norm_q_sq / (4.0*Y))
            term1 = gamma_q * (exp_term - 1.0)
            # Real-space sum in Q
            sum_real = np.zeros((3,3), dtype=complex)
            for h in range(-n_max, n_max+1):
                for k in range(-n_max, n_max+1):
                    for l in range(-n_max, n_max+1):
                        R = np.array([h,k,l], dtype=float) * a
                        x_lk = R + pos_j
                        dx = pos_i - x_lk
                        r = np.linalg.norm(dx)
                        if r < 1e-12 and i == j:
                            # self-term
                            Hmat = compute_H0()
                        else:
                            x_scaled = np.sqrt(Y) * dx
                            Hmat = compute_H(x_scaled)
                        phase = np.exp(-1j * np.dot(q, dx))
                        sum_real += Hmat * phase
            Q = (-4.0*np.pi/v_a) * term1 - (4.0*np.pi/v_a) * sum_rec + (Y**1.5) * sum_real
            # Final C
            C_ij = (4.0*np.pi/v_a) * gamma_q - Q
            # Assign block
            for a in range(3):
                for b in range(3):
                    C[3*i+a, 3*j+b] = C_ij[a,b]
    # Ensure Hermitian symmetry
    C = (C + C.conj().T) / 2.0
    return np.real(C)

def get_transformation_matrix():
    """Return 5x15 matrix T mapping Cartesian 15-vector to Sigma_3 basis [p_A, p_B, p_O1, p_ORot, p_ODist]"""
    sqrt2_inv = 1.0 / np.sqrt(2.0)
    T = np.zeros((5, 15))
    # p_A: A_x = -A_y = p_A/sqrt2
    T[0, 0] = sqrt2_inv   # A_x
    T[0, 1] = -sqrt2_inv  # A_y
    # p_B: B_x = -B_y = p_B/sqrt2
    T[1, 3] = sqrt2_inv   # B_x
    T[1, 4] = -sqrt2_inv  # B_y
    # p_O1: O1_x = -O1_y = p_O1/sqrt2
    T[2, 6] = sqrt2_inv   # O1_x
    T[2, 7] = -sqrt2_inv  # O1_y
    # p_ORot: O2_x = -O3_y = p_ORot/sqrt2
    T[3, 9] = sqrt2_inv   # O2_x (index 9 = 3*3+0? O2 is atom index 3: x=9, y=10, z=11)
    T[3, 13] = -sqrt2_inv # O3_y (O3 atom index 4: x=12, y=13)
    # p_ODist: O3_x = -O2_y = p_ODist/sqrt2
    T[4, 12] = sqrt2_inv  # O3_x
    T[4, 10] = -sqrt2_inv # O2_y
    return T

def compute_c_a_orot(xi):
    """Compute C_A-ORot for given xi along (xi,xi,0)"""
    q_frac = np.array([xi, xi, 0.0])
    q_cart = q_frac * 2.0 * np.pi  # reduced wave vector in Cartesian
    C_cart = compute_coulomb_cartesian(q_cart)
    T = get_transformation_matrix()
    M = T @ C_cart @ T.T
    return M[0, 3]  # C_A-ORot

def compute_s_min(xi):
    """Compute lowest stiffness eigenvalue for given xi with polarizabilities"""
    alpha_A = 4.9
    alpha_B = 0.37
    alpha_OA = 4.38
    alpha_OB = 2.9
    diag_inv_alpha = np.array([1.0/alpha_A, 1.0/alpha_B, 1.0/alpha_OA, 1.0/alpha_OA, 1.0/alpha_OB])
    C_cart = compute_coulomb_cartesian(np.array([xi, xi, 0.0]) * 2.0*np.pi)
    T = get_transformation_matrix()
    M = T @ C_cart @ T.T
    S = M + np.diag(diag_inv_alpha)
    eigvals = np.linalg.eigvalsh(S)
    return np.min(eigvals)


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
    xi_vals = np.arange(0, 0.52, 0.02)
    ref_coulomb = {}
    ref_stiffness = {}
    for xi in xi_vals:
        ref_coulomb[xi] = compute_c_a_orot(xi)
        ref_stiffness[xi] = compute_s_min(xi)
    return {'ref_coulomb': ref_coulomb, 'ref_stiffness': ref_stiffness, 'xi_vals': xi_vals}


# === block: score_0 (check id='coulomb') ===
def score_0(artifact, step, ctx):
    ref_dict = ctx['ref_coulomb']
    xi_vals = ctx['xi_vals']
    if not artifact or not isinstance(artifact, list):
        return 0.0
    rows = artifact
    tol = 0.02
    n_total = len(xi_vals)
    within_tol = 0
    values_by_xi = {}
    for row in rows:
        try:
            xi_f = float(row['xi'])
            c = float(row['C_A_ORot'])
        except (ValueError, KeyError):
            continue
        xi_closest = min(xi_vals, key=lambda k: abs(k - xi_f))
        if abs(xi_closest - xi_f) > 1e-9:
            continue
        diff = abs(c - ref_dict[xi_closest])
        if diff <= tol:
            within_tol += 1
        values_by_xi[xi_closest] = c
    points_score = within_tol / n_total if n_total > 0 else 0.0
    nonz_xi = [x for x in xi_vals if 0 < x < 0.5]
    neg_count = 0
    for xi in nonz_xi:
        c = values_by_xi.get(xi)
        if c is not None and c < 0:
            neg_count += 1
    neg_score = neg_count / len(nonz_xi) if nonz_xi else 1.0
    c0 = values_by_xi.get(0.0)
    nonzero_score = 1.0 if c0 is not None and abs(c0) > 1e-3 else 0.0
    score = 0.7 * points_score + 0.2 * neg_score + 0.1 * nonzero_score
    return score


# === block: score_1 (check id='stiffness') ===
def score_1(artifact, step, ctx):
    ref_dict = ctx['ref_stiffness']
    xi_vals = ctx['xi_vals']
    if not artifact or not isinstance(artifact, list):
        return 0.0
    rows = artifact
    tol_rel = 0.05
    n_total = len(xi_vals)
    within_tol = 0
    s_by_xi = {}
    for row in rows:
        try:
            xi_f = float(row['xi'])
            s = float(row['S_min'])
        except (ValueError, KeyError):
            continue
        xi_closest = min(xi_vals, key=lambda k: abs(k - xi_f))
        if abs(xi_closest - xi_f) > 1e-9:
            continue
        ref_s = ref_dict[xi_closest]
        rel_diff = abs(s - ref_s) / max(abs(ref_s), 1e-12)
        if rel_diff <= tol_rel:
            within_tol += 1
        s_by_xi[xi_closest] = s
    points_score = within_tol / n_total if n_total > 0 else 0.0
    if s_by_xi:
        xi_min_agent = min(s_by_xi, key=lambda x: s_by_xi[x])
        s_min_val = s_by_xi[xi_min_agent]
        s_at_0 = s_by_xi.get(0.0)
        cond = (0.05 <= xi_min_agent <= 0.3) and (s_at_0 is not None and s_at_0 > s_min_val + 1e-6)
        min_score = 1.0 if cond else 0.0
    else:
        min_score = 0.0
    score = 0.6 * points_score + 0.4 * min_score
    return score


_SCORERS = {
    'coulomb': score_0,
    'stiffness': score_1,
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
