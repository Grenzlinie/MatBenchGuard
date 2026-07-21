#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
# Install necessary numerical packages from Tsinghua mirror
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
# Set output directory
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_hc_entropy_multiple.csv ===
python3 << 'EOF'
import numpy as np
from scipy.integrate import dblquad

Jxd = Jyd = -1.0
Jx = -0.8
Jy = -3.0
dx = dy = 1
N0 = 3

def D(K, d):
    return np.cosh(K)**(2*d+2) - np.sinh(K)**(2*d+2)

def Ccoeff(K, Kd, d):
    cd = np.cosh(Kd)**(d+1) + np.sinh(Kd)**(d+1)
    cs = np.cosh(Kd)**(d+1) - np.sinh(Kd)**(d+1)
    return 0.5 * np.exp(2*K) * cd**2 + 0.5 * np.exp(-2*K) * cs**2

def Scoeff(K, Kd, d):
    cd = np.cosh(Kd)**(d+1) + np.sinh(Kd)**(d+1)
    cs = np.cosh(Kd)**(d+1) - np.sinh(Kd)**(d+1)
    return 0.5 * np.exp(2*K) * cd**2 - 0.5 * np.exp(-2*K) * cs**2

def integrand(phi, theta, C1, C2, S1, S2, D1, D2):
    val = C1*C2 - S1*D2*np.cos(phi) - S2*D1*np.cos(theta)
    val = np.maximum(val, 1e-300)
    return np.log(val)

def loglam(T):
    Kxd = Jxd / T
    Kyd = Jyd / T
    Kx = Jx / T
    Ky = Jy / T
    C1v = Ccoeff(Kx, Kxd, dx)
    S1v = Scoeff(Kx, Kxd, dx)
    D1v = D(Kxd, dx)
    C2v = Ccoeff(Ky, Kyd, dy)
    S2v = Scoeff(Ky, Kyd, dy)
    D2v = D(Kyd, dy)
    I, _ = dblquad(integrand, 0, 2*np.pi, lambda t: 0, lambda t: 2*np.pi,
                   args=(C1v, C2v, S1v, S2v, D1v, D2v), epsabs=1e-6, epsrel=1e-6)
    return I / (8*np.pi**2)

def compute_thermo(T_arr):
    N = len(T_arr)
    loglam_arr = np.zeros(N)
    for i, T in enumerate(T_arr):
        loglam_arr[i] = loglam(T)
    lnL = loglam_arr / N0 + np.log(2)
    dlnL_dT = np.gradient(lnL, T_arr)
    S_cell = lnL + T_arr * dlnL_dT
    C_cell = T_arr * np.gradient(S_cell, T_arr)
    C_spin = C_cell / N0
    S_spin = S_cell / N0
    return C_spin, S_spin

T = np.linspace(0.1, 10, 200)
C, S = compute_thermo(T)

output_path = '/app/outputs/step_01_hc_entropy_multiple.csv'
with open(output_path, 'w') as f:
    f.write('temperature,heat_capacity,entropy\n')
    for t, c, s in zip(T, C, S):
        f.write(f'{t:.8f},{c:.8f},{s:.8f}\n')
EOF

# === solve block: step_02_hc_isotropic_equal.csv ===
python3 /solution/compute.py --step step_02 --output "$OUTDIR/step_02_hc_isotropic_equal.csv"

# === solve block: step_03_Tc_isotropic.txt ===
python3 /solution/compute.py --step step_03 --output "$OUTDIR/step_03_Tc_isotropic.txt"
