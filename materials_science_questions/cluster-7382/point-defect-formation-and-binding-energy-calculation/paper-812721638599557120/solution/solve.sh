#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transport_coefficients.csv ===
python3 -c "
import csv
with open('/app/outputs/transport_coefficients.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['coordination_order','D_d0','T_d0','alpha'])
    vals=[(1,0.1237,-0.2473),(2,0.365,-0.605),(3,5.31,4.70),(4,5.43,4.61),(5,5.8,5.12)]
    for order,d,t in vals:
        w.writerow([order,d,t,t/d])
"
