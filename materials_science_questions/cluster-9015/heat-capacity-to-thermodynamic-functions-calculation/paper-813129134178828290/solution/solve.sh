#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
# No additional setup; using Python stdlib only.

# === solve block: thermodynamic_functions.csv ===
# Compute smoothed thermodynamic functions and write CSV
python3 - <<'PYEOF'
import csv
import math

# Polynomial coefficients for three intervals
a0, a1, a2, a3 = 55.606, 0.23556, -1.9546e-4, -1.2072e-8
b0, b1, b2, b3 = 429.55, -0.66985, 4.0801e-4, -1.8387e7
c0, c1, c2 = 135.72, -0.060195, 6.7994e-5

S0 = 136.57
T0 = 298.15

def cp(T):
    if T <= 500.0:
        return a0 + a1*T + a2*T*T + a3*T*T*T
    elif T <= 573.0:
        return b0 + b1*T + b2*T*T + b3/(T*T)
    else:
        return c0 + c1*T + c2*T*T

# Fine grid numerical integration
step = 0.1
T_vals = []
cp_vals = []
cp_over_T_vals = []
T = 200.0
while T <= 700.0:
    cp_val = cp(T)
    T_vals.append(T)
    cp_vals.append(cp_val)
    cp_over_T_vals.append(cp_val / T)
    T += step

n = len(T_vals)
cum_H = [0.0]
cum_S = [0.0]  # integral of Cp/T
for i in range(1, n):
    dT = T_vals[i] - T_vals[i-1]
    dH = 0.5 * (cp_vals[i-1] + cp_vals[i]) * dT
    dS = 0.5 * (cp_over_T_vals[i-1] + cp_over_T_vals[i]) * dT
    cum_H.append(cum_H[-1] + dH)
    cum_S.append(cum_S[-1] + dS)

def index_of(T):
    idx = int(round((T - 200.0) / step))
    if idx < 0:
        idx = 0
    if idx >= n:
        idx = n - 1
    return idx

idx0 = index_of(T0)
H0 = cum_H[idx0]
S0_cum = cum_S[idx0]

with open('/app/outputs/thermodynamic_functions.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T', 'Cp', 'H_T_minus_H298', 'S_T'])
    for T in range(200, 701, 5):
        idx = index_of(T)
        cp_val = cp_vals[idx]
        H_val = cum_H[idx] - H0
        S_val = S0 + (cum_S[idx] - S0_cum)
        w.writerow([T, round(cp_val, 1), round(H_val), round(S_val, 1)])
PYEOF
