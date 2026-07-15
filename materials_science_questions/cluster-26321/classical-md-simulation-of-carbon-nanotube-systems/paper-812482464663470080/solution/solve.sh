#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: histogram_initial.csv ===
python3 /solution/generate_histograms.py --type initial --output "$OUTDIR/histogram_initial.csv"

# === solve block: histogram_evolved.csv ===
python3 /solution/generate_histograms.py --type evolved --output "$OUTDIR/histogram_evolved.csv"
