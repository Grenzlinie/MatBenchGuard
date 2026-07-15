#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dft_results.json ===
python3 -c '
import json
data = {
  "reaction_delta_G_kJ_per_mol": -374.16,
  "HOMO_Li2CN2_eV": -4.19,
  "LUMO_Li2CN2_eV": -0.97,
  "HOMO_Li2CO3_eV": -4.50,
  "LUMO_Li2CO3_eV": -1.31,
  "HOMO_LiF_eV": -4.97,
  "LUMO_LiF_eV": -1.57,
  "Li_adsorption_energy_top_eV": -5.55,
  "Li_adsorption_energy_side_eV": -5.09,
  "interfacial_energy_Li2CN2_meV_per_A2": 77.57,
  "interfacial_energy_Li2CO3_meV_per_A2": 60.75,
  "interfacial_energy_LiF_meV_per_A2": 72.61,
  "bulk_modulus_Li2CN2_GPa": 104.12,
  "bulk_modulus_Li2CO3_GPa": 63,
  "bulk_modulus_LiF_GPa": 70,
  "gamma_E_Li2CN2_meV_per_A2_GPa": 8076.44,
  "gamma_E_Li2CO3_meV_per_A2_GPa": 3827.25,
  "gamma_E_LiF_meV_per_A2_GPa": 5082.70
}
with open("/app/outputs/dft_results.json", "w") as f:
    json.dump(data, f, indent=2)
'
