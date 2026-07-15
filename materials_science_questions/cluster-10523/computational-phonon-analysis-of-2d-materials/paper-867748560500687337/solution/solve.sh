#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: summary_dirac_bandgaps.json ===
python3 /solution/generate_outputs.py summary_dirac_bandgaps.json > /app/outputs/summary_dirac_bandgaps.json

# === solve block: supercell_dispersion.csv ===
python3 /solution/generate_outputs.py supercell_dispersion.csv > /app/outputs/supercell_dispersion.csv
