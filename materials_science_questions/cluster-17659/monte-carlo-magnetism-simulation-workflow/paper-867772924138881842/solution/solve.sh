#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: main_loop.csv ===
python3 /solution/compute_magnetization.py main > $OUTDIR/main_loop.csv

# === solve block: return_loop.csv ===
python3 /solution/compute_magnetization.py return > $OUTDIR/return_loop.csv
