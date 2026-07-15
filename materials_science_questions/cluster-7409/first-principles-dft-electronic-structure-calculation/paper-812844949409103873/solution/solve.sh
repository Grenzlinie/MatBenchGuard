#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
chmod +x /solution/generate_outputs.py

# === solve block: band_structure.dat ===
python3 /solution/generate_outputs.py band_structure > /app/outputs/band_structure.dat

# === solve block: dos.dat ===
python3 /solution/generate_outputs.py dos > /app/outputs/dos.dat

# === solve block: band_gap.txt ===
python3 /solution/generate_outputs.py band_gap > /app/outputs/band_gap.txt
