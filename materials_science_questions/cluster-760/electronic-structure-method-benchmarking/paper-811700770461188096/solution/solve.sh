#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 /solution/generate_results.py
