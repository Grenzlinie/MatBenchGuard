#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: deceleration_phase.csv ===
python3 /solution/generate_outputs.py deceleration_phase.csv

# === solve block: radial_density.csv ===
python3 /solution/generate_outputs.py radial_density.csv
