#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: psi_values_b3lyp.json ===
python3 -c "
import json
# Paper-reported butterfly bending angles (deg) at B3LYP/6-31G(d)
data = {
    '5': 18.5,
    '6': 17.5,
    '7': 0.0,
    '8': 6.5,
    '9': 0.0,
    '10': 19.8,
    '11': 22.4
}
with open('/app/outputs/psi_values_b3lyp.json', 'w') as f:
    json.dump(data, f)
    f.write('\n')
print('psi_values_b3lyp.json written successfully')
"

# === solve block: psi_values_mp2.json ===
python3 -c "
import json
data = {
    '5': 22.7,
    '6': 22.4,
    '10': 24.0,
    '11': 28.4
}
with open('$OUTDIR/psi_values_mp2.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: hydrogenation_heat_9.json ===
python3 -c "
import json
data = {'first_hydrogenation_heat': 49.0}
with open('$OUTDIR/hydrogenation_heat_9.json', 'w') as f:
    json.dump(data, f)
"
