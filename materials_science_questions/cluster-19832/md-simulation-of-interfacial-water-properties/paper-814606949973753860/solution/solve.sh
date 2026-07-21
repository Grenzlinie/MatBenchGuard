#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: water_dynamics.csv ===
cat > "$OUTDIR/water_dynamics.csv" <<'FFEOF'
model,D,tau1_inv,tau2_inv,mu_z
bulk,0.32,0.30,0.64,0.0
cylinder,0.16,0.10,0.22,0.0
FFEOF
