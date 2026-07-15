#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: critical_supersaturation_table.csv ===
python3 << 'EOF'
import csv
header = ['P_e', 'theta_no_diff', 'theta_with_diff']
data = [
    [1e-12, 20.0, 110.0],
    [1e-11, 10.5, 43.575],
    [1e-10, 6.2, 16.74],
    [1e-9, 4.2, 6.72],
    [1e-8, 3.0, 3.75],
    [1e-7, 2.35, 2.538],
    [1e-6, 1.95, 1.989],
]
with open('/app/outputs/critical_supersaturation_table.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
EOF
