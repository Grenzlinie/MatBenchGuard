#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: front_speed_one_component.txt ===
echo 90.0 > /app/outputs/front_speed_one_component.txt

# === solve block: binary_bond_angle_distribution.csv ===
python3 /solution/generate_bond_angle.py > /app/outputs/binary_bond_angle_distribution.csv
