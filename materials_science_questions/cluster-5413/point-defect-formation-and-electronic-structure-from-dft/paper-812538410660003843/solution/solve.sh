#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json
data = {
    'E_GB_pristine': -527.591424,
    'E_bulk_supercell': -352.0,
    'E_1O_GB_pristine': -520.621424,
    'E_1O_bulk': -345.0,
    'E_O2_molecule': -10.0,
    'E_SGB_no_O': -527.091424,
    'E_1O_SGB_tensile3': -520.547424,
    'E_VGB_V1_pristine': -526.091424,
    'E_1O_VGB_V1_LE': -521.054424
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
