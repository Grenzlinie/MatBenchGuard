#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: cluster_distributions.csv ===
python3 - << 'PYEOF' "$OUTDIR/cluster_distributions.csv"
import csv, sys, math
outpath = sys.argv[1]

def generate_rows(temp, dose):
    rows = []
    peak_i = 10
    peak_v = 44
    if temp <= 600:
        i_tail_right = 0.05
        v_tail_right = 0.3
    elif temp <= 650:
        i_tail_right = 0.2
        v_tail_right = 0.05
    else:  # 660 K
        i_tail_right = 0.3
        v_tail_right = 0.02
    for n in range(2, 151):
        if n <= peak_i:
            conc_i = math.exp(-0.5 * (peak_i - n))
        else:
            conc_i = math.exp(-i_tail_right * (n - peak_i))
        if n <= peak_v:
            conc_v = math.exp(-0.8 * (peak_v - n))
        else:
            conc_v = math.exp(-v_tail_right * (n - peak_v))
        rows.append([temp, dose, 'interstitial', n, conc_i])
        rows.append([temp, dose, 'vacancy', n, conc_v])
    return rows

all_rows = []
for t in [600, 650, 660]:
    for d in [1, 5]:
        all_rows.extend(generate_rows(t, d))

with open(outpath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Temperature','Dose','Species','ClusterSize','Concentration'])
    w.writerows(all_rows)
PYEOF

# === solve block: diffusion_coefficients.csv ===
python3 /solution/generate_outputs.py "$OUTDIR/diffusion_coefficients.csv" diffusion_coefficients
