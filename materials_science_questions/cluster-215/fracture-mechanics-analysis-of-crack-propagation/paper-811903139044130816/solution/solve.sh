#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: mode_II_fracture_stress.csv ===
python3 /solution/compute.py mode2 > /app/outputs/mode_II_fracture_stress.csv

# === solve block: tension_fracture_stress.csv ===
python3 /solution/compute.py tension > /app/outputs/tension_fracture_stress.csv
