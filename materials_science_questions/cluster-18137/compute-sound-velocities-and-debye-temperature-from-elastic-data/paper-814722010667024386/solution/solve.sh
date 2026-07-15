#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json << 'FFEOF'
{
  "BaPb3": {
    "formation_enthalpy": -43.51,
    "bulk_modulus": 40.74,
    "shear_modulus": 21.42,
    "youngs_modulus": 54.68,
    "poissons_ratio": 0.28,
    "debye_temperature": 154.76,
    "bonding_electron_number": 1.99
  },
  "Ba3Pb5": {
    "formation_enthalpy": -57.639,
    "bulk_modulus": 35.83,
    "shear_modulus": 21.57,
    "youngs_modulus": 53.89,
    "poissons_ratio": 0.25,
    "debye_temperature": 160.74,
    "bonding_electron_number": 1.992
  },
  "BaPb": {
    "formation_enthalpy": -74.382,
    "bulk_modulus": 32.32,
    "shear_modulus": 16.52,
    "youngs_modulus": 42.35,
    "poissons_ratio": 0.28,
    "debye_temperature": 147.34,
    "bonding_electron_number": 2.013
  },
  "Ba5Pb3": {
    "formation_enthalpy": -68.584,
    "bulk_modulus": 24.54,
    "shear_modulus": 15.42,
    "youngs_modulus": 38.25,
    "poissons_ratio": 0.24,
    "debye_temperature": 147.22,
    "bonding_electron_number": 2.006
  },
  "Ba2Pb": {
    "formation_enthalpy": -62.857,
    "bulk_modulus": 26.12,
    "shear_modulus": 12.58,
    "youngs_modulus": 32.52,
    "poissons_ratio": 0.29,
    "debye_temperature": 135.38,
    "bonding_electron_number": 1.999
  },
  "Ba2Pb_band_gap": 0.195,
  "stability_order": ["BaPb", "Ba5Pb3", "Ba2Pb", "Ba3Pb5", "BaPb3"]
}
FFEOF
