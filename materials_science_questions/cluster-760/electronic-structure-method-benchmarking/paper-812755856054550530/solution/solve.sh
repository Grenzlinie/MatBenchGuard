#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: raw_energies.json ===
cat > /app/outputs/raw_energies.json <<'EOF'
{
  "CH3OH": {
    "cci_plus_davidson_hartree": -115.54566,
    "zero_point_energy_hartree": 0.05258
  },
  "CH2O-H2": {
    "cci_plus_davidson_hartree": -115.39071,
    "zero_point_energy_hartree": 0.04407
  },
  "CH2O+H2": {
    "cci_plus_davidson_hartree": -115.50189,
    "zero_point_energy_hartree": 0.03768
  },
  "CH2-H2O": {
    "cci_plus_davidson_hartree": -115.40561,
    "zero_point_energy_hartree": 0.04366
  },
  "1CH2+H2O": {
    "cci_plus_davidson_hartree": -115.39040,
    "zero_point_energy_hartree": 0.03884
  },
  "HCOH-H2": {
    "cci_plus_davidson_hartree": -115.39640,
    "zero_point_energy_hartree": 0.04225
  },
  "HCOH+H2": {
    "cci_plus_davidson_hartree": -115.41465,
    "zero_point_energy_hartree": 0.03828
  }
}
EOF
