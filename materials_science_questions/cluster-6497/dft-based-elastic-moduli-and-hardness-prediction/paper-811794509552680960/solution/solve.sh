#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_01_structural.csv ===
cat > "$OUTDIR/step_01_structural.csv" <<'FFEOF'
phase,a,c,u,c_a,B,B_prime,E_coh
ZB,4.67,,,,192.33,4.07,8.89
RS,4.33,,,,297.67,4.15,11.90
CsCl,2.71,,,,251.03,4.70,12.25
WZ,3.37,5.26,0.372,1.559,171.34,4.63,11.43
FFEOF

# === solve block: step_02_elastic.csv ===
cat > "$OUTDIR/step_02_elastic.csv" <<'FFEOF'
C11,C12,C44,G,E,nu,A,zeta,lambda,mu,vl,vt,vm,theta_D
243.47,166.46,8.22,16.16,47.16,0.45,0.22,0.77,146.35,16.26,5217.5,1434.3,1636.2,208.66
FFEOF
