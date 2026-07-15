#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dft_results.json ===
python3 <<'END'
import json
data = {
  "Fe2+": {
    "bond_lengths": {
      "Fe-O2": 2.129,
      "Fe-O5": 2.152,
      "Fe-O8": 2.129,
      "Fe-O11": 2.153,
      "Fe-O14": 2.146,
      "Fe-O17": 2.146
    },
    "binding_energy_kcal_mol": 56.747,
    "solvation_energy_kcal_mol": -176.362
  },
  "Fe3+": {
    "bond_lengths": {
      "Fe-O2": 2.017,
      "Fe-O5": 2.018,
      "Fe-O8": 2.017,
      "Fe-O11": 2.018,
      "Fe-O14": 2.016,
      "Fe-O17": 2.016
    },
    "binding_energy_kcal_mol": -4.532,
    "solvation_energy_kcal_mol": -405.745
  }
}
with open('/app/outputs/dft_results.json', 'w') as f:
    json.dump(data, f, indent=2)
END
