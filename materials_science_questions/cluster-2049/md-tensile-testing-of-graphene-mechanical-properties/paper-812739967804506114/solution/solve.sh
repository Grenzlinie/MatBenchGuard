#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: interlayer_distances.json ===
python3 /solution/write_interlayer_distances.py > $OUTDIR/interlayer_distances.json
