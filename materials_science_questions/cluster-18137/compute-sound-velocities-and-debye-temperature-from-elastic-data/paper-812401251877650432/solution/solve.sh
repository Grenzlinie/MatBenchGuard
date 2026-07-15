#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_constants.csv ===
python3 <<'PYEOF'
import csv

rows = [
    [0, 96.2, 36.2, 93.1, 101.2],
    [0.068, 102.9, 38.9, 98.7, 102.6],
    [0.14, 109.6, 41.6, 99.7, 103.8],
    [0.21, 115.4, 43.8, 105.7, 104.8],
]

with open('/app/outputs/elastic_constants.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x', 'E', 'G', 'K', 'theta_m'])
    w.writerows(rows)
PYEOF
