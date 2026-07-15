#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.json ===
python3 <<'PYEOF'
import json
data = [
  {"system": "pure", "phase": "R", "total_energy": -696.736, "formation_helmholtz": -232.160, "formation_O_rich": None, "formation_V_rich": None},
  {"system": "pure", "phase": "M1", "total_energy": -701.388, "formation_helmholtz": -236.812, "formation_O_rich": None, "formation_V_rich": None},
  {"system": "P@O", "phase": "R", "total_energy": -693.583, "formation_helmholtz": -228.159, "formation_O_rich": 4.001, "formation_V_rich": 0.301},
  {"system": "P@O", "phase": "M1", "total_energy": -695.955, "formation_helmholtz": -230.531, "formation_O_rich": 6.281, "formation_V_rich": 2.581},
  {"system": "P@V", "phase": "R", "total_energy": -696.792, "formation_helmholtz": -232.455, "formation_O_rich": -7.695, "formation_V_rich": -0.296},
  {"system": "P@V", "phase": "M1", "total_energy": -699.645, "formation_helmholtz": -235.308, "formation_O_rich": -5.895, "formation_V_rich": 1.504},
  {"system": "P@i", "phase": "R", "total_energy": -703.259, "formation_helmholtz": -233.358, "formation_O_rich": -1.199, "formation_V_rich": -1.199},
  {"system": "P@i", "phase": "M1", "total_energy": -705.671, "formation_helmholtz": -235.770, "formation_O_rich": 1.042, "formation_V_rich": 1.042},
  {"system": "As@O", "phase": "R", "total_energy": -692.497, "formation_helmholtz": -227.782, "formation_O_rich": 4.378, "formation_V_rich": 0.678},
  {"system": "As@O", "phase": "M1", "total_energy": -694.926, "formation_helmholtz": -230.211, "formation_O_rich": 6.601, "formation_V_rich": 2.901},
  {"system": "As@V", "phase": "R", "total_energy": -693.536, "formation_helmholtz": -229.908, "formation_O_rich": -5.148, "formation_V_rich": 2.251},
  {"system": "As@V", "phase": "M1", "total_energy": -696.886, "formation_helmholtz": -233.258, "formation_O_rich": -3.846, "formation_V_rich": 3.553},
  {"system": "As@i", "phase": "R", "total_energy": -699.146, "formation_helmholtz": -229.954, "formation_O_rich": 2.206, "formation_V_rich": 2.206},
  {"system": "As@i", "phase": "M1", "total_energy": -702.065, "formation_helmholtz": -232.873, "formation_O_rich": 3.939, "formation_V_rich": 3.939},
  {"system": "Bi@O", "phase": "R", "total_energy": -692.782, "formation_helmholtz": -228.826, "formation_O_rich": 3.334, "formation_V_rich": -0.366},
  {"system": "Bi@O", "phase": "M1", "total_energy": -693.090, "formation_helmholtz": -229.134, "formation_O_rich": 7.677, "formation_V_rich": 3.977},
  {"system": "Bi@V", "phase": "R", "total_energy": -693.161, "formation_helmholtz": -230.292, "formation_O_rich": -5.531, "formation_V_rich": 1.868},
  {"system": "Bi@V", "phase": "M1", "total_energy": -695.336, "formation_helmholtz": -232.467, "formation_O_rich": -3.055, "formation_V_rich": 4.344},
  {"system": "Bi@i", "phase": "R", "total_energy": -697.626, "formation_helmholtz": -229.193, "formation_O_rich": 2.966, "formation_V_rich": 2.966},
  {"system": "Bi@i", "phase": "M1", "total_energy": -698.787, "formation_helmholtz": -230.354, "formation_O_rich": 6.458, "formation_V_rich": 6.458}
]
with open('/app/outputs/formation_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: properties.json ===
python3 <<'PYEOF'
import json
data = [
  {"system": "pure", "Eg2": 0.631, "Tc": 340},
  {"system": "P@O", "Eg2": 0.531, "Tc": 173.4},
  {"system": "P@V", "Eg2": 0.459, "Tc": 223.3},
  {"system": "P@i", "Eg2": 0.483, "Tc": 176.3},
  {"system": "As@O", "Eg2": 0.426, "Tc": 177.5},
  {"system": "As@V", "Eg2": 0.43, "Tc": 244.8},
  {"system": "As@i", "Eg2": 0.478, "Tc": 213.3},
  {"system": "Bi@O", "Eg2": 0.297, "Tc": 22.6},
  {"system": "Bi@V", "Eg2": 0.299, "Tc": 159.0},
  {"system": "Bi@i", "Eg2": 0.3, "Tc": 84.8}
]
with open('/app/outputs/properties.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
