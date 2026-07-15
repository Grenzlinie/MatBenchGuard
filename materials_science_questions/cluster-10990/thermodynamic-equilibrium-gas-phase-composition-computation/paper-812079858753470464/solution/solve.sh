#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: ti_cl_output_deposition.csv ===
python3 /solution/generate.py ti_cl_output_deposition.csv

# === solve block: ti_cl_output_etching.csv ===
python3 /solution/generate.py ti_cl_output_etching.csv

# === solve block: species_pressures_deposition.json ===
python3 /solution/generate.py species_pressures_deposition.json
