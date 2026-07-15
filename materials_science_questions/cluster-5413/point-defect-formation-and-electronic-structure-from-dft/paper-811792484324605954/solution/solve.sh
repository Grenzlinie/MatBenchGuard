#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_00_isolated_energies.json ===
python3 -c "
import json
with open('$OUTDIR/step_00_isolated_energies.json', 'w') as f:
    json.dump({
        'lattice_energy_CeO2': -105.65,
        'lattice_energy_NiO': -41.99,
        'defect_energies': {
            'VO': 15.40,
            'NiCe': 53.27,
            'Ni_i': -22.14,
            'Gd_Ce': 32.19
        }
    }, f, indent=2)
    f.write('\n')
"

# === solve block: step_01_binding_energies.json ===
python3 -c "
import json
with open('$OUTDIR/step_01_binding_energies.json', 'w') as f:
    json.dump({
        'reaction_energies': {
            'vacancy_compensation': 5.00,
            'interstitial_route': 9.46
        },
        'clusters': [
            {'label': 'Ni_VO_1st_neighbour', 'delta_E': 1.45},
            {'label': 'Ni_VO_2nd_neighbour', 'delta_E': 1.24},
            {'label': 'Ni_VO_3rd_neighbour', 'delta_E': 0.95},
            {'label': '2Ni_2VO_110_div2_most_stable', 'delta_E': 4.15},
            {'label': 'Gd_2Gd_VO_x', 'delta_E': 0.78},
            {'label': 'Gd_4Gd_2VO_x', 'delta_E': 1.42}
        ]
    }, f, indent=2)
    f.write('\n')
"

# === solve block: step_02_comparison_table.json ===
python3 -c "
import json
with open('$OUTDIR/step_02_comparison_table.json', 'w') as f:
    json.dump({
        'Ni_clusters': [
            {'n_vacancies': 1, 'delta_E': 1.45, 'delta_E_per_vac': 1.45},
            {'n_vacancies': 2, 'delta_E': 4.15, 'delta_E_per_vac': 2.08}
        ],
        'Gd_clusters': [
            {'n_vacancies': 1, 'delta_E': 0.78, 'delta_E_per_vac': 0.78},
            {'n_vacancies': 2, 'delta_E': 1.42, 'delta_E_per_vac': 0.71}
        ],
        'increase_Ni': {'delta_E': 2.70, 'delta_E_per_vac': 0.63},
        'increase_Gd': {'delta_E': 0.64, 'delta_E_per_vac': -0.07}
    }, f, indent=2)
    f.write('\n')
"
