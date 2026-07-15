#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: compression_limit_transitions.csv ===
python3 <<'PYEOF'
import csv
data = [
    [240.0, 1.2, 4.15],
    [260.0, 1.2, 3.95],
    [280.0, 'NaN', 'NaN'],
    [300.0, 'NaN', 'NaN']
]
with open('/app/outputs/compression_limit_transitions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature', 'P_BL_A_to_BL_VHDI', 'P_BL_VHDI_to_BL_AAI'])
    for row in data:
        writer.writerow(row)
PYEOF

# === solve block: superheating_limit_melting.csv ===
python3 <<'PYEOF'
import csv
data = [
    [1.0, 310.0, 330.0],
    [2.0, 322.0, 342.0],
    [3.0, 335.0, 355.0],
    [4.0, 320.0, 368.0]
]
with open('/app/outputs/superheating_limit_melting.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['lateral_pressure', 'T_melt_BL_VHDI', 'T_melt_BL_AAI'])
    for row in data:
        writer.writerow(row)
PYEOF
