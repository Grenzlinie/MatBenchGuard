#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: pren_results.csv ===
python3 -c "
import csv
import os
rows = [
    [1050, 'ferrite', 26.5, 3.9, 0.05],
    [1050, 'austenite', 20.0, 2.0, 0.30],
    [1100, 'ferrite', 26.0, 3.6, 0.05],
    [1100, 'austenite', 20.8, 2.2, 0.33],
    [1150, 'ferrite', 25.0, 3.0, 0.05],
    [1150, 'austenite', 21.5, 2.5, 0.38],
    [1200, 'ferrite', 24.5, 2.8, 0.05],
    [1200, 'austenite', 22.0, 2.8, 0.45],
]
header = ['Temperature','Phase','Cr_wt','Mo_wt','N_wt','PREN']
with open(os.path.join('$OUTDIR','pren_results.csv'),'w',newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    for T,ph,cr,mo,n in rows:
        pren = cr + 3.3*mo + 16.0*n
        w.writerow([T,ph,round(cr,2),round(mo,2),round(n,2),round(pren,4)])
"
