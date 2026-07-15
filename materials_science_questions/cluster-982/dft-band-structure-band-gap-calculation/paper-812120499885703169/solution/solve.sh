#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gap.txt ===
cat > "$OUTDIR/band_gap.txt" <<'FFEOF'
Band gap = 4.65 eV
Type: Indirect
VBM at Gamma and CBM at D
FFEOF

# === solve block: epsilon_im.csv ===
# Generate epsilon_im.csv with a peak at 7.3 eV
python3 /solution/gen_epsilon.py "$OUTDIR"
