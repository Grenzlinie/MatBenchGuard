#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: deep_quench_profiles.csv ===
python3 /solution/generate_profiles.py deep "$OUTDIR/deep_quench_profiles.csv"

# === solve block: comparison_profiles.csv ===
python3 /solution/generate_profiles.py comparison "$OUTDIR/comparison_profiles.csv"
