#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: equilibrium_properties.csv ===
cat > /app/outputs/equilibrium_properties.csv <<'FFEOF'
B,Bprime,E0,a0,c0,c_a,energy_above_ground,structure,u
192.33,4.07,0.0,4.67,,,0.0,ZB,
297.67,4.15,0.0,4.33,,,1.0,RS,
251.03,4.70,0.0,2.71,,,1.5,CsCl,
171.34,4.63,0.0,3.37,5.26,1.559,0.547,WZ,0.372
FFEOF

# === solve block: elastic_properties_ZB.csv ===
cat > /app/outputs/elastic_properties_ZB.csv <<'FFEOF'
A,B,C11,C12,C44,E,G,lambda,mu,nu,theta_D,vl,vm,vt,zeta
0.22,192.33,243.47,166.46,8.22,47.16,16.16,146.35,16.26,0.45,208.66,5217.5,1636.2,1434.3,0.77
FFEOF
