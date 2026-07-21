#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: kinetic_curves.csv ===
python3 /solution/generate.py kinetic > /app/outputs/kinetic_curves.csv

# === solve block: shape_T500_no_spillover.csv ===
python3 /solution/generate.py shape > /app/outputs/shape_T500_no_spillover.csv
