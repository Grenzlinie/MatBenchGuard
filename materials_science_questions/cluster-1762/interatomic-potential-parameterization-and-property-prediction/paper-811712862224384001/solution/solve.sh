#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predicted_properties.json ===
cat > "/app/outputs/predicted_properties.json" <<'FFEOF'
{
  "AlH2_fluorite_formation_eV_per_atom": 0.393,
  "AlH3_trigonal_formation_eV_per_atom": 0.375,
  "AlH_rocksalt_formation_eV_per_atom": 0.392,
  "AlH_zincblende_formation_eV_per_atom": 0.310,
  "H2_bond_length_angstrom": 0.742,
  "H2_cohesive_eV_per_atom": -2.373,
  "H_Oh_solution_eV": 0.824,
  "H_Oh_vacancy_formation_eV": 1.363,
  "H_Td_solution_eV": 0.693,
  "H_Td_vacancy_formation_eV": 1.320,
  "H_bcc_bond_length_angstrom": 1.643,
  "H_bcc_cohesive_eV_per_atom": -1.867,
  "H_fcc_bond_length_angstrom": 1.686,
  "H_fcc_cohesive_eV_per_atom": -1.861,
  "H_hcp_bond_length_angstrom": 1.686,
  "H_hcp_cohesive_eV_per_atom": -1.861,
  "H_migration_barrier_eV": 0.189,
  "H_sc_bond_length_angstrom": 1.600,
  "H_sc_cohesive_eV_per_atom": -1.876
}
FFEOF
