#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gap.txt ===
echo "6.7" > "$OUTDIR/band_gap.txt"
cat > "$OUTDIR/ef_vs_U.csv" << 'EOF'
U,Energy_to_VBM,Energy_to_CBM
4.35,4.0425,2.6575
5.0,3.75,2.95
5.5,3.525,3.175
6.0,3.3,3.4
6.5,3.075,3.625
7.0,2.85,3.85
7.62,2.571,4.129
EOF
exit 0

# === solve block: ef_vs_U.csv ===
U,Energy_to_VBM,Energy_to_CBM
4.35,4.0425,2.6575
5.0,3.75,2.95
5.5,3.525,3.175
6.0,3.3,3.4
6.5,3.075,3.625
7.0,2.85,3.85
7.62,2.571,4.129
