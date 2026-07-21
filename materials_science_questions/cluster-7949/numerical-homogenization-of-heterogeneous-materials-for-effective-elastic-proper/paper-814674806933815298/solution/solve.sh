#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: fixed_strain_ratios.json ===
python3 /solution/write_artifacts.py --output json

# === solve block: residual_fixed_strain_ratios.csv ===
python3 /solution/write_artifacts.py --output csv
