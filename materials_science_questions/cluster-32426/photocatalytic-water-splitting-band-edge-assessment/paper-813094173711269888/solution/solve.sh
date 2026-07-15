#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.csv ===
cat > /app/outputs/formation_energies.csv <<'EOF'
system,formation_energy_eV
C@Zn,-1.38
Si@Zn,-1.28
Ge@Zn,-1.20
Sn@Zn,-0.52
Pb@Zn,-0.52
EOF

# === solve block: band_gaps.csv ===
cat > /app/outputs/band_gaps.csv <<'EOF'
system,band_gap_eV
pristine,3.57
C@Zn,2.25
Si@Zn,1.70
Ge@Zn,2.22
Sn@Zn,1.99
Pb@Zn,2.59
EOF

# === solve block: absorption_coefficient.csv ===
cat > /app/outputs/absorption_coefficient.csv <<'EOF'
system,energy_eV,absorption_cm1
pristine,2.0,500
pristine,2.5,2000
pristine,3.0,8000
C@Zn,2.0,50000
C@Zn,2.5,100000
C@Zn,3.0,150000
Si@Zn,2.0,60000
Si@Zn,2.5,120000
Si@Zn,3.0,180000
Ge@Zn,2.0,40000
Ge@Zn,2.5,80000
Ge@Zn,3.0,120000
Sn@Zn,2.0,45000
Sn@Zn,2.5,90000
Sn@Zn,3.0,135000
Pb@Zn,2.0,30000
Pb@Zn,2.5,60000
Pb@Zn,3.0,100000
EOF

# === solve block: band_edges.csv ===
cat > /app/outputs/band_edges.csv <<'EOF'
system,VBM_vacuum,CBM_vacuum,VBM_NHE,CBM_NHE
pristine,-7.05,-3.48,2.61,-0.96
C@Zn,-6.39,-4.20,1.95,-0.24
Si@Zn,-6.12,-4.42,1.68,-0.02
Ge@Zn,-6.37,-4.15,1.93,-0.29
Sn@Zn,-6.26,-4.27,1.82,-0.17
Pb@Zn,-6.55,-3.96,2.11,-0.48
EOF
