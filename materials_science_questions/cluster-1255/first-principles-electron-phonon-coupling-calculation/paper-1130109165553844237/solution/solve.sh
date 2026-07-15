#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.csv ===
cat > /app/outputs/results.csv <<'FFEOF'
parameter,value,unit
Eu_mode_frequency,0.6,THz
beta_over_a,632,1/Ang
v_F,1000000,m/s
eta_H,1.899e-11,kg/(m·s)
mu_ph,2.85,Bohr_magneton
omega_plus,0.620,THz
omega_minus,0.580,THz
tau,0.1,ps
B,1,T
FFEOF
