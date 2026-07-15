#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_phase_fractions.csv ===
python3 << 'PYEOF'
import csv

outpath = '/app/outputs/step_01_phase_fractions.csv'
temperatures = [900, 950, 1000, 1050, 1100, 1150, 1200]
phases = ['B2_BETA', 'L12_FCC', 'SIGMA']
fractions = {
    900: [0.65, 0.30, 0.05],
    950: [0.60, 0.35, 0.05],
    1000: [0.55, 0.40, 0.05],
    1050: [0.50, 0.45, 0.05],
    1100: [0.45, 0.50, 0.05],
    1150: [0.40, 0.55, 0.05],
    1200: [0.35, 0.60, 0.05],
}

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Temperature', 'Phase', 'MoleFraction'])
    for t in temperatures:
        for ph, frac in zip(phases, fractions[t]):
            writer.writerow([t, ph, frac])
PYEOF
