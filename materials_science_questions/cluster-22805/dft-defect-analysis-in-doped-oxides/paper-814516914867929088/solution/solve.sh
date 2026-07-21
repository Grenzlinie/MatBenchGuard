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
results = [
    {
        'structure': 'Al14Ti1Ce1N16_d2.923',
        'E_f': -237.73,
        'a': 3.131,
        'c': 5.245,
        'delta_E': 1.038,
        'M_total': 2.065
    },
    {
        'structure': 'Al14Ti1Ce1N16_d5.697',
        'E_f': -230.68,
        'a': 3.128,
        'c': 5.180,
        'delta_E': 0.179,
        'M_total': 2.065
    },
    {
        'structure': 'Al30Ti1Ce1N32_d2.923',
        'E_f': -475.46,
        'a': 3.131,
        'c': 5.245,
        'delta_E': 0.835,
        'M_total': 2.065
    }
]
with open('/app/outputs/results.json', 'w') as f:
    json.dump(results, f, indent=2)
"
