#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: nucleation_rates.csv ===
python3 << 'PYEOF'
import csv, math, os

outdir = os.environ.get('OUTDIR', '/app/outputs')
outfile = os.path.join(outdir, 'nucleation_rates.csv')

sigma = 201.0
dGA_over_k = 5.25e4
N = 1.0e22
rho_c = 2.45
M = 150.0
A = 6.02214076e23
k_B = 1.380649e-16
h = 6.62607015e-27

T_C = [575.7, 562.6, 549.6, 536.7, 523.5, 510.4, 497.3, 484.3, 471.2, 458.2,
       445.1, 432.0, 419.0, 405.9, 392.9, 379.8, 366.7, 353.7, 340.6, 327.6]

rows = []
for Tc in T_C:
    T = Tc + 273.15
    dGv = (8790.0 - 6.53 * T) * 1e6
    r_star = -2 * sigma / dGv
    Kv = (8 * N / (3 * h)) * math.sqrt(k_B * T * sigma) * ((4 * math.pi * rho_c * A / M) ** (1./3.)) * (r_star ** 2)
    kinetic = -dGA_over_k / T
    barrier = 16 * math.pi * (sigma ** 3) / (3 * (dGv ** 2) * k_B * T)
    I = Kv * math.exp(kinetic) * math.exp(-barrier)
    rows.append((Tc, I))

with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Temperature_C', 'I'])
    writer.writerows(rows)
PYEOF
