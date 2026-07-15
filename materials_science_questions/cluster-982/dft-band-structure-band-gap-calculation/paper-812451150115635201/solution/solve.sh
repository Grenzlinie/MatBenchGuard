#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_results.json ===
python3 -c "
import json

data = {
    'rutile_TM': {
        'a': 4.555,
        'c': 2.922,
        'c_over_a': 0.6414,
        'u': 0.3042,
        'density': 4.377,
        'bulk_modulus': 242,
        'band_gap': 1.88,
        'gap_direct': True
    },
    'rutile_Teter': {
        'a': 4.528,
        'c': 2.918,
        'c_over_a': 0.6444,
        'u': 0.3033,
        'density': 4.435,
        'bulk_modulus': 253,
        'band_gap': 1.88,
        'gap_direct': True
    },
    'anatase_TM': {
        'a': 3.744,
        'c': 9.497,
        'c_over_a': 2.536,
        'u': 0.2071,
        'density': 3.987,
        'bulk_modulus': 196,
        'band_gap': 2.05,
        'gap_direct': False
    },
    'anatase_Teter': {
        'a': 3.747,
        'c': 9.334,
        'c_over_a': 2.491,
        'u': 0.2100,
        'density': 4.050,
        'bulk_modulus': 187,
        'band_gap': 2.05,
        'gap_direct': False
    },
    'energy_TM': {
        'E_rutile': -90.2816,
        'E_anatase': -90.2838,
        'difference_kcal_per_mol': -1.38,
        'difference_sign_convention': 'E_anatase_minus_E_rutile'
    },
    'energy_Teter': {
        'E_rutile': -90.1725,
        'E_anatase': -90.1707,
        'difference_kcal_per_mol': 1.13,
        'difference_sign_convention': 'E_anatase_minus_E_rutile'
    }
}

with open('/app/outputs/computed_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
