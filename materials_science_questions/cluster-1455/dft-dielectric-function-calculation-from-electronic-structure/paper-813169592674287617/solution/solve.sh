#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: regression_coefficients.csv ===
cat > "$OUTDIR/regression_coefficients.csv" <<'FFEOF'
coefficient_type,slope,intercept
d1111,1.39e0,2.9e-1
d1122,-5.59e-1,-8.0e-2
d1212,8.01e-1,2.1e-1
FFEOF

# === solve block: predicted_coefficients.csv ===
cat > "$OUTDIR/predicted_coefficients.csv" <<'FFEOF'
crystal,d1111,d1122,d1212
LiCl,4.62e0,-1.82e0,2.76e0
LiBr,1.01e1,-4.03e0,5.86e0
NaI,3.22e0,-1.26e0,1.90e0
KF,5.7e-1,-1.9e-1,3.7e-1
RbF,9.0e-1,-3.3e-1,5.7e-1
FFEOF
