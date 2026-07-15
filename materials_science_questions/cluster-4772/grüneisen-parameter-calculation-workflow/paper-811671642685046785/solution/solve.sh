#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs

# === solve block: step_02_room_temp_isotherm.csv ===
python3 /solution/generate_outputs.py isotherm "$OUTDIR/step_02_room_temp_isotherm.csv"

# === solve block: step_03_shock_hugoniot.csv ===
python3 /solution/generate_outputs.py hugoniot "$OUTDIR/step_03_shock_hugoniot.csv"

# === solve block: step_04_gruneisen_gamma.csv ===
python3 /solution/generate_outputs.py gruneisen "$OUTDIR/step_04_gruneisen_gamma.csv"
