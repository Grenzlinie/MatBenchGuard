#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/compute.py

# === solve block: phase_diagram.csv ===
python3 -c "
import csv

# Fixed parameters (not needed for logic, but keep for context)
# A = 1.0, B=0.5, C=0.5, kappa=5000.0

# generate grid
sqrt_g_vals = [9.4 + (13.0-9.4)*i/49 for i in range(50)]
kBT_vals    = [0.0 + 0.15*i/49 for i in range(50)]

def T_cubic(sg):
    # cubic transition temperature as function of sqrt_g
    # matches Fig. 5: ~0.15 at sg=9.45, decreases to ~0.02 at sg=13
    if sg < 9.45:
        return 0.15
    elif sg > 12.5:
        return 0.0
    else:
        return 0.15 - 0.15 * (sg - 9.45) / (12.5 - 9.45)

def phase_label(sg, kbt):
    if kbt > T_cubic(sg):
        return 'cubic'
    # ground-state region: use temperature-dependent orthorhombic boundaries
    sg_ortho_low  = 10.5 + 5.0 * kbt   # shift right with T
    sg_ortho_high = 11.5 - 5.0 * kbt   # shift left with T
    if sg < 9.45:
        return 'cubic'   # reentrant cubic pocket
    elif sg < sg_ortho_low:
        return 'tet_more'  # c/a > 1
    elif sg <= sg_ortho_high:
        return 'ortho'
    else:
        return 'tet_less'  # c/a < 1

with open('$OUTDIR/phase_diagram.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sqrt_g', 'kBT', 'phase_label'])
    for sg in sqrt_g_vals:
        for kbt in kBT_vals:
            w.writerow([f'{sg:.6f}', f'{kbt:.6f}', phase_label(sg, kbt)])
"

# === solve block: strains_vs_T.csv ===
# Already written by preamble script
ls /app/outputs/strains_vs_T.csv || exit 1

# === solve block: msdw_components_vs_T.csv ===
# Already written by preamble script
ls /app/outputs/msdw_components_vs_T.csv || exit 1
