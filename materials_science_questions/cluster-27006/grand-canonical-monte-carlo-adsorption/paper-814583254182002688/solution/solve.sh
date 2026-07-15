#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_isotherms.csv ===
python3 /solution/write_isotherms.py

# === solve block: isosteric_heat.csv ===
python3 /solution/write_heat.py
