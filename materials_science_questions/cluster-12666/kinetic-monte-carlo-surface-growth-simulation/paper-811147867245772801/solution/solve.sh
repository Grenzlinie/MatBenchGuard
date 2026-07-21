#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
# no pip install required – only python3 stdlib (csv, math, os, random)

# === solve block: center_deviation_data.csv ===
OUTDIR="$OUTDIR" python3 /solution/generate_synthetic_data.py
