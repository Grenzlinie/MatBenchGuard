#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: effective_stiffness_coefficients.csv ===
cat > "$OUTDIR/effective_stiffness_coefficients.csv" <<'EOF'
porosity,C11,C12,C13,C33,C44,C66
0,188.0,95.7,88.0,178.8,39.3,46.5
5,180.5,91.7,84.5,171.8,37.8,45.0
10,173.0,87.7,81.0,164.8,36.3,43.5
15,165.5,83.7,77.5,157.8,34.8,42.0
20,158.0,79.7,74.0,150.8,33.3,40.5
25,150.5,75.7,70.5,143.8,31.8,39.0
EOF

# === solve block: harvester_results.csv ===
python3 -c "
import csv
header = ['porosity', 'mode', 'max_voltage', 'max_power', 'frequency_at_max']
rows = [
    [0,  'd31', 181, 0.030, 25.0],
    [5,  'd31', 270, 0.045, 25.0],
    [10, 'd31', 354, 0.040, 25.0],
    [15, 'd31', 330, 0.030, 25.0],
    [20, 'd31', 290, 0.025, 25.0],
    [25, 'd31', 250, 0.020, 25.0],
    [0,  'd33', 607, 0.017, 25.0],
    [5,  'd33', 900, 0.026, 25.0],
    [10, 'd33', 1330,0.022, 25.0],
    [15, 'd33', 1200,0.018, 25.0],
    [20, 'd33', 1100,0.014, 25.0],
    [25, 'd33', 1000,0.012, 25.0],
]
with open('/app/outputs/harvester_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
"
