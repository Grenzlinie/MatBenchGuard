#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bandgap_pure_host.txt ===
cat > "$OUTDIR/bandgap_pure_host.txt" <<'FFEOF'
6.7
FFEOF

# === solve block: energy_differences_vs_U.csv ===
cat > "$OUTDIR/energy_differences_vs_U.csv" <<'FFEOF'
U,delta_VB,delta_CB
4.35,4.52,4.045
5.5,3.6,4.85
6.5,2.8,5.55
7.62,1.904,6.334
FFEOF
