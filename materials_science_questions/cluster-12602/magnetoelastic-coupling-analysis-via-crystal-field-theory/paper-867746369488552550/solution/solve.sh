#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple sympy numpy

# === solve block: predicted_results.csv ===
python3 - "$OUTDIR" << 'EOF'
import sys, os
import numpy as np

# cross‑version NumPy trapezoidal integration
try:
    from numpy import trapezoid as trapz
except ImportError:
    from numpy import trapz

outdir = sys.argv[1]

# --- fixed mesoscopic parameters ---
a = 85e-6
chi = 13.1
h0 = 300e-6
rho0 = 1.5e-3
n = 1e10/(2*np.pi)
mu = 1.0
R = 2e-3
mu0 = 4*np.pi*1e-7

# --- use mu0 * H^2 = 1 for dimensionless deformation amplitudes ---
mu0_H2 = 1.0
H = np.sqrt(mu0_H2 / mu0)       # ensures mu0*H**2 == mu0_H2

# --- discretization ---
Npts = 200
q0h0_vals = np.linspace(-2, 2, Npts)   # at least 50 points

# numerical integration helper
Nr = 2000
def avg_int(fun, R, Nr=Nr):
    r = np.linspace(0, R, Nr)
    dr = r[1] - r[0]
    y = r * fun(r)
    return (2.0 / R**2) * trapz(y, dx=dr)

rows = []
for q0h0 in q0h0_vals:
    # avoid q0=0 singularities by using a very small value
    if abs(q0h0) < 1e-12:
        q0 = 1e-12
        sin_half = q0h0/2
        cos_half = 1.0
        sin_q0h0 = q0h0
        cos_q0h0 = 1.0
    else:
        q0 = q0h0 / h0
        sin_half = np.sin(q0h0/2)
        cos_half = np.cos(q0h0/2)
        sin_q0h0 = np.sin(q0h0)
        cos_q0h0 = np.cos(q0h0)

    # ---- mesoscopic geometry ----
    d0 = np.sqrt(h0**2 + 4*rho0**2 * sin_half**2)

    # deformation amplitudes A and tau (Eqs 16,17)
    geom_A = (4*rho0**4*sin_half**4 - 10*h0**2*rho0**2*sin_half**2 + h0**4) / (mu * d0)
    A_val = -8*np.pi * n * a**6 * (chi/(chi+3))**2 * geom_A * mu0_H2

    geom_tau = ((h0**2 - rho0**2*sin_half**2) * sin_q0h0) / (mu * R**2 * d0)
    tau_val = -96*np.pi * n * a**6 * (chi/(chi+3))**2 * h0 * rho0**2 * geom_tau * mu0_H2

    # ---- alpha_parallel and alpha_perp (Eqs 47,48) ----
    C = q0*R - np.arctan(q0*R)                           # q0R - arctan(q0R)
    termA = (chi+3)*d0 + 4*chi*a**3 * (h0**2 - rho0**2 + rho0**2*cos_q0h0)
    denom_par = (4*np.pi*n*chi*a**3 * C * termA
                 + 3*chi*a**3 * rho0*h0*sin_q0h0 * (q0**2*R**2 - np.log(1+q0**2*R**2)))
    alpha_par = mu0 * (chi+3)**2 * C * d0 / denom_par

    denom_perp = (4*np.pi*n*chi*a**3 * C * termA
                  - 3*chi*a**3 * rho0*h0*sin_q0h0 * np.log(1+q0**2*R**2))
    alpha_perp = mu0 * (chi+3)**2 * C * d0 / denom_perp

    # ---- mesoscopic energy coefficients (per μ0 H^2) ----
    pref = n * a**6 * (chi/(chi+3))**2
    c_A_meso = 24*np.pi * pref * (4*rho0**4*sin_half**4 - 10*h0**2*rho0**2*sin_half**2 + h0**4) / d0
    c_tau_meso = 48*np.pi * pref * h0 * rho0**2 * (h0**2 - rho0**2*sin_half**2) * sin_q0h0 / d0

    # ---- mesoscopic magnetization coefficients (per H) ----
    M_phi_const = 24*np.pi * pref * h0 * rho0 * sin_q0h0 / d0
    M_phi_A = 36*np.pi * pref * h0 * rho0 * (8*rho0**2*sin_half**2 - 3*h0**2) * sin_q0h0 / d0
    M_phi_tau = 12*np.pi * pref * h0**2 * rho0 * (
        2*h0**2*cos_q0h0 - rho0**2 * (9*np.sin(q0h0/2) + np.sin(3*q0h0/2))) / d0

    # ---- precompute common macroscopic integrals ----
    # B1 = (alpha_par - alpha_perp) / (alpha_par * alpha_perp)
    B1 = (alpha_par - alpha_perp) / (alpha_par * alpha_perp)

    # Integrals for energy A terms
    term1_int = avg_int(lambda r: 0.5 * B1 * 3*q0**2*r**2 / (1+q0**2*r**2)**2, R)
    # basis for B2 (energy A)
    int_E_A_B2 = avg_int(lambda r: -0.5 * (1 - 0.5*q0**2*r**2) / (1+q0**2*r**2)**2, R)
    # basis for ζ3 (energy A)
    int_E_A_zeta3 = avg_int(lambda r: -(1 - 0.5*q0**2*r**2) / (1+q0**2*r**2), R)   # this will be multiplied by 1/α⊥^2
    # basis for B3 (energy A)
    int_E_A_B3 = avg_int(lambda r: -2.0 / (1+q0**2*r**2), R)

    # Integrals for energy tau terms
    Et1 = avg_int(lambda r: B1 * q0**2*r**2 / (1+q0**2*r**2)**2, R)
    int_E_tau_B2 = avg_int(lambda r: 0.5 * q0**2*r**2 / (1+q0**2*r**2)**2, R)
    int_E_tau_zeta3 = avg_int(lambda r: 0.5 * q0**2*r**2 / (1+q0**2*r**2), R)    # multiplied by 1/α⊥^2
    int_E_tau_B3 = avg_int(lambda r: 0.5 * q0**2*r**2 / (1+q0**2*r**2), R)

    # Integrals for magnetization A terms
    MA1 = avg_int(lambda r: B1 * (3*q0*r*(1-q0**2*r**2)) / (2*(1+q0**2*r**2)**2), R)
    int_M_A_B2 = avg_int(lambda r: q0*r*(1-0.5*q0**2*r**2) / ((1+q0**2*r**2)**2), R)
    int_M_A_zeta4zeta6 = avg_int(lambda r: 0.5 * q0*r / (1+q0**2*r**2), R)      # for (ζ4+ζ6)/(α∥α⊥) and -ζ6/α⊥^2

    # Integrals for magnetization tau terms
    MT1 = avg_int(lambda r: B1 * q0*r*(1-q0**2*r**2) / (1+q0**2*r**2)**2, R)
    int_M_tau_B2 = avg_int(lambda r: q0**3 * r**3 / (1+q0**2*r**2)**2, R)
    int_M_tau_zeta4zeta6 = avg_int(lambda r: 0.5 * q0 * r, R)    # factor for (ζ4+ζ6)/(α∥α⊥)

    # ---- helper constants for linear system ----
    # 1/α∥, 1/α⊥, 1/α∥^2, etc.
    ia1 = 1.0/alpha_par
    ia2 = 1.0/alpha_perp
    ia1sq = ia1*ia1
    ia2sq = ia2*ia2
    d_alpha = alpha_par - alpha_perp

    # -- Equation 1: I_A = c_A_meso
    # contributions from B2 (in I_A) to zeta
    a2_z1 = int_E_A_B2 * ia1sq
    a2_z3 = int_E_A_B2 * (ia1sq - ia2sq)
    a2_z4 = int_E_A_B2 * (2 * d_alpha / (alpha_par**2 * alpha_perp))
    a2_z6 = int_E_A_B2 * (d_alpha**2 / (alpha_par**2 * alpha_perp**2))

    # contribution from ζ3/α⊥^2 term
    a3_z3 = - int_E_A_zeta3 * ia2sq

    # contribution from B3 (in I_A) to zeta
    a4_z4 = int_E_A_B3 * (1.0/(alpha_par * alpha_perp))
    a4_z6 = int_E_A_B3 * (d_alpha/(alpha_par * alpha_perp**2))

    # constant term ζ6/α⊥^2
    a5_z6 = - ia2sq

    row1 = [a2_z1, a2_z3 + a3_z3, a2_z4 + a4_z4, a2_z6 + a4_z6 + a5_z6]
    rhs1 = c_A_meso - term1_int

    # -- Equation 2: I_tau = q0 * c_tau_meso
    # contributions from B2
    b2_z1 = int_E_tau_B2 * ia1sq
    b2_z3 = int_E_tau_B2 * (ia1sq - ia2sq)
    b2_z4 = int_E_tau_B2 * (2 * d_alpha / (alpha_par**2 * alpha_perp))
    b2_z6 = int_E_tau_B2 * (d_alpha**2 / (alpha_par**2 * alpha_perp**2))
    # ζ3/α⊥^2 term
    b3_z3 = int_E_tau_zeta3 * ia2sq
    # B3 term
    b4_z4 = int_E_tau_B3 * (1.0/(alpha_par*alpha_perp))
    b4_z6 = int_E_tau_B3 * (d_alpha/(alpha_par*alpha_perp**2))

    row2 = [b2_z1, b2_z3 + b3_z3, b2_z4 + b4_z4, b2_z6 + b4_z6]
    rhs2 = q0 * c_tau_meso - Et1

    # -- Equation 3: G_A_avg = M_phi_A / μ0
    c2_z1 = int_M_A_B2 * ia1sq
    c2_z3 = int_M_A_B2 * (ia1sq - ia2sq)
    c2_z4 = int_M_A_B2 * (2 * d_alpha / (alpha_par**2 * alpha_perp))
    c2_z6 = int_M_A_B2 * (d_alpha**2 / (alpha_par**2 * alpha_perp**2))

    # ζ4+ζ6 terms
    contrib_zeta4 = int_M_A_zeta4zeta6 / (alpha_par * alpha_perp)
    contrib_zeta6_magA = contrib_zeta4 - int_M_A_zeta4zeta6 * ia2sq   # (1/(α∥α⊥) - 1/α⊥^2)

    row3 = [c2_z1, c2_z3,
            c2_z4 + contrib_zeta4,
            c2_z6 + contrib_zeta6_magA]
    rhs3 = M_phi_A / mu0 - MA1

    # -- Equation 4: G_tau_avg = (q0/μ0) * M_phi_tau
    d2_z1 = int_M_tau_B2 * ia1sq
    d2_z3 = int_M_tau_B2 * (ia1sq - ia2sq)
    d2_z4 = int_M_tau_B2 * (2 * d_alpha / (alpha_par**2 * alpha_perp))
    d2_z6 = int_M_tau_B2 * (d_alpha**2 / (alpha_par**2 * alpha_perp**2))

    contrib_zeta4_tau = int_M_tau_zeta4zeta6 / (alpha_par * alpha_perp)
    contrib_zeta6_tau = contrib_zeta4_tau     # same as ζ4 for this term

    row4 = [d2_z1, d2_z3,
            d2_z4 + contrib_zeta4_tau,
            d2_z6 + contrib_zeta6_tau]
    rhs4 = (q0/mu0) * M_phi_tau - MT1

    # solve linear system
    A_mat = np.array([row1, row2, row3, row4])
    b_vec = np.array([rhs1, rhs2, rhs3, rhs4])
    try:
        zeta_vec = np.linalg.solve(A_mat, b_vec)
    except np.linalg.LinAlgError:
        # fallback: use least-squares
        zeta_vec, _, _, _ = np.linalg.lstsq(A_mat, b_vec, rcond=None)
    zeta1, zeta3, zeta4, zeta6 = zeta_vec

    # store row
    rows.append([q0h0, A_val, tau_val, alpha_par, alpha_perp, zeta1, zeta3, zeta4, zeta6])

# write CSV
out_path = os.path.join(outdir, 'predicted_results.csv')
with open(out_path, 'w', newline='') as f:
    import csv
    writer = csv.writer(f)
    writer.writerow(['q0h0','A','tau','alpha_parallel','alpha_perp','zeta1','zeta3','zeta4','zeta6'])
    writer.writerows(rows)
EOF
