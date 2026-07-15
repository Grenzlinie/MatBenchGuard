#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_functions.csv ===
cat > /app/outputs/thermodynamic_functions.csv <<'EOF'
T,Cp,H,S
450,222.8,4.225,9.592
500,225.0,15.42,33.18
550,227.1,26.72,54.72
600,229.0,38.12,74.56
650,230.9,49.62,92.97
700,232.8,61.22,110.2
750,234.6,72.90,126.3
800,236.4,84.68,141.5
850,238.2,96.54,155.9
900,241.0,108.5,169.5
950,241.7,120.5,182.6
1000,243.5,132.7,195.0
EOF
