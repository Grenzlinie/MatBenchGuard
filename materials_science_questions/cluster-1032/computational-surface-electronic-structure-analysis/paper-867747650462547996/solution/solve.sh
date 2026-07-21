#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy

# === solve block: ldos_decay.csv ===
python3 << 'PYEOF'
import os, csv, numpy as np
from scipy.special import jv, yv

omega = -0.7
U_nz = 1.0
a0 = 0.01
outpath = '/app/outputs/ldos_decay.csv'

# regularised on-site Green's function coefficient g0(ω) at cutoff a0
omega_abs = abs(omega)
sgn = np.sign(omega)
f0_cut = -sgn * jv(0, omega_abs * a0) - 1j * yv(0, omega_abs * a0)
g0_val = (1j * omega / 4.0) * f0_cut

denom = 1.0 - (U_nz ** 2) * (g0_val ** 2)
B_val = (U_nz * omega ** 2) / (16.0 * np.pi * denom)

R_vals = np.logspace(np.log10(0.1), 1.0, 50)   # 50 points from 0.1 a to 10 a
rows = []
for R in R_vals:
    f0 = -sgn * jv(0, omega_abs * R) - 1j * yv(0, omega_abs * R)
    f1 = -1j * jv(1, omega_abs * R) + sgn * yv(1, omega_abs * R)
    # Eq.(14): delta_rho = 2 Im(B) U n_z (f0^2 - f1^2)  -- product of Im(B) with the real part of (f0^2 - f1^2)
    delta_rho = 2.0 * U_nz * np.imag(B_val) * np.real(f0**2 - f1**2)
    rho = omega_abs / 4.0 + delta_rho
    rows.append((R, rho))

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['R', 'rho'])
    writer.writerows(rows)
PYEOF

# === solve block: spin_parity.csv ===
python3 /solution/compute.py spin_parity

# === solve block: rkky_decay.csv ===
python3 /solution/compute.py rkky_decay

# === solve block: resonance_energy.txt ===
python3 /solution/compute.py resonance_energy
