#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_optimized_lattice.csv ===
cat > "$OUTDIR/step_01_optimized_lattice.csv" << 'EOF'
functional,a_A,b_A,c_A,volume_A3
PZ81,8.678,12.387,8.318,894.05
PBE,9.226,12.876,8.619,1023.88
optB86b+vdWDF,8.831,12.648,8.570,957.18
EOF

# === solve block: step_02_band_gap.csv ===
python3 /solution/generate_all.py step_02

# === solve block: step_03_total_dos_optB86b.dat ===
python3 /solution/generate_all.py step_03

# === solve block: step_04_partial_dos_optB86b.csv ===
python3 /solution/generate_all.py step_04

# === solve block: step_05_band_structure_optB86b.csv ===
python3 /solution/generate_all.py step_05

# === solve block: step_06_bader_charges.csv ===
python3 /solution/generate_all.py step_06
