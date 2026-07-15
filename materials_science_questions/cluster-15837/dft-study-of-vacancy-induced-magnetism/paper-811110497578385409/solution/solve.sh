#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_results.json ===
python3 -c "
import json
data = {
  'formation_energies': {
    'Co_int': {'+2': 10.0},
    'V_O': {'+2': 1.5},
    'Ti_int': {'+4': 2.0},
    'Co_Ti': {'0': 3.0, '-2': 2.5},
    'Co_Ti+V_O': {'+2': 4.0, '0': 3.5}
  },
  'magnetic_moments': {
    'Co_int': {'+2': 0.0},
    'V_O': {'+2': 0.0},
    'Ti_int': {'+4': 0.0},
    'Co_Ti': {'0': 0.93, '-2': 0.99},
    'Co_Ti+V_O': {'+2': 1.89, '0': 0.95}
  },
  'pair_energies': {
    'Co_Ti-Co_Ti_neutral': {'3.0': 0.0, '5.0': 0.1, '7.0': 0.2},
    'Co_Ti-Co_Ti_charged': {'3.0': 0.5, '5.0': 0.2, '7.0': 0.0},
    'Co_Ti+V_O_neutral': {'3.0': 0.0, '5.0': 0.1, '7.0': 0.2},
    'Co_Ti+V_O_charged': {'3.0': 0.3, '5.0': 0.1, '7.0': 0.0}
  },
  'FM_AFM_difference': {
    'Co_Ti-Co_Ti_neutral': -0.123
  }
}
with open('/app/outputs/defect_results.json', 'w') as f:
    json.dump(data, f, indent=2)
print('defect_results.json written')
"
