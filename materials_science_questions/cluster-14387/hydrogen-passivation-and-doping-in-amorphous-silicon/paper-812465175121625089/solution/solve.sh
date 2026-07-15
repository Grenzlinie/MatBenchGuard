#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_energies.csv ===
python3 /solution/compute.py

# === solve block: kinetic_energies.csv ===
echo 'already produced'

# === solve block: angle_dist_HA.csv ===
echo 'already produced'

# === solve block: angle_dist_QHA.csv ===
echo 'already produced'
