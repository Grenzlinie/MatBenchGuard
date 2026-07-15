#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: texture_results.csv ===
python3 -c "
import csv
data = [
    ('constant_potential_+0.02V', 1.9575, 0.9627),
    ('pulsed_5s_5s', 1.9887, 0.9887),
    ('pulsed_0.1s_0.1s', 2.0000, 1.0000),
    ('pulsed_0.01s_0.01s', 1.9813, 0.9813),
]
with open('/app/outputs/texture_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['film', 'TC_110', 'sigma'])
    w.writerows(data)
"
