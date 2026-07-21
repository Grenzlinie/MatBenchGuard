#!/usr/bin/env python3
"""Reference oracle: compute Bi2Se3 cylindrical TI eigenenergies and overlap integrals."""

import os, csv
import numpy as np
from scipy.special import jv
from scipy.optimize import minimize_scalar
from scipy.integrate import quad

# material parameters for Bi2Se3 (Table 1)
m0 = -0.169  # eV
m1 = 3.353   # eV Å^2
m2 = 29.375  # eV Å^2
A  = 2.513   # eV Å
B  = 1.836   # eV Å (unused for kz=0)
R0_ang = 14.9  # R0 = 1.49 nm = 14.9 Å

# radial values (nm) -> convert to Å for computation
R_vals_nm = [2*1.49, 4*1.49, 6*1.49, 8*1.49, 10*1.49]  # exact multiples
R_vals_ang = [r*10 for r in R_vals_nm]

def kappa(E):
    """Compute kappa_plus and kappa_minus for kz=0 (Eq.8)."""
    base = -(m0/m2 + A**2/(2*m2**2))
    disc = A**4/(4*m2**4) + E**2/m2**2 + A**2*m0/m2**3
    if disc < 0:
        disc = 0  # should not happen for realistic energies
    sqrt_disc = np.sqrt(disc)
    # ensure ordering: kappa_plus corresponds to +sqrt(disc), kappa_minus to -sqrt(disc)
    inner_plus = base + sqrt_disc
    inner_minus = base - sqrt_disc
    # return sqrt with positive imaginary part convention? use principal sqrt
    kp = np.sqrt(inner_plus + 0j)
    km = np.sqrt(inner_minus + 0j)
    return kp, km

def delta(E, k):
    """Delta_eta = m2*k^2 + m0 - E"""
    return m2 * k**2 + m0 - E

def alpha_det_score(E, j, R):
    """Score = |det(alpha block)|^2 for secular equation (12a)."""
    if np.abs(E) < 1e-9:
        return 1e30
    kp, km = kappa(E)
    Dp = delta(E, kp)
    Dm = delta(E, km)
    if np.abs(Dp) < 1e-12 or np.abs(Dm) < 1e-12:
        return 1e30
    Jp_m = jv(j-0.5, kp*R)
    Jp_p = jv(j+0.5, kp*R)
    Jm_m = jv(j-0.5, km*R)
    Jm_p = jv(j+0.5, km*R)
    det = (A*kp/Dp) * Jp_m * Jm_p - (A*km/Dm) * Jm_m * Jp_p
    return np.abs(det)**2

def find_root(j, R, sign):
    """Find smallest |E| root with given sign for alpha block secular eq."""
    # approximate energy from large-radius expansion
    E_approx = sign * A * np.abs(j) / R
    # search bracket: around E_approx, extended if needed
    if sign > 0:
        low = max(1e-5, E_approx*0.3)
        high = E_approx*3.0 + 0.1
    else:
        high = min(-1e-5, E_approx*0.3)
        low = E_approx*3.0 - 0.1
    # coarse grid to locate minima
    energies = np.linspace(low, high, 300)
    scores = np.array([alpha_det_score(E, j, R) for E in energies])
    # find local minima
    from scipy.signal import argrelextrema
    # simple approach: find indices where score < threshold and is a local minimum
    # choose energy with smallest |E| that is a decent candidate
    threshold = 1e-3
    candidate_indices = []
    for i in range(1, len(energies)-1):
        if scores[i] < scores[i-1] and scores[i] < scores[i+1] and scores[i] < threshold:
            candidate_indices.append(i)
    if not candidate_indices:
        # fallback: use the global minimum
        i_min = np.argmin(scores)
        candidate_indices = [i_min]
    # among candidates, pick the one with smallest |E|
    best_E = energies[candidate_indices[0]]
    best_min = scores[candidate_indices[0]]
    for idx in candidate_indices:
        if np.abs(energies[idx]) < np.abs(best_E):
            best_E = energies[idx]
            best_min = scores[idx]
    # refine with bounded scalar minimization around best_E
    bracket = (best_E - 0.02, best_E + 0.02)
    # ensure bracket stays in sign
    if sign > 0:
        bracket = (max(1e-6, bracket[0]), bracket[1])
    else:
        bracket = (bracket[0], min(-1e-6, bracket[1]))
    res = minimize_scalar(lambda x: alpha_det_score(x, j, R), bracket=bracket, method='bounded')
    if res.success and alpha_det_score(res.x, j, R) < 1e-5:
        return res.x
    else:
        # fallback: return best guess from grid
        return best_E

def radial_wavefunction(E, j, R, rho_arr):
    """Compute normalized radial components Phi1, Phi2, Phi3, Phi4 for alpha solution (kz=0).
    Returns array of shape (4, len(rho_arr)) """
    kp, km = kappa(E)
    Dp = delta(E, kp)
    Dm = delta(E, km)
    # Build 2x2 alpha block matrix (complex)
    A_mat = np.array([
        [ (1j*A*kp/Dp) * jv(j-0.5, kp*R), (1j*A*km/Dm) * jv(j-0.5, km*R) ],
        [ jv(j+0.5, kp*R), jv(j+0.5, km*R) ]
    ], dtype=complex)
    # null space via SVD
    U, S, Vh = np.linalg.svd(A_mat)
    alpha = Vh[-1, :]  # coefficients (alpha_+, alpha_-), up to normalization
    # compute radial functions on grid
    Phi = np.zeros((4, len(rho_arr)), dtype=complex)
    for eta_idx, eta in enumerate([kp, km]):
        a = alpha[eta_idx]
        D = delta(E, eta)
        J_minus = jv(j-0.5, eta * rho_arr)
        J_plus  = jv(j+0.5, eta * rho_arr)
        # component 1
        Phi[0] += a * (1j*A*eta/D) * J_minus
        # component 4
        Phi[3] += a * J_plus
        # components 2 and 3 are zero for alpha solution
    # normalization integral sum_i |Phi_i|^2 * rho d rho
    def norm_integrand(rho):
        # compute Phi at rho
        Phi_rho = np.zeros(4, dtype=complex)
        for eta_idx, eta in enumerate([kp, km]):
            a = alpha[eta_idx]
            D = delta(E, eta)
            Jm = jv(j-0.5, eta * rho)
            Jp = jv(j+0.5, eta * rho)
            Phi_rho[0] += a * (1j*A*eta/D) * Jm
            Phi_rho[3] += a * Jp
        return rho * np.sum(np.abs(Phi_rho)**2)
    norm, _ = quad(norm_integrand, 0, R, limit=200)
    alpha /= np.sqrt(norm)
    # recompute Phi with normalized alpha
    Phi[:] = 0.0
    for eta_idx, eta in enumerate([kp, km]):
        a = alpha[eta_idx]
        D = delta(E, eta)
        J_minus = jv(j-0.5, eta * rho_arr)
        J_plus  = jv(j+0.5, eta * rho_arr)
        Phi[0] += a * (1j*A*eta/D) * J_minus
        Phi[3] += a * J_plus
    return Phi

def overlap_integral(Phi1, Phi2, R, rho_arr):
    """Compute integral rho * conj(Phi1) * Phi2 drho on grid using trapezoidal rule."""
    integrand = rho_arr * np.conj(Phi1) * Phi2
    return np.trapz(integrand, rho_arr)

# main
outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)

# output 1: eigenenergies
energies_rows = []
for R_nm, R_ang in zip(R_vals_nm, R_vals_ang):
    for j in [0.5, 1.5]:
        E_pos = find_root(j, R_ang, sign=1)
        energies_rows.append({'j': j, 'R': R_nm, 'energy': E_pos})

with open(os.path.join(outdir, 'step_01_eigenenergies.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['j','R','energy'])
    writer.writeheader()
    writer.writerows(energies_rows)

# output 2: overlap integrals
overlap_rows = []
# fine radial grid
rho_arr = np.linspace(0, 1, 2000)  # relative to R, but we need absolute? We'll scale later
for R_nm, R_ang in zip(R_vals_nm, R_vals_ang):
    # state 1: s=+, j=0.5
    E_p = find_root(0.5, R_ang, sign=1)
    Phi_p = radial_wavefunction(E_p, 0.5, R_ang, rho_arr * R_ang)  # absolute radial coordinate
    # state 2: s=-, j=-0.5
    E_n = find_root(-0.5, R_ang, sign=-1)
    Phi_n = radial_wavefunction(E_n, -0.5, R_ang, rho_arr * R_ang)
    # S14 = int_0^R rho * conj(Phi1_{s=+,j=0.5}) * Phi4_{s=-,j=-0.5}
    S14 = overlap_integral(Phi_p[0], Phi_n[3], R_ang, rho_arr * R_ang)
    S14_abs = np.abs(S14)
    # S23 = int conj(Phi2_{s=+}) * Phi3_{s=-} — both are zero for alpha solutions
    S23_abs = 0.0
    overlap_rows.append({'j': 0.5, 'R': R_nm, 'S_14': S14_abs, 'S_23': S23_abs})

with open(os.path.join(outdir, 'step_02_overlap_integrals.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['j','R','S_14','S_23'])
    writer.writeheader()
    writer.writerows(overlap_rows)
