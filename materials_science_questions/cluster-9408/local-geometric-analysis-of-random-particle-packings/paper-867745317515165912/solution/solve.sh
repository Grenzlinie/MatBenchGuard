#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: frustrated_mass_vs_epsilon.csv ===
python3 /solution/generate_data.py > "/app/outputs/frustrated_mass_vs_epsilon.csv"
