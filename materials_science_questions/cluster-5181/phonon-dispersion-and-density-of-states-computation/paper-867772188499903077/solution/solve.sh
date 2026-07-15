#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: compound_1_results.json ===
python3 /solution/write_outputs.py 1

# === solve block: compound_2_results.json ===
python3 /solution/write_outputs.py 2

# === solve block: compound_3_results.json ===
python3 /solution/write_outputs.py 3

# === solve block: compound_4_results.json ===
python3 /solution/write_outputs.py 4
