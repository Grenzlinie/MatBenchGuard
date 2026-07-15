#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: absorption_spectra.csv ===
python3 /solution/compute_absorption.py --output-csv /app/outputs/absorption_spectra.csv

# === solve block: absorption_edges.json ===
python3 /solution/compute_absorption.py --output-json /app/outputs/absorption_edges.json
