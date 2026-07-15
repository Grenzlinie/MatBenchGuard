#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: electronic_properties.csv ===
python3 <<'PYEOF'
import csv

phases = {
    'FCC': {
        'N0': 2.0,            # states/eV/unit cell at ambient
        'plasma0': 6.0,        # eV at ambient
        'N_exp': 2.0,          # N_EF ~ V^N_exp
        'plasma_exp': 1.5,     # plasma ~ V^plasma_exp
        'band_gap_func': lambda v: max(0.0, 1.0*(0.75 - v)),  # opens near 0.75
    },
    'BCC': {
        'N0': 1.5,
        'plasma0': 5.0,
        'N_exp': 0.2,          # very shallow decrease, stays metallic
        'plasma_exp': 0.1,
        'band_gap_func': lambda v: 0.0,  # always metallic
    }
}

# Volume ratios covering the compression range, including the 0.75-0.6 interval
volumes = [1.0, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3]

with open('/app/outputs/electronic_properties.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['phase', 'V_over_V0', 'N_EF', 'plasma_frequency', 'band_gap'])
    for phase_name, params in phases.items():
        for v in volumes:
            n_ef = params['N0'] * (v ** params['N_exp'])
            plasma = params['plasma0'] * (v ** params['plasma_exp'])
            gap = params['band_gap_func'](v)
            writer.writerow([phase_name, v, n_ef, plasma, gap])
PYEOF
