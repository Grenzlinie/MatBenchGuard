#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetization_curves.csv ===
python3 /solution/compute_all.py

# === solve block: magnetization_vs_delta.csv ===
echo "magnetization_vs_delta.csv already written by the previous step"
