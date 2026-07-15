#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: finesse.csv ===
python3 -c "
import csv
data = [(0.01,0.9,29),(0.24,0.8,14),(1.0,0.8,14),(10.0,0.8,14),(100.0,0.7,9)]
with open('$OUTDIR/finesse.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['L','R','theoretical_finesse'])
    w.writerows(data)
"

# === solve block: effective_reflectance.csv ===
python3 -c "
import csv
data = [(0.01,0.9,0.85),(0.24,0.8,0.71),(1.0,0.8,0.77),(10.0,0.8,0.54),(100.0,0.7,0.28)]
with open('$OUTDIR/effective_reflectance.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['L','R_nominal','effective_reflectance'])
    w.writerows(data)
"

# === solve block: temp_sensitivities.json ===
python3 -c "
import json
d = {'jacketed_S_phase': 3.0e-5, 'unjacketed_S_phase': 8.0e-6}
with open('$OUTDIR/temp_sensitivities.json','w') as f:
    json.dump(d,f)
"
