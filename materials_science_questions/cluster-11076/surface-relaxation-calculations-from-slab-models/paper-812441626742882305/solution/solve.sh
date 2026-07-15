#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: gsf_energy.csv ===
python3 /solution/generate_reference.py /app/outputs/gsf_energy.csv

# === solve block: interlayer_spacings.csv ===
python3 /solution/generate_reference.py /app/outputs/interlayer_spacings.csv

# === solve block: summary.csv ===
python3 /solution/generate_reference.py /app/outputs/summary.csv
