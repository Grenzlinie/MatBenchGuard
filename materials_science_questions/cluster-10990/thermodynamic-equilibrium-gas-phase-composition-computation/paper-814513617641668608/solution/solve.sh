#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phase_diagram.csv ===
python3 /solution/generate_outputs.py

# === solve block: yield_map_BN_Si3N4.csv ===
:

# === solve block: yield_map_SiC_C_B4C.csv ===
:

# === solve block: trend_summary.txt ===
:
