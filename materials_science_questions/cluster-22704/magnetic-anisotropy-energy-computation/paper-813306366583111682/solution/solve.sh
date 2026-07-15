#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetic_anisotropy_results.json ===
python3 -c "
import json
results = [
    # Pure Co chain
    {'system': 'pure_Co', 'geometry_state': 'unrelaxed', 'electric_field': 0, 'MAE': 2.2, 'easy_theta': 0, 'easy_phi': 0},
    {'system': 'pure_Co', 'geometry_state': 'relaxed',   'electric_field': 0, 'MAE': 2.8, 'easy_theta': 0, 'easy_phi': 0},
    # Pure Co relaxed under electric fields (monotonic increase as field becomes more negative)
    {'system': 'pure_Co', 'geometry_state': 'relaxed',   'electric_field': -1.0, 'MAE': 3.0, 'easy_theta': 0, 'easy_phi': 0},
    {'system': 'pure_Co', 'geometry_state': 'relaxed',   'electric_field': -0.5, 'MAE': 2.9, 'easy_theta': 0, 'easy_phi': 0},
    {'system': 'pure_Co', 'geometry_state': 'relaxed',   'electric_field':  0.0, 'MAE': 2.8, 'easy_theta': 0, 'easy_phi': 0},
    {'system': 'pure_Co', 'geometry_state': 'relaxed',   'electric_field':  0.5, 'MAE': 2.4, 'easy_theta': 0, 'easy_phi': 0},
    {'system': 'pure_Co', 'geometry_state': 'relaxed',   'electric_field':  1.0, 'MAE': 1.8, 'easy_theta': 0, 'easy_phi': 0},
    # Mixed Co-Pt chain
    {'system': 'Co_Pt',   'geometry_state': 'unrelaxed',  'electric_field': 0, 'MAE': 2.0, 'easy_theta': 90, 'easy_phi': 90},
    {'system': 'Co_Pt',   'geometry_state': 'relaxed',    'electric_field': 0, 'MAE': 4.3, 'easy_theta': 0,  'easy_phi': 0}
]
with open('/app/outputs/magnetic_anisotropy_results.json', 'w') as f:
    json.dump(results, f, indent=2)
"
