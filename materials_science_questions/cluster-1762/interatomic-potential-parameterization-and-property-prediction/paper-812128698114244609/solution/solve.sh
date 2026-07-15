#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_and_total_energy.json ===
mkdir -p /app/outputs
python3 /solution/write_results.py
