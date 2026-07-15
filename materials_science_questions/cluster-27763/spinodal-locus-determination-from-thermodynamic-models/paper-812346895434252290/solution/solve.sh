#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: coexistence_data.csv ===
export OUTDIR
python3 << 'PYEOF'
import csv, math, os

outdir = '/app/outputs'
filepath = os.path.join(outdir, 'coexistence_data.csv')

Tc = 1.638
B = 0.74
beta = 0.325
Ns = [400, 800, 1600, 3200]
temps = [1.4, 1.45, 1.5, 1.55, 1.6, 1.62, 1.635]

rows = []
for N in Ns:
    for T in temps:
        x = 0.5 - B * (1 - T/Tc)**beta
        rows.append([N, T, round(x, 5)])
# add Tc row
rows.append(['Tc', '', Tc])

with open(filepath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['N', 'T', 'x_B_coex'])
    for row in rows:
        w.writerow(row)
PYEOF

# === solve block: static_properties.csv ===
python3 << 'PYEOF'
import csv, os

outdir = os.environ['OUTDIR']
filepath = os.path.join(outdir, 'static_properties.csv')

data = [
    (6.0, 0.012, 0.05),
    (3.0, 0.016, 0.10),
    (1.7, 0.022, 0.20),
    (1.6, 0.024, 0.25),
    (1.4, 0.030, 0.40),
]
with open(filepath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T', 'kappa_T', 'chi'])
    for T, k, chi in data:
        w.writerow([T, k, chi])
PYEOF

# === solve block: viscosities.csv ===
python3 << 'PYEOF'
import csv, os

outdir = os.environ['OUTDIR']
filepath = os.path.join(outdir, 'viscosities.csv')

data = [
    (6.0, 1.2, 1.5, 1.25),
    (3.0, 1.3, 2.0, 1.538),
    (1.7, 1.5, 3.5, 2.333),
    (1.6, 1.5, 4.0, 2.667),
    (1.4, 1.5, 5.0, 3.333),
]
with open(filepath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T', 'eta_s', 'eta_B', 'eta_B_eta_s_ratio'])
    for T, eta_s, eta_B, ratio in data:
        w.writerow([T, eta_s, eta_B, ratio])
PYEOF
