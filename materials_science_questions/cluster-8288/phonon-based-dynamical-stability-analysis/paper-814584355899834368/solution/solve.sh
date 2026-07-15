#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: p6_3_band_structure.json ===
python3 /solution/solve.py band_structure

# === solve block: band_gaps.json ===
python3 /solution/solve.py gaps

# === solve block: p6_3_phonon_dispersion.json ===
python3 /solution/solve.py phonon
