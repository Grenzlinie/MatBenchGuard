#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimized_parameters.json ===
python3 -c "
import json
data = {
    'AlP': {
        'Delta_H_298': -163150,
        'S_298': 40.34,
        'Cp': {
            'a': 48.53,
            'b': 0.00457,
            'c': -690000
        }
    },
    'liquid': {
        'delta_g_AlP': [-21443, 6.9036],
        'ternary_FeP_Al': {
            'g_FeP_Al_101': [-20920, 5.6484],
            'g_FeP_Al_011': -104600
        }
    }
}
with open('$OUTDIR/optimized_parameters.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: alp_phase_diagram.csv ===
python3 /solution/write_alp_diagram.py "$OUTDIR/alp_phase_diagram.csv"

# === solve block: fealp_isothermal_sections.csv ===
python3 /solution/write_isotherms.py "$OUTDIR/fealp_isothermal_sections.csv"

# === solve block: p_activity_coefficient.csv ===
python3 /solution/write_activity.py "$OUTDIR/p_activity_coefficient.csv"
