#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_properties.json ===
python3 << 'PYEOF'
import json
data = {
    "lattice_constant": 4.48,
    "band_gap": 6.15,
    "C11": 105.49,
    "C12": 19.75,
    "C44": 17.29,
    "B_H": 48.33,
    "G_H": 25.12,
    "E_H": 64.22,
    "Debye_temperature": 431,
    "E_100": 99.26,
    "E_110": 53.47,
    "E_111": 46.34
}
with open('/app/outputs/computed_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
print('computed_properties.json written')
PYEOF
