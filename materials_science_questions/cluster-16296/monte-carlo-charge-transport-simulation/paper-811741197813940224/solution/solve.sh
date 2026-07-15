#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
python3 /solution/compute.py /app/outputs/results.csv
