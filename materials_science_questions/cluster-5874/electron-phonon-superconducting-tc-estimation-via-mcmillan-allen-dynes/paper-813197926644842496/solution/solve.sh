#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: rmta_parameters.csv ===
python3 -c "
import csv
data = [['atom','eta','lambda'],
        ['Li','0.415','0.42'],
        ['Pd','0.344','0.07'],
        ['H','0.213','0.20'],
        ['total','','0.69']]
with open('/app/outputs/rmta_parameters.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerows(data)
"
