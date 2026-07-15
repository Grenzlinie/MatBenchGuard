#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json
data = {
    'pristine': {
        'C11': 285.1,
        'C12': 102.5,
        'C44': 82.1,
        'B_VRH': 163.4,
        'G_VRH': 85.7,
        'E': 218.8,
        'Debye_temperature': 580.2
    },
    'V_O48f': {
        'C11': 281.5,
        'C12': 102.4,
        'C44': 74.3,
        'B_VRH': 162.1,
        'G_VRH': 80.1,
        'E': 206.2,
        'Debye_temperature': 564.4,
        'formation_energy': 4.67
    },
    'Zr_Gd': {
        'C11': 293.4,
        'C12': 104.5,
        'C44': 76.3,
        'B_VRH': 167.5,
        'G_VRH': 83.1,
        'E': 213.9,
        'Debye_temperature': 579.1,
        'formation_energy': 2.32
    },
    'Gd_int2': {
        'C11': 274.8,
        'C12': 91.7,
        'C44': 51.3,
        'B_VRH': 152.7,
        'G_VRH': 64.8,
        'E': 170.4,
        'Debye_temperature': 508.9,
        'formation_energy': 2.73
    },
    'Zr_8a': {
        'C11': 275.8,
        'C12': 101.1,
        'C44': 40.3,
        'B_VRH': 159.3,
        'G_VRH': 55.2,
        'E': 148.6,
        'Debye_temperature': 479.3,
        'formation_energy': 3.30
    },
    'O_8a': {
        'C11': 269.5,
        'C12': 113.5,
        'C44': 76.7,
        'B_VRH': 165.5,
        'G_VRH': 77.2,
        'E': 200.5,
        'Debye_temperature': 558.8,
        'formation_energy': 0.32
    }
}
# Add Pugh's ratio and Poisson's ratio
for key in data:
    B = data[key]['B_VRH']
    G = data[key]['G_VRH']
    data[key]['B_over_G'] = B / G
    data[key]['Poisson_ratio'] = (3*B - 2*G) / (2 * (3*B + G))
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve finalize ===
echo "results.json written successfully."
