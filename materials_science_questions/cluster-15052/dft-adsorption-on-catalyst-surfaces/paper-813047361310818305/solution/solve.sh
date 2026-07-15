#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: pristine_results.json ===
cat << 'EOF' > "$OUTDIR/pristine_results.json"
{
  "pristine_slab": {
    "band_gap_eV": 2.71,
    "total_energy_eV": -1234.56
  },
  "adsorption": [
    {
      "molecule": "H2O",
      "site": "c-v",
      "E_ads_eV": -0.30,
      "delta_Q_e": -0.07,
      "bond_lengths_ang": [0.99, 0.99],
      "bond_angle_deg": 104.17
    },
    {
      "molecule": "H2S",
      "site": "c-h",
      "E_ads_eV": -0.40,
      "delta_Q_e": -0.04,
      "bond_lengths_ang": [1.36, 1.36],
      "bond_angle_deg": 92.38
    },
    {
      "molecule": "CO2",
      "site": "c-h",
      "E_ads_eV": -0.50,
      "delta_Q_e": -0.02,
      "bond_lengths_ang": [1.18, 1.18],
      "bond_angle_deg": 177.43
    }
  ]
}
EOF

# === solve block: doped_results.json ===
python3 /solution/write_outputs.py doped_results.json

# === solve block: field_results.json ===
python3 /solution/write_outputs.py field_results.json
