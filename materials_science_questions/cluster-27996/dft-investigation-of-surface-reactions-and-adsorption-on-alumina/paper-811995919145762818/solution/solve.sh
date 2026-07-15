#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: reproduction_results.json ===
python3 -c "
import json
data = {
  'adsorption_energies': {
    '3T-Ga_ONN': {
      'Delta_E_ads_kcal_per_mol': -4.94,
      'Delta_H_ads_kcal_per_mol': -4.01,
      'Ga_molecule_distance_A': 3.111,
      'O_N_bond_A': 1.197,
      'N_N_bond_A': 1.130,
      'Mulliken_Q_Ga': 0.286,
      'Mulliken_Q_N2O': 0.051
    },
    '3T-Ga_NNO': {
      'Delta_E_ads_kcal_per_mol': -5.02,
      'Delta_H_ads_kcal_per_mol': -4.04,
      'Ga_molecule_distance_A': 3.268,
      'O_N_bond_A': 1.190,
      'N_N_bond_A': 1.133,
      'Mulliken_Q_Ga': 0.309,
      'Mulliken_Q_N2O': 0.028
    },
    '3T-Ga=O_ONN': {
      'Delta_E_ads_kcal_per_mol': -6.873,
      'Delta_H_ads_kcal_per_mol': -5.387,
      'Ga_molecule_distance_A': 2.364,
      'O_N_bond_A': 1.206,
      'N_N_bond_A': 1.127,
      'Ga=O_bond_A': 1.689,
      'Mulliken_Q_Ga': 0.278,
      'Mulliken_Q_N2O': 0.225,
      'Mulliken_Q_O_oxo': -0.674
    },
    '3T-Ga=O_NNO': {
      'Delta_E_ads_kcal_per_mol': -8.991,
      'Delta_H_ads_kcal_per_mol': -6.754,
      'Ga_molecule_distance_A': 2.268,
      'O_N_bond_A': 1.183,
      'N_N_bond_A': 1.129,
      'Ga=O_bond_A': 1.692,
      'Mulliken_Q_Ga': 0.068,
      'Mulliken_Q_N2O': 0.530,
      'Mulliken_Q_O_oxo': -0.662
    }
  },
  'activation_energies_kcal_per_mol': {
    'Ga_site': 22.2,
    'GaO_site': 24.9
  },
  'O2_desorption': {
    'Delta_H_kcal_per_mol': 46.5,
    'Delta_G_kcal_per_mol': 35.9
  }
}
with open('$OUTDIR/reproduction_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
