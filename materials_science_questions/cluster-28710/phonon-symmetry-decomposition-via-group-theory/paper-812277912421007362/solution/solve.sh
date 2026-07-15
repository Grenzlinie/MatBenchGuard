#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: d2h_table.csv ===
python3 /solution/write_tables.py d2h

# === solve block: d2_table.csv ===
python3 /solution/write_tables.py d2
