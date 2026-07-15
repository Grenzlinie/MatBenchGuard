#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: superconducting_properties.csv ===
python3 /solution/generate_csv.py
