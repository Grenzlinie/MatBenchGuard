#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR
# Ensure any necessary packages (none needed; the oracle just copies a static file)

# === solve block: predictions.csv ===
cp /solution/predictions_template.csv $OUTDIR/predictions.csv
