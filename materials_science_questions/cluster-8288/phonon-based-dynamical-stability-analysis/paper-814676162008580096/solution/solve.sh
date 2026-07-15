#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optimized_structures.json ===
python3 /solution/write_outputs.py /app/outputs/optimized_structures.json

# === solve block: eos_parameters.json ===
python3 /solution/write_outputs.py /app/outputs/eos_parameters.json

# === solve block: band_gaps.json ===
python3 /solution/write_outputs.py /app/outputs/band_gaps.json

# === solve block: phonon_frequencies.json ===
python3 /solution/write_outputs.py /app/outputs/phonon_frequencies.json
