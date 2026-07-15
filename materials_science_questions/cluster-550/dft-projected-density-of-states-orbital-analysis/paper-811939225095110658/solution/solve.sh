#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gaps.csv ===
printf 'compound,gap_Gamma,gap_M\nAgAlO2,1.7,3.3\nAgGaO2,1.2,3.2\nAgInO2,0.6,3.5\n' > "$OUTDIR/band_gaps.csv"
