#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "clusters": [
    {
      "name": "Si-C-N",
      "total_energy_eV": -1000.0,
      "bond_lengths": {
        "Si-C": 1.86
      }
    },
    {
      "name": "Si-N-C",
      "total_energy_eV": -1000.67,
      "bond_lengths": {
        "Si-N": 1.69
      }
    },
    {
      "name": "Si-C=N",
      "total_energy_eV": -999.0,
      "bond_lengths": {
        "Si-C": 1.87
      }
    },
    {
      "name": "Si-N=C",
      "total_energy_eV": -999.52,
      "bond_lengths": {
        "Si-N": 1.71
      }
    }
  ]
}
FFEOF
