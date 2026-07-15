#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: threshold_current_densities.csv ===
python3 -c "
import csv, math, sys

params = {
    0.0:  {'P1': 0.92, 'P2': 0.0014},
    0.10: {'P1': 0.85, 'P2': 0.2},
}
alpha_W = 19.0
g = 10.0
Gamma = 0.27

rows = []
for R_um in [22, 50, 60, 70]:
    for eps in [0.0, 0.10]:
        R_cm = R_um * 1e-4
        A_cm2 = math.pi * R_cm**2 / (1 + 2*eps)
        sqrt_A_pi = math.sqrt(A_cm2 * math.pi)
        p = params[eps]
        P1, P2 = p['P1'], p['P2']
        alpha_M = -math.log(P1) / (2 * sqrt_A_pi * (1 - P2))
        Jth = (alpha_W + alpha_M) / (g * Gamma)
        rows.append([R_um, eps, Jth])

writer = csv.writer(sys.stdout)
writer.writerow(['R', 'epsilon', 'computed_Jth'])
writer.writerows(rows)
" > /app/outputs/threshold_current_densities.csv

# === solve block: mode_spacing.txt ===
python3 -c "
import math
R = 70.0e-4        # cm
eps = 0.16
Phi_deg = 50.0
Phi = math.radians(Phi_deg)
r = R / math.sqrt(1 + 2*eps) * math.sqrt(1 + 2*eps * math.cos(2*Phi))
L = 4*r + 4*r * math.cos(Phi)
neff = 3.15
delta_nu = 1/(L * neff)
print(delta_nu)
" > /app/outputs/mode_spacing.txt
