#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: loocv_predictions_973K.csv ===
cp /solution/loocv_predictions_973K.csv /app/outputs/loocv_predictions_973K.csv
