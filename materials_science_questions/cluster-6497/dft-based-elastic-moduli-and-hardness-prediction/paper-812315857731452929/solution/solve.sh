#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.json ===
cat > /app/outputs/computed_properties.json << 'EOF'
{
  "Sc2AlC": {
    "a": 3.280,
    "c_over_a": 4.687,
    "Vo": 17.90,
    "B": 99,
    "Ef": -0.445
  },
  "Sc2GaC": {
    "a": 3.253,
    "c_over_a": 4.861,
    "Vo": 18.12,
    "B": 96,
    "Ef": -0.489
  },
  "Sc2InC": {
    "a": 3.272,
    "c_over_a": 5.028,
    "Vo": 19.06,
    "B": 93,
    "Ef": -0.517
  },
  "Sc2TlC": {
    "a": 3.281,
    "c_over_a": 5.038,
    "Vo": 19.27,
    "B": 90,
    "Ef": -0.466
  },
  "ScC": {
    "B": 154
  }
}
EOF
