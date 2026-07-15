#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: contributions.csv ===
cat > /app/outputs/contributions.csv <<'CSVEOF'
contribution,dyn_per_cm2_min,dyn_per_cm2_max,ksi_min,ksi_max
delta_tau_rho,2000000000.0,2600000000.0,29.0,38.0
delta_tau_lambda,1400000000.0,1900000000.0,21.0,27.0
delta_tau_f,-1400000000.0,-1400000000.0,-21.0,-21.0
sum,2000000000.0,3100000000.0,29.0,44.0
tensile_yield_increment,4000000000.0,6200000000.0,58.0,88.0
CSVEOF
