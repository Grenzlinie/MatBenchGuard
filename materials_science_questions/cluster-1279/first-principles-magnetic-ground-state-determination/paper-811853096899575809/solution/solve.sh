#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetic_results.csv ===
cat > /app/outputs/magnetic_results.csv <<'FFEOF'
system,delta_EFM_meV,M_total_FM,M_total_AFM,M_Fe1_FM,M_Fe2_FM,M_Fe1_AFM,M_Fe2_AFM
b-IFO,84.8,9.82,0.03,3.97,3.91,3.95,-3.90
b-IFO-VO,-12.5,9.13,0.02,3.77,3.77,3.76,-3.77
b-IFCO-i,-7.3,7.97,0.02,3.55,3.52,3.34,-3.55
b-IFCO-VO-i,-90.4,8.66,-0.12,3.71,3.73,3.70,-3.71
FFEOF
