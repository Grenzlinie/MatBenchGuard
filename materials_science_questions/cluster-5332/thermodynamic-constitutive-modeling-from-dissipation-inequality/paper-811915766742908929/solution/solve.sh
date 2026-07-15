#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 /solution/generate.py

# === solve block: critical_velocity.txt ===
# written by generate.py

# === solve block: k_s_vs_velocity.csv ===
# written by generate.py
