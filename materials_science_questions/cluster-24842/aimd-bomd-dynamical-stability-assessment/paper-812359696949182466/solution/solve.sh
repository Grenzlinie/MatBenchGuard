#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ga17_specific_heat.csv ===
python3 /solution/generate_specific_heat.py \
  --T0 650 --T-min 150 --T-max 1100 --step 5 \
  --sigma 30 --amplitude 1.0 --baseline 0.2 \
  --output "$OUTDIR/ga17_specific_heat.csv"

# === solve block: ga13_specific_heat.csv ===
python3 /solution/generate_specific_heat.py \
  --T0 1400 --T-min 40 --T-max 1750 --step 5 \
  --sigma 40 --amplitude 1.0 --baseline 0.2 \
  --output "$OUTDIR/ga13_specific_heat.csv"
