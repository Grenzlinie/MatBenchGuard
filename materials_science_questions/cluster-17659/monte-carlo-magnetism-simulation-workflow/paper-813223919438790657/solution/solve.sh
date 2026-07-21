#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: az_data.csv ===
python3 << 'EOF'
import csv

zs = [1, 2, 3, 3.5, 4, 5, 5.5, 6, 6.5, 7]
Ls = [24, 36, 48, 60, 90, 120]

eta_map = {
    1: 2.0,
    2: 2.0,
    3: 2.0,
    3.5: 2.0,
    4: 0.45,
    5: 0.3,
    5.5: 0.25,
    6: 0.2,
    6.5: 0.0,
    7: 0.0
}

with open('/app/outputs/az_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['z', 'L', 'A_z'])
    for z in zs:
        eta = eta_map[z]
        for L in Ls:
            A_z = L ** (2 - eta)
            writer.writerow([z, L, A_z])
EOF
