#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: monte_carlo_results.csv ===
python3 /solution/generate_csv.py
