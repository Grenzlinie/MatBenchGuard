#!/usr/bin/env python3
"""Compute dimensionless glide force Fg for edge dislocation near elliptical inhomogeneity."""
import csv, math, cmath
import numpy as np

R_default = 1.0
G1_default = 1.0
Nmax = 50          # unperturbed series truncation
N = 50             # perturbative series truncation
M = 200            # collocation points

def compute_AB_coeffs(m, r0_over_R, phi0_rad, R=R_default, kappa1=1.8, G1=G1_default):
    gamma = G1 * (0 - 1j) / (math.pi * R * (kappa1 + 1))
    t = r0_over_R * cmath.exp(1j * phi0_rad)
    disc = t**2 - 4*m
    sq = cmath.sqrt(disc)
    zeta0_1 = (t + sq) / 2.0
    zeta0_2 = (t - sq) / 2.0
    if abs(zeta0_1) >= abs(zeta0_2):
        zeta0 = zeta0_1
    else:
        zeta0 = zeta0_2
    rho0 = abs(zeta0)
    theta0 = cmath.phase(zeta0)
    Mval = (rho0**2 - 1) * (1 - m * cmath.exp(2j*theta0)) / (rho0**2 * cmath.exp(2j*theta0) - m)
    A, B = [], []
    for k in range(1, Nmax+1):
        factor = zeta0**(-k)
        Ak = -R * gamma * factor / k
        Bk = R * gamma * (1.0/k + Mval) * factor
        A.append(Ak)
        B.append(Bk)
    return A, B, zeta0, gamma

def evaluate_force_from_perturbative(U_sol, N, m, zeta0, kappa1, G1=G1_default):
    phi_p_at = 0j
    psi_p_at = 0j
    phi_p_prime_at = 0j
    psi_p_prime_at = 0j
    phi_p_double_at = 0j
    for k in range(1, N+1):
        a = U_sol[k-1]
        b = U_sol[N + k - 1]
        if a != 0:
            zk = zeta0 ** (-k)
            phi_p_at += a * zk
            phi_p_prime_at += -k * a * zeta0**(-(k+1))
            phi_p_double_at += k*(k+1) * a * zeta0**(-(k+2))
        if b != 0:
            psi_p_at += b * zeta0**(-k)
            psi_p_prime_at += -k * b * zeta0**(-(k+1))
    om = R_default * (zeta0 + m/zeta0)
    om_prime = R_default * (1 - m/zeta0**2)
    om_double = 2 * R_default * m / (zeta0**3)
    Phi_p = phi_p_prime_at / om_prime
    Phi_p_prime = (phi_p_double_at * om_prime - phi_p_prime_at * om_double) / (om_prime**2)
    gamma_val = G1 * (-1j) / (math.pi * R_default * (kappa1 + 1))
    term1 = (Phi_p + np.conj(Phi_p)) / gamma_val
    term2 = (np.conj(om) * Phi_p_prime + psi_p_prime_at) / (np.conj(gamma_val) * om_prime)
    T = term1 + term2
    return T.real

def solve_hole(m, nu1, r0_over_R, phi0_rad):
    kappa1 = 3 - 4*nu1
    A, B, zeta0, gamma = compute_AB_coeffs(m, r0_over_R, phi0_rad, kappa1=kappa1)
    thetas = np.linspace(0, 2*math.pi, M, endpoint=False)
    sigmas = np.exp(1j * thetas)
    omega = R_default * (sigmas + m / sigmas)
    omega_prime = R_default * (1 - m / sigmas**2)
    phi_star = np.zeros(M, dtype=complex)
    eta_star = np.zeros(M, dtype=complex)
    phi_star_prime = np.zeros(M, dtype=complex)
    for k_idx in range(Nmax):
        k = k_idx + 1
        Ak = A[k_idx]
        Bk = B[k_idx]
        term = sigmas**(-k)
        phi_star += Ak * term
        eta_star += Bk * term
        phi_star_prime += -k * Ak * sigmas**(-(k+1))
    RHS_trac = -( phi_star + omega * np.conj(phi_star_prime) / np.conj(omega_prime) + np.conj(eta_star) )
    Nunknowns = 2*N
    def compute_LHS_trac_unk(U):
        phi_p = np.zeros(M, dtype=complex)
        psi_p = np.zeros(M, dtype=complex)
        phi_p_prime = np.zeros(M, dtype=complex)
        for k in range(1, N+1):
            a = U[k-1]
            if a != 0:
                sigma_neg_k = sigmas**(-k)
                phi_p += a * sigma_neg_k
                phi_p_prime += -k * a * sigmas**(-(k+1))
        for k in range(1, N+1):
            b = U[N + k - 1]
            if b != 0:
                sigma_neg_k = sigmas**(-k)
                psi_p += b * sigma_neg_k
        return phi_p + omega * np.conj(phi_p_prime) / np.conj(omega_prime) + np.conj(psi_p)
    Ntot_real = 2 * Nunknowns
    J = np.zeros((2*M, Ntot_real), dtype=np.float64)
    for idx in range(Nunknowns):
        U = np.zeros(Nunknowns, dtype=complex)
        U[idx] = 1.0
        col_real = np.concatenate([compute_LHS_trac_unk(U).real, compute_LHS_trac_unk(U).imag])
        J[:, 2*idx] = col_real
        U = np.zeros(Nunknowns, dtype=complex)
        U[idx] = 1j
        col_imag = np.concatenate([compute_LHS_trac_unk(U).real, compute_LHS_trac_unk(U).imag])
        J[:, 2*idx+1] = col_imag
    B_real = np.concatenate([RHS_trac.real, RHS_trac.imag])
    x, _, _, _ = np.linalg.lstsq(J, B_real, rcond=None)
    U_sol = np.zeros(Nunknowns, dtype=complex)
    for idx in range(Nunknowns):
        U_sol[idx] = x[2*idx] + 1j * x[2*idx+1]
    return evaluate_force_from_perturbative(U_sol, N, m, zeta0, kappa1)

def solve_rigid(m, nu1, r0_over_R, phi0_rad):
    kappa1 = 3 - 4*nu1
    A, B, zeta0, gamma = compute_AB_coeffs(m, r0_over_R, phi0_rad, kappa1=kappa1)
    thetas = np.linspace(0, 2*math.pi, M, endpoint=False)
    sigmas = np.exp(1j * thetas)
    omega = R_default * (sigmas + m / sigmas)
    omega_prime = R_default * (1 - m / sigmas**2)
    phi_star = np.zeros(M, dtype=complex)
    eta_star = np.zeros(M, dtype=complex)
    phi_star_prime = np.zeros(M, dtype=complex)
    for k_idx in range(Nmax):
        k = k_idx + 1
        Ak = A[k_idx]
        Bk = B[k_idx]
        term = sigmas**(-k)
        phi_star += Ak * term
        eta_star += Bk * term
        phi_star_prime += -k * Ak * sigmas**(-(k+1))
    # Displacement = 0 on boundary
    RHS_disp = -(1/(2*G1_default)) * ( kappa1 * phi_star - omega * np.conj(phi_star_prime) / np.conj(omega_prime) - np.conj(eta_star) )
    Nunknowns = 2*N
    def compute_LHS_disp_unk(U):
        phi_p = np.zeros(M, dtype=complex)
        psi_p = np.zeros(M, dtype=complex)
        phi_p_prime = np.zeros(M, dtype=complex)
        for k in range(1, N+1):
            a = U[k-1]
            if a != 0:
                sigma_neg_k = sigmas**(-k)
                phi_p += a * sigma_neg_k
                phi_p_prime += -k * a * sigmas**(-(k+1))
        for k in range(1, N+1):
            b = U[N + k - 1]
            if b != 0:
                sigma_neg_k = sigmas**(-k)
                psi_p += b * sigma_neg_k
        return (1/(2*G1_default)) * ( kappa1 * phi_p - omega * np.conj(phi_p_prime) / np.conj(omega_prime) - np.conj(psi_p) )
    Ntot_real = 2 * Nunknowns
    J = np.zeros((2*M, Ntot_real), dtype=np.float64)
    for idx in range(Nunknowns):
        U = np.zeros(Nunknowns, dtype=complex)
        U[idx] = 1.0
        col_real = np.concatenate([compute_LHS_disp_unk(U).real, compute_LHS_disp_unk(U).imag])
        J[:, 2*idx] = col_real
        U = np.zeros(Nunknowns, dtype=complex)
        U[idx] = 1j
        col_imag = np.concatenate([compute_LHS_disp_unk(U).real, compute_LHS_disp_unk(U).imag])
        J[:, 2*idx+1] = col_imag
    B_real = np.concatenate([RHS_disp.real, RHS_disp.imag])
    x, _, _, _ = np.linalg.lstsq(J, B_real, rcond=None)
    U_sol = np.zeros(Nunknowns, dtype=complex)
    for idx in range(Nunknowns):
        U_sol[idx] = x[2*idx] + 1j * x[2*idx+1]
    return evaluate_force_from_perturbative(U_sol, N, m, zeta0, kappa1)

def solve_general(m, Gamma, nu1, nu2, r0_over_R, phi0_rad):
    kappa1 = 3 - 4*nu1
    kappa2 = 3 - 4*nu2
    G2 = Gamma * G1_default
    A, B, zeta0, gamma = compute_AB_coeffs(m, r0_over_R, phi0_rad, kappa1=kappa1)
    thetas = np.linspace(0, 2*math.pi, M, endpoint=False)
    sigmas = np.exp(1j * thetas)
    omega = R_default * (sigmas + m / sigmas)
    omega_prime = R_default * (1 - m / sigmas**2)
    phi_star = np.zeros(M, dtype=complex)
    eta_star = np.zeros(M, dtype=complex)
    phi_star_prime = np.zeros(M, dtype=complex)
    for k_idx in range(Nmax):
        k = k_idx + 1
        Ak = A[k_idx]
        Bk = B[k_idx]
        term = sigmas**(-k)
        phi_star += Ak * term
        eta_star += Bk * term
        phi_star_prime += -k * Ak * sigmas**(-(k+1))
    RHS_disp = -(1/(2*G1_default)) * ( kappa1 * phi_star - omega * np.conj(phi_star_prime) / np.conj(omega_prime) - np.conj(eta_star) )
    RHS_trac = -( phi_star + omega * np.conj(phi_star_prime) / np.conj(omega_prime) + np.conj(eta_star) )
    Nunknowns = 4*N + 1  # a_k, b_k, c_k, d_0, d_k
    def compute_LHS_unk(U):
        phi_p = np.zeros(M, dtype=complex)
        psi_p = np.zeros(M, dtype=complex)
        phi_i = np.zeros(M, dtype=complex)
        psi_i = np.zeros(M, dtype=complex)
        phi_p_prime = np.zeros(M, dtype=complex)
        phi_i_prime = np.zeros(M, dtype=complex)
        for k in range(1, N+1):
            a = U[k-1]
            if a != 0:
                s_neg = sigmas**(-k)
                phi_p += a * s_neg
                phi_p_prime += -k * a * sigmas**(-(k+1))
        for k in range(1, N+1):
            b = U[N + k - 1]
            if b != 0:
                psi_p += b * sigmas**(-k)
        for k in range(1, N+1):
            c = U[2*N + k - 1]
            if c != 0:
                s_pos = sigmas**k
                phi_i += c * s_pos
                phi_i_prime += k * c * sigmas**(k-1)
        d0 = U[3*N]
        if d0 != 0:
            psi_i += d0 * np.ones(M)
        for k in range(1, N+1):
            d = U[3*N + k]
            if d != 0:
                psi_i += d * sigmas**k
        LHS_disp = (1/(2*G1_default)) * ( kappa1 * phi_p - omega * np.conj(phi_p_prime) / np.conj(omega_prime) - np.conj(psi_p) ) \
                   - (1/(2*G2)) * ( kappa2 * phi_i - omega * np.conj(phi_i_prime) / np.conj(omega_prime) - np.conj(psi_i) )
        LHS_trac = (phi_p + omega * np.conj(phi_p_prime) / np.conj(omega_prime) + np.conj(psi_p)) \
                   - (phi_i + omega * np.conj(phi_i_prime) / np.conj(omega_prime) + np.conj(psi_i))
        return LHS_disp, LHS_trac
    Ntot_real = 2 * Nunknowns
    J = np.zeros((4*M, Ntot_real), dtype=np.float64)
    for idx in range(Nunknowns):
        U = np.zeros(Nunknowns, dtype=complex)
        U[idx] = 1.0
        Ld, Lt = compute_LHS_unk(U)
        col_real = np.concatenate([Ld.real, Ld.imag, Lt.real, Lt.imag])
        J[:, 2*idx] = col_real
        U = np.zeros(Nunknowns, dtype=complex)
        U[idx] = 1j
        Ld, Lt = compute_LHS_unk(U)
        col_imag = np.concatenate([Ld.real, Ld.imag, Lt.real, Lt.imag])
        J[:, 2*idx+1] = col_imag
    B_real = np.concatenate([RHS_disp.real, RHS_disp.imag, RHS_trac.real, RHS_trac.imag])
    x, _, _, _ = np.linalg.lstsq(J, B_real, rcond=None)
    U_sol = np.zeros(Nunknowns, dtype=complex)
    for idx in range(Nunknowns):
        U_sol[idx] = x[2*idx] + 1j * x[2*idx+1]
    # force uses only a_k, b_k
    return evaluate_force_from_perturbative(U_sol[:2*N], N, m, zeta0, kappa1)

def compute_Fg(case):
    m, Gamma, nu1, nu2, r0_over_R, phi0_deg = case
    phi0 = math.radians(phi0_deg)
    if Gamma == 0.0:
        return solve_hole(m, nu1, r0_over_R, phi0)
    elif Gamma > 1e9:
        return solve_rigid(m, nu1, r0_over_R, phi0)
    else:
        return solve_general(m, Gamma, nu1, nu2, r0_over_R, phi0)

test_cases = [
    (0.0, 0.0, 0.3, 0.3, 5.0, 0.0),
    (0.0, 0.0, 0.3, 0.3, 5.0, 90.0),
    (0.5, 0.0, 0.3, 0.3, 5.0, 30.0),
    (0.5, 0.0, 0.3, 0.3, 5.0, 150.0),
    (-0.5, 0.0, 0.3, 0.3, 5.0, 60.0),
    (-0.5, 0.0, 0.3, 0.3, 5.0, 120.0),
    (0.0, 1e10, 0.3, 0.3, 5.0, 0.0),
    (0.0, 1e10, 0.3, 0.3, 5.0, 90.0),
    (0.5, 1e10, 0.3, 0.3, 5.0, 30.0),
    (-0.5, 1e10, 0.3, 0.3, 5.0, 60.0),
    (0.0, 0.1, 0.3, 0.3, 5.0, 0.0),
    (0.0, 10.0, 0.3, 0.3, 5.0, 0.0),
    (0.5, 0.1, 0.3, 0.3, 5.0, 90.0),
    (-0.5, 10.0, 0.3, 0.3, 5.0, 90.0),
    (0.0, 0.0, 0.3, 0.3, 2.0, 0.0),
    (0.0, 1e10, 0.3, 0.3, 2.0, 0.0),
    (0.9, 0.0, 0.3, 0.3, 5.0, 0.0),
    (-0.9, 0.0, 0.3, 0.3, 5.0, 0.0),
]

out_path = '/app/outputs/glide_force_values.csv'
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['m', 'Gamma', 'nu1', 'nu2', 'r0_over_R', 'phi0_deg', 'Fg'])
    for case in test_cases:
        Fg = compute_Fg(case)
        writer.writerow([case[0], case[1], case[2], case[3], case[4], case[5], Fg])
