#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cyclic_response.csv ===
python3 /solution/generate.py cyclic

# === solve block: compressive_response.csv ===
python3 /solution/generate.py compressive
