#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: single_model_top30.csv ===
python3 /solution/generate_csv.py single > $OUTDIR/single_model_top30.csv

# === solve block: partitioned_model_top30.csv ===
python3 /solution/generate_csv.py partitioned > $OUTDIR/partitioned_model_top30.csv
