#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 /solution/generate_outputs.py

# === solve block: load_displacement.csv ===
echo 'load_displacement.csv ready'

# === solve block: split_length.csv ===
echo 'split_length.csv ready'

# === solve block: ablation_peak_loads.csv ===
echo 'ablation_peak_loads.csv ready'
