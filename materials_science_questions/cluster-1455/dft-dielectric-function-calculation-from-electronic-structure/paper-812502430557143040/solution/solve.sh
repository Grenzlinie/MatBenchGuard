#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimized_lattice.csv ===
cat > "$OUTDIR/optimized_lattice.csv" <<'EOF'
compound,a,b,c,V
Sr3GaAs3,12.706,19.175,6.484,1579.7
Ba3GaAs3,13.3195,19.9121,6.7800,1798.2
EOF

# === solve block: elastic_constants.csv ===
cat > "$OUTDIR/elastic_constants.csv" <<'EOF'
compound,C11,C12,C13,C22,C23,C33,C44,C55,C66
Sr3GaAs3,93.3,22.1,27.2,82.8,26.9,81.5,28.8,28.4,26.5
Ba3GaAs3,84.4,16.8,22.4,79.7,22.9,76.4,20.5,23.4,20.6
EOF

# === solve block: electronic_and_optical.csv ===
cat > "$OUTDIR/electronic_and_optical.csv" <<'EOF'
compound,bandgap,me_100,me_010,me_001,mh_100,mh_010,mh_001,epsilon1_100,epsilon1_010,epsilon1_001
Sr3GaAs3,1.271,0.39,0.45,2.05,1.61,0.19,2.24,8.33,8.64,7.98
Ba3GaAs3,1.285,0.43,1.05,9.98,1.73,0.70,3.13,8.66,9.17,8.32
EOF
