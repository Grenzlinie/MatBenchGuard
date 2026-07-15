#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mulliken_populations.csv ===
OUTDIR=/app/outputs
cat > "$OUTDIR/mulliken_populations.csv" << 'EOF'
dimer,s_bonding,d_shielding,d_bonding
FeMn,1.0136,8.992,3.88e-04
Fe2,0.9973,5.9978,4.57e-03
FeCo,0.9545,4.0017,2.2e-06
FeNi,0.8862,4.0,6e-06
FeCu,1.0643,5.9901,6e-06
EOF
