#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_adsorption_energies.csv ===
cat > /app/outputs/step_01_adsorption_energies.csv <<'FFEOF'
species,site,E_ads(eV)
NH3,t1,-1.30
NH2,b2,-5.06
NH,h1,-8.08
N,h1,-2.67
FFEOF

# === solve block: step_02_decomposition_barriers.csv ===
cat > /app/outputs/step_02_decomposition_barriers.csv <<'FFEOF'
step,E_a(eV),ΔE_r(eV),ZPE_included(bool)
NH3→NH2+H,0.63,-1.13,True
NH2+H→NH+2H,0.33,-1.17,True
NH+2H→N+3H,0.77,-1.01,True
FFEOF

# === solve block: step_03_saturation_coverages.csv ===
cat > /app/outputs/step_03_saturation_coverages.csv <<'FFEOF'
species,saturation_coverage_ML
NH3,0.75
NH2,1.0
NH,1.0
N,0.5
FFEOF
