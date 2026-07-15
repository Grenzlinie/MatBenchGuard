#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: absorption_spectra.csv ===
python3 /solution/gen_spectra.py spectra > /app/outputs/absorption_spectra.csv

# === solve block: plasmon_summary.csv ===
python3 /solution/gen_spectra.py summary > /app/outputs/plasmon_summary.csv
