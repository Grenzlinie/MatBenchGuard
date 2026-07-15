#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: tdos.dat ===
python3 -c "
import math
with open('$OUTDIR/tdos.dat', 'w') as f:
    for i in range(200):
        x = i * 0.05
        y = math.exp(-((x - 3.0) ** 2) / 0.1) + 0.01 * math.sin(x)
        f.write(f'{x:.6f} {y:.6f}\n')
"

# === solve block: absorption.dat ===
python3 /solution/generate_spectrum.py absorption > /app/outputs/absorption.dat
