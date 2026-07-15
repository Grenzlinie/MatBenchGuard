#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: relative_energies.json ===
python3 -c "
import json
data = {
    'n=4': [
        {'isomer': 'BL4', 'rel_energy': 0.0, 'point_group': 'C3v'},
        {'isomer': 'L4', 'rel_energy': 4.2, 'point_group': 'Cs'},
        {'isomer': 'C4', 'rel_energy': 5.6, 'point_group': 'Cs'}
    ],
    'n=5': [
        {'isomer': 'BL5_1', 'rel_energy': 0.0, 'point_group': 'Td'},
        {'isomer': 'BL5_2', 'rel_energy': 3.7},
        {'isomer': 'BC5_1', 'rel_energy': 5.2},
        {'isomer': 'BC5_2', 'rel_energy': 6.0},
        {'isomer': 'BC5_3', 'rel_energy': 7.1},
        {'isomer': 'L5', 'rel_energy': 8.4},
        {'isomer': 'C5', 'rel_energy': 9.6},
        {'isomer': 'BL5_3', 'rel_energy': 10.0}
    ],
    'n=6': [
        {'isomer': 'BL6_1', 'rel_energy': 0.0, 'point_group': 'Cs'},
        {'isomer': 'BC6_1', 'rel_energy': 0.0, 'point_group': 'Cs'},
        {'isomer': 'BL6_2', 'rel_energy': 3.1},
        {'isomer': 'BC6_2', 'rel_energy': 3.5},
        {'isomer': 'BC6_3', 'rel_energy': 3.6},
        {'isomer': 'BC6_4', 'rel_energy': 4.2},
        {'isomer': 'BC6_5', 'rel_energy': 4.5},
        {'isomer': 'BC6_6', 'rel_energy': 5.0},
        {'isomer': 'BC6_7', 'rel_energy': 5.5},
        {'isomer': 'BC6_8', 'rel_energy': 6.0},
        {'isomer': 'BC6_9', 'rel_energy': 6.5},
        {'isomer': 'DC6_2', 'rel_energy': 5.8},
        {'isomer': 'L6', 'rel_energy': 7.5}
    ],
    'n=7': [
        {'isomer': 'BC7_1', 'rel_energy': 0.0},
        {'isomer': 'BL7_1', 'rel_energy': 0.0},
        {'isomer': 'BC7_2', 'rel_energy': 0.0},
        {'isomer': 'BL7_2', 'rel_energy': 1.4},
        {'isomer': 'BC7_4', 'rel_energy': 2.8},
        {'isomer': 'BC7_5', 'rel_energy': 2.9},
        {'isomer': 'BL7_3', 'rel_energy': 3.1},
        {'isomer': 'BC7_6', 'rel_energy': 3.6},
        {'isomer': 'BC7_7', 'rel_energy': 3.6},
        {'isomer': 'BC7_8', 'rel_energy': 3.7},
        {'isomer': 'BL7_4', 'rel_energy': 4.0},
        {'isomer': 'BC7_10', 'rel_energy': 4.0},
        {'isomer': 'BC7_11', 'rel_energy': 4.3},
        {'isomer': 'BC7_12', 'rel_energy': 4.4},
        {'isomer': 'BL7_6', 'rel_energy': 6.7},
        {'isomer': 'BL7_8', 'rel_energy': 7.0},
        {'isomer': 'L7', 'rel_energy': 8.8},
        {'isomer': 'DC7_1', 'rel_energy': 2.5},
        {'isomer': 'DC7_2', 'rel_energy': 2.7},
        {'isomer': 'TC7_2', 'rel_energy': 3.0}
    ],
    'n=8': [
        {'isomer': 'DC8_1', 'rel_energy': 0.0, 'point_group': 'Cs'},
        {'isomer': 'BC8_1', 'rel_energy': 0.0},
        {'isomer': 'BC8_2', 'rel_energy': 0.0},
        {'isomer': 'BTC8_1', 'rel_energy': 0.0},
        {'isomer': 'BDC8_1', 'rel_energy': 0.0},
        {'isomer': 'BL8_1', 'rel_energy': 0.0},
        {'isomer': 'BC8_3', 'rel_energy': 0.2},
        {'isomer': 'BC8_4', 'rel_energy': 0.0},
        {'isomer': 'BDC8_2', 'rel_energy': 0.0},
        {'isomer': 'BDC8_3', 'rel_energy': 3.1},
        {'isomer': 'DC8_3', 'rel_energy': 3.6},
        {'isomer': 'BC8_6', 'rel_energy': 3.6},
        {'isomer': 'BL8_3', 'rel_energy': 3.7},
        {'isomer': 'BC8_7', 'rel_energy': 3.9},
        {'isomer': 'BC8_5', 'rel_energy': 4.5},
        {'isomer': 'DC8_2', 'rel_energy': 5.0},
        {'isomer': 'TC8_2', 'rel_energy': 5.5},
        {'isomer': 'Ca8', 'rel_energy': 6.2}
    ],
    'n=9': [
        {'isomer': 'TC9_1', 'rel_energy': 0.0, 'point_group': 'Cs'},
        {'isomer': 'BL9_1', 'rel_energy': 0.6},
        {'isomer': 'BL9_3', 'rel_energy': 1.8},
        {'isomer': 'BC9_1', 'rel_energy': 2.3},
        {'isomer': 'DC9_1', 'rel_energy': 3.0},
        {'isomer': 'BCa9', 'rel_energy': 3.5},
        {'isomer': 'L9', 'rel_energy': 4.2}
    ]
}
with open('/app/outputs/relative_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
print('relative_energies.json written')
"

# === solve block: population_n7_n9.json ===
python3 -c "
import json
data = {
    'n=7': {
        '25K': {
            'BC7_1': 0.96,
            'BL7_1': 0.04,
            'BC7_2': 0.00,
            'BL7_2': 0.00,
            'BC7_4': 0.00,
            'BC7_5': 0.00,
            'BL7_3': 0.00,
            'BC7_6': 0.00,
            'BC7_7': 0.00,
            'BC7_8': 0.00,
            'BL7_4': 0.00,
            'BC7_10': 0.00,
            'BC7_11': 0.00,
            'BC7_12': 0.00,
            'BL7_6': 0.00,
            'BL7_8': 0.00,
            'L7': 0.00,
            'DC7_1': 0.00,
            'DC7_2': 0.00,
            'TC7_2': 0.00
        },
        '100K': {
            'BC7_1': 0.45,
            'BL7_1': 0.52,
            'BC7_2': 0.01,
            'BL7_2': 0.01,
            'BC7_4': 0.00,
            'BC7_5': 0.00,
            'BL7_3': 0.00,
            'BC7_6': 0.00,
            'BC7_7': 0.00,
            'BC7_8': 0.00,
            'BL7_4': 0.00,
            'BC7_10': 0.00,
            'BC7_11': 0.00,
            'BC7_12': 0.00,
            'BL7_6': 0.00,
            'BL7_8': 0.00,
            'L7': 0.00,
            'DC7_1': 0.00,
            'DC7_2': 0.00,
            'TC7_2': 0.00
        }
    },
    'n=8': {
        '25K': {
            'BL8_1': 0.30,
            'BC8_3': 0.25,
            'BC8_1': 0.20,
            'DC8_1': 0.15,
            'BC8_2': 0.10,
            'BTC8_1': 0.00,
            'BDC8_1': 0.00,
            'BC8_4': 0.00,
            'BDC8_2': 0.00,
            'BDC8_3': 0.00,
            'DC8_3': 0.00,
            'BC8_6': 0.00,
            'BL8_3': 0.00,
            'BC8_7': 0.00,
            'BC8_5': 0.00,
            'DC8_2': 0.00,
            'TC8_2': 0.00,
            'Ca8': 0.00
        },
        '100K': {
            'BL8_1': 0.90,
            'BC8_3': 0.07,
            'BC8_1': 0.01,
            'DC8_1': 0.01,
            'BC8_2': 0.01,
            'BTC8_1': 0.00,
            'BDC8_1': 0.00,
            'BC8_4': 0.00,
            'BDC8_2': 0.00,
            'BDC8_3': 0.00,
            'DC8_3': 0.00,
            'BC8_6': 0.00,
            'BL8_3': 0.00,
            'BC8_7': 0.00,
            'BC8_5': 0.00,
            'DC8_2': 0.00,
            'TC8_2': 0.00,
            'Ca8': 0.00
        }
    },
    'n=9': {
        '25K': {
            'TC9_1': 0.55,
            'BL9_1': 0.45,
            'BL9_3': 0.00,
            'BC9_1': 0.00,
            'DC9_1': 0.00,
            'BCa9': 0.00,
            'L9': 0.00
        },
        '100K': {
            'BL9_1': 0.96,
            'TC9_1': 0.03,
            'BL9_3': 0.01,
            'BC9_1': 0.00,
            'DC9_1': 0.00,
            'BCa9': 0.00,
            'L9': 0.00
        }
    }
}
with open('/app/outputs/population_n7_n9.json', 'w') as f:
    json.dump(data, f, indent=2)
print('population_n7_n9.json written')
"

# === solve finalize ===
echo "All artifacts written successfully."
