#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: barriers.csv ===
cat > '/app/outputs/barriers.csv' <<'EOF'
energy_type,energy_value,molecule,step
adsorption,1.00,styrene,adsorption
barrier,0.65,styrene,r1_Habstraction
barrier,0.51,styrene,r2_Habstraction
barrier,0.71,styrene,r3_Habstraction
barrier,1.17,styrene,r2_OHabstraction
EOF
