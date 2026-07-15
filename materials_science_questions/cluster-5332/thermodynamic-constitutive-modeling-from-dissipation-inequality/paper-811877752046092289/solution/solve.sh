#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: step_01_energetics.csv ===
python3 <<'PYEOF'
import csv
import math
import os

K1 = 1e9          # Pa
K2 = 5e9          # Pa
sigma_y2 = 30e6   # Pa
ell = 1.0         # m
V = 2.0           # m^3
K_eq = (K1 + K2) / 2.0

N = 20
Ei_max = 0.1
Ei_step = Ei_max / (N - 1)  # so endpoints 0.0 and 0.1 are included

rows = []
for i in range(N):
    E_i = i * Ei_step
    # stored energy W^i (J)
    W_i = 0.5 * V * (K1 / K2) * K_eq * (E_i ** 2)
    # overall stress (Pa)
    Sigma = (K_eq / K2) * (sigma_y2 + K1 * E_i)
    # total strain (dimensionless)
    E_total = Sigma / K_eq + E_i
    # total free energy (J)
    Psi = 0.5 * V * K_eq * (E_total - E_i) ** 2 + W_i
    # dissipation rate (W), assuming dE^i/dt = 1 s^{-1}
    D = V * (K_eq / K2) * sigma_y2 * 1.0
    # differential Taylor–Quinney coefficient
    beta_d = 1.0 / (1.0 + (K1 / sigma_y2) * E_i)
    # integral Taylor–Quinney coefficient
    beta_int = 1.0 / (1.0 + (K1 / (2.0 * sigma_y2)) * E_i)
    rows.append([E_i, W_i, Psi, D, beta_d, beta_int])

outpath = os.path.join(os.environ.get('OUTDIR', '/app/outputs'), 'step_01_energetics.csv')
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['E_i', 'W_i', 'Psi', 'D', 'beta_d', 'beta_int'])
    writer.writerows(rows)
PYEOF
