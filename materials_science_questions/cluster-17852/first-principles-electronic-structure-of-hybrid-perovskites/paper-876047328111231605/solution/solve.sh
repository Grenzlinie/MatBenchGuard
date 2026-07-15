#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json

result = {
  "compounds": [
    {
      "name": "(CsMA)NaBiCl6",
      "band_gap_eV": 3.69,
      "gap_type": "indirect",
      "cbm_kpoint": "X",
      "vbm_kpoint": "M",
      "formation_energy_kJ_per_mol": -5126.4
    },
    {
      "name": "(CsMA)NaBiBr6",
      "band_gap_eV": 3.07,
      "gap_type": "indirect",
      "cbm_kpoint": "X",
      "vbm_kpoint": "M",
      "formation_energy_kJ_per_mol": -4955.3
    },
    {
      "name": "(CsMA)NaBiI6",
      "band_gap_eV": 2.36,
      "gap_type": "indirect",
      "cbm_kpoint": "X",
      "vbm_kpoint": "\u0393",
      "formation_energy_kJ_per_mol": -4706.0,
      "dielectric_constant_zero_freq": 3.24,
      "max_refractive_index": 2.50,
      "absorption_coefficient_order": "10^6"
    }
  ]
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF
