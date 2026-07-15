#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: chi0_over_chi_vs_Gamma.csv ===
cat > /app/outputs/chi0_over_chi_vs_Gamma.csv <<'FFEOF'
Gamma,chi0_over_chi
2.0,0.92
5.0,0.82
7.0,0.72
8.0,0.62
10.0,0.35
12.0,0.10
14.0,0.02
FFEOF
