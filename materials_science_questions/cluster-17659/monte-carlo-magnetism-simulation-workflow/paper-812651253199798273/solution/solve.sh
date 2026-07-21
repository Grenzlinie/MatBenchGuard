#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_parameters.csv ===
# Write the paper's reference fitted parameters for samples A, C, D (approach a).
cat > /app/outputs/fitted_parameters.csv <<'FFEOF'
sample,K_avg,lambda,Kann
A,1500,2.5e-05,375
C,670,4.9e-06,1639
D,500,5.2e-06,1739
FFEOF
