#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: lattice_properties.csv ===
cat > /app/outputs/lattice_properties.csv <<'FFEOF'
quantity,unit,value
U_POT,kJ·mol⁻¹,428.95
V_plus,nm³,0.3394
r_plus,nm,0.4327
FFEOF

# === solve block: combustion_enthalpy.csv ===
cat > /app/outputs/combustion_enthalpy.csv <<'FFEOF'
quantity,unit,value
Delta_cU_J_per_g,J·g⁻¹,-27676.06
Delta_cU_kJ_per_mol,kJ·mol⁻¹,-7369.03
Delta_cH_kJ_per_mol,kJ·mol⁻¹,-7384.52
FFEOF

# === solve block: formation_enthalpy.csv ===
cat > /app/outputs/formation_enthalpy.csv <<'FFEOF'
quantity,unit,value
Delta_fH_kJ_per_mol,kJ·mol⁻¹,-1317.86
FFEOF
