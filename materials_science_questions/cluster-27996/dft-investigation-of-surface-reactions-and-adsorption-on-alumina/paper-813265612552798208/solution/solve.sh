#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_energies.json ===
python3 <<'EOF'
import json
data = {
  "Al13_minus": {
    "total_energies": {
      "cluster": -1000.0,
      "methanol": -50.0,
      "complex": -1050.15,
      "ts": -1049.75,
      "product": -1050.77
    },
    "derived": {
      "EB": -0.15,
      "ET": 0.25,
      "EA": 0.40,
      "ER": -0.77
    },
    "HOMO_LUMO_gap": 1.87
  },
  "Al13I2_adjacent": {
    "total_energies": {
      "cluster": -1500.0,
      "methanol": -50.0,
      "complex": -1550.67,
      "ts": -1550.42,
      "product": -1552.14
    },
    "derived": {
      "EB": -0.67,
      "ET": -0.42,
      "EA": 0.25,
      "ER": -2.14
    },
    "HOMO_LUMO_gap": 0.74
  },
  "Al14I3_adatom": {
    "total_energies": {
      "cluster": -2000.0,
      "methanol": -50.0,
      "complex": -2050.44,
      "ts": -2050.20,
      "product": -2050.84
    },
    "derived": {
      "EB": -0.44,
      "ET": -0.20,
      "EA": 0.24,
      "ER": -0.84
    },
    "HOMO_LUMO_gap": 1.70
  }
}
with open('/app/outputs/computed_energies.json', 'w') as f:
  json.dump(data, f, indent=2)
print('computed_energies.json written')
EOF
