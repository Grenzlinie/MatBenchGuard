#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: relative_enthalpies.csv ===
python3 /solution/write_outputs.py /app/outputs/relative_enthalpies.csv

# === solve block: rrkm_stabilization.csv ===
python3 /solution/write_outputs.py /app/outputs/rrkm_stabilization.csv
