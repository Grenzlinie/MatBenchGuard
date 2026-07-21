#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: water_flux_data.csv ===
python3 /solution/gen.py --outdir /app/outputs --file water_flux_data.csv

# === solve block: salt_rejection_data.csv ===
python3 /solution/gen.py --outdir /app/outputs --file salt_rejection_data.csv

# === solve block: pmf_profiles.csv ===
python3 /solution/gen.py --outdir /app/outputs --file pmf_profiles.csv
