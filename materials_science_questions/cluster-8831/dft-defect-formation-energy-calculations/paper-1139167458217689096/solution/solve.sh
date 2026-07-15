#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_materials_list.txt ===
python3 /solution/generate.py

# === solve block: step_02_delta_G_pbx.csv ===
true

# === solve block: step_03_stability_summary.json ===
true
