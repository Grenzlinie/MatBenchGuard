#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: results.csv ===
python3 <<'PYEOF'
import csv, math

rho0 = 1.0
U_rho0 = 1.0
U = U_rho0 / rho0
n = 2
W_c = 1.0

J_rho0_values = [0.05, 0.1, 0.2, 0.3, 0.5]

rows = []
for J_rho0 in J_rho0_values:
    J = J_rho0 / rho0
    T_c = 1.13 * W_c * math.exp(-2.0 / J_rho0)
    if (U + J) * rho0 > 1:
        T_AF = n / (2.0 * rho0 * math.log((U + J) * rho0 / ((U + J) * rho0 - 1)))
    else:
        T_AF = 0.0
    T_AF_gt_T_c = (T_AF > T_c) and (T_AF > 0)
    rows.append([J_rho0, U_rho0, n, W_c, T_c, T_AF, str(T_AF_gt_T_c)])

with open('/app/outputs/results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Jρ0', 'Uρ0', 'n', 'W_c', 'T_c', 'T_AF', 'T_AF_gt_T_c'])
    writer.writerows(rows)
PYEOF
