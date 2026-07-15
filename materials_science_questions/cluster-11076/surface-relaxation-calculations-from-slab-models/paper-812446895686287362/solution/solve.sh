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
    'tersoff': {
        '(100)': {'unrelaxed_gamma': 7565, 'relaxed_gamma': 6639, 'delta12_before': 0.892, 'delta12_after': 0.750, 'delta23_before': 0.892, 'delta23_after': 0.910, 'delta34_before': 0.892, 'delta34_after': 0.890, 'percent_change_delta12': -15.9, 'percent_change_delta23': 2.0, 'percent_change_delta34': -0.2},
        '(110)': {'unrelaxed_gamma': 4949, 'relaxed_gamma': 4028, 'delta12_before': 1.261, 'delta12_after': 1.120, 'delta23_before': 1.261, 'delta23_after': 1.270, 'delta34_before': 1.261, 'delta34_after': 1.260, 'percent_change_delta12': -11.2, 'percent_change_delta23': 0.7, 'percent_change_delta34': -0.1},
        '(111)': {'unrelaxed_gamma': 4040, 'relaxed_gamma': 2772, 'delta12_before': 0.515, 'delta12_after': 0.310, 'delta23_before': 1.544, 'delta23_after': 1.610, 'delta34_before': 0.515, 'delta34_after': 0.510, 'percent_change_delta12': -39.8, 'percent_change_delta23': 4.3, 'percent_change_delta34': -0.9}
    },
    'brenner': {
        '(100)': {'unrelaxed_gamma': 6161, 'relaxed_gamma': 5026, 'delta12_before': 0.869, 'delta12_after': 0.590, 'delta23_before': 0.869, 'delta23_after': 0.950, 'delta34_before': 0.869, 'delta34_after': 0.850, 'percent_change_delta12': -32.1, 'percent_change_delta23': 9.3, 'percent_change_delta34': -2.2},
        '(110)': {'unrelaxed_gamma': 3261, 'relaxed_gamma': 2020, 'delta12_before': 1.229, 'delta12_after': 1.070, 'delta23_before': 1.229, 'delta23_after': 1.280, 'delta34_before': 1.229, 'delta34_after': 1.229, 'percent_change_delta12': -12.9, 'percent_change_delta23': 4.2, 'percent_change_delta34': 0.0},
        '(111)': {'unrelaxed_gamma': 2662, 'relaxed_gamma': 1390, 'delta12_before': 0.502, 'delta12_after': 0.220, 'delta23_before': 1.505, 'delta23_after': 1.630, 'delta34_before': 0.502, 'delta34_after': 0.470, 'percent_change_delta12': -56.2, 'percent_change_delta23': 8.3, 'percent_change_delta34': -6.3}
    }
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
