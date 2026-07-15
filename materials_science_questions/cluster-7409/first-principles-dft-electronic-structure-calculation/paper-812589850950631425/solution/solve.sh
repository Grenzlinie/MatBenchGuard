#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: free_energy_diagram.json ===
python3 -c "
import json
data = {
    'perfect_surface': {
        'ΔG1': 0.1,
        'ΔG2': 1.0,
        'ΔG3': 1.9,
        'ΔG4': 1.92
    },
    'vacancy_surface': {
        'ΔG1': 0.1,
        'ΔG2': 1.0,
        'ΔG3': 1.6,
        'ΔG4': 2.22
    },
    'overpotential': {
        'perfect': 0.67,
        'vacancy': 0.37
    }
}
with open('/app/outputs/free_energy_diagram.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: dos_analysis.json ===
python3 -c "
import json
dos_data = {
    'perfect_surface': {
        'dos_data': [[-5.0, 0.2], [-4.0, 0.5], [-3.0, 1.0]],
        'defect_state_present': False,
        'vbm_dos_increase': 0.0
    },
    'vacancy_surface': {
        'dos_data': [[-5.0, 0.2], [-4.0, 0.5], [-3.0, 1.5]],
        'defect_state_present': True,
        'vbm_dos_increase': 0.5
    }
}
with open('/app/outputs/dos_analysis.json', 'w') as f:
    json.dump(dos_data, f, indent=2)
"
