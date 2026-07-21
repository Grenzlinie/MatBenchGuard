#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: contact_angle_results.csv ===
cat > "/app/outputs/contact_angle_results.csv" <<'FFEOF'
cavity_density_rhocav_sigma3,contact_angle_degrees,normalized_lambda_over_rB,period_lambda_sigma
0.05,68,0.1,2
0.1,78,0.2,4
0.2,72,0.35,6
0.3,65,0.5,8
0.4,62,0.7,10
0.5,68,0.9,12
FFEOF
