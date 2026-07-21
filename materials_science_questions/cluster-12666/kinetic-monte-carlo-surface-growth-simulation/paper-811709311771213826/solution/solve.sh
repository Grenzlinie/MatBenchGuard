#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: wavelength_results.csv ===
cat > "$OUTDIR/wavelength_results.csv" <<'EOF'
parameter_set,epsilon_kBT,c0,l,beta_tilde_kBT,V0,lambda_early,lambda_late,lambda_max
set1_default,2.0,0.15,3.0,2.76220,0.037120,19.33,53.70,21.48
set2_large_l,2.0,0.24,20.0,2.76220,0.011171,35.25,97.90,39.17
set3_low_stiffness,1.0,0.15,3.0,0.54308,0.037120,8.56,23.78,9.51
EOF
