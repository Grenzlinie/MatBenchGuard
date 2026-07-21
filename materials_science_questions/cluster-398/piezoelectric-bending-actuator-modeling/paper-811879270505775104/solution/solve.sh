#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 /solution/generate_outputs.py

# === solve block: step_01_coefficients.json ===
:

# === solve block: step_02_voltage_dependence.csv ===
:
