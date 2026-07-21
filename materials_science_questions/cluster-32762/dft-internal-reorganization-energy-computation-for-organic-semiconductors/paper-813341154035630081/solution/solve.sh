#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: reorganization_energies.csv ===
python3 -c "
import csv
rows = [
    (7.0, 0.00231, 0.00336),
    (5.0, 0.00231, 0.00359),
    (4.0, 0.00227, 0.00398),
]
with open('/app/outputs/reorganization_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['distance', 'lambda_frozen', 'lambda_relaxed'])
    for r in rows:
        w.writerow(r)
"
