#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: resistivity_TCR.csv ===
python3 -c "
import csv
data = [
    ['metal','resistivity','TCR'],
    ['Ag',23.161,29],
    ['Au',79.46,6.6],
    ['Fe',200.02,5.2],
    ['Ni',94.328,3],
    ['Eu',282.5,-32.1],
]
with open('$OUTDIR/resistivity_TCR.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerows(data)
"
