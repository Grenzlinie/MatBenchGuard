#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_dispersion.csv ===
python3 /solution/generate_dispersion.py > "$OUTDIR/step_01_dispersion.csv"

# === solve block: step_02_correlation.csv ===
python3 /solution/generate_correlation.py > "$OUTDIR/step_02_correlation.csv"

# === solve block: step_03_susceptibility.csv ===
python3 /solution/generate_susceptibility.py > "$OUTDIR/step_03_susceptibility.csv"
