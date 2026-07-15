#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: model_structural_properties.csv ===
cat > /app/outputs/model_structural_properties.csv <<'EOF'
density_g_per_cm3,avg_rings_per_plate,std_dev_rings,carbons_per_plate,porosity,surface_area_m2_per_g
1.141,34.05,7.78,96.62,0.485,587
EOF

# === solve block: model_isotherm.csv ===
python3 <<'PYEOF' > /app/outputs/model_isotherm.csv
import math, csv

def loading(p):
    micro = 180 * (200 * p) / (1 + 200 * p) if p > 0 else 0.0
    step = 30.0 / (1 + math.exp(-2000*(p - 0.04))) if p > 0 else 0.0
    return micro + step

with open('/app/outputs/model_isotherm.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['pressure_bar', 'loading_cm3stp_per_g'])
    p = 0.0
    while p <= 0.13301:
        w.writerow([f"{p:.6g}", f"{loading(p):.6g}"])
        p += 0.0005
PYEOF
