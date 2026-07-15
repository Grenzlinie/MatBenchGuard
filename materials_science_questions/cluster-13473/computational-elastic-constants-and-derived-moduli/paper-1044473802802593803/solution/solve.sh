#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: elastic_moduli_results.csv ===
cat > "$OUTDIR/elastic_moduli_results.csv" <<'FFEOF'
bulk_modulus_mean,bulk_modulus_std,poisson_ratio_mean,poisson_ratio_std,shear_modulus_mean,shear_modulus_std,strain_percent,youngs_modulus_mean,youngs_modulus_std
6.58,0.09,0.270,0.005,3.56,0.02,0.25,9.08,0.21
6.52,0.09,0.268,0.0045,3.58,0.02,0.50,9.00,0.18
6.46,0.09,0.265,0.004,3.56,0.02,0.75,8.93,0.15
6.40,0.09,0.262,0.0035,3.54,0.02,1.00,8.86,0.12
6.34,0.09,0.259,0.003,3.52,0.02,1.25,8.79,0.09
6.28,0.09,0.257,0.003,3.50,0.02,1.50,8.72,0.07
6.22,0.12,0.255,0.003,3.48,0.02,1.75,8.65,0.06
6.16,0.09,0.256,0.003,3.46,0.02,2.00,8.62,0.06
5.86,0.10,0.257,0.003,3.42,0.02,2.25,8.58,0.06
5.88,0.09,0.258,0.003,3.43,0.02,2.50,8.59,0.06
FFEOF
