#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
# Ensure Python3 is available (base image has it) and make helper executable.
chmod +x /solution/generate.py

# === solve block: resistivity_temperature.csv ===
python3 /solution/generate.py resistivity_temperature.csv

# === solve block: fitted_parameters.json ===
python3 /solution/generate.py fitted_parameters.json

# === solve block: lorenz_number_300K.txt ===
python3 /solution/generate.py lorenz_number_300K.txt
