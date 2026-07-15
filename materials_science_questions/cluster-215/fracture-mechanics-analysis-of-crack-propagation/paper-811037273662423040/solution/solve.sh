#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: predicted_G_IRs.csv ===
cat > /app/outputs/predicted_G_IRs.csv <<'FFEOF'
thread_type,stitch_density,G_IRs_predicted
2-ply Kevlar,4,2.03
2-ply Kevlar,8,2.82
2-ply Kevlar,12,4.10
3-ply Kevlar,4,2.59
4-ply Kevlar,4,2.90
4-ply Kevlar,8,4.54
T900 carbon,4,3.8
T900 carbon,8,6.0
FFEOF
