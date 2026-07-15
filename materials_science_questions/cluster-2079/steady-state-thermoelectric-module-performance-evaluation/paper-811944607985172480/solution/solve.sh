#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_tec_parameters.csv ===
python3 /solution/writer.py step_01

# === solve block: step_02_predictions.csv ===
python3 /solution/writer.py step_02
