#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: kappa_values.csv ===
python3 -c "
import csv, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, 'kappa_values.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x', 'temperature_K', 'kappa_WmK'])
    w.writerows([
        [-0.02, 800, 2.68],
        [0.0, 800, 5.5],
        [0.02, 800, 3.06],
        [0.04, 800, 2.2],
        [0.08, 800, 1.8],
        [0.125, 800, 1.7],
        [0.25, 800, 1.7],
        [-0.02, 1600, 1.72],
        [0.0, 1600, 3.0],
        [0.02, 1600, 1.94],
        [0.04, 1600, 1.75],
        [0.08, 1600, 1.72],
        [0.125, 1600, 1.7],
        [0.25, 1600, 1.7]
    ])
"
