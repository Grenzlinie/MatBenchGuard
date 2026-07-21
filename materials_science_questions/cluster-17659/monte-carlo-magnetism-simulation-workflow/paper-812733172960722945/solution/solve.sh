#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: pips_trends.csv ===
cat > /app/outputs/pips_trends.csv <<'FFEOF'
FZC_mean,MCS_at_fixed_degree,T_q,condition_id,k,k1_mean
14.0,20000,0.4,k01_T04,0.01,0.25
7.0,2000,0.4,k1_T04,0.1,0.40
10.0,20000,0.3,k01_T03,0.01,0.35
FFEOF
