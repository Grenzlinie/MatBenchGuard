#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: lattice_parameters.json ===
python3 -c "
import json

exp_ceNbo4 = {'a': 7.261, 'b': 11.403, 'c': 5.162, 'beta': 130.53}
exp_ceNbo4_25 = {'a': 14.373, 'b': 22.792, 'c': 11.832, 'beta': 105.07}
calc_ceNbo4 = {'a': 7.690, 'b': 11.171, 'c': 5.438, 'beta': 135.01}
calc_ceNbo4_25 = {'a': 14.977, 'b': 22.462, 'c': 11.954, 'beta': 106.69}

def pct(calc, exp):
    return round((calc - exp) / exp * 100, 2)

out = {
    'CeNbO4': {
        'a': calc_ceNbo4['a'],
        'b': calc_ceNbo4['b'],
        'c': calc_ceNbo4['c'],
        'beta': calc_ceNbo4['beta'],
        'percent_diff_a': pct(calc_ceNbo4['a'], exp_ceNbo4['a']),
        'percent_diff_b': pct(calc_ceNbo4['b'], exp_ceNbo4['b']),
        'percent_diff_c': pct(calc_ceNbo4['c'], exp_ceNbo4['c']),
        'percent_diff_beta': pct(calc_ceNbo4['beta'], exp_ceNbo4['beta'])
    },
    'CeNbO4_25': {
        'a': calc_ceNbo4_25['a'],
        'b': calc_ceNbo4_25['b'],
        'c': calc_ceNbo4_25['c'],
        'beta': calc_ceNbo4_25['beta'],
        'percent_diff_a': pct(calc_ceNbo4_25['a'], exp_ceNbo4_25['a']),
        'percent_diff_b': pct(calc_ceNbo4_25['b'], exp_ceNbo4_25['b']),
        'percent_diff_c': pct(calc_ceNbo4_25['c'], exp_ceNbo4_25['c']),
        'percent_diff_beta': pct(calc_ceNbo4_25['beta'], exp_ceNbo4_25['beta'])
    }
}

with open('/app/outputs/lattice_parameters.json', 'w') as f:
    json.dump(out, f, indent=2)
print('Written lattice_parameters.json')
"
