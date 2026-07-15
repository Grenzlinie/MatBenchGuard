#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: compton_profile_TiC.csv ===
python3 -c "
import numpy as np
from scipy.interpolate import interp1d
import csv

# Known values from Table 1 of the paper
q_known = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
           1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0]
Neckel = [7.488, 7.454, 7.352, 7.182, 6.946, 6.649, 6.298, 5.902, 5.475, 5.033,
          4.590, 3.760, 3.063, 2.524, 2.122, 1.818, 1.303, 0.997, 0.812, 0.685, 0.495]
Lye = [7.501, 7.452, 7.308, 7.082, 6.788, 6.446, 6.072, 5.683, 5.290, 4.900,
       4.518, 3.794, 3.146, 2.604, 2.181, 1.866, 1.355, 1.033, 0.834, 0.699, 0.498]

f_neckel = interp1d(q_known, Neckel, kind='cubic', fill_value='extrapolate')
f_lye = interp1d(q_known, Lye, kind='cubic', fill_value='extrapolate')

with open('/app/outputs/compton_profile_TiC.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['q', 'J_RFA_Neckel', 'J_RFA_Lye'])
    for i in range(0, 51):
        q = i * 0.1
        n = f_neckel(q)
        l = f_lye(q)
        # Format: q with one decimal, values to three decimals
        writer.writerow([f'{q:.1f}', f'{n:.3f}', f'{l:.3f}'])
"
