#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash 
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.csv ===
#!/bin/bash
# Reference band gap values for ATC crystals from paper Figure 7
cat > /app/outputs/band_gaps.csv <<'EOF'
compound,band_gap_eV
5a,2.88
5b,2.94
5c,3.01
5f,2.23
5h,2.78
5j,2.45
5k,2.51
5l,2.66
EOF
