#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: bulk_properties.json ===
cat > "$OUTDIR/bulk_properties.json" << 'EOF'
{
  "lattice_constants": {
    "a": 3.993,
    "b": 7.810,
    "c": 7.589,
    "volume": 236.66
  },
  "co_magnetic_moments": [
    {"label": "Co1_octa", "moment_muB": 3.015},
    {"label": "Co2_octa", "moment_muB": -3.015},
    {"label": "Co1_pyr", "moment_muB": -2.908},
    {"label": "Co2_pyr", "moment_muB": 2.908}
  ],
  "co_bader_charges": [
    {"label": "Co1_octa", "charge_e": 1.456},
    {"label": "Co2_octa", "charge_e": 1.456},
    {"label": "Co1_pyr", "charge_e": 1.388},
    {"label": "Co2_pyr", "charge_e": 1.391}
  ],
  "band_gap_GGA+U": 0.9
}
EOF

# === solve block: vacancy_formation_energies.csv ===
python3 /solution/write_outputs.py --file vacancy_formation_energies.csv

# === solve block: perfect_adsorption_properties.csv ===
python3 /solution/write_outputs.py --file perfect_adsorption_properties.csv

# === solve block: defective_adsorption_properties.csv ===
python3 /solution/write_outputs.py --file defective_adsorption_properties.csv
