#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: zt_ordered_400K.csv ===
python3 /solution/generate_zt.py --temp 400 --output /app/outputs/zt_ordered_400K.csv

# === solve block: zt_ordered_temperatures.csv ===
python3 /solution/generate_zt.py --all --output /app/outputs/zt_ordered_temperatures.csv
