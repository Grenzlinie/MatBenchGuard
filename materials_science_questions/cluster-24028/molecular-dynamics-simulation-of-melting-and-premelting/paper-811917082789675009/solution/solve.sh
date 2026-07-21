#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p $OUTDIR
# Oracle writes synthetic artifacts directly, no network, no heavy compute.

# === solve block: spatial_distribution.csv ===
python3 /solution/gen.py spatial > $OUTDIR/spatial_distribution.csv

# === solve block: size_distribution.csv ===
python3 /solution/gen.py size > $OUTDIR/size_distribution.csv

# === solve block: order_parameters.csv ===
python3 /solution/gen.py order > $OUTDIR/order_parameters.csv

# === solve block: melting_curve.csv ===
python3 /solution/gen.py melting > $OUTDIR/melting_curve.csv
