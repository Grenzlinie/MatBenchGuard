#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_cu_model.csv ===
python3 - <<'PYEOF'
import numpy as np
from scipy.optimize import fsolve
import csv

# Physical constants
k_B = 1.380649e-23   # J/K
N_A = 6.02214076e23  # 1/mol
T = 400.0            # K
kT = k_B * T         # J per particle

# Site parameters (per unit cell)
g_A = 2
g_B = 4
u_A = 0.0
u_B = 5.0 * kT

def occ(mu, u, g):
    return g / (np.exp((u - mu) / kT) + 1.0)

def total_occ(mu):
    return occ(mu, u_A, g_A) + occ(mu, u_B, g_B)

def mu_for_x(x):
    if x <= 0:
        return -100.0 * kT
    # initial guess: midpoint of the two site energies
    mu0 = 2.5 * kT
    sol = fsolve(lambda mu: total_occ(mu[0]) - x, mu0, maxfev=2000)
    return sol[0]

def compute_state(x):
    mu = mu_for_x(x)
    nA = occ(mu, u_A, g_A)
    nB = occ(mu, u_B, g_B)
    # safe log terms
    def safe_log(n, g):
        term1 = 0.0 if n <= 0 else n * np.log(n)
        term2 = 0.0 if g - n <= 0 else (g - n) * np.log(g - n)
        return term1, term2
    Sa = g_A * np.log(g_A) - safe_log(nA, g_A)[0] - safe_log(nA, g_A)[1]
    Sb = g_B * np.log(g_B) - safe_log(nB, g_B)[0] - safe_log(nB, g_B)[1]
    S = k_B * (Sa + Sb)
    U = nA * u_A + nB * u_B
    return nA, nB, S, U, mu

eps = 1e-6
xs = np.arange(0.0, 4.05, 0.1)
rows = []
for x in xs:
    nA, nB, S, U, mu = compute_state(x)
    # partial molar quantities via finite differences
    if x == 0.0:
        _, _, Sr, Ur, _ = compute_state(x + eps)
        dSdx = (Sr - S) / eps
        dUdx = (Ur - U) / eps
    elif x >= 3.98:  # near 4.0, use backward difference
        _, _, Sl, Ul, _ = compute_state(x - eps)
        dSdx = (S - Sl) / eps
        dUdx = (U - Ul) / eps
    else:
        _, _, Sl, Ul, _ = compute_state(x - eps)
        _, _, Sr, Ur, _ = compute_state(x + eps)
        dSdx = (Sr - Sl) / (2 * eps)
        dUdx = (Ur - Ul) / (2 * eps)
    # convert to molar units
    mu_mol = mu * N_A
    S_bar = dSdx * N_A
    H_bar = dUdx * N_A
    rows.append((x, nA, nB, S, U, mu_mol, S_bar, H_bar))

with open('/app/outputs/step_01_cu_model.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x','n_A','n_B','S','U','mu','S_bar','H_bar'])
    for row in rows:
        writer.writerow([f"{v:.6f}" for v in row])
PYEOF
