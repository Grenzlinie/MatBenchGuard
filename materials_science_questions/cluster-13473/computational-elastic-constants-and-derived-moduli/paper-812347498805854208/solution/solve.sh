#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: poisson_ratio.csv ===
python3 << PYEOF
import csv

output_path = "$OUTDIR/poisson_ratio.csv"
with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alpha', 'nu_P'])
    for i in range(0, 101, 10):
        alpha = i / 100.0
        nu = (1 - 2*alpha*alpha) / (3 - 2*alpha*alpha)
        writer.writerow([alpha, nu])
PYEOF
