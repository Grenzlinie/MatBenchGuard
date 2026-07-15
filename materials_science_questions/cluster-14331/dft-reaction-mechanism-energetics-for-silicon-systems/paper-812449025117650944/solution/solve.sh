#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: energies.json ===
cat > "$OUTDIR/energies.json" << 'FFEOF'
{
  "surface": {
    "ts2a_raw_MP2_energy_hartree": -1238.089687,
    "ts2b_raw_MP2_energy_hartree": -1238.066274,
    "reactants_sum_raw_MP2_energy_hartree": -1238.151873,
    "ts2a_MP2_Ea_kcal_mol_raw": 39.0,
    "ts2b_MP2_Ea_kcal_mol_raw": 53.7,
    "ts2a_MP2_Ea_kcal_mol_with_ZPE": 40.7,
    "ts2b_MP2_Ea_kcal_mol_with_ZPE": 55.4
  },
  "gas_phase": {
    "SiH4_MP2_energy_hartree": -291.338992,
    "SiH3_MP2_energy_hartree": -290.698237,
    "H_MP2_energy_hartree": -0.498232,
    "Si2H6_MP2_energy_hartree": -581.512441,
    "SiH_bond_enthalpy_kcal_mol": 83.4,
    "SiSi_bond_enthalpy_kcal_mol": 68.8
  }
}
FFEOF
