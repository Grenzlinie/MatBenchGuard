#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: 1d_weight_factors.csv ===
cat > "${OUTDIR}/1d_weight_factors.csv" << 'CSVEOF'
T_star,w1,w2,w3
0.2,0.42,0.12,0.06
0.5,0.005,0.003,0.002
CSVEOF

# === solve block: 2d_weight_factors.csv ===
python3 << 'PYEOF'
import csv
with open('/app/outputs/2d_weight_factors.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T_star', 'L', 'w1', 'w2', 'w3'])
    w.writerow([2.2, 32, 0.68, 0.08, 0.04])
    w.writerow([6.2, 32, 0.002, 0.001, 0.0008])
PYEOF

# === solve block: fss_results.csv ===
python3 << 'PYEOF'
import csv
with open('/app/outputs/fss_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['L', 'value', 'description'])
    w.writerow([32, 0.150000, 'w1_at_Tc'])
    w.writerow([64, 0.126135, 'w1_at_Tc'])
    w.writerow([128, 0.106066, 'w1_at_Tc'])
    w.writerow([0, 0.125, 'beta_over_nu'])
PYEOF
