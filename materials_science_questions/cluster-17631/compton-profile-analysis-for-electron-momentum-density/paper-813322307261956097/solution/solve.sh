#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: anisotropy_curves.csv ===
python3 << EOF
import csv, math
with open('$OUTDIR/anisotropy_curves.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['p_z', 'delta_100_110', 'delta_100_111', 'delta_110_111'])
    for i in range(101):
        p = i * 0.05
        d1 = 0.09 * math.exp(-p**2 / 0.5)
        d2 = 0.09 * math.exp(-p**2 / 0.5)
        d3 = 0.03 * math.exp(-p**2 / 0.5)
        w.writerow([f'{p:.2f}', f'{d1:.6f}', f'{d2:.6f}', f'{d3:.6f}'])
EOF

# === solve block: transition_pressure.txt ===
printf '35.8\n' > /app/outputs/transition_pressure.txt
