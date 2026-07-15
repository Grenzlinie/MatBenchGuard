#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: effective_deflections.csv ===
python3 /solution/generate_artifacts.py --which effective_deflections.csv --outdir /app/outputs

# === solve block: parametric_curves.csv ===
python3 /solution/generate_artifacts.py --which parametric_curves.csv --outdir /app/outputs
