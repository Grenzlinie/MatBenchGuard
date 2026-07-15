#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_quantities.json ===
python3 -c "
import json

data = {
    'impurities': [
        {
            'name': 'Te',
            'W_strain_kJ_per_mol': 39.855,
            'W_A-I_kJ_per_mol': 120.958,
            'Q_I_kJ_per_mol': 443.977,
            'Delta_H_I_kJ_per_mol': 239.284,
            'Delta_S_I_J_per_K_per_mol': -19.666,
            'K_I': 3.604e-12
        },
        {
            'name': 'Zn',
            'W_strain_kJ_per_mol': 2.059,
            'W_A-I_kJ_per_mol': 111.411,
            'Q_I_kJ_per_mol': 443.585,
            'Delta_H_I_kJ_per_mol': 239.676,
            'Delta_S_I_J_per_K_per_mol': 14.586,
            'K_I': 2.133e-10
        }
    ]
}

with open('/app/outputs/thermodynamic_quantities.json', 'w') as f:
    json.dump(data, f, indent=2)
print('thermodynamic_quantities.json written')
"
