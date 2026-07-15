#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: final_results.json ===
cat > /app/outputs/final_results.json <<'EOF'
{
  "cluster_2": {
    "physisorbed": {
      "electronic_energy_rel_kcal_mol": -2.02,
      "zpe_corrected_energy_rel_kcal_mol": -0.45
    },
    "transition": {
      "electronic_energy_rel_kcal_mol": 22.87,
      "zpe_corrected_energy_rel_kcal_mol": 21.75
    },
    "chemisorbed": {
      "electronic_energy_rel_kcal_mol": -4.17,
      "zpe_corrected_energy_rel_kcal_mol": 0.77
    },
    "transition_AlH_Angstrom": 1.81,
    "transition_OH_Angstrom": 1.23,
    "chemisorbed_dihedral_O1_O2_Al_Ob_deg": 101.0
  },
  "cluster_3": {
    "physisorbed": {
      "electronic_energy_rel_kcal_mol": -0.87,
      "zpe_corrected_energy_rel_kcal_mol": 0.54
    },
    "transition": {
      "electronic_energy_rel_kcal_mol": 28.27,
      "zpe_corrected_energy_rel_kcal_mol": 29.74
    },
    "chemisorbed": {
      "electronic_energy_rel_kcal_mol": 9.61,
      "zpe_corrected_energy_rel_kcal_mol": 14.22
    }
  },
  "cluster_9": {
    "physisorbed": {
      "electronic_energy_rel_kcal_mol": -1.22,
      "zpe_corrected_energy_rel_kcal_mol": 0.14
    },
    "transition": {
      "electronic_energy_rel_kcal_mol": 35.16,
      "zpe_corrected_energy_rel_kcal_mol": 36.30
    },
    "chemisorbed": {
      "electronic_energy_rel_kcal_mol": 18.14,
      "zpe_corrected_energy_rel_kcal_mol": 22.87
    }
  }
}
EOF
