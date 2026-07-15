#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 /solution/prepare_data.py

# === solve block: initial_microstructure.csv ===
python3 /solution/write_outputs.py initial_microstructure.csv

# === solve block: recrystallization_kinetics.csv ===
python3 /solution/write_outputs.py recrystallization_kinetics.csv

# === solve block: orientation_distribution.json ===
python3 /solution/write_outputs.py orientation_distribution.json

# === solve block: boundary_moments.csv ===
python3 /solution/write_outputs.py boundary_moments.csv
