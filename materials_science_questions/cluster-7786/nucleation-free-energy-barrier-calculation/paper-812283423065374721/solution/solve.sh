#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
cp /solution/compute.py /app/compute.py

# === solve block: surface_energies.csv ===
python3 /app/compute.py surface_energies.csv /app/outputs

# === solve block: vapor_pressure_298K.txt ===
python3 /app/compute.py vapor_pressure_298K.txt /app/outputs

# === solve block: critical_dimensions.csv ===
python3 /app/compute.py critical_dimensions.csv /app/outputs
