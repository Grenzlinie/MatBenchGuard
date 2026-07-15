#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
python3 -c "
import json
data = {
    'adsorption_site_energy_order': ['hcp','fcc','bridge','on-top'],
    'configuration_energy_order': ['III','IV','II','I']
}
with open('/app/outputs/dft_results.json', 'w') as f:
    json.dump(data, f)
"
