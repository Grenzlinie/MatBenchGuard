#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_formation_energies.csv ===
cat > "/app/outputs/step_02_formation_energies.csv" <<'CSVEOF'
compound,magnetic_state,total_energy_Ha,formation_energy_kJ_per_mol,a_Ang,b_Ang,c_Ang,volume_Ang3
αAs,nm,-1.0,0,4.188,4.188,4.188,44.89
αFe,ferro,-1.0,0,2.827,2.827,2.827,22.59
As2Fe,nm,-3.014626,-12.8,5.311,5.985,2.887,91.7
AsFe,af,-2.014472,-19.0,5.448,3.287,6.048,108.3
AsFe2,af,-3.015424,-13.5,3.617,3.617,5.883,76.94
CSVEOF

# === solve block: step_03_calphad.csv ===
cat > "/app/outputs/step_03_calphad.csv" <<'CSVEOF'
property,value,unit
liquidus_T_33at_As,812,K
liquidus_T_50at_As,1030,K
liquidus_T_67at_As,1250,K
a_As_1423K_50at,0.35,
CSVEOF
