#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: simulation_results.csv ===
python3 /solution/generate_results.py /app/outputs/simulation_results.csv
