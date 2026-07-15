#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ce_spectrum_N1.csv ===
python3 /solution/helper.py 1 "$OUTDIR/ce_spectrum_N1.csv"

# === solve block: ce_spectrum_N2.csv ===
python3 /solution/helper.py 2 "$OUTDIR/ce_spectrum_N2.csv"

# === solve finalize ===
# final consistency – nothing to do
