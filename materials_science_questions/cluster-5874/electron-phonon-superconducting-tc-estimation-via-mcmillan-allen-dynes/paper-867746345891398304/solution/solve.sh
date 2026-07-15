#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_alph2F_data.json ===
python3 /solution/generate_alph2f.py step_01

# === solve block: step_02_elph_params.csv ===
python3 /solution/generate_alph2f.py step_02
