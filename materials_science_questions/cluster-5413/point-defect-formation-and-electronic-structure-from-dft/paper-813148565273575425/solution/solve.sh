#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 /solution/generate_ov_data.py

# === solve block: ov_per_sample.json ===
true

# === solve block: ov_statistics.csv ===
true
