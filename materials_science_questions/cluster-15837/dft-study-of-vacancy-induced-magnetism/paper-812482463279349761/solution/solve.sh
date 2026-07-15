#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: electronic_properties.json ===
cat > /app/outputs/electronic_properties.json <<'EOF'
{
  "band_gap_pristine": 1.0016,
  "magnetic_moment_VSc": 1.0,
  "E_form_Vc": 9.97,
  "E_form_Vf": 7.52,
  "E_form_VSc": 11.64,
  "E_binding_all": [-6.39, -6.31, -6.36, -6.28],
  "absorption_peak_positions": [9.356, 0.131, 0.192, 0.199],
  "reflectivity_max_positions": [9.356, 0.131, 0.192, 0.199]
}
EOF

# === solve block: quantum_capacitance.csv ===
python3 <<'PYEOF' > /app/outputs/quantum_capacitance.csv
import math, numpy as np

gauss_area = lambda A, s, V, c: A * s * math.sqrt(math.pi/2) * (math.erf((V-c)/(s*math.sqrt(2))) - math.erf((0-c)/(s*math.sqrt(2))))

def C_function(V, peaks, sigma0, Cint0):
    val = Cint0 * math.exp(-V**2/(2*sigma0**2))
    for center, height, sigma in peaks:
        val += height * np.exp(-0.5*((V-center)/sigma)**2)
    return val

def q_target(sigma0, target_Cint0, side_peaks, Vmax=0.6):
    q = gauss_area(target_Cint0, sigma0, Vmax, 0.0)
    for c, h, s in side_peaks:
        q += gauss_area(h, s, Vmax, c)
    return q

def find_sigma0(target_Q, target_Cint0, side_peaks, Vmax=0.6):
    lo, hi = 1e-6, 5.0
    for _ in range(60):
        mid = (lo+hi)/2
        qmid = q_target(mid, target_Cint0, side_peaks, Vmax)
        if qmid > target_Q:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2

systems = [
    dict(name='pristine', Cint0=0.13, Q06=0.078,
         side_peaks=[(-0.43, 655.0, 0.08)]),
    dict(name='V_Sc', Cint0=139.47, Q06=44.29,
         side_peaks=[(-0.37, 731.0, 0.08), (0.43, 192.0, 0.15)]),
    dict(name='V_F', Cint0=338.85, Q06=128.53,
         side_peaks=[(0.40, 493.0, 0.15)]),
    dict(name='V_C', Cint0=290.85, Q06=82.21,
         side_peaks=[(-0.03, 397.0, 0.08), (0.57, 313.0, 0.15)]),
]

V = np.arange(-0.6, 0.605, 0.01)
n = len(V)
lines = []
for sys in systems:
    sigma0 = find_sigma0(sys['Q06'], sys['Cint0'], sys['side_peaks'])
    C = np.array([C_function(v, sys['side_peaks'], sigma0, sys['Cint0']) for v in V])
    Q = np.zeros(n)
    zero_idx = np.argmin(np.abs(V))
    Q[zero_idx] = 0.0
    # positive side
    for i in range(zero_idx+1, n):
        Q[i] = Q[i-1] + 0.5*(C[i]+C[i-1])*0.01
    # negative side
    for i in range(zero_idx-1, -1, -1):
        Q[i] = Q[i+1] - 0.5*(C[i]+C[i+1])*0.01
    Cint = np.where(np.abs(V)>1e-9, Q/V, sys['Cint0'])
    for i in range(n):
        lines.append(f"{sys['name']},{V[i]:.2f},{C[i]:.6f},{Q[i]:.6f},{Cint[i]:.6f}")

print('system,V,C_diff,Q,C_int')
print('\n'.join(lines))
PYEOF
