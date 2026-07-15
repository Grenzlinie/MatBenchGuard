#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optimized_structures_and_energies.json ===
python3 /solution/generate_output.py /app/outputs/optimized_structures_and_energies.json

# === solve block: optimized_structures_and_energies.json ===
python3 /solution/generate_output.py /app/outputs/optimized_structures_and_energies.json
