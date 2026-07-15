#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_results.json ===
cat > /app/outputs/adsorption_results.json <<'FFEOF'
{
  "Mg_adsorption_energy": -3.20,
  "pristine_C3B_band_gap": 0.66,
  "gas_adsorptions": [
    {"molecule": "NO", "configuration": "N-end", "E_ad": -1.11, "distance": 2.17},
    {"molecule": "NO", "configuration": "O-end", "E_ad": -1.02, "distance": 2.20},
    {"molecule": "N2O", "configuration": "N-end", "E_ad": -1.10, "distance": 2.18},
    {"molecule": "NO2", "configuration": "O-end", "E_ad": -1.62, "distance": 2.15},
    {"molecule": "NO2", "configuration": "N-end", "E_ad": -1.35, "distance": 2.21},
    {"molecule": "NH3", "configuration": "N-end", "E_ad": -1.15, "distance": 2.16}
  ],
  "pristine_gas_adsorptions": [
    {"molecule": "NO", "E_ad": -0.31},
    {"molecule": "N2O", "E_ad": -0.32},
    {"molecule": "NO2", "E_ad": -0.34},
    {"molecule": "NH3", "E_ad": -0.72}
  ]
}
FFEOF
