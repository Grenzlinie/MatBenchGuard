#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dZ_HCl.csv ===
python3 /solution/generate_outputs.py --output hcl

# === solve block: dZ_HF.csv ===
python3 /solution/generate_outputs.py --output hf

# === solve block: dZ_nonstandard.csv ===
python3 /solution/generate_outputs.py --output nonstandard
