#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "
import json
data = {
    'J_values': {
        'LiCrS2': 7.03,
        'LiCrSe2': 8.11,
        'LiCrTe2': 9.91,
        'NaCrS2': 7.50,
        'NaCrSe2': 7.81,
        'NaCrTe2': 8.52
    },
    'Tc_Ising': {
        'LiCrS2': 640,
        'LiCrSe2': 820,
        'LiCrTe2': 880,
        'NaCrS2': 690,
        'NaCrSe2': 760,
        'NaCrTe2': 780
    },
    'Tc_Heisenberg': {
        'LiCrS2': 209,
        'LiCrSe2': 237,
        'LiCrTe2': 285,
        'NaCrS2': 217,
        'NaCrSe2': 226,
        'NaCrTe2': 234
    },
    'band_gaps': {
        'LiCrSe2': {'without_SOC': 2.21, 'with_SOC': 2.02},
        'NaCrSe2': {'without_SOC': 0.91, 'with_SOC': 0.77},
        'NaCrTe2': {'without_SOC': 0.83, 'with_SOC': 0.59}
    },
    'hole_mobilities': {
        'NaCrS2': {'x': 1100.0, 'y': 1200.0},
        'NaCrSe2': {'x': 1132.5, 'y': 1239.2},
        'NaCrTe2': {'x': 2166.5, 'y': 3071.6}
    }
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
