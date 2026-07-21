#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: porosity_nsd.csv ===
python3 -c "
import csv, os
with open('$OUTDIR/porosity_nsd.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['nsd_nm2','porosity','surface_volume_ratio'])
    data = [(0.5,0.28,1.8),(1.0,0.22,2.0),(1.74,0.18,2.5),(2.5,0.12,2.9),(4.0,0.07,3.5),(6.0,0.04,3.8)]
    w.writerows(data)
"

# === solve block: porosity_x.csv ===
python3 -c "
import csv, os
with open('$OUTDIR/porosity_x.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x','porosity','surface_volume_ratio'])
    data = [(0.0,0.03,3.0),(0.5,0.05,2.8),(1.0,0.08,2.5),(1.5,0.12,2.3),(1.8,0.15,2.2),(2.0,0.17,2.0)]
    w.writerows(data)
"
