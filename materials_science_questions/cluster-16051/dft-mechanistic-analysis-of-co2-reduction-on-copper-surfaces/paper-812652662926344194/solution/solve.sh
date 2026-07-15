#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_energies.json ===
python3 <<'PYEOF'
import json
data = {
   "adsorption_energies": [
      {"system": "Cu(111)", "adsorbate": "CO₂*", "site": "Cu", "adsorption_free_energy_eV": 0.73, "activation_angle_deg": 119},
      {"system": "Cu(111)", "adsorbate": "H*", "site": "Cu", "adsorption_free_energy_eV": -0.14},
      {"system": "Cu(111)-O", "adsorbate": "CO₂*", "site": "X", "adsorption_free_energy_eV": 0.55, "activation_angle_deg": 117},
      {"system": "Cu(111)-O", "adsorbate": "H*", "site": "X", "adsorption_free_energy_eV": -0.68},
      {"system": "Cu(111)-O", "adsorbate": "X_adatom", "site": "Cu", "adsorption_free_energy_eV": 1.28},
      {"system": "Cu(111)-S", "adsorbate": "CO₂*", "site": "X", "adsorption_free_energy_eV": 1.47, "activation_angle_deg": 119},
      {"system": "Cu(111)-S", "adsorbate": "H*", "site": "X", "adsorption_free_energy_eV": 0.57},
      {"system": "Cu(111)-S", "adsorbate": "X_adatom", "site": "Cu", "adsorption_free_energy_eV": -0.92},
      {"system": "Cu(111)-Se", "adsorbate": "CO₂*", "site": "X", "adsorption_free_energy_eV": 1.57, "activation_angle_deg": 119},
      {"system": "Cu(111)-Se", "adsorbate": "H*", "site": "X", "adsorption_free_energy_eV": 0.93},
      {"system": "Cu(111)-Se", "adsorbate": "X_adatom", "site": "Cu", "adsorption_free_energy_eV": -1.22},
      {"system": "Cu(111)-Te", "adsorbate": "CO₂*", "site": "X", "adsorption_free_energy_eV": 1.59, "activation_angle_deg": 119},
      {"system": "Cu(111)-Te", "adsorbate": "H*", "site": "X", "adsorption_free_energy_eV": 1.15},
      {"system": "Cu(111)-Te", "adsorbate": "X_adatom", "site": "Cu", "adsorption_free_energy_eV": -1.71}
   ]
}
with open('/app/outputs/adsorption_energies.json','w') as f:
   json.dump(data, f, indent=2)
PYEOF

# === solve block: electronic_properties.json ===
python3 <<'PYEOF'
import json
data = [
   {"system": "Cu(111)-O", "chalcogen": "O", "Bader_charge_X_e": -0.93, "p_band_center_X_eV": -2.50, "d_band_shift_Cu_eV": -0.16},
   {"system": "Cu(111)-S", "chalcogen": "S", "Bader_charge_X_e": -0.59, "p_band_center_X_eV": -1.61, "d_band_shift_Cu_eV": -0.07},
   {"system": "Cu(111)-Se", "chalcogen": "Se", "Bader_charge_X_e": -0.43, "p_band_center_X_eV": -1.28, "d_band_shift_Cu_eV": -0.05},
   {"system": "Cu(111)-Te", "chalcogen": "Te", "Bader_charge_X_e": -0.21, "p_band_center_X_eV": -0.88, "d_band_shift_Cu_eV": -0.07}
]
with open('/app/outputs/electronic_properties.json','w') as f:
   json.dump(data, f, indent=2)
PYEOF
