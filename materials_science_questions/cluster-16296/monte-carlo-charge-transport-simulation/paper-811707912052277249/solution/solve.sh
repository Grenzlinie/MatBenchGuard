#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: scattering_rates_lifetimes.csv ===
cat > /app/outputs/scattering_rates_lifetimes.csv << 'FFEOF'
T_lattice,tau43_inv,tau42_inv,tau4,tau3,fraction_eLO_43
25,0.047,0.12,6.0,0.5,0.7
100,0.45,0.22,1.5,0.5,0.8
200,2.5,0.83,0.3,0.5,0.85
FFEOF

# === solve finalize ===
echo 'Oracle outputs written.'
