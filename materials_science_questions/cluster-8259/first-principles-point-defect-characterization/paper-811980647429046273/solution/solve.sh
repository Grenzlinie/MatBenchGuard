#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: step_01_annealing_curve.csv ===
python3 << 'EOF'
import numpy as np
from scipy.integrate import solve_ivp
import csv, math, os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
out_path = os.path.join(OUTDIR, 'step_01_annealing_curve.csv')

# Physical constants and parameters
k     = 8.617333262145e-5   # eV/K
Ta    = 500.0                # K
eps0  = 0.10                 # eV
eps_w = 0.29                 # eV
v0    = 1.0e12               # s^{-1}
ratio = 0.01                 # b+ / b0

# Derived quantities
vt = v0 * math.exp(-3.0 * eps0 / (k * Ta))
# Choose offset C so that the peak of the Gaussian occurs near t_peak = 1000 s
t_peak = 1000.0
C = k * Ta * math.log(vt * t_peak)   # epsilon_t - center (eV)

def eps_d(t):
    return k * Ta * math.log(vt * t)   # demarcation energy relative to epsilon_t (set epsilon_t=0)

def G(eps):
    sigma = eps_w
    return (1.0 / (math.sqrt(2.0 * math.pi) * sigma)) * np.exp(-eps**2 / (2.0 * sigma**2))

def ode(t, K):
    """ODE for K0 fraction: d[K0]/dt"""
    K0 = K[0]
    if t <= 0:
        return [0]
    Kp = (1.0 - K0) / 2.0          # K+ (charge neutrality + total conservation)
    factor = K0 / (K0 + ratio * Kp)   # capture fraction
    arg = eps_d(t) - C             # energy relative to Gaussian centre
    dK = -2.0 * G(arg) * k * Ta / t * factor
    return [dK]

# Integration
sol = solve_ivp(ode, [1.0, 10000.0], [1.0],
                t_eval=np.logspace(0, 4, 20),
                method='RK45', rtol=1e-6, atol=1e-8)
fraction = np.clip(sol.y[0], 0.0, None)   # ensure non‑negative

# Write CSV
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time_s', 'fraction_remaining'])
    for t, fr in zip(np.logspace(0, 4, 20), fraction):
        writer.writerow([t, fr])
EOF
