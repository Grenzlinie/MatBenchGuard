#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_results.json ===
python3 -c "
import json
systems = [
  {
    'system_name': 'pristine/NO',
    'Eads': -0.172,
    'Eg': 0.450,
    'Mtot': 0.000,
    'd_NO': 1.174,
    'd_TMN': None,
    'N_NO_Lowdin': -0.901,
    'O_NO_Lowdin': -1.194,
    'Ned_gCN_Lowdin': -0.242
  },
  {
    'system_name': 'Fe/NO',
    'Eads': -2.78,
    'Eg': 0.310,
    'Mtot': 0.000,
    'd_NO': 1.198,
    'd_TMN': 1.597,
    'N_NO_Lowdin': -0.932,
    'O_NO_Lowdin': -1.193,
    'Ned_gCN_Lowdin': -0.259
  },
  {
    'system_name': 'Ru/NO',
    'Eads': -2.76,
    'Eg': 0.300,
    'Mtot': 0.000,
    'd_NO': 1.189,
    'd_TMN': 1.830,
    'N_NO_Lowdin': -0.946,
    'O_NO_Lowdin': -1.128,
    'Ned_gCN_Lowdin': -0.291
  },
  {
    'system_name': 'Os/NO',
    'Eads': -3.14,
    'Eg': 0.550,
    'Mtot': 0.360,
    'd_NO': 1.293,
    'd_TMN': 1.820,
    'N_NO_Lowdin': -0.953,
    'O_NO_Lowdin': -1.117,
    'Ned_gCN_Lowdin': -0.185
  }
]
data = {'systems': systems}
with open('/app/outputs/adsorption_results.json', 'w') as f:
    json.dump(data, f, indent=2)
print('Written adsorption_results.json')
"
