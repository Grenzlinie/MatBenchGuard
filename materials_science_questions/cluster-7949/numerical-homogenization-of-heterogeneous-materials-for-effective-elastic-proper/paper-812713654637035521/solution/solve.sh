#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: youngs_modulus_vs_hydration.csv ===
sed -i 's/from scipy\.special import arccosh/from numpy import arccosh/' /solution/helper.py
sed -i 's/omegacp/omega_cp/g' /solution/helper.py
sed -i 's/omegah/omega_h/g' /solution/helper.py
python3 -c "
with open('/solution/helper.py','r') as f: d=f.read()
with open('/solution/helper.py','w') as f:
    f.write('ka = 135 / (3 * (1 - 2 * 0.3))\nmua = 135 / (2 * (1 + 0.3))\nkh = 25.3 / (3 * (1 - 2 * 0.29))\nmuh = 25.3 / (2 * (1 + 0.29))\n' + d)
"
python3 /solution/helper.py youngs $OUTDIR/youngs_modulus_vs_hydration.csv

# === solve block: diffusivity_vs_wc_mature.csv ===
python3 /solution/helper.py diffusivity /app/outputs/diffusivity_vs_wc_mature.csv
