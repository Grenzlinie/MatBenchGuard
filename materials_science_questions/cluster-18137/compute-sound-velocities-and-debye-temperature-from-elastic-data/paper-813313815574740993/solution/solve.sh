#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 /solution/make_outputs.py

# === solve block: elastic_and_moduli.json ===
echo ''

# === solve block: thermophysical.json ===
echo ''
