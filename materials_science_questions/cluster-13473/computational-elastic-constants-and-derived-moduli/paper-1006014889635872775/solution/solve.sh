#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: shear_modulus_distributions.csv ===
python3 /solution/generate.py shear_modulus_distributions.csv

# === solve block: average_moduli.csv ===
python3 /solution/generate.py average_moduli.csv

# === solve block: gb_fraction.csv ===
python3 /solution/generate.py gb_fraction.csv

# === solve block: mean_field_params.csv ===
python3 /solution/generate.py mean_field_params.csv
