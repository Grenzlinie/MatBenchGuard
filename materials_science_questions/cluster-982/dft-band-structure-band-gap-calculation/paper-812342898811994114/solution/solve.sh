#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_02_structural_properties.csv ===
cat > "$OUTDIR/step_02_structural_properties.csv" << 'EOF'
compound,structure,a_eq_angstrom,B0_Mbar,B0_prime
SrS,B1,5.99,0.545,4.43
SrSe,B1,6.234,0.467,4.252
SrTe,B1,6.64,0.392,3.927
SrS,B2,3.59,0.66,3.594
SrSe,B2,3.763,0.483,4.025
SrTe,B2,4.009,0.456,3.64
EOF

# === solve block: step_04_band_gaps.csv ===
cat > "$OUTDIR/step_04_band_gaps.csv" << 'EOF'
compound,indirect_gap_Gamma_X_eV
SrS,2.326
SrSe,2.046
SrTe,1.552
EOF
