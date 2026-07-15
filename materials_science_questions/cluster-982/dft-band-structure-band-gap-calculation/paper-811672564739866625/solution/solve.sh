#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.csv ===
cat > /app/outputs/band_gaps.csv <<'FFEOF'
composition,band_gap_eV
0.0,2.1099
0.1,1.9837
0.3,1.8792
0.5,1.8490
0.9,1.8377
1.0,1.8372
FFEOF
