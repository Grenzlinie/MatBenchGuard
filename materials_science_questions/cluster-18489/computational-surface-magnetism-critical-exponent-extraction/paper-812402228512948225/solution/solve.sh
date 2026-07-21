#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_thermal.csv ===
python3 /solution/gen_thermal.py > /app/outputs/step_01_thermal.csv

# === solve block: step_02_profile.csv ===
python3 /solution/gen_profile.py > /app/outputs/step_02_profile.csv
