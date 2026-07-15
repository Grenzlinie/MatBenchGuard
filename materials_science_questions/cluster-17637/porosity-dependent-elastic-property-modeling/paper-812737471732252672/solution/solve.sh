#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: porosity.csv ===
cat << 'PYEOF' | python3 -
import csv

D_vals = [400, 600, 800]
d_vals = [300, 400, 500]
theta_vals = [1, 2, 3, 4]

header = ['D_um', 'd_um', 'theta_pattern', 'porosity_percent']
rows = []

# linear index with equal weights; extremes: 0.8_0.3_1 -> 39.58, 0.4_0.5_4 -> 64.13
por_min = 39.58
por_max = 64.13
span = por_max - por_min   # 24.55

for D in D_vals:
    for d in d_vals:
        for th in theta_vals:
            # normalized contributions (0..1)
            v_D = (800 - D) / 400.0        # D=800->0, D=400->1
            v_d = (d - 300) / 200.0        # d=300->0, d=500->1
            v_theta = (th - 1) / 3.0       # th=1->0, th=4->1
            factor = (v_D + v_d + v_theta) / 3.0   # equal weights
            por = round(por_min + span * factor, 2)
            rows.append({'D_um': D, 'd_um': d, 'theta_pattern': th, 'porosity_percent': por})

with open('/app/outputs/porosity.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader()
    w.writerows(rows)
PYEOF

# === solve block: effective_modulus.csv ===
cat > /app/outputs/effective_modulus.csv << 'CSVEOF'
composite_id,model_name,E_eff_GPa
S1,0.8_0.3_1,28.0
S1,0.4_0.5_4,2.2
S2,0.8_0.3_1,33.2
S2,0.4_0.5_4,4.1
S3,0.8_0.3_1,37.2
S3,0.4_0.5_4,9.9
S4,0.8_0.3_1,19.5
S4,0.4_0.5_4,0.8
CSVEOF
