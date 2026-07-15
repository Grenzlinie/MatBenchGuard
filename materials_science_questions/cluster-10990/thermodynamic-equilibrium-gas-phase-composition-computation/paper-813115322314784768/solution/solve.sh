#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: initial_temperatures.csv ===
cat > "$OUTDIR/initial_temperatures.csv" <<'CSVEOF'
Oxide,T_calc_K,T_expt_vacuum_K,T_expt_1atm_Ar_K
FeO,1285,1270,1250
CoO,1195,1100,
NiO,1045,923,973
Cu2O,850,900,800
CSVEOF

# === solve block: activation_energies.csv ===
cat > "$OUTDIR/activation_energies.csv" <<'CSVEOF'
Oxide,Mode,Ea_calculated_kJ_per_mol
FeO,Equimolar,312
FeO,Isobaric,468
NiO,Equimolar,300
Cu2O,Equimolar,202
CSVEOF

# === solve block: equilibrium_pressures.csv ===
cat > "$OUTDIR/equilibrium_pressures.csv" <<'CSVEOF'
Oxide,T_K,P_M_dissociation_atm,P_M_evaporation_atm,P_O2_calculated_condensate_atm,P_O2_experimental_atm
FeO,1700,2.1e-7,4.1e-6,3.44e-10,
CoO,1700,8.0e-7,2.3e-6,4.77e-08,5e-08
NiO,1700,3.1e-6,3.0e-6,1.57e-06,4e-08
Cu2O,1500,1.3e-5,8.1e-6,3.19e-05,
Cu2O,1300,2.1e-7,1.5e-7,1.90e-07,2e-06
CSVEOF
