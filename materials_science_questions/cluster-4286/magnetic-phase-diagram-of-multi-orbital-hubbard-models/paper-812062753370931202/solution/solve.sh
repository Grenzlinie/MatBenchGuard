#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: delta_L_values.csv ===
python3 /solution/write_outputs.py delta_L

# === solve block: leading_constant_report.json ===
python3 /solution/write_outputs.py leading_constant
