#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_02_bulk_properties.json ===
python3 -c "
import json
data = [
    {
        'method': 'LDA',
        'a_rhombohedral': 5.10,
        'cos_alpha': 0.568,
        'V0': 83.49,
        'c11': 496,
        'c12': 166,
        'c13': 129,
        'c33': 493,
        'c14': 18,
        'c44': 153
    },
    {
        'method': 'GGA',
        'a_rhombohedral': 5.16,
        'cos_alpha': 0.569,
        'V0': 86.81,
        'c11': 454,
        'c12': 151,
        'c13': 108,
        'c33': 458,
        'c14': 21,
        'c44': 132
    }
]
with open('/app/outputs/step_02_bulk_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_03_sfe_values.json ===
python3 -c "
import json
data = [
    {'fault_id': 'a', 'LDA': 0.42, 'GGA': 0.35, 'shell_Gale_Henson_0K': 0.65, 'shell_Gale_Henson_1800K': 0.52, 'shell_Minervini_0K': 0.69, 'shell_Minervini_1800K': 0.58},
    {'fault_id': 'b', 'LDA': 0.51, 'GGA': 0.41, 'shell_Gale_Henson_0K': None, 'shell_Gale_Henson_1800K': None, 'shell_Minervini_0K': None, 'shell_Minervini_1800K': None},
    {'fault_id': 'c', 'LDA': 0.56, 'GGA': 0.46, 'shell_Gale_Henson_0K': None, 'shell_Gale_Henson_1800K': None, 'shell_Minervini_0K': None, 'shell_Minervini_1800K': None},
    {'fault_id': 'd', 'LDA': 0.80, 'GGA': 0.62, 'shell_Gale_Henson_0K': None, 'shell_Gale_Henson_1800K': None, 'shell_Minervini_0K': None, 'shell_Minervini_1800K': None},
    {'fault_id': 'e', 'LDA': 0.61, 'GGA': 0.50, 'shell_Gale_Henson_0K': None, 'shell_Gale_Henson_1800K': None, 'shell_Minervini_0K': None, 'shell_Minervini_1800K': None}
]
with open('/app/outputs/step_03_sfe_values.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_04_dislocation_spacing.csv ===
python3 -c "
import math

# LDA values from Table I/II/III
c11 = 496e9   # Pa
c12 = 166e9   # Pa
gamma = 0.42  # J/m^2
bp = 0.275e-9 # m

M = (c11**2 - c12**2) / (8.0 * math.pi * c11)

theta_deg = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]

with open('/app/outputs/step_04_dislocation_spacing.csv', 'w') as f:
    f.write('theta_deg,d0_nm\n')
    for deg in theta_deg:
        rad = math.radians(deg)
        x = math.sqrt(3) * gamma / (bp * M * 2.0 * rad)
        alpha = 0.5 - math.atan(x) / math.pi   # ensures 0 < alpha < 0.5
        d = bp / (2.0 * math.sin(rad / 2.0))
        d0 = alpha * d
        d0_nm = d0 / 1e-9
        f.write(f'{deg},{d0_nm:.4f}\n')
"
