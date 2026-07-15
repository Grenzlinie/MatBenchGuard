#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: simulation_results.csv ===
python3 /solution/generate_csv.py "$OUTDIR/simulation_results.csv"
