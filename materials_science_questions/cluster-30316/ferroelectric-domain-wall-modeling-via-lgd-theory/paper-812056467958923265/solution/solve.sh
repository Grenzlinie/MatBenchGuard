#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_equilibrium_stripe_period.csv ===
cat > /app/outputs/step_01_equilibrium_stripe_period.csv <<'FFEOF'
stripe_period_nm
13.2
FFEOF

# === solve block: step_02_transition_temperature.csv ===
cat > /app/outputs/step_02_transition_temperature.csv <<'FFEOF'
Tc_K
963.0
FFEOF
