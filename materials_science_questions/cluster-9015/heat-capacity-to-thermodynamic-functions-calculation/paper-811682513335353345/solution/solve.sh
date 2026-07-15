#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: thermodynamic_functions.csv ===
python3 /solution/compute_thermo.py > /app/outputs/thermodynamic_functions.csv
