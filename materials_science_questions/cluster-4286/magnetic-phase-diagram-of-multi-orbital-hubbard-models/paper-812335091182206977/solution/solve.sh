#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_cf_sf_doping.csv ===
python3 /solution/generate.py step_01 /app/outputs/step_01_cf_sf_doping.csv

# === solve block: step_02_cf_sf_interaction.csv ===
python3 /solution/generate.py step_02 /app/outputs/step_02_cf_sf_interaction.csv

# === solve block: step_03_ring_exchange.csv ===
python3 /solution/generate.py step_03 /app/outputs/step_03_ring_exchange.csv

# === solve block: step_04_projected_cf_doping.csv ===
python3 /solution/generate.py step_04 /app/outputs/step_04_projected_cf_doping.csv
