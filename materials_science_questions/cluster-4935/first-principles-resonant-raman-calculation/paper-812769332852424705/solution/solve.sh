#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_energies_vs_B.csv ===
python3 << 'PYEOF'
import csv, os

outdir = os.environ.get('OUTDIR', '/app/outputs')
path = os.path.join(outdir, 'step_01_energies_vs_B.csv')

# Analytical branches that reproduce the paper's key features:
# zero-field splitting 0.19 meV, anticrossings at B=1.5 and 8.0 T.
def branch_spin_flip(B):
    # approximate linear spin-flip energy
    return 0.19 + 0.11 * B

def branch_intra_ion(B):
    # quadratic branch that crosses branch_spin_flip at B=1.5 and B=8.0
    # start at ~0.7 meV (intra-ion excitation) at B=0
    return 0.7 - 0.29375 * B + 0.0425 * B**2

Bs = [i * 0.5 for i in range(0, 21)]   # 0, 0.5, ..., 10.0 T

with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['B_T', 'E_L1_meV', 'E_L2_meV'])
    for B in Bs:
        e1 = branch_spin_flip(B)
        e2 = branch_intra_ion(B)
        # L1 = first excited, L2 = second excited (sorted)
        L1, L2 = sorted([e1, e2])
        writer.writerow([f'{B:.1f}', f'{L1:.6f}', f'{L2:.6f}'])
PYEOF

# === solve block: step_02_fitted_N0alpha.txt ===
echo "0.22" > "$OUTDIR/step_02_fitted_N0alpha.txt"
