#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: DD_DH_ratio.csv ===
python3 - "$OUTDIR/DD_DH_ratio.csv" << 'PYEOF'
import csv, math, sys

k_B = 0.0861733034  # meV/K
omega_H = 69.0
omega_D = 47.0
omega_perp_H = 1.82 * omega_H
omega_par_H = 0.02 * omega_H
omega_perp_D = omega_perp_H * 0.68
omega_par_D = omega_par_H * 0.68

Tmin, Tmax, N = 773.0, 1373.0, 60

rows = []
for i in range(N):
    T = Tmin + i * (Tmax - Tmin) / (N - 1)
    hb2 = 1.0 / (2.0 * k_B * T)
    # O site: three dimensions
    sh_H = math.sinh(hb2 * omega_H)
    sh_D = math.sinh(hb2 * omega_D)
    # activated state: two perpendicular, one parallel
    sh_perp_H = math.sinh(hb2 * omega_perp_H)
    sh_perp_D = math.sinh(hb2 * omega_perp_D)
    sh_par_H = math.sinh(hb2 * omega_par_H)
    sh_par_D = math.sinh(hb2 * omega_par_D)

    ratio = (sh_H / sh_D) ** 3 * (sh_perp_H / sh_perp_D) ** 2 * (sh_par_H / sh_par_D)
    rows.append((T, ratio))

outpath = sys.argv[1]
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'ratio_DD_DH'])
    writer.writerows(rows)
PYEOF
