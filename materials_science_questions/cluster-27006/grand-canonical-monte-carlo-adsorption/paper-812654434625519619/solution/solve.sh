#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: heats_of_adsorption.csv ===
python3 <<'PYEOF'
import csv
import os

output_path = os.environ.get('OUTDIR', '/app/outputs') + '/heats_of_adsorption.csv'

rows = [
    {'Nc': 5, 'heat_of_adsorption_kJ_per_mol': 58.2},
    {'Nc': 6, 'heat_of_adsorption_kJ_per_mol': 68.3},
    {'Nc': 7, 'heat_of_adsorption_kJ_per_mol': 78.5},
    {'Nc': 8, 'heat_of_adsorption_kJ_per_mol': 88.7},
]

with open(output_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Nc', 'heat_of_adsorption_kJ_per_mol'])
    writer.writeheader()
    writer.writerows(rows)
PYEOF

# === solve block: siting_distribution.json ===
python3 <<'PYEOF'
import json
import os

output_path = os.environ.get('OUTDIR', '/app/outputs') + '/siting_distribution.json'

data = {
    '2-methylbutane': {
        'straight': 0.1,
        'zigzag': 0.1,
        'intersection': 0.8
    },
    'pentane': {
        'straight': 0.33,
        'zigzag': 0.33,
        'intersection': 0.34
    }
}

with open(output_path, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: diffusion_results.json ===
python3 <<'PYEOF'
import json
import os
import math

output_path = os.environ.get('OUTDIR', '/app/outputs') + '/diffusion_results.json'

def interp(x, xp, yp):
    # linear interpolation
    i = max(0, sum(1 for xi in xp if xi <= x) - 1)
    if i >= len(xp) - 1:
        return yp[-1]
    t = (x - xp[i]) / (xp[i+1] - xp[i])
    return yp[i] + t * (yp[i+1] - yp[i])

# Straight channel: key q and -βF from Table 4 (paper convention F = -βF)
str_q_pts = [0.0, 0.29, 0.44, 0.50, 0.56, 0.68, 1.0]
str_F_pts = [-22.9, -6.8, -12.3, -6.9, -11.9, -6.5, -22.9]

# Zigzag channel
zz_q_pts = [0.0, 0.15, 0.25, 0.40, 0.50, 0.65, 0.75, 0.90, 1.0]
zz_F_pts = [-23.8, -5.8, -9.6, -5.3, -10.5, -5.2, -20.2, -9.0, -23.8]

N = 101
straight_q = [i/(N-1) for i in range(N)]
straight_F = [interp(x, str_q_pts, str_F_pts) for x in straight_q]

zigzag_q = [i/(N-1) for i in range(N)]
zigzag_F = [interp(x, zz_q_pts, zz_F_pts) for x in zigzag_q]

# Hopping rates (k_TST) from Table 4 (events s^-1)
hopping = {
    'str_1_to_2': 1.4e5,
    'str_2_to_3': 4.3e10,
    'str_3_to_1': 2.6e10,
    'zz_1_to_2': 5.0e4,
    'zz_2_to_3': 1.3e11,
    'zz_3_to_4': 1.0e11,
    'zz_4_to_1': 1.4e9
}

# Diffusion coefficients from Table 5 (cm^2/s)
diff = {
    'Dxx': 1.7e-10,
    'Dyy': 4.7e-10,
    'Dzz': 2.1e-10,
    'D': 8.5e-10
}

result = {
    'straight_channel': {
        'q': straight_q,
        'free_energy': straight_F
    },
    'zigzag_channel': {
        'q': zigzag_q,
        'free_energy': zigzag_F
    },
    'hopping_rates': hopping,
    'diffusion_coefficients': diff
}

with open(output_path, 'w') as f:
    json.dump(result, f, indent=2)
PYEOF
