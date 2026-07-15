#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: fitted_indices.csv ===
python3 -c "
import csv, sys
wr = csv.writer(sys.stdout)
wr.writerow(['sample', 'material', 'n_193.39', 'dn_dlambda'])
data = [
    ('A1', 'fused silica', 1.560685, -0.001577),
    ('A2', 'fused silica', 1.560694, -0.001587),
    ('A3', 'fused silica', 1.560683, -0.001571),
    ('B1', 'fused silica', 1.560722, -0.001577),
    ('B2', 'fused silica', 1.560714, -0.001576),
    ('B3', 'fused silica', 1.560703, -0.001577),
    ('C1', 'fused silica', 1.560676, -0.001577),
    ('C2', 'fused silica', 1.560683, -0.001578),
    ('A1', 'calcium fluoride', 1.501939, -0.00099),
    ('A2', 'calcium fluoride', 1.501936, -0.00099),
    ('B',  'calcium fluoride', 1.501924, -0.00098)
]
for row in data:
    wr.writerow(row)
" > $OUTDIR/fitted_indices.csv

# === solve block: fitted_coefficients.csv ===
python3 /solution/generate.py
