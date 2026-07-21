#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gap_vs_diameter.csv ===
python3 /solution/generate.py band_gap > /app/outputs/band_gap_vs_diameter.csv

# === solve block: ZT_vs_diameter.csv ===
python3 /solution/generate.py zt > /app/outputs/ZT_vs_diameter.csv
