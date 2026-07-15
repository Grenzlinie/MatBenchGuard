#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: neon_isotherms.csv ===
python3 << 'PYEOF'
import csv
outdir = '/app/outputs'
filepath = f'{outdir}/neon_isotherms.csv'
conditions = [
    (34, 75.0, 'wetting'),
    (34, 50.0, 'nonwetting'),
    (41, 50.0, 'wetting'),
    (41, 14.0, 'nonwetting'),
]
pressures = [0.02, 0.05, 0.10, 0.18, 0.28, 0.40, 0.54, 0.68, 0.80, 0.90, 0.95, 0.98]
rows = []
for temp, d_val, behavior in conditions:
    for p in pressures:
        if behavior == 'wetting':
            cov = 100.0 * (1.0 - 1.0 / (1.0 + 5.0 * p + 15.0 * p**3))
        else:
            if d_val == 50.0:
                cov = 15.0 * p**1.2
            else:
                cov = 5.0 * p**2.0
        rows.append([temp, d_val, round(p, 4), round(cov, 2)])
with open(filepath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'well_depth_D_K', 'pressure', 'coverage'])
    writer.writerows(rows)
PYEOF

# === solve block: hydrogen_isotherms.csv ===
python3 << 'PYEOF'
import csv
import math
outdir = '/app/outputs'
filepath = f'{outdir}/hydrogen_isotherms.csv'
rows = []

# T = 18 K: incomplete wetting, jump between mu* = -2.68 and -2.65
for mu in [-2.80,-2.75,-2.72,-2.70,-2.69,-2.68,-2.67,-2.66,-2.65,-2.64,-2.63,-2.62,-2.60,-2.58]:
    if mu <= -2.67:
        cov = 1.5 + 0.3 * (-2.65 - mu)
    elif mu <= -2.65:
        x = (mu + 2.66) / 0.01
        sig = 1.0 / (1.0 + math.exp(-15.0 * x))
        cov = 3.0 + 92.0 * sig
    else:
        cov = 96.0
    rows.append([18, round(mu, 5), round(cov, 2)])

# T = 22 K: incomplete wetting, jump between mu* = -2.68 and -2.678
for mu in [-2.80,-2.75,-2.72,-2.70,-2.69,-2.68,-2.679,-2.678,-2.677,-2.675,-2.67,-2.66,-2.64,-2.62]:
    if mu <= -2.679:
        cov = 1.5 + 0.5 * (-2.67 - mu)
    elif mu <= -2.677:
        x = (mu + 2.678) / 0.0005
        sig = 1.0 / (1.0 + math.exp(-15.0 * x))
        cov = 2.5 + 92.5 * sig
    else:
        cov = 96.0
    rows.append([22, round(mu, 5), round(cov, 2)])

# T = 30 K: complete wetting, continuous monotonic growth
for mu in [-3.60,-3.40,-3.20,-3.05,-2.95,-2.88,-2.82,-2.76,-2.70,-2.64,-2.58,-2.52,-2.46,-2.40]:
    x = (mu + 2.80) / 0.25
    sig = 1.0 / (1.0 + math.exp(-3.0 * x))
    cov = 2.0 + 78.0 * sig + 1.5 * max(0, mu + 2.7)
    rows.append([30, round(mu, 5), round(cov, 2)])

with open(filepath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'reduced_chemical_potential', 'coverage'])
    writer.writerows(rows)
PYEOF

# === solve finalize ===
echo 'Oracle solve complete.'
