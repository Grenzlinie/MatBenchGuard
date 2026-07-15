#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: delta_E.csv ===
cat > /app/outputs/delta_E.csv << 'EOF'
configuration,Li_vacancy_concentration,delta_E_eV
V@(0,1),0,0.31
V@(0,1),6.25,0.15
V@(0,1),12.50,0.05
V@(0,1),18.75,0.02
V@(0,2),0,0.12
V@(0,2),6.25,0.06
V@(0,2),12.50,0.02
V@(0,2),18.75,0.01
V@(0,3),0,0.11
V@(0,3),6.25,0.05
V@(0,3),12.50,0.02
V@(0,3),18.75,0.01
V@(0,4),0,0.09
V@(0,4),6.25,0.04
V@(0,4),12.50,0.01
V@(0,4),18.75,0.00
EOF

# === solve block: magnetic_moments.csv ===
cat > /app/outputs/magnetic_moments.csv << 'EOF'
configuration,Li_vacancy_concentration,V_magnetic_moment_uB
V@(0,1),0,3.20
V@(0,1),6.25,3.10
V@(0,1),12.50,3.00
V@(0,1),18.75,2.90
V@(0,2),0,3.14
V@(0,2),6.25,3.04
V@(0,2),12.50,2.94
V@(0,2),18.75,2.84
V@(0,3),0,3.10
V@(0,3),6.25,3.00
V@(0,3),12.50,2.90
V@(0,3),18.75,2.80
V@(0,4),0,3.18
V@(0,4),6.25,3.08
V@(0,4),12.50,2.98
V@(0,4),18.75,2.88
EOF
