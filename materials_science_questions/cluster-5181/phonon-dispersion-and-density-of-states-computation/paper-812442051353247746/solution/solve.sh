#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
# install nothing extra, python3 and stdlib are sufficient

# === solve block: born_effective_charges.json ===
python3 -c "
import json
data = {
    'Ti_principal': [6.678, 6.678, 5.713],
    'O_principal': [-1.161, -5.517, -2.856]
}
with open('/app/outputs/born_effective_charges.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: phonon_frequencies.json ===
python3 -c "
import json
modes = {
    'Eg(1)': 145.6,
    'Eg(2)': 171.1,
    'B1g(1)': 398.4,
    'B1g(2)': 518.4,
    'A1g': 535.9,
    'Eg(3)': 662.1,
    'Eu(1)_TO': 248.6,
    'Eu(1)_LO': 340.6,
    'A2u(1)_TO': 375.3,
    'A2u(1)_LO': 743.1,
    'Eu(2)_TO': 479.9,
    'Eu(2)_LO': 892.2,
    'B2u': 564.6
}
with open('/app/outputs/phonon_frequencies.json', 'w') as f:
    json.dump(modes, f, indent=2)
"

# === solve block: dielectric_tensors.json ===
python3 -c "
import json
data = {
    'electronic_xx_noscissor': 7.07,
    'electronic_zz_noscissor': 6.21,
    'electronic_xx_scissor': 6.00,
    'electronic_zz_scissor': 5.39,
    'static_xx': 45.9,
    'static_zz': 24.4
}
with open('/app/outputs/dielectric_tensors.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve finalize ===
echo "All outputs written."
