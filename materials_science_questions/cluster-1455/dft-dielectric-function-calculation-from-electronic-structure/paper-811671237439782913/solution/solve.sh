#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: bulk_band_structure.csv ===
python3 /solution/generate_data.py /app/outputs bulk_band_structure.csv

# === solve block: bulk_reflectivity.csv ===
python3 /solution/generate_data.py /app/outputs bulk_reflectivity.csv

# === solve block: surface_band_structure.csv ===
python3 /solution/generate_data.py /app/outputs surface_band_structure.csv

# === solve block: surface_dos.csv ===
python3 /solution/generate_data.py /app/outputs surface_dos.csv

# === solve block: surface_dielectric_function.csv ===
python3 /solution/generate_data.py /app/outputs surface_dielectric_function.csv
