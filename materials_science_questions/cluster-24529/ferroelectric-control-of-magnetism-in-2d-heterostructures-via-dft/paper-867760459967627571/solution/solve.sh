#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 /solution/compute.py

# === solve block: step_01_spin_density_profile.csv ===
OUTDIR=${OUTDIR:-/app/outputs}
python3 << 'PYEOF'
import os
import numpy as np
import csv

outdir = os.environ.get('OUTDIR', '/app/outputs')

# ---------- fixed parameters ----------
S0 = 1.0
lam_sf = 5.0
lam_phi = 1.0
lam_J = 1.0

lam_par_inv2 = 1.0 / lam_sf**2 + 1.0 / lam_phi**2
k_hat = np.sqrt(lam_par_inv2 - 1j / lam_J**2)

D_torque = 1.0          # arbitrary units for torque steps (02,04,05)
vF      = 5e5           # m/s
D_cm2s  = 5.0           # cm^2/s for efficiency (step 03)
D_nm2s  = D_cm2s * 1e14  # convert to nm^2/s
vF_nms  = vF * 1e9       # convert to nm/s

# =====================  Step 01  =====================
d = 8.0
z = np.linspace(0.0, d, 100)
S_hat = S0 * np.cosh(k_hat * (z - d)) / np.cosh(k_hat * d)
S_perp = np.real(S_hat)
S_z    = -np.imag(S_hat)

with open(os.path.join(outdir, 'step_01_spin_density_profile.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['z', 'S_perp', 'S_z'])
    for i in range(len(z)):
        w.writerow([z[i], S_perp[i], S_z[i]])

# =====================  Step 02  =====================
prefactor = S0 * (1.0/lam_phi**2 - 1j/lam_J**2) * D_torque / k_hat
d_vals = np.arange(0.5, 20.001, 0.5)
T_hat_step2 = prefactor * np.sinh(k_hat * d_vals) / np.cosh(k_hat * d_vals)
T_perp_step2 = np.real(T_hat_step2)
T_z_step2    = np.imag(T_hat_step2)

with open(os.path.join(outdir, 'step_02_torque_vs_d.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['d', 'T_perp', 'T_z'])
    for i in range(len(d_vals)):
        w.writerow([d_vals[i], T_perp_step2[i], T_z_step2[i]])

# =====================  Step 03  =====================
theta_hat = -np.sqrt(2)/2 * D_nm2s / (vF_nms * k_hat) * (1/lam_phi**2 - 1j/lam_J**2)
theta_perp = np.real(theta_hat)
theta_z    = np.imag(theta_hat)

with open(os.path.join(outdir, 'step_03_torque_efficiency.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['theta_perp', 'theta_z'])
    w.writerow([theta_perp, theta_z])

# =====================  Steps 04 & 05 helper  =====================
def solve_two_layer(d1, d2, S1, S2):
    """
    Solve spin-diffusion ODE d^2 S/dz^2 = k_hat^2 S for two layers
    (0..d1 & d1..d1+d2) with Dirichlet boundaries S(0)=S1, S(d1+d2)=S2
    and continuity of S and dS/dz at z=d1.
    Returns integrated complex torque T_hat.
    """
    if d1 <= 0:
        # single layer of thickness d2 with opposite boundaries
        # analytic solution yields zero torque (antisymmetric)
        return 0.0 + 0.0j

    L = d1 + d2
    # build linear system M * [A1, B1, A2, B2]^T = rhs
    M = np.zeros((4, 4), dtype=complex)
    rhs = np.zeros(4, dtype=complex)

    # 1) S(0) = A1 + B1 = S1
    M[0, 0] = 1.0
    M[0, 1] = 1.0
    rhs[0] = S1

    # 2) S(L) = A2 e^{kL} + B2 e^{-kL} = S2
    M[1, 2] = np.exp(k_hat * L)
    M[1, 3] = np.exp(-k_hat * L)
    rhs[1] = S2

    # 3) continuity of S at z = d1
    M[2, 0] = np.exp(k_hat * d1)
    M[2, 1] = np.exp(-k_hat * d1)
    M[2, 2] = -np.exp(k_hat * d1)
    M[2, 3] = -np.exp(-k_hat * d1)
    rhs[2] = 0.0

    # 4) continuity of dS/dz at z = d1 (derivative factor k_hat cancels if non-zero)
    M[3, 0] = k_hat * np.exp(k_hat * d1)
    M[3, 1] = -k_hat * np.exp(-k_hat * d1)
    M[3, 2] = -k_hat * np.exp(k_hat * d1)
    M[3, 3] = k_hat * np.exp(-k_hat * d1)
    rhs[3] = 0.0

    coeff = np.linalg.solve(M, rhs)
    A1, B1, A2, B2 = coeff[0], coeff[1], coeff[2], coeff[3]

    # compute torque via  T_hat = D * [dS/dz(L) - dS/dz(0)] - (1/τ_sf) ∫ S dz
    dSdz_0 = k_hat * (A1 - B1)
    dSdz_L = k_hat * (A2 * np.exp(k_hat * L) - B2 * np.exp(-k_hat * L))

    int_S = (A1 * (np.exp(k_hat * d1) - 1.0) + B1 * (1.0 - np.exp(-k_hat * d1))) / k_hat
    int_S += (A2 * (np.exp(k_hat * L) - np.exp(k_hat * d1)) + B2 * (np.exp(-k_hat * d1) - np.exp(-k_hat * L))) / k_hat

    tau_sf_inv = D_torque / lam_sf**2
    T_hat = D_torque * (dSdz_L - dSdz_0) - tau_sf_inv * int_S
    return T_hat

# =====================  Step 04  =====================
d2 = 6.0
d1_vals = np.arange(0.0, 10.001, 0.1)
S1_val = 1.0
S2_val = -1.0

T_perp_d1 = []
T_z_d1    = []
for d1 in d1_vals:
    T_hat = solve_two_layer(d1, d2, S1_val, S2_val)
    T_perp_d1.append(np.real(T_hat))
    T_z_d1.append(np.imag(T_hat))

with open(os.path.join(outdir, 'step_04_TI_mdTI_torque_d1.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['d1', 'T_perp', 'T_z'])
    for i in range(len(d1_vals)):
        w.writerow([d1_vals[i], T_perp_d1[i], T_z_d1[i]])

# =====================  Step 05  =====================
d1_fixed = 3.0
ratios = np.arange(0.1, 1.901, 0.1)
T_perp_r = []
T_z_r    = []
for r in ratios:
    mag1 = 2.0 * r / (1.0 + r)
    mag2 = 2.0 / (1.0 + r)
    S1_r =  mag1
    S2_r = -mag2
    T_hat = solve_two_layer(d1_fixed, d2, S1_r, S2_r)
    T_perp_r.append(np.real(T_hat))
    T_z_r.append(np.imag(T_hat))

with open(os.path.join(outdir, 'step_05_TI_mdTI_torque_ratio.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ratio', 'T_perp', 'T_z'])
    for i in range(len(ratios)):
        w.writerow([ratios[i], T_perp_r[i], T_z_r[i]])
PYEOF

# === solve block: step_02_torque_vs_d.csv ===
true

# === solve block: step_03_torque_efficiency.csv ===
true

# === solve block: step_04_TI_mdTI_torque_d1.csv ===
true

# === solve block: step_05_TI_mdTI_torque_ratio.csv ===
true
