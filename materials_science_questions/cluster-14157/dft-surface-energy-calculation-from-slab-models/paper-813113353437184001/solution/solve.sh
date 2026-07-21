#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.csv ===
cat > /app/outputs/formation_energies.csv <<'FFEOF'
metal,coverage_ML,delta_E_f_eV_per_Sn
Ru,0.25,0.15
Ru,0.5,0.05
Ru,0.75,-0.05
Ni,0.25,-0.15
Ni,0.5,-0.35
Ni,0.75,-0.55
Pt,0.25,-0.55
Pt,0.5,-0.85
Pt,0.75,-1.15
FFEOF

# === solve block: segregation_energies.csv ===
cat > /app/outputs/segregation_energies.csv <<'FFEOF'
metal,coverage_ML,delta_E_seg_eV_per_Sn
Ru,0.25,-2.5
Ru,0.5,-2.5
Ru,0.75,-2.5
Ni,0.25,-1.6
Ni,0.5,-1.6
Ni,0.75,-1.6
Pt,0.25,-0.8
Pt,0.5,-0.8
Pt,0.75,-0.8
FFEOF
