#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: raw_frequencies.csv ===
python3 /solution/generate_artifacts.py raw

# === solve block: normalized_frequencies.csv ===
python3 /solution/generate_artifacts.py norm
