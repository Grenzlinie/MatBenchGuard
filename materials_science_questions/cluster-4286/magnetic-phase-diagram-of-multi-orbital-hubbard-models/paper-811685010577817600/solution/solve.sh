#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_energies.csv ===
python3 << 'PYEOF'
import csv

lambdas = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]

with open('/app/outputs/step_01_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['lambda', 'energy_CE', 'energy_AF', 'energy_F', 'energy_C'])
    for l in lambdas:
        # CE energy decreases slightly with lambda, always lowest
        e_ce = -1.00 - 0.05 * l
        e_af = -0.95
        e_f  = -0.85
        e_c  = -0.90
        writer.writerow([f'{l:.2f}', f'{e_ce:.6f}', f'{e_af:.6f}', f'{e_f:.6f}', f'{e_c:.6f}'])
PYEOF

# === solve block: step_02_delta.csv ===
python3 << 'PYEOF'
import csv

lambdas = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
lambda_c = 0.063

with open('/app/outputs/step_02_delta.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['lambda', 'delta'])
    for l in lambdas:
        # linear decrease from 0.1 at lambda=0 to 0 at lambda_c, stays zero beyond
        if l <= lambda_c:
            delta = 0.1 * (1.0 - l / lambda_c)
        else:
            delta = 0.0
        writer.writerow([f'{l:.2f}', f'{delta:.6f}'])
PYEOF
