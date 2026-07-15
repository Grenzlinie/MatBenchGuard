#!/usr/bin/env python3
import numpy as np
from scipy.linalg import eigh, block_diag
import sys

# constants
kB_cm = 0.69503476      # cm⁻¹/K
kB_erg = 1.380649e-16   # erg/K
NA = 6.02214076e23
muB_cgs = 9.274009994e-21  # erg/G
factor_chiT = NA * muB_cgs**2 / kB_erg  # N_A * μ_B^2 / k_B, ≈ 0.37512

def spin_operators(S):
    """Return (Sx, Sy, Sz) for spin S in the |S, m> basis with m = S, S-1, ..., -S."""
    d = int(2*S + 1)
    Sz = np.diag(np.arange(S, -S-1, -1))
    Sp = np.zeros((d, d), dtype=complex)
    Sm = np.zeros((d, d), dtype=complex)
    for i in range(d):
        m = S - i
        if i > 0:   # raising from m-1 -> m
            Sp[i, i-1] = np.sqrt(S*(S+1) - (m-1)*m)
        if i < d-1: # lowering from m+1 -> m
            Sm[i, i+1] = np.sqrt(S*(S+1) - (m+1)*m)
    Sx = 0.5 * (Sp + Sm)
    Sy = -0.5j * (Sp - Sm)
    return Sx, Sy, Sz

def orbital_L_operators():
    """Return (Lx, Ly, Lz) for fictitious L=1 in basis m=1,0,-1."""
    Lz = np.diag([1, 0, -1])
    Lp = np.zeros((3,3), dtype=complex)
    Lp[0,1] = np.sqrt(2)  # |1> <- |0>
    Lp[1,2] = np.sqrt(2)  # |0> <- |-1>
    Lm = Lp.T
    Lx = 0.5 * (Lp + Lm)
    Ly = -0.5j * (Lp - Lm)
    return Lx, Ly, Lz

def build_hs_matrices(kappa, g0):
    """Build S=3/2 and L=1 operators, then the hs block Hamiltonian (spin-orbit only)
       and magnetic moment operators μ_x, μ_y, μ_z (in μ_B units)."""
    Sx, Sy, Sz = spin_operators(1.5)
    Lx, Ly, Lz = orbital_L_operators()

    I3 = np.eye(3, dtype=complex)
    I4 = np.eye(4, dtype=complex)

    # Spin-orbit coupling: H_SO = factor * (L·S) with factor = - (3/2)*kappa*lambda
    # We'll build later with lambda
    Lx_op = np.kron(Lx, I4)
    Ly_op = np.kron(Ly, I4)
    Lz_op = np.kron(Lz, I4)
    Sx_op = np.kron(I3, Sx)
    Sy_op = np.kron(I3, Sy)
    Sz_op = np.kron(I3, Sz)

    HS_LS = Lx_op @ Sx_op + Ly_op @ Sy_op + Lz_op @ Sz_op

    # Zeeman operators (for susceptibility)
    mu_x_hs = g0 * Sx_op - 1.5 * kappa * Lx_op
    mu_y_hs = g0 * Sy_op - 1.5 * kappa * Ly_op
    mu_z_hs = g0 * Sz_op - 1.5 * kappa * Lz_op

    return HS_LS, (mu_x_hs, mu_y_hs, mu_z_hs)

def build_ls_operators(g0, Delta):
    """Build ls block operators: I2 splitting and magnetic moment."""
    # Orbital doublet (u,v) with spin 1/2
    sx, sy, sz = spin_operators(0.5)
    I2_orb = np.eye(2, dtype=complex)  # identity for orbital space
    # Zeeman: only spin contributes
    mu_x_ls = g0 * np.kron(I2_orb, sx)
    mu_y_ls = g0 * np.kron(I2_orb, sy)
    mu_z_ls = g0 * np.kron(I2_orb, sz)

    # Low-symmetry splitting H = (Δ/2) * I₂
    # I₂ eigenvalues: u -> -1, v -> +1
    I2_ls = np.diag([-1, -1, +1, +1])  # ordering: u_up, u_down, v_up, v_down
    H_ls_split = (Delta/2) * I2_ls

    return H_ls_split, I2_ls, (mu_x_ls, mu_y_ls, mu_z_ls)

def van_vleck_chiT(eigvals, eigvecs, mu_x, mu_y, mu_z, T):
    """Compute χT (cm³ K mol⁻¹) using the Van Vleck formula."""
    beta = 1.0 / (kB_cm * T)
    Z = np.sum(np.exp(-eigvals * beta))

    # transform moment operators to eigenbasis
    mu_x_prime = eigvecs.conj().T @ mu_x @ eigvecs
    mu_y_prime = eigvecs.conj().T @ mu_y @ eigvecs
    mu_z_prime = eigvecs.conj().T @ mu_z @ eigvecs

    def compute_component(mu_prime):
        n = len(eigvals)
        diag = 0.0
        off = 0.0
        boltz = np.exp(-eigvals * beta)
        for i in range(n):
            diag += np.abs(mu_prime[i,i])**2 * boltz[i]
        for i in range(n):
            for j in range(i+1, n):
                diff = eigvals[j] - eigvals[i]
                if np.abs(diff) < 1e-10:
                    val = beta * boltz[i]
                else:
                    val = (boltz[i] - boltz[j]) / diff
                off += 2.0 * np.abs(mu_prime[i,j])**2 * val
        return (diag + off) / Z

    total_x = compute_component(mu_x_prime)
    total_y = compute_component(mu_y_prime)
    total_z = compute_component(mu_z_prime)
    chiT = factor_chiT * (total_x + total_y + total_z) / 3.0
    return chiT

def compute_hs_only_chiT(params, T_range):
    """χT for permanently high-spin ions (free hs Co(II))."""
    kappa = params["kappa"]
    g0 = params["g0"]
    lambda_val = params["lambda_val"]
    HS_LS, mu_ops = build_hs_matrices(kappa, g0)
    factor_so = -1.5 * kappa * lambda_val
    H_hs = factor_so * HS_LS
    eigvals, eigvecs = eigh(H_hs)
    chiT_vals = np.array([van_vleck_chiT(eigvals, eigvecs, *mu_ops, T) for T in T_range])
    return chiT_vals

def compute_active_chiT(params, T_range):
    """χT for SCO-active fraction via self-consistent mean-field."""
    J1 = params["J1"]
    J2 = params["J2"]
    Delta_hl = params["Delta_hl"]
    Delta = params["Delta"]
    kappa = params["kappa"]
    g0 = params["g0"]
    lambda_val = params["lambda_val"]

    # Build hs block
    HS_LS, mu_hs = build_hs_matrices(kappa, g0)
    factor_so = -1.5 * kappa * lambda_val
    H_hs_so = factor_so * HS_LS  # 12x12

    # Build ls block
    H_ls_split_block, I2_ls_block, mu_ls = build_ls_operators(g0, Delta)  # 4x4

    # Assemble full 16x16 H0 (without mean-field)
    H_so_full = block_diag(H_hs_so, np.zeros((4,4)))
    I_full = np.diag([1]*12 + [-1]*4)  # tau operator
    I2_full = np.diag([0]*12 + list(np.diag(I2_ls_block)))

    H_gap = (Delta_hl / 2.0) * I_full
    H_ls_full = block_diag(np.zeros((12,12)), H_ls_split_block)
    H0 = H_so_full + H_gap + H_ls_full

    # Full moment operators (for susceptibility after convergence)
    mu_full = []
    for i in range(3):
        mu_full.append(block_diag(mu_hs[i], mu_ls[i]))

    chiT_vals = []

    for T in T_range:
        # Self-consistent loop
        tau = -0.5   # initial guess
        I2bar = 0.5
        converged = False
        for _ in range(500):
            H_mf = -J1 * tau * I_full - J2 * I2bar * I2_full
            H = H0 + H_mf
            eigvals, eigvecs = eigh(H)
            beta = 1.0 / (kB_cm * T)
            boltz = np.exp(-eigvals * beta)
            Z = np.sum(boltz)
            tau_exp = np.sum(np.diag(eigvecs.conj().T @ I_full @ eigvecs) * boltz) / Z
            I2bar_exp = np.sum(np.diag(eigvecs.conj().T @ I2_full @ eigvecs) * boltz) / Z
            if np.abs(tau_exp - tau) < 1e-6 and np.abs(I2bar_exp - I2bar) < 1e-6:
                converged = True
                break
            mixing = 0.3
            tau = tau + mixing * (tau_exp - tau)
            I2bar = I2bar + mixing * (I2bar_exp - I2bar)
        if not converged:
            raise RuntimeError(f"SCF did not converge for compound {params['name']} at T={T}")
        chiT = van_vleck_chiT(eigvals, eigvecs, mu_full[0], mu_full[1], mu_full[2], T)
        chiT_vals.append(chiT)

    return np.array(chiT_vals)

def main():
    outpath = sys.argv[1]
    compounds = [
        {"name": "1", "J1": 24.4, "J2": 132.0, "Delta_hl": 885.0, "Delta": -300.0,
         "lambda_val": -180.0, "kappa": 0.8, "g0": 2.0, "y_hs": 0.204},
        {"name": "2", "J1": 18.6, "J2": 100.7, "Delta_hl": 1264.0, "Delta": -300.0,
         "lambda_val": -180.0, "kappa": 0.8, "g0": 2.0, "y_hs": 0.04},
        {"name": "3", "J1": 18.6, "J2": 100.7, "Delta_hl": 894.0, "Delta": -300.0,
         "lambda_val": -180.0, "kappa": 0.8, "g0": 2.0, "y_hs": 0.018},
    ]

    T_range = np.arange(50, 355, 5)   # 50, 55, ..., 350

    with open(outpath, "w") as f:
        for comp in compounds:
            print(f"Computing compound {comp['name']}...", file=sys.stderr)
            chiT_hs = compute_hs_only_chiT(comp, T_range)
            chiT_active = compute_active_chiT(comp, T_range)
            y = comp["y_hs"]
            for i, T in enumerate(T_range):
                ct = y * chiT_hs[i] + (1.0 - y) * chiT_active[i]
                f.write(f"{comp['name']},{T:.1f},{ct:.6f}\n")
    print("Done.", file=sys.stderr)

if __name__ == "__main__":
    main()
