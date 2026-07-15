#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: electrostatic_contributions.json ===
python3 -c "
import json
data = {
    'fcc': {'A_l': 0.2115, '2B_l': 0.9479},
    'bcc': {'A_l': 0.1994, '2B_l': 0.7423}
}
with open('/app/outputs/electrostatic_contributions.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: exchange_contributions.json ===
python3 -c "
import json
data = [
  {'metal': 'Li', 'A_I': -0.060, '2B_I': 0.342},
  {'metal': 'Na', 'A_I': -0.037, '2B_I': 0.238},
  {'metal': 'K',  'A_I': -0.0103, '2B_I': 0.092},
  {'metal': 'Cu', 'A_I': 4.528, '2B_I': 6.316}
]
with open('/app/outputs/exchange_contributions.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: total_elastic_constants.json ===
python3 -c "
import json
data = [
  {'metal': 'Li', 'A': 0.279, '2B': 1.605, 'c11': 1.49, 'c12': 1.21},
  {'metal': 'Na', 'A': 0.106, '2B': 0.770, 'c11': 0.92, 'c12': 0.81},
  {'metal': 'K',  'A': 0.0541, '2B': 0.332, 'c11': 0.44, 'c12': 0.38},
  {'metal': 'Cu', 'A': 5.1, '2B': 8.9, 'c11': 17.5, 'c12': 12.4}
]
with open('/app/outputs/total_elastic_constants.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: debye_temperatures.json ===
python3 -c "
import json
data = [
  {'metal': 'Li', 'Theta': 339},
  {'metal': 'Na', 'Theta': 135},
  {'metal': 'K',  'Theta': 90}
]
with open('/app/outputs/debye_temperatures.json', 'w') as f:
    json.dump(data, f)
"
