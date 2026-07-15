#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: grating_period.txt ===
python3 /solution/compute.py --grating_period > /app/outputs/grating_period.txt

# === solve block: insertion_losses.csv ===
python3 /solution/compute.py --insertion_losses > /app/outputs/insertion_losses.csv
