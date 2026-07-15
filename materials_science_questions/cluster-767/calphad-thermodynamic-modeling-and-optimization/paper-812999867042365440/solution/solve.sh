#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_thermo_calc_results.csv ===
cat > /app/outputs/step_01_thermo_calc_results.csv <<'FFEOF'
compound,mole_fraction_Bi,number_of_Bi_atoms,mixing_heat_J_per_mol,potential_shift_delta_E_V,equilibrium_potential_E_calc_V
Bi2Pd,0.67,2,329250,-0.13,0.12
BiPd,0.5,1,164630,-0.15,0.14
BiPd3,0.25,1,164630,-0.23,0.34
FFEOF
