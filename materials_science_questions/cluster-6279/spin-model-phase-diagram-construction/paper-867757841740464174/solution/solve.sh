#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json
data = {
    'first_order_transitions': [
        {'J_over_Jprime': 0.35, 'Tc': 1.2018},
        {'J_over_Jprime': 0.4, 'Tc': 1.2918},
        {'J_over_Jprime': 0.5, 'Tc': 1.4851}
    ],
    'DLRO_transitions': [
        {'J_over_Jprime': 0.8, 'Tc': 2.114, 'nu': 0.608, 'gamma': 1.18},
        {'J_over_Jprime': 1.0, 'Tc': 2.547, 'nu': 0.630, 'gamma': 1.22},
        {'J_over_Jprime': 2.5, 'Tc': 5.835, 'nu': 0.649, 'gamma': 1.30},
        {'J_over_Jprime': 'inf', 'Tc': 2.196, 'nu': 0.669, 'gamma': 1.34}
    ],
    'QLRO_transitions': [
        {'J_over_Jprime': 0, 'Tc': 1.099, 'nu': 0.661, 'gamma': 1.34},
        {'J_over_Jprime': 0.1, 'Tc': 1.104, 'nu': 0.661, 'gamma': 1.34},
        {'J_over_Jprime': 0.2, 'Tc': 1.121, 'nu': 0.663, 'gamma': 1.34},
        {'J_over_Jprime': 0.3, 'Tc': 1.165, 'nu': 0.649, 'gamma': 1.32}
    ]
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
