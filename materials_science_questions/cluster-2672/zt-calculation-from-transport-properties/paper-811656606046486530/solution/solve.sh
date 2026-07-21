#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_lattice_constant.txt ===
echo "9.466" > "$OUTDIR/step_01_lattice_constant.txt"

# === solve block: step_02_dos_peak_energy.txt ===
echo "0.21" > "$OUTDIR/step_02_dos_peak_energy.txt"

# === solve block: step_03_ideal_ZT.txt ===
python3 /solution/compute_zt.py 0.21 > "$OUTDIR/step_03_ideal_ZT.txt"
