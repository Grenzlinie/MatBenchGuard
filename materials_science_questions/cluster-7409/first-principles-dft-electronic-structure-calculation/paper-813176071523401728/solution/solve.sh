#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'FFEOF'
sample,band_gap_eV
pure,3.24
2at%,3.23
5.1at%,3.10
6.2at%,3.05
FFEOF
