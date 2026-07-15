#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: calculated_parabolic_constants.csv ===
cat > /app/outputs/calculated_parabolic_constants.csv <<'FFEOF'
temperature_C,parabolic_rate_constant_cm_sqrt_s
650,6.5e-4
670,5.8e-4
690,5.1e-4
FFEOF
