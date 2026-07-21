#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_dispersion_check.json ===
python3 <<'PYEOF' > "$OUTDIR/step_01_dispersion_check.json"
import json
import sys
import numpy as np

mu = 0.01
C = 0.1

def zeta(P, Q, omega):
    return -2 * C * np.cos(P) + 2 * C + 4 * np.cos(Q) - mu * omega**2 + 8

def sigma(omega, k1, k2):
    z12 = zeta(k1, k2, omega)
    z21 = zeta(k2, k1, omega)
    return (144 * np.sin(k1)**2 * z12 +
            144 * np.sin(k2)**2 * z21 +
            (24 * np.cos(k2) + 24 * np.cos(k1) + omega**2 - 48) * z12 * z21)

# Compute invariant points
omega1 = 4 * np.sqrt(6)
s1 = sigma(omega1, np.pi, np.pi)

omega2 = 0.0
s2 = sigma(omega2, 0.0, 0.0)

omega3 = 4 * np.sqrt(3)
s3 = sigma(omega3, 0.0, np.pi)
s4 = sigma(omega3, np.pi, 0.0)

result = {
    "omega_4sqrt6_pi_pi": float(s1),
    "omega_0_0_0": float(s2),
    "omega_4sqrt3_0_pi": float(s3),
    "omega_4sqrt3_pi_0": float(s4)
}

json.dump(result, sys.stdout)
PYEOF

# === solve block: step_02_greens_function.json ===
# Compute the Green's function displacement field inline to avoid the bug in calc_greens.py
python3 <<'PYEOF' > "$OUTDIR/step_02_greens_function.json"
import json
import sys
import numpy as np
from scipy.integrate import nquad

mu = 0.01
C = 0.1
omega = 9.8
f_w = -1.0

def zeta(P, Q):
    return -2 * C * np.cos(P) + 2 * C + 4 * np.cos(Q) - mu * omega**2 + 8

def sigma(k1, k2):
    z12 = zeta(k1, k2)
    z21 = zeta(k2, k1)
    return (144 * np.sin(k1)**2 * z12 +
            144 * np.sin(k2)**2 * z21 +
            (24 * np.cos(k2) + 24 * np.cos(k1) + omega**2 - 48) * z12 * z21)

def W_F(k1, k2):
    z12 = zeta(k1, k2)
    z21 = zeta(k2, k1)
    return z12 * z21 * f_w / sigma(k1, k2)

def integrand(k1, k2, m, n):
    return W_F(k1, k2) * np.exp(1j * (k1 * m + k2 * n))

results = []
for m in range(-2, 3):
    for n in range(-2, 3):
        val, err = nquad(lambda k1, k2: integrand(k1, k2, m, n),
                         [[-np.pi, np.pi], [-np.pi, np.pi]],
                         opts={'epsabs': 1e-8, 'epsrel': 1e-8})
        # The inverse Fourier transform normalisation factor 1/(4π²)
        w = val.real / (4 * np.pi**2)
        results.append({"m": m, "n": n, "w": w})

json.dump(results, sys.stdout, allow_nan=False)
PYEOF
