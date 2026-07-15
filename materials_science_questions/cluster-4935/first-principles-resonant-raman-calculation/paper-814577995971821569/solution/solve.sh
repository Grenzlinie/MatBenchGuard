#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: table_II_efficiencies.csv ===
cat > "${OUTDIR}/table_II_efficiencies.csv" <<'FFEOF'
polarization,bare,screened,unscreened,unscreened_normalized
yy,6.9,1.1,5.8,1.0
x+y,x+y,4.0,0.64,3.4,0.59
xx,3.9,0.31,3.6,0.62
x+y,x-y,3.0,0.05,2.9,0.50
xy,1.6,0.0,1.6,0.27
FFEOF

# === solve block: table_III_mass_fluctuations.csv ===
cat > "${OUTDIR}/table_III_mass_fluctuations.csv" <<'FFEOF'
polarization,sheet,bare,screened
yy,chain,0.79,0.62
yy,antibonding_plane,0.88,0.29
yy,bonding_plane,0.06,0
yy,apical_oxygen,0.,0.07
yy,total,1.82,0.28
x+y,x+y,chain,0.25,0.15
x+y,x+y,antibonding_plane,0.47,0.25
x+y,x+y,bonding_plane,0.20,0.01
x+y,x+y,apical_oxygen,0.14,0.05
x+y,x+y,total,1.06,0.17
xx,chain,0.02,0
xx,antibonding_plane,0.66,0.23
xx,bonding_plane,0.29,0.05
xx,apical_oxygen,0.06,0.04
xx,total,1.03,0.08
x+y,x-y,chain,0.20,0.16
x+y,x-y,antibonding_plane,0.46,0
x+y,x-y,bonding_plane,0.10,0.01
x+y,x-y,apical_oxygen,0.02,0
x+y,x-y,total,0.78,0.01
xy,chain,0.05,0
xy,antibonding_plane,0.16,0
xy,bonding_plane,0.13,0
xy,apical_oxygen,0.08,0
xy,total,0.42,0
FFEOF

# === solve finalize ===
echo "All outputs written."
