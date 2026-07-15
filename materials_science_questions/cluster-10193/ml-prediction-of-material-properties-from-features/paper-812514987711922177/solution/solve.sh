#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 /solution/generate_outputs.py

# === solve block: step_01_test_predictions.csv ===
echo 'step_01_test_predictions.csv already generated.'

# === solve block: step_02_extrapolation_results.csv ===
echo 'step_02_extrapolation_results.csv already generated.'
