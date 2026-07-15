#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: gruneisen_parameters.csv ===
python3 /solution/gen_outputs.py --output gamma

# === solve block: computed_raman_frequencies.csv ===
python3 /solution/gen_outputs.py --output frequency
