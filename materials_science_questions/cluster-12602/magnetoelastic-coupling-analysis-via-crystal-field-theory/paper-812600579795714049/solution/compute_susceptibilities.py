#!/usr/bin/env python3
"""Compute magnetic susceptibilities for the third-order susceptibility paper."""
import argparse
import csv
import os
import numpy as np
from scipy.linalg import expm

# Physical constants (energy unit = Kelvin)
J = 6
GJ = 7/6          # Landé factor for Tm3+
MU_B = 1.0
KB = 1.0

# Lea-Leask-Wolf parameters for TmCu (paper Table I)
W = 1.4           # K
x = -0.42
THETA_STAR = -3.0  # K
G1 = 10.3e-3       # K  (mK -> K)
G2 = -60e-3        # K

# Bilinear exchange coefficient n = Theta*/C, C = gJ^2 muB^2 J(J+1)/3
C = (GJ**2 * MU_B**2) * J * (J+1) / 3.0
n = THETA_STAR / C

def op_Jz():
    """J_z matrix in |J,M> basis (M from J to -J)."""
    N = int(2*J + 1)
    Jz = np.zeros((N, N))
    for i in range(N):
        m = J - i
        Jz[i, i] = m
    return Jz

def op_Jx():
    """J_x matrix in |J,M> basis."""
    N = int(2*J + 1)
    Jx = np.zeros((N, N))
    for i in range(N):
        m = J - i
        if i > 0:
            mp = J - (i-1)
            Jx[i-1, i] = 0.5 * np.sqrt(J*(J+1) - mp*m)
            Jx[i, i-1] = 0.5 * np.sqrt(J*(J+1) - m*mp)
    return Jx

def op_Jy():
    """J_y matrix."""
    N = int(2*J + 1)
    Jy = np.zeros((N, N), dtype=complex)
    for i in range(N):
        m = J - i
        if i > 0:
            mp = J - (i-1)
            Jy[i-1, i] = -0.5j * np.sqrt(J*(J+1) - mp*m)
            Jy[i, i-1] =  0.5j * np.sqrt(J*(J+1) - m*mp)
    return Jy

def op_O20():
    """O_2^0 = 3 J_z^2 - J(J+1) matrix."""
    Jz = op_Jz()
    return 3 * Jz @ Jz - J*(J+1) * np.eye(int(2*J+1))

def build_H_llw(W, x):
    """Cubic CEF Hamiltonian in LLW form for |J,M> basis, quantization axis [001]."""
    N = int(2*J + 1)
    # Stevens operators
    Jz = op_Jz()
    Jplus = np.zeros((N, N), dtype=complex)
    Jminus = np.zeros((N, N), dtype=complex)
    for i in range(N):
        m = J - i
        if i > 0:
            mp = J - (i-1)
            Jplus[i-1, i] = np.sqrt(J*(J+1) - mp*m)
            Jminus[i, i-1] = np.sqrt(J*(J+1) - m*mp)
    Jz2 = Jz @ Jz
    Jz4 = Jz2 @ Jz2
    Jz6 = Jz4 @ Jz2

    # O_4^0
    O40 = 35 * Jz4 - (30*J*(J+1) - 25) * Jz2 + (3*J**2*(J+1)**2 - 6*J*(J+1)) * np.eye(N)
    # O_4^4 = 1/2 (J_+^4 + J_-^4)
    Jp4 = Jplus @ Jplus @ Jplus @ Jplus
    Jm4 = Jminus @ Jminus @ Jminus @ Jminus
    O44 = 0.5 * (Jp4 + Jm4)

    # O_6^0
    O60 = (231 * Jz6
           - (315*J*(J+1) - 735) * Jz4
           + (105*J**2*(J+1)**2 - 525*J*(J+1) + 294) * Jz2
           - (5*J**3*(J+1)**3 - 40*J**2*(J+1)**2 + 60*J*(J+1)) * np.eye(N))
    # O_6^4 = 1/2 (J_+^4 + J_-^4) * (11 J_z^2 - J(J+1) - 38) + ... actually standard:
    # O_6^4 = 1/4 (J_+^4 + J_-^4)(11 J_z^2 - J(J+1) - 38)  (for J<=8?) but LLW uses specific combination.
    # I'll use the standard cubic combination as given in literature:
    # O6 (cubic) = O_6^0 - 21 O_6^4, with O_6^4 = 1/4 (J_+^4+J_-^4)(11 J_z^2 - J(J+1) - 38)
    O64 = 0.25 * (Jp4 + Jm4) @ (11 * Jz2 - J*(J+1) - 38)

    # LLW parameters: F4=60, F6=2520 for J=6
    F4 = 60
    F6 = 2520
    H = W * ( x * (O40 + 5*O44)/F4 + (1 - np.abs(x)) * (O60 - 21*O64)/F6 )
    return H

def diagonalize(H):
    E, V = np.linalg.eigh(H)
    # Ensure real
    E = np.real(E)
    V = np.real(V)
    return E, V

def compute_susceptibilities(E, V, Jz_op, O20_op, T_arr):
    """Compute CEF-only susceptibilities for one direction."""
    N = len(E)
    # Degeneracies (we'll treat each eigenvalue individually, but use eigenvectors matrix)
    # We'll compute sums as in Appendix A using explicit loop over eigenstates (all columns of V)
    # Eigenvalues E are unique? We'll treat each eigenstate separately.
    # V columns are eigenvectors; V[:, i] is state i, eigenvalue E[i].
    # Use full matrix elements in eigenbasis: Jz_ik_jl = V^H @ Jz_op @ V, etc.
    Jz_diag = V.T @ Jz_op @ V
    O20_diag = V.T @ O20_op @ V
    # We'll need off-diagonal elements too.
    chi0_1 = np.zeros_like(T_arr)
    chi0_3 = np.zeros_like(T_arr)
    chi2 = np.zeros_like(T_arr)
    chi2_2 = np.zeros_like(T_arr)

    for idx_t, T in enumerate(T_arr):
        beta = 1.0 / T
        # Boltzmann factors
        f = np.exp(-beta * E)
        Z = np.sum(f)
        f /= Z  # normalised

        # chi0^(1) Eq. (A5)
        sum_1 = 0.0
        for i in range(N):
            for k in range(N):  # state k in degenerate subspace? We'll treat all states individually.
                # Actually, the paper sums over i (level) and k (degeneracy index).
                # Our diagonalization gives N states, each considered distinct.
                # So we can sum over all i (state index) with population f_i.
                fi = f[i]
                # part 1: -2 sum_{j != i} |J_{i,k=0, j,l}? We'll sum over all distinct states j.
                # Since we treat all states equally, sum over all j != i.
                # We need matrix elements J_{ik,jl}. For non-degenerate, k=l=0.
                # For each state i, we use the matrix element J_{i,j}.
                # So J_{ik,jl} -> Jz_diag[i,j].
                # The sum over k and l inside the inner sum is just summing over degenerate indices when levels are degenerate.
                # But our states are individually indexed, so we can just sum over all j.
                off_term = 0.0
                for j in range(N):
                    if j == i:
                        continue
                    off_term += np.abs(Jz_diag[i, j])**2 / (E[i] - E[j])
                diag_term = np.abs(Jz_diag[i, i])**2 / T
                sum_1 += fi * (-2 * off_term + diag_term)
        chi0_1[idx_t] = GJ**2 * MU_B**2 * sum_1

        # chi2 Eq. (A6)
        sum_2 = 0.0
        for i in range(N):
            fi = f[i]
            off_term = 0.0
            for j in range(N):
                if j == i:
                    continue
                off_term += np.abs(O20_diag[i, j])**2 / (E[i] - E[j])
            diag_term = np.abs(O20_diag[i, i])**2 / T
            sum_2 += fi * (-2 * off_term + diag_term)
        chi2[idx_t] = sum_2

        # chi2^(2) Eq. (A7) - complex. Implement exactly.
        # Note: Jz_ik,jl etc. We'll compute using full matrix.
        sum_2_2 = 0.0
        for i in range(N):
            fi = f[i]
            # term A
            termA = 0.0
            for j in range(N):
                if j == i:
                    continue
                for jp in range(N):
                    if jp == i:
                        continue
                    # J_{ik,jl} Q_{jl,j' l'} J_{j' l', i k} + 2 Q_{ik,jl} J_{jl,j'l'} J_{j'l',ik}
                    # Here ik is state i, jl is j, j'l' is jp.
                    term1 = Jz_diag[i, j] * O20_diag[j, jp] * Jz_diag[jp, i]
                    term2 = 2 * O20_diag[i, j] * Jz_diag[j, jp] * Jz_diag[jp, i]
                    denom = (E[i] - E[j]) * (E[i] - E[jp])
                    termA += (term1 + term2) / denom if denom != 0 else 0.0
            # term B
            termB = 0.0
            for j in range(N):
                if j == i:
                    continue
                val = (np.abs(Jz_diag[i, j])**2 * O20_diag[i, i]
                       + 2 * O20_diag[i, j] * Jz_diag[j, i] * Jz_diag[i, i])
                denom = (E[i] - E[j]) * (1.0/(E[i] - E[j]) + 1.0/T)
                termB -= val * (1.0/(E[i] - E[j]) + 1.0/T)  # actually already factored
            # term C
            termC = 0.5 * Jz_diag[i, i]**2 * O20_diag[i, i] / (T**2)
            sum_2_2 += fi * (termA + termB + termC)
        chi2_2[idx_t] = GJ**2 * MU_B**2 * sum_2_2

        # chi0^(3) Eq. (A8)
        # This is huge; implement literally.
        term1 = -0.5 * (chi0_1[idx_t])**2 / T  # -1/(2kBT) (chi0)^2
        sum_3 = 0.0
        for i in range(N):
            fi = f[i]
            # term (i) triple sum
            t1 = 0.0
            for j in range(N):
                if j == i: continue
                for jp in range(N):
                    if jp == i: continue
                    for jpp in range(N):
                        if jpp == i: continue
                        val = (Jz_diag[i,j] * Jz_diag[j,jp] * Jz_diag[jp,jpp] * Jz_diag[jpp,i])
                        denom = (E[i]-E[j]) * (E[i]-E[jp]) * (E[i]-E[jpp])
                        t1 += val / denom if denom != 0 else 0.0
            # term (ii) two sums
            t2 = 0.0
            for j in range(N):
                if j == i: continue
                for jp in range(N):
                    if jp == i: continue
                    val = (np.abs(Jz_diag[i,j])**2 * np.abs(Jz_diag[i,jp])**2
                           + 2 * Jz_diag[i,j] * Jz_diag[j,jp] * Jz_diag[jp,i] * Jz_diag[i,i])
                    denom = (E[i]-E[j]) * (E[i]-E[jp])
                    factor = (2.0/(E[i]-E[j]) + 1.0/T)
                    t2 += val * factor / denom if denom != 0 else 0.0
            # term (iii) single sum
            t3 = 0.0
            for j in range(N):
                if j == i: continue
                val = np.abs(Jz_diag[i,i])**2 * np.abs(Jz_diag[i,j])**2
                denom = E[i]-E[j] if E[i]!=E[j] else 1e-12
                t3 -= val * (2.0/denom**2 + 2.0/(denom*T) + 1.0/T**2) / denom
            # term (iv) diagonal
            t4 = (1.0/(6.0*T**3)) * np.abs(Jz_diag[i,i])**4
            inner = -4 * t1 + 2 * t2 + t3 + t4
            sum_3 += fi * inner
        chi0_3_val = GJ**4 * MU_B**4 * sum_3 + term1
        chi0_3[idx_t] = chi0_3_val

    return chi0_1, chi0_3, chi2, chi2_2

def rotation_matrix_111():
    """Unitary rotation matrix U that rotates the basis so that [111] becomes new z."""
    # Euler angles: α=45°, β=acos(1/√3), γ=0.
    alpha = np.pi/4
    beta = np.arccos(1.0/np.sqrt(3.0))
    Jz = op_Jz()
    Jy = op_Jy()
    U_z = expm(-1j * alpha * Jz)
    U_y = expm(-1j * beta * Jy)
    U = U_z @ U_y
    return U

def compute_111_direction(H_orig, T_arr):
    """Compute susceptibilities for [111] by rotating Hamiltonian."""
    U = rotation_matrix_111()
    H_new = U.conj().T @ H_orig @ U
    E_new, V_new = np.linalg.eigh(H_new)
    E_new = np.real(E_new)
    V_new = np.real(V_new)
    # Jz' and O2'^0 in the new basis are simply the standard Jz and O20 operators
    Jz_std = op_Jz()
    O20_std = op_O20()
    chi0_1p, chi0_3p, chi2p, chi2_2p = compute_susceptibilities(E_new, V_new, Jz_std, O20_std, T_arr)
    # chi0_1 should be equal to chi0_1 (isotropic)
    return chi0_1p, chi0_3p, chi2p, chi2_2p

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--temp-min', type=float, default=5)
    parser.add_argument('--temp-max', type=float, default=100)
    parser.add_argument('--num-temp', type=int, default=100)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    T_arr = np.linspace(args.temp_min, args.temp_max, args.num_temp)

    # ----- [001] direction -----
    H_001 = build_H_llw(W, x)
    E_001, V_001 = diagonalize(H_001)
    Jz_001 = op_Jz()
    O20_001 = op_O20()
    chi0_1, chi0_3, chi2, chi2_2 = compute_susceptibilities(E_001, V_001, Jz_001, O20_001, T_arr)

    # total chi_M^(1)
    chi_M1 = chi0_1 / (1 - n * chi0_1)

    # total chi_M^(3) for [001]
    denom_enh = (1 - n * chi0_1)**4
    term_cef = chi0_3 / denom_enh
    term_quad = 2 * G1 * (chi2_2**2) / (denom_enh * (1 - G1 * chi2))
    chi_M3_001 = term_cef + term_quad

    # ----- [111] direction -----
    chi0_1_111, chi0_3_111, chi2_111, chi2_2_111 = compute_111_direction(H_001, T_arr)
    # n is same; chi0_1_111 should be same as chi0_1 (check)
    # Actually, due to isotropy, chi0_1_111 = chi0_1 exactly (within numerical), we'll use it.
    chi_M1_111 = chi0_1_111 / (1 - n * chi0_1_111)
    denom_enh_111 = (1 - n * chi0_1_111)**4
    term_cef_111 = chi0_3_111 / denom_enh_111
    # Note: formula for [111] has 1/6 G2 factor:
    # chi_M^(3)' = chi0_3' / (1-n chi0_1)^4 + (1/6)*G2 * (chi2_2')^2 / ((1-n chi0_1)^4 * (1 - G2*chi2'/12))
    # per Appendix B, Eq. (B6)
    quad_denom_111 = 1 - (G2 / 12.0) * chi2_111
    term_quad_111 = (1.0/6.0) * G2 * (chi2_2_111**2) / (denom_enh_111 * quad_denom_111)
    chi_M3_111 = term_cef_111 + term_quad_111

    # Write chi_M1.csv
    with open(os.path.join(args.output_dir, 'chi_M1.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'chi_M1'])
        for T, val in zip(T_arr, chi_M1):
            writer.writerow([T, val])

    # Write chi_M3.csv
    with open(os.path.join(args.output_dir, 'chi_M3.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'chi_M3_001', 'chi_M3_111'])
        for T, v001, v111 in zip(T_arr, chi_M3_001, chi_M3_111):
            writer.writerow([T, v001, v111])

if __name__ == '__main__':
    main()
