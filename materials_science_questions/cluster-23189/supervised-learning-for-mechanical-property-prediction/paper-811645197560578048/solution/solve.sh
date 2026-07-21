#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: forward_predictions.csv ===
python3 /solution/compute.py forward /app/outputs/forward_predictions.csv

# === solve block: inverse_Vf_predictions.csv ===
python3 /solution/compute.py inverse_vf /app/outputs/inverse_Vf_predictions.csv

# === solve block: angle_predictions.csv ===
python3 /solution/compute.py angle /app/outputs/angle_predictions.csv
