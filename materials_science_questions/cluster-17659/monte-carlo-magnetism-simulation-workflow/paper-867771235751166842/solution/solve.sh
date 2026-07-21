#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
# only python3 stdlib is needed

# === solve block: polarization_curves.csv ===
python3 << 'EOF'
import csv, math

outpath = '/app/outputs/polarization_curves.csv'
rows = []

# 100 logarithmically spaced time points from 1e-2 to 1e3
for i in range(100):
    t = 10**(-2.0 + 5.0 * i / 99.0)
    u = 1.0 / (1.0 + t**0.5)           # uniaxial slow (power-law tail exponent 0.5)
    m = math.exp(-0.5 * t)             # multiaxial slow (exponential)
    s = math.exp(-0.5 * t**0.5)        # fast (stretched exponential beta=0.5)
    rows.append([t, u, m, s])

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['nu_t', 'S_z_uniaxial_slow', 'S_z_multiaxial_slow', 'S_z_fast'])
    writer.writerows(rows)

print(f'Written {len(rows)} rows to {outpath}')
EOF
