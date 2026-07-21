#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: thermodynamic_data.csv ===
python3 << 'PYEOF' > /tmp/run_log.txt
import numpy as np
from scipy.optimize import brentq
import csv, os, sys

delta = 0.2
I = 1.0

# --- critical temperatures ---
def neel_eq(beta):
    return (I/(2*delta)) * np.tanh(beta*delta/2) - 1.0

beta_N = brentq(neel_eq, 0.5, 10.0)
T_N = 1.0 / beta_N

def fm_critical_eq(beta):
    return (beta/4.0) * (1.0 / np.cosh(beta*delta/2)**2) - 1.0

beta_C = None
# locate larger root: scan from 5 to 30
for lo in np.linspace(5, 30, 100):
    hi = lo + 1e-3
    if fm_critical_eq(lo) * fm_critical_eq(hi) < 0:
        beta_C = brentq(fm_critical_eq, lo, hi)
        break
if beta_C is None:
    beta_C = brentq(fm_critical_eq, 10, 20)
T_C = 1.0 / beta_C

# --- temperature grid with high density near transitions ---
T_max = 1.5 * T_N
n_base = 800
T_vals = np.linspace(1e-12, T_max, n_base)  # very small, but not zero to avoid inf
# refine around T_N and T_C
delta_T = 0.05 * T_N
T_extra_N = np.linspace(T_N - delta_T, T_N + delta_T, 200)
T_extra_C = np.linspace(T_C - delta_T, T_C + delta_T, 200)
T_arr = np.unique(np.sort(np.concatenate([T_vals, T_extra_N, T_extra_C, [T_N] + ([T_C] if T_C else [])])))
# Exclude T=0 row for now, will prepend
mask = T_arr > 1e-10
T_arr = T_arr[mask]
betas = 1.0 / T_arr

# --- thermodynamic functions ---
def paramagnetic_E(beta):
    return -delta * np.tanh(beta*delta/2) + 0.25

def paramagnetic_S(beta):
    return 2*np.log(2) - beta*delta*np.tanh(beta*delta/2) + 2*np.log(np.cosh(beta*delta/2))

def paramagnetic_C_exact(beta):
    return (beta**2) * (delta**2 / 4) * (1.0 / np.cosh(beta*delta/2)**2)

# --- arrays for T>0 rows ---
E_P   = np.zeros_like(betas)
E_F   = np.zeros_like(betas)
E_SDW = np.zeros_like(betas)
mu_F   = np.zeros_like(betas)
mu_SDW = np.zeros_like(betas)
S_P    = np.zeros_like(betas)
S_SDW  = np.zeros_like(betas)

for i, beta in enumerate(betas):
    # paramagnetic
    E_P[i] = paramagnetic_E(beta)
    S_P[i] = paramagnetic_S(beta)

    # spin-density wave
    if beta > beta_N:
        try:
            mu = brentq(lambda mu: 0.5/np.sqrt(delta**2 + (mu/2)**2) * np.tanh(beta*np.sqrt(delta**2 + (mu/2)**2)/2) - 1.0, 0.0, 1.0)
        except ValueError:
            mu = 0.0
        mu_SDW[i] = mu
        d = np.sqrt(delta**2 + (mu/2)**2)
        E_SDW[i] = - (delta**2 / d) * np.tanh(beta*d/2) + 0.25 * (1 - mu**2)
        S_SDW[i] = 2*np.log(2) - (1+2*d)*np.log(1+2*d) - (1-2*d)*np.log(1-2*d) if d < 0.5 else 2*np.log(2)
    else:
        mu_SDW[i] = 0.0
        E_SDW[i] = E_P[i]
        S_SDW[i] = S_P[i]

    # ferromagnetic
    if beta_C and beta > beta_C:
        try:
            mu = brentq(lambda mu: 0.5*(np.tanh(beta*(delta+mu/2)/2) - np.tanh(beta*(delta-mu/2)/2)) - mu, 0.0, 1.0)
        except ValueError:
            mu = 0.0
        mu_F[i] = mu
        if mu > 0:
            E_F[i] = - delta * mu * np.sinh(beta*delta) / np.sinh(beta*mu/2) + 0.25 * (1 - mu**2)
        else:
            E_F[i] = E_P[i]
    else:
        mu_F[i] = 0.0
        E_F[i] = E_P[i]

# --- specific heats ---
C_P   = paramagnetic_C_exact(betas)
C_F   = np.gradient(E_F, betas) * (-betas**2)
C_SDW = np.gradient(E_SDW, betas) * (-betas**2)

# --- Prepend T=0 row with exact analytic values ---
T0 = 0.0
E_P0 = 0.05
E_F0 = 0.0
E_SDW0 = -0.04
mu_F0 = 1.0
mu_SDW0 = np.sqrt(1 - (2*delta/I)**2)
C_P0 = 0.0
C_F0 = 0.0
C_SDW0 = 0.0
S_P0 = 0.0
S_SDW0 = 0.0

T_final = np.insert(T_arr, 0, T0)
E_P_final = np.insert(E_P, 0, E_P0)
E_F_final = np.insert(E_F, 0, E_F0)
E_SDW_final = np.insert(E_SDW, 0, E_SDW0)
mu_F_final = np.insert(mu_F, 0, mu_F0)
mu_SDW_final = np.insert(mu_SDW, 0, mu_SDW0)
C_P_final = np.insert(C_P, 0, C_P0)
C_F_final = np.insert(C_F, 0, C_F0)
C_SDW_final = np.insert(C_SDW, 0, C_SDW0)
S_P_final = np.insert(S_P, 0, S_P0)
S_SDW_final = np.insert(S_SDW, 0, S_SDW0)

# --- write CSV ---
outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, 'thermodynamic_data.csv')
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T', 'E_P', 'E_F', 'E_SDW', 'mu_F', 'mu_SDW', 'C_P', 'C_F', 'C_SDW', 'S_P', 'S_SDW'])
    for i in range(len(T_final)):
        writer.writerow([T_final[i], E_P_final[i], E_F_final[i], E_SDW_final[i], mu_F_final[i], mu_SDW_final[i], C_P_final[i], C_F_final[i], C_SDW_final[i], S_P_final[i], S_SDW_final[i]])
print('CSV written to', outpath)
PYEOF
