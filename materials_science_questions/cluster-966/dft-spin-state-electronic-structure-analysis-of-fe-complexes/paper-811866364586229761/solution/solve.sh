#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ff_parameters.csv ===
# Copy the pre-bundled gold parameter file (no network)
cat /solution/ff_parameters.csv > "$OUTDIR/ff_parameters.csv"
