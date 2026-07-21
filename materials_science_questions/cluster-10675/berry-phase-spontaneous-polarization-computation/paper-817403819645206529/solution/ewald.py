import numpy as np
from scipy.special import erfc
import csv
import sys

# Constants
Y = 2.0  # Ewald parameter in dimensionless units (a=1, Y*a^2 estimated from paper)
Nt = 5   # reciprocal space cutoff
Nr = 5   # real space cutoff
pi = np.pi

# Atom positions (fractional) for cubic ABO3: A, B, O1, O2, O3
atom_names = ['A', 'B', 'O1', 'O2', 'O3']
frac_pos = np.array([
    [0.0, 0.0, 0.0],
    [0.5, 0.5, 0.5],
    [0.5, 0.5, 0.0],
    [0.5, 0.0, 0.5],
    [0.0, 0.5, 0.5]
])

# Pre‑compute reciprocal lattice vectors tau (2π * integer triplets)
tau_vectors = []
for l in range(-Nt, Nt+1):
    for m in range(-Nt, Nt+1):
        for n in range(-Nt, Nt+1):
            v = np.array([l, m, n], dtype=float)
            if np.all(v == 0):
                continue
            tau_vectors.append(2 * pi * v)
tau_vectors = np.array(tau_vectors)

# Pre‑compute real space lattice vectors R (cell origin = (i,j,k) for a=1)
R_vectors = []
for i in range(-Nr, Nr+1):
    for j in range(-Nr, Nr+1):
        for k in range(-Nr, Nr+1):
            R_vectors.append(np.array([i, j, k], dtype=float))
R_vectors = np.array(R_vectors)

def H_function(x, gamma, gammap):
    """Compute H_{γ,γ'}(x) for distance d (x = sqrt(Y) * |d|)."""
    if x < 1e-12:
        # limit x->0: (4/(3√π)) δ_{\gamma\gamma'}
        return (4.0 / (3.0 * np.sqrt(pi))) * (1.0 if gamma == gammap else 0.0)
    x2 = x * x
    erfcx = erfc(x)
    # Eq A3: H = (x_g x_g' / x^2) * [ 3/x^3 erfc(x) + 2/√π (3/x^2 + 2) exp(-x^2) ] - δ_{γ,γ'} * [ 1/x^3 erfc(x) + 2/√π 1/x^2 exp(-x^2) ]
    common = (2.0 / np.sqrt(pi)) * np.exp(-x2)
    term1 = (3.0 / x**3 * erfcx + common * (3.0 / x2 + 2.0))
    term2 = (1.0 / x**3 * erfcx + common * (1.0 / x2))
    if gamma == gammap:
        return term1 - term2
    else:
        return 0.0  # off-diagonal are zero for isotropic media? Actually no, but we compute per component
    # Actually the full expression includes (x_g x_g'/x^2) factor. We must compute per component.
    # So we should compute the whole tensor for a given vector diff.

def compute_H_matrix(d_vector):
    """Return 3x3 H_{γ,γ'} for displacement vector d."""
    d = d_vector
    d_norm = np.linalg.norm(d)
    x = np.sqrt(Y) * d_norm
    if x < 1e-12:
        return np.eye(3) * (4.0 / (3.0 * np.sqrt(pi)))
    d_hat = d / d_norm
    erfcx = erfc(x)
    common = (2.0 / np.sqrt(pi)) * np.exp(-x * x)
    term1 = (3.0 / x**3 * erfcx + common * (3.0 / x**2 + 2.0))
    term2 = (1.0 / x**3 * erfcx + common / x**2)
    H = np.outer(d_hat, d_hat) * term1 - np.eye(3) * term2
    return H

def compute_C_matrix(q_cart):
    """Compute the 15x15 Coulomb coefficient matrix C_{k,k',γ,γ'} for wave vector q_cart."""
    n_atoms = 5
    n_comp = 3
    size = n_atoms * n_comp
    C = np.zeros((size, size))
    v_a = 1.0  # volume = 1
    q_sq = np.dot(q_cart, q_cart)
    
    # Term from (4π/v_a) q_γ q_γ' / q^2  (Eq A1) — added later
    # Pre‑compute Q matrix
    Q = np.zeros((size, size))

    # Contribution from first/second terms of Eq A2 (reciprocal part)
    # term1 = - (4π/v_a) * (q_γ q_γ' / q^2) * [exp(-q^2/(4Y)) - 1]
    if q_sq > 1e-20:
        factor = (4.0 * pi / v_a)
        exp_term = np.exp(-q_sq / (4.0 * Y)) - 1.0
        for a1 in range(n_atoms):
            for a2 in range(n_atoms):
                delta_r = frac_pos[a1] - frac_pos[a2]
                # The second term sum over tau includes exp(i τ·delta_r)
                for gamma in range(3):
                    for gammap in range(3):
                        idx1 = a1 * 3 + gamma
                        idx2 = a2 * 3 + gammap
                        # term1 part
                        Q[idx1, idx2] += - factor * (q_cart[gamma] * q_cart[gammap] / q_sq) * exp_term
                        # term2: sum over tau != 0
                        sum_recip = 0.0
                        for tau in tau_vectors:
                            k = tau + q_cart
                            k_sq = np.dot(k, k)
                            phase = np.exp(1j * np.dot(tau, delta_r))
                            sum_recip += (k[gamma] * k[gammap] / k_sq) * np.exp(-k_sq / (4.0 * Y)) * phase
                        Q[idx1, idx2] += - factor * sum_recip
    # Real‑space term: Y^{3/2} * sum_{l'} H_{γ,γ'}(√Y |d|) * exp(-i q·d)
    # where d = x(lk) - x(l'k') = (0 + r_k) - (l' + r_k') = - (l' + r_k' - r_k)
    for a1 in range(n_atoms):
        for a2 in range(n_atoms):
            r1 = frac_pos[a1]
            r2 = frac_pos[a2]
            sum_real = np.zeros((3, 3), dtype=complex)
            for R in R_vectors:
                d = r1 - (R + r2)  # displacement vector (Cartesian, unit=1)
                phase = np.exp(-1j * np.dot(q_cart, d))
                H_mat = compute_H_matrix(d)
                sum_real += H_mat * phase
            # special self term: l'=0,k=k' handled by the above; H_function already gives correct limit
            for gamma in range(3):
                for gammap in range(3):
                    idx1 = a1 * 3 + gamma
                    idx2 = a2 * 3 + gammap
                    Q[idx1, idx2] += Y**1.5 * sum_real[gamma, gammap]

    # Total C = (4π/v_a) (q_γ q_γ' / q^2) - Q
    if q_sq > 1e-20:
        fac = (4.0 * pi / v_a)
        for gamma in range(3):
            for gammap in range(3):
                extra = fac * (q_cart[gamma] * q_cart[gammap] / q_sq)
                for a1 in range(n_atoms):
                    for a2 in range(n_atoms):
                        idx1 = a1 * 3 + gamma
                        idx2 = a2 * 3 + gammap
                        C[idx1, idx2] = extra - Q[idx1, idx2]
    else:
        C = -Q  # limit q=0
    return np.real(C)  # should be real

# Transformation to Σ3 basis (Eq 1)
def build_transformation_matrix():
    """Return 15 x 5 matrix T mapping Σ3 basis vector to Cartesian dipole components."""
    T = np.zeros((15, 5))
    inv_sqrt2 = 1.0 / np.sqrt(2.0)
    # ordering: p_A, p_B, p_O1, p_ORot, p_ODist
    # A: (0,0,0)
    T[0, 0] = inv_sqrt2   # A_x
    T[1, 0] = -inv_sqrt2  # A_y
    # A_z = 0
    # B: (0.5,0.5,0.5)
    T[3, 1] = inv_sqrt2   # B_x
    T[4, 1] = -inv_sqrt2  # B_y
    # O1: (0.5,0.5,0)
    T[6, 2] = inv_sqrt2   # O1_x
    T[7, 2] = -inv_sqrt2  # O1_y
    # O2: (0.5,0,0.5) — p_ORot and p_ODist components
    T[9, 3] = inv_sqrt2   # O2_x = p_ORot/√2
    T[10, 4] = -inv_sqrt2 # O2_y = -p_ODist/√2
    # O3: (0,0.5,0.5)
    T[12, 4] = inv_sqrt2  # O3_x = p_ODist/√2
    T[13, 3] = -inv_sqrt2 # O3_y = -p_ORot/√2
    return T

def compute_q_points():
    xi_vals = np.linspace(0, 0.5, 26)  # 0.00 to 0.50 inclusive
    q_list = []
    for xi in xi_vals:
        if xi == 0.0:
            xi_use = 1e-12
        else:
            xi_use = xi
        q_cart = 2 * pi * np.array([xi_use, xi_use, 0.0])
        q_list.append(q_cart)
    return xi_vals, q_list

def main():
    xi_vals, q_list = compute_q_points()
    T = build_transformation_matrix()
    C_A_ORot = []
    S_min_vals = []
    # Polarizabilities for stiffness (in Å^3, but we use a=1 so units consistent)
    alpha_A = 4.9
    alpha_B = 0.37
    alpha_O_A = 4.38
    alpha_O_B = 2.9
    inv_alphas = [1/alpha_A, 1/alpha_B, 1/alpha_O_A, 1/alpha_O_A, 1/alpha_O_B]
    for q_cart in q_list:
        C_cart = compute_C_matrix(q_cart)
        # Transform to Sigma3 basis
        M = T.T @ C_cart @ T  # real symmetric
        C_A_ORot.append(M[0, 3])
        # Stiffness matrix
        S = M + np.diag(inv_alphas)
        eigvals = np.linalg.eigvalsh(S)
        S_min_vals.append(eigvals[0])
    # write coulomb
    with open('/app/outputs/coulomb_coefficients.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['xi', 'C_A_ORot'])
        for x, c in zip(xi_vals, C_A_ORot):
            writer.writerow([f"{x:.2f}", f"{c:.8f}"])
    # write stiffness
    with open('/app/outputs/stiffness_dispersion.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['xi', 'S_min'])
        for x, s in zip(xi_vals, S_min_vals):
            writer.writerow([f"{x:.2f}", f"{s:.8f}"])

if __name__ == '__main__':
    main()
