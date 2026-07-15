#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: model_results.json ===
python3 -c "
import json
result = {
    'x_0_73': {
        'core': {'p0': 0.15, 'p_leq1': 0.49},
        'surface': {'p0': 0.39, 'p_leq1': 0.82}
    },
    'x_0_65': {
        'core': {'p0': 0.075, 'p_leq1': 0.32},
        'surface': {'p0': 0.27, 'p_leq1': 0.72}
    },
    'overall_inverted_fraction': {
        'x_0_73': 0.21,
        'x_0_65': 0.12375
    },
    'overall_canted_fraction': {
        'x_0_73': 0.5725,
        'x_0_65': 0.42
    },
    'reduction_if_20_percent_inverted': 0.6
}
with open('/app/outputs/model_results.json', 'w') as f:
    json.dump(result, f, indent=2)
"
