#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: performance.csv ===
cat > /app/outputs/performance.csv <<'FFEOF'
method,target,d_m
GRNN,r1,16.3
GRNN,r2,11.8
GRNN,fd,8.2
GRNN,a,20.8
GRNN,b,22.8
GRNN,c,23.7
RBF,r1,18.6
RBF,r2,14.4
RBF,fd,7.6
RBF,a,19.6
RBF,b,22.1
RBF,c,25.8
FFEOF
