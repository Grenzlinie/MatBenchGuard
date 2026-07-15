#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: pdos.csv ===
python3 /solution/generate.py pdos > /app/outputs/pdos.csv

# === solve block: results.json ===
python3 /solution/generate.py results > /app/outputs/results.json
