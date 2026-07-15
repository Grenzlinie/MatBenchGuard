#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dos_curve.csv ===
python3 /solution/generate_outputs.py --dos-curve /app/outputs/dos_curve.csv

# === solve block: dos_peaks.json ===
python3 /solution/generate_outputs.py --peaks /app/outputs/dos_peaks.json

# === solve finalize ===
echo 'All outputs written.'
