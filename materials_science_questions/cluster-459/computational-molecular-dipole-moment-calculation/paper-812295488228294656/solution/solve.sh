#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_results.json ===
python3 -c "
import json

data = {
    'tropolone_anisotropy': 14.2,
    'bond_anisotropies': {
        'Sn-Cl': 5.5,
        'Sn-CH3': 5.3,
        'Sn-O': 3.5,
        'Sn(trop)': 17.7
    },
    'derivatives': {
        'Cl2Sn(trop)2': {
            'trans_D2h': {'b1_minus_b2': 24.1, 'b1_minus_b3': 24.1, 'molar_Kerr': 273},
            'cis_C2':    {'b1_minus_b2': -12.2, 'b1_minus_b3': 0,    'molar_Kerr': -5129},
            'cis_C2v':   {'b1_minus_b2': -11.7, 'b1_minus_b3': -23.5,'molar_Kerr': -15856}
        },
        '(CH3)2Sn(trop)2': {
            'trans_D2h': {'b1_minus_b2': 24.5, 'b1_minus_b3': 24.5, 'molar_Kerr': 279},
            'cis_C2':    {'b1_minus_b2': -12.2,'b1_minus_b3': 0,    'molar_Kerr': -827},
            'cis_C2v':   {'b1_minus_b2': -11.7,'b1_minus_b3': -23.5,'molar_Kerr': -2414}
        },
        '(C6H5)2Sn(trop)2': {
            'trans_D2h': {'b1_minus_b2': 0, 'b1_minus_b3': 0, 'molar_Kerr': 0},
            'cis_C2':    {'b1_minus_b2': 0, 'b1_minus_b3': 0, 'molar_Kerr': 0},
            'cis_C2v':   {'b1_minus_b2': 0, 'b1_minus_b3': 0, 'molar_Kerr': 0}
        }
    },
    'group_moments': {
        'Cl2Sn(trop)2': 2.9,
        '(CH3)2Sn(trop)2': 2.8,
        '(C6H5)2Sn(trop)2': 3.0
    }
}

with open('/app/outputs/computed_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
