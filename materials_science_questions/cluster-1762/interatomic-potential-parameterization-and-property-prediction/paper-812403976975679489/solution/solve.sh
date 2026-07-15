#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: rgs_properties.json ===
python3 /solution/compute_rgs.py > "$OUTDIR/rgs_properties.json"
