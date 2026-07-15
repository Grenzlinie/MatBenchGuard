#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 /solution/compute.py

# === solve block: fcc_isoactivity_1273K.csv ===
# File already written by preamble

# === solve block: liquid_solubility_1823K.csv ===
# File already written
