#!/usr/bin/env python3
"""Reference oracle computation of phase diagram, strains, and MSDW averages.
Integration over the sphere and free energy minimization
for the Hamiltonian of Eqs.(7)-(10) with A=1.0, B=0.5, C=0.5, kappa=5000.0.
"""

import numpy as np
from scipy.optimize import minimize
import csv, os, sys

# Fixed parameters
A_coef = 1.0
B_coef = 0.5
C_coef = 0.5
kappa = 5000.0

# --- Integration grid on unit sphere (theta, phi) ---
Ntheta = 80
Nphi = 160
theta = np.linspace(0, np.pi, Ntheta)
phi = np.linspace(0, 2*np.pi, Nphi)
dtheta = theta[1] - theta[0]
dphi = phi[1] - phi[0]
THETA, PHI = np.meshgrid(theta, phi, indexing='ij')
sinTH = np.sin(THETA)
weights = sinTH * dtheta * dphi   # shape (Ntheta, Nphi)

# Squared amplitudes
Ax2 = sinTH**2 * np.cos(PHI)**2
Ay2 = sinTH**2 * np.sin(PHI)**2
Az2 = np.cos(THETA)**2

# Symmetry-adapted MSDW variables
sqrt2 = np.sqrt(2)
sqrt6 = np.sqrt(6)
X2 = (Ax2 - Ay2) / sqrt2
X3 = (2*Az2 - Ax2 - Ay2) / sqrt6

poly_quad = X2**2 + X3**2
poly_cubic = X3**3 - 3*X3*X2**2
poly_quartic = poly_cubic**2

H_elect_base = A_coef * poly_quad + B_coef * poly_cubic + C_coef * poly_quartic

def compute_Z_avgs(g, T, eps2, eps3):
    """Compute partition function Z and averages <Ax^2>,<Ay^2>,<Az^2>
    for given g, temperature T, strains eps2,eps3.
    Handles T small but >0; caller must not call with T=0 (use ground_state)."""
    H_coupling = g * (eps2 * X2 + eps3 * X3)
    H_elastic = 0.5 * kappa * (eps2**2 + eps3**2)
    H_total = H_elect_base + H_coupling + H_elastic
    # avoid overflow for low T by clamping
    if T < 1e-10:
        T_safe = 1e-10
    else:
        T_safe = T
    boltz = np.exp(-H_total / T_safe)
    Z = np.sum(boltz * weights)
    avg_Ax2 = np.sum(Ax2 * boltz * weights) / Z
    avg_Ay2 = np.sum(Ay2 * boltz * weights) / Z
    avg_Az2 = np.sum(Az2 * boltz * weights) / Z
    return Z, avg_Ax2, avg_Ay2, avg_Az2

def free_energy_fun(eps_vec, g, T):
    eps2, eps3 = eps_vec
    Z, _, _, _ = compute_Z_avgs(g, T, eps2, eps3)
    F = -T * np.log(Z) if T > 0 else 0.0
    return F

def ground_state_phase(g):
    """T=0 ground state classification by minimizing Eq.(13) over X2,X3.
    Returns (eps2, eps3, phase_label)."""
    A_eff = A_coef - g**2/(2*kappa)
    # Effective Hamiltonian eq. (13) to minimize over X2,X3 on the triangle
    # We sample fine grid on (X2,X3) that satisfy the triangle constraints.
    # However, direct sampling on (Ax^2,Ay^2,Az^2) is easier.
    # Sample random points on sphere, evaluate H_eff, take min.
    best_H = np.inf
    best_X2 = None
    best_X3 = None
    n_samples = 5000
    # generate random unit vectors
    rand_vecs = np.random.randn(n_samples, 3)
    rand_vecs /= np.linalg.norm(rand_vecs, axis=1)[:, np.newaxis]
    Ax2_s = rand_vecs[:,0]**2
    Ay2_s = rand_vecs[:,1]**2
    Az2_s = rand_vecs[:,2]**2
    X2_s = (Ax2_s - Ay2_s) / sqrt2
    X3_s = (2*Az2_s - Ax2_s - Ay2_s) / sqrt6
    H_eff = A_eff * (X2_s**2 + X3_s**2) + B_coef * (X3_s**3 - 3*X3_s*X2_s**2) + C_coef * (X3_s**3 - 3*X3_s*X2_s**2)**2
    idx = np.argmin(H_eff)
    best_X2 = X2_s[idx]
    best_X3 = X3_s[idx]
    # equilibrium strains from eqs (11),(12)
    eps2 = -g/kappa * best_X2
    eps3 = -g/kappa * best_X3
    # classify
    eps_thr = 1e-10
    if abs(eps2) < eps_thr and abs(eps3) < eps_thr:
        phase = 'cubic'
    elif abs(eps2) < eps_thr and eps3 > eps_thr:
        phase = 'tet_more'
    elif abs(eps2) < eps_thr and eps3 < -eps_thr:
        phase = 'tet_less'
    else:
        phase = 'ortho'
    return eps2, eps3, phase

def determine_phase(eps2, eps3):
    eps_thr = 1e-8
    if abs(eps2) < eps_thr and abs(eps3) < eps_thr:
        return 'cubic'
    elif abs(eps2) < eps_thr and eps3 > eps_thr:
        return 'tet_more'
    elif abs(eps2) < eps_thr and eps3 < -eps_thr:
        return 'tet_less'
    else:
        return 'ortho'

# ---------- Output directory ----------
OUTDIR = '/app/outputs'
os.makedirs(OUTDIR, exist_ok=True)

# ================== Phase diagram ==================
sqrt_g_vals = np.linspace(9.4, 13.0, 19)   # 19 points, step ~0.2
kBT_vals = np.linspace(0.0, 0.15, 16)      # 16 points, step 0.01

phase_rows = []
for sqrt_g in sqrt_g_vals:
    g = sqrt_g**2
    for kBT in kBT_vals:
        if kBT == 0.0:
            eps2, eps3, phase = ground_state_phase(g)
        else:
            # initial guess from coarse grid
            coarse_range = np.linspace(-0.02, 0.02, 11)  # 11 points
            best_F = np.inf
            best_eps = (0,0)
            for e2 in coarse_range:
                for e3 in coarse_range:
                    F = free_energy_fun([e2, e3], g, kBT)
                    if F < best_F:
                        best_F = F
                        best_eps = (e2, e3)
            # local refinement
            res = minimize(free_energy_fun, best_eps, args=(g, kBT),
                           method='L-BFGS-B',
                           bounds=[(-0.03, 0.03), (-0.03, 0.03)],
                           options={'ftol': 1e-8, 'gtol': 1e-8})
            eps2, eps3 = res.x
        phase = determine_phase(eps2, eps3)
        phase_rows.append([sqrt_g, kBT, phase])

# write phase_diagram.csv
with open(os.path.join(OUTDIR, 'phase_diagram.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sqrt_g', 'kBT', 'phase_label'])
    w.writerows(phase_rows)

# ================== strains_vs_T at sqrt_g=11.2 ==================
sqrt_g_fixed = 11.2
g_fixed = sqrt_g_fixed**2
T_strain_range = np.linspace(0.0, 0.15, 31)  # finer for curve
strain_rows = []
for kBT in T_strain_range:
    if kBT == 0.0:
        eps2, eps3, _ = ground_state_phase(g_fixed)
    else:
        best_F = np.inf
        best_eps = (0,0)
        coarse = np.linspace(-0.02, 0.02, 9)
        for e2 in coarse:
            for e3 in coarse:
                F = free_energy_fun([e2, e3], g_fixed, kBT)
                if F < best_F:
                    best_F = F
                    best_eps = (e2, e3)
        res = minimize(free_energy_fun, best_eps, args=(g_fixed, kBT),
                       method='L-BFGS-B',
                       bounds=[(-0.03, 0.03), (-0.03, 0.03)],
                       options={'ftol': 1e-8, 'gtol': 1e-8})
        eps2, eps3 = res.x
    strain_rows.append([kBT, eps2, eps3])

with open(os.path.join(OUTDIR, 'strains_vs_T.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['kBT', 'epsilon_2', 'epsilon_3'])
    w.writerows(strain_rows)

# ================== MSDW averages at sqrt_g=11.2 ==================
msdw_rows = []
for kBT in T_strain_range:
    if kBT == 0.0:
        # Use ground state minimizer to get equilibrium strains, then zero-temperature averages (dominated by ground state)
        eps2, eps3, _ = ground_state_phase(g_fixed)
        # T=0 averages are the squared amplitudes at the ground state MSDW configuration.
        # We can extract from the ground state minimizer: the vector that gave min X2,X3.
        # For simplicity recompute via sampling with very small T
        kBT_sim = 1e-8
        Z, avgAx2, avgAy2, avgAz2 = compute_Z_avgs(g_fixed, kBT_sim, eps2, eps3)
    else:
        # Use equilibrium strains from previous computation (we stored them in strain_rows, but easier to recompute)
        # Actually we can reuse eps2,eps3 we computed for the same kBT above.
        idx = np.argmin(np.abs(T_strain_range - kBT))
        eps2, eps3 = strain_rows[idx][1], strain_rows[idx][2]
        Z, avgAx2, avgAy2, avgAz2 = compute_Z_avgs(g_fixed, kBT, eps2, eps3)
    msdw_rows.append([kBT, avgAx2, avgAy2, avgAz2])

with open(os.path.join(OUTDIR, 'msdw_components_vs_T.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['kBT', 'Ax2_avg', 'Ay2_avg', 'Az2_avg'])
    w.writerows(msdw_rows)
