#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dft_energies.json ===
cat > /app/outputs/dft_energies.json <<'FFEOF'
{
  "N-C": {
    "total_energies": {
      "clean": 0.0,
      "*COOH": -0.52,
      "*CO": 0.44,
      "*H": -0.337
    },
    "gas_energies": {
      "CO2": 0.414,
      "CO": 0.42,
      "H2": 0.13
    },
    "UL_CO2": -0.6,
    "UL_H2": 0.0,
    "UL_diff": -0.6
  },
  "Ni-N-C": {
    "total_energies": {
      "clean": 0.0,
      "*COOH": -0.12,
      "*CO": -0.06,
      "*H": 0.363
    },
    "gas_energies": {
      "CO2": 0.414,
      "CO": 0.42,
      "H2": 0.13
    },
    "UL_CO2": -0.3,
    "UL_H2": -0.5,
    "UL_diff": 0.2
  }
}
FFEOF
