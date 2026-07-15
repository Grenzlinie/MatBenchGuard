#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: kink_predictions.csv ===
python3 /solution/compute_kink.py

# === solve block: rotation_rate.csv ===
echo "rotation_rate.csv already written by compute_kink.py"
