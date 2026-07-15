#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cheLPG_charges.csv ===
python3 /solution/generate.py csv > /app/outputs/cheLPG_charges.csv

# === solve block: terminal_voltage.json ===
python3 /solution/generate.py json > /app/outputs/terminal_voltage.json
