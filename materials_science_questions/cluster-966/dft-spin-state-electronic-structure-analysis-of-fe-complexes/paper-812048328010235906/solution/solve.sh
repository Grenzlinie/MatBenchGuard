#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_configurations.json ===
cat <<'EOF' > /app/outputs/adsorption_configurations.json
{
  "1Ads": {
    "Fe_Ha": 2.304,
    "Fe_Hb": 2.243,
    "O_Ha": 3.231,
    "O_Hb": 2.767,
    "H_H": 0.753,
    "Fe_O": 1.670,
    "angle_O_Fe_Ha": 107.77,
    "angle_O_Fe_Hb": 88.76,
    "dihedral_O_Fe_Ha_Hb": 1.92,
    "adsorption_energy_kJ_mol": -17.5,
    "HH_frequency_cm1": 4015.7
  },
  "2Ads": {
    "Fe_Ha": 2.387,
    "Fe_Hb": 2.330,
    "O_Ha": 3.188,
    "O_Hb": 3.225,
    "H_H": 0.751,
    "Fe_O": 1.670,
    "angle_O_Fe_Ha": 102.26,
    "angle_O_Fe_Hb": 106.42,
    "dihedral_O_Fe_Ha_Hb": 105.35,
    "adsorption_energy_kJ_mol": -18.1,
    "HH_frequency_cm1": 4047.2
  },
  "3Ads": {
    "Fe_Ha": 2.382,
    "Fe_Hb": 2.346,
    "O_Ha": 3.095,
    "O_Hb": 3.165,
    "H_H": 0.751,
    "Fe_O": 1.695,
    "angle_O_Fe_Ha": 97.11,
    "angle_O_Fe_Hb": 101.68,
    "dihedral_O_Fe_Ha_Hb": 105.86,
    "adsorption_energy_kJ_mol": -9.9,
    "HH_frequency_cm1": 4052.5
  }
}
EOF
