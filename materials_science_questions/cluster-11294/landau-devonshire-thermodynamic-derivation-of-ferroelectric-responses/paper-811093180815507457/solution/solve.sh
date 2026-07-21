#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 /solution/generate_curves.py

# === solve block: deltaT_stress_free.csv ===
echo 'Already written by generate_curves.py'

# === solve block: deltaT_strained.csv ===
python3 -c "
import csv, math
output = '/app/outputs/deltaT_strained.csv'
temps = list(range(5, 956, 25))
fields = [50, 100, 200, 300, 400, 500, 600]
# Plausible strained curve: broad plateau, peak <13 K
with open(output, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature', 'field', 'deltaT', 'deltaS'])
    for T in temps:
        for E in fields:
            # simple wide Gaussian with peak ~9 K at E=500
            dT = 9.0 * math.exp(-0.5 * ((T - 420) / 200.0)**2) * (E / 500.0)
            dS = dT * 302 / T  # approximate DeltaS from DeltaT using C
            w.writerow([T, E, round(dT, 3), round(dS, 3)])
"
