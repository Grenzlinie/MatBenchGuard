#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: relative_energies_and_band_gaps.csv ===
cat > "$OUTDIR/relative_energies_and_band_gaps.csv" << 'EOF'
method,structure,relative_energy_eV,band_gap_classification
LDA/DZP,a,0.62,0.35
LDA/DZP,b,0.0,Metal
LDA/DZP,c,0.39,0.20
LDA/DZP,d,0.98,Semimetal
VDW-DF/DZP,a,0.30,0.30
VDW-DF/DZP,b,0.0,Metal
VDW-DF/DZP,c,0.52,0.20
VDW-DF/DZP,d,0.61,Semimetal
EOF
