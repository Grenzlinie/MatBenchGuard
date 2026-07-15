#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy

# === solve block: reproduced_results.json ===
cat > /tmp/fit.py << 'PYEOF'
import json
import numpy as np
from scipy.optimize import curve_fit

# experimental data from Table I
p_k = np.array([0.0, 0.4733, 1.0937, 1.7775, 2.4820, 4.0198, 4.8537,
                5.7285, 6.6440, 7.6018, 9.6467, 11.8751, 14.0055])  # 10^3 kg/cm^2
eps110 = np.array([0.0, 0.34, 0.68, 1.18, 1.68, 2.33, 2.65, 3.13,
                   3.45, 3.77, 4.39, 5.01, 5.62])           # percent
eps200 = np.array([0.0, 0.45, 1.20, 1.64, 2.08, 2.66, 2.95, 3.23,
                   3.51, 3.80, 4.49, 5.18, 5.58])           # percent

# convert to kg/cm^2 and fractional strain
P = p_k * 1e3
y110 = eps110 / 100.0
y200 = eps200 / 100.0

def cubic(x, A, B, C):
    return A*x - B*x**2 + C*x**3

p0 = (1e-5, 1e-10, 1e-14)

# fit (110) plane
popt110, _ = curve_fit(cubic, P, y110, p0=p0)
A110, B110, C110 = popt110

# fit (200) plane
popt200, _ = curve_fit(cubic, P, y200, p0=p0)
A200, B200, C200 = popt200

# volumetric strain (-DeltaV/V0)
y_vol = 1.447 * (y110 + 0.382 * y200)
popt_vol, _ = curve_fit(cubic, P, y_vol, p0=p0)
A_v, B_v, C_v = popt_vol

# Grüneisen parameter
gamma0 = -0.5 + (B_v / A_v)

result = {
    "plane_110": {"A": A110, "B": B110, "C": C110},
    "plane_200": {"A": A200, "B": B200, "C": C200},
    "volumetric": {"A_v": A_v, "B_v": B_v, "C_v": C_v},
    "gamma_0": gamma0
}

with open("/app/outputs/reproduced_results.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF
python3 /tmp/fit.py
