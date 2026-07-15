#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: dos_18A_hcovered.csv ===
python3 << 'EOF' > "$OUTDIR/dos_18A_hcovered.csv"
import numpy as np

# energy grid matching original step size
E = np.arange(-10.0, 10.0, 0.01)

# band edges for a 1.6 eV gap
VBM = -0.8   # valence band maximum
CBM =  0.8   # conduction band minimum

# shape parameters: Gaussian peaks centred at ±3 eV, width σ
A, sigma = 5.0, 1.0
E0_val  = -3.0
E0_cond =  3.0

# zero density everywhere by default; fill bands
dos = np.zeros_like(E)

# valence band: non‑zero only for E <= VBM, goes to zero at VBM
mask_val = E <= VBM
dos[mask_val] = A * (VBM - E[mask_val]) * np.exp(-((E[mask_val] - E0_val) ** 2) / (2 * sigma ** 2))

# conduction band: non‑zero only for E >= CBM, goes to zero at CBM
mask_cond = E >= CBM
dos[mask_cond] = A * (E[mask_cond] - CBM) * np.exp(-((E[mask_cond] - E0_cond) ** 2) / (2 * sigma ** 2))

# the gap region (−0.8 eV to 0.8 eV) remains zero

# CSV header and rows
print('energy_eV,total_DOS')
for en, d in zip(E, dos):
    print(f'{en:.2f},{d:.12f}')
EOF

# === solve block: dos_18A_dangling.csv ===
python3 /solution/generate_dos.py dangling > "$OUTDIR/dos_18A_dangling.csv"

# === solve block: dos_18A_truncated.csv ===
python3 /solution/generate_dos.py truncated > "$OUTDIR/dos_18A_truncated.csv"

# === solve block: bandgap_vs_diameter.csv ===
python3 /solution/generate_bg_table.py > "$OUTDIR/bandgap_vs_diameter.csv"
