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
    'terminations': [
        {
            'termination': 'Cr',
            'lattice_constant': 'a_ZB',
            'minority_gap_ev': 2.0,
            'exchange_splitting_ev': 3.5,
            'half_metallic': True,
            'magnetic_moments': [
                {'atom': 'Cr', 'layer': 'S', 'moment_mu_B': 3.57},
                {'atom': 'P', 'layer': 'S-1', 'moment_mu_B': -0.24},
                {'atom': 'Cr', 'layer': 'center', 'moment_mu_B': 3.22},
                {'atom': 'P', 'layer': 'center', 'moment_mu_B': -0.22}
            ]
        },
        {
            'termination': 'Cr',
            'lattice_constant': 'a_InP',
            'minority_gap_ev': 2.0,
            'exchange_splitting_ev': 3.5,
            'half_metallic': True,
            'magnetic_moments': [
                {'atom': 'Cr', 'layer': 'S', 'moment_mu_B': 3.68},
                {'atom': 'P', 'layer': 'S-1', 'moment_mu_B': -0.33},
                {'atom': 'Cr', 'layer': 'center', 'moment_mu_B': 3.35},
                {'atom': 'P', 'layer': 'center', 'moment_mu_B': -0.35}
            ]
        },
        {
            'termination': 'P',
            'lattice_constant': 'a_ZB',
            'minority_gap_ev': 0.0,
            'exchange_splitting_ev': 3.5,
            'half_metallic': False,
            'magnetic_moments': [
                {'atom': 'P', 'layer': 'S', 'moment_mu_B': -0.55},
                {'atom': 'Cr', 'layer': 'S-1', 'moment_mu_B': 2.30},
                {'atom': 'P', 'layer': 'center', 'moment_mu_B': -0.22},
                {'atom': 'Cr', 'layer': 'center', 'moment_mu_B': 3.22}
            ]
        },
        {
            'termination': 'P',
            'lattice_constant': 'a_InP',
            'minority_gap_ev': 0.0,
            'exchange_splitting_ev': 3.5,
            'half_metallic': False,
            'magnetic_moments': [
                {'atom': 'P', 'layer': 'S', 'moment_mu_B': -0.76},
                {'atom': 'Cr', 'layer': 'S-1', 'moment_mu_B': 2.73},
                {'atom': 'P', 'layer': 'center', 'moment_mu_B': -0.35},
                {'atom': 'Cr', 'layer': 'center', 'moment_mu_B': 3.35}
            ]
        }
    ]
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
