#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: damage_vs_parameters.csv ===
python3 /solution/write_csv.py

# === solve block: piezo_coefficients.csv ===
python3 /solution/write_csv.py
