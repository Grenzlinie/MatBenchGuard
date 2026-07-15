#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR="/app/outputs"

# === solve block: step_01_geometry.csv ===
cat > "${OUTDIR}/step_01_geometry.csv" <<'CSVEOF'
label,unit,value
r(C-O1),Å,1.187
r(C-O2,3),Å,1.346
r(O2-O3),Å,1.657
angle(O2CO3),deg,76
CSVEOF

# === solve block: step_02_formation_energy.csv ===
cat > "${OUTDIR}/step_02_formation_energy.csv" <<'CSVEOF'
reaction,delta_E_eV
CO2+O1D->CO3,2.83
CO3+CO->2CO2,7.12
CSVEOF

# === solve block: step_03_excited_states.csv ===
cat > "${OUTDIR}/step_03_excited_states.csv" <<'CSVEOF'
state,delta_E_eV,f_L,f_v,dominant_excitation
B1(x),2.47,0.00,0.00,1a1-5b2
A1(z),4.96,0.00,0.00,4b2-5b2
A2,6.14,–,–,2b1-5b2
B2(y),7.45,0.22,0.20,8a1-5b2
A2,7.85,–,–,4b2-3b1
CSVEOF
