#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: mode_gruneisen.csv ===
python3 /solution/generate.py mode_gruneisen.csv "$OUTDIR/mode_gruneisen.csv"

# === solve block: thermal_expansion.json ===
python3 /solution/generate.py thermal_expansion.json "$OUTDIR/thermal_expansion.json"
