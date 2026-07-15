#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: focal_domain_energies.json ===
python3 -c "
import numpy as np
from scipy.special import ellipk
import json
K1=1.0; a=1.0; e=0.5; r_c=0.01; f_val=1.0; R=2.0
K_e2 = ellipk(e**2)
W_n = 4*np.pi*K1*a*(1-e**2)*K_e2*np.log(a/r_c)
W_p = (np.pi/8)*K1*f_val*(R/f_val)**4*np.log(R**2/(4*f_val*r_c))
result = {'W_n': float(W_n), 'W_p': float(W_p), 'parabolic_favored': bool(W_p < W_n)}
with open('$OUTDIR/focal_domain_energies.json', 'w') as f:
    json.dump(result, f, indent=2)
"
