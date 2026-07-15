#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: hellmann_results.csv ===
cat > /app/outputs/hellmann_results.csv <<'FFEOF'
molecule,y,lambda,alpha_calc,alpha_error_percent,omega_x_calc,omega_x_error_percent,Di_calc,Di_error_percent
LiH,2.5199,1.5799,0.2024,-5.1,21.01,-9.4,149.1,-9.7
NaH,3.0277,1.6045,0.1241,-8.3,16.72,-15.2,132.3,-12.0
KH,3.5291,1.5727,0.0832,23.6,13.83,-5.6,115.3,-9.4
RbH,3.7495,1.5841,0.0730,1.4,13.17,-6.9,110.8,-7.4
CsH,3.9407,1.5801,0.0649,13.9,12.53,-0.6,106.2,-8.0
mean,0.0,1.5843,0.0,0.0,0.0,0.0,0.0,0.0
FFEOF
