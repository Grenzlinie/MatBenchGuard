#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: distribution_moments.csv ===
python3 /solution/generate_csvs.py /app/outputs
[ -f /app/outputs/distribution_moments.csv ] || { echo "Missing distribution_moments.csv"; exit 1; }

# === solve block: emission_rates_realistic.csv ===
python3 /solution/generate_csvs.py /app/outputs
[ -f /app/outputs/emission_rates_realistic.csv ] || { echo "Missing emission_rates_realistic.csv"; exit 1; }

# === solve block: emission_rates_cosh.csv ===
python3 /solution/generate_csvs.py /app/outputs
[ -f /app/outputs/emission_rates_cosh.csv ] || { echo "Missing emission_rates_cosh.csv"; exit 1; }
