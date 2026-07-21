#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: step_01_deflections_partial.csv ===
python3 /solution/gen_deflections.py step01 "$OUTDIR"

# === solve block: step_02_deflections_half.csv ===
python3 /solution/gen_deflections.py step02 "$OUTDIR"

# === solve block: step_03_central_deflections.csv ===
python3 /solution/gen_deflections.py step03 "$OUTDIR"
