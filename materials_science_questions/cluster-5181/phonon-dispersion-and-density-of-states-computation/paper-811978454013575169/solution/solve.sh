#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: copper_dispersion.tsv ===
python3 << PYEOF
import numpy as np, math

A1=35.228; A2=1.875; K1=-0.040; K2=-0.988; aKe=0.1113
M_u = 63.55; u2g = 1.660539e-24
mass_g = M_u * u2g

def G_func(u,v,w):
    if u*u+v*v+w*w == 0:
        return 0.0
    eps = 1e-12
    total = 0.0
    for x,y,z in [(u,v,w), (v,w,u), (w,u,v)]:
        N1 = math.sin(x) + math.sin(y) - math.sin((x+y+z)/2) - math.sin((x+y-z)/2)
        N2 = math.sin(x) - math.sin(y) - math.sin((x+y+z)/2) - math.sin((x-y-z)/2)
        den1 = (x-y)**2 - z**2
        den2 = (x+y)**2 - z**2
        if abs(den1) < eps: den1 = eps if den1 >=0 else -eps
        if abs(den2) < eps: den2 = eps if den2 >=0 else -eps
        total += (x+y)/den1 * N1 + (x-y)/den2 * N2
    return -2.0 / (u*u + v*v + w*w) * total

directions = []
for qx in np.arange(0.0, 1.01, 0.1):
    directions.append((qx, 0.0, 0.0))
    directions.append((qx, qx, 0.0))
    directions.append((qx, qx, qx))

with open('$OUTDIR/copper_dispersion.tsv', 'w') as f:
    f.write("qx\tqy\tqz\tfreq1\tfreq2\tfreq3\n")
    for q1,q2,q3 in directions:
        u = math.pi * q1; v = math.pi * q2; w = math.pi * q3
        G = G_func(u,v,w)
        C1 = math.cos(u); C2 = math.cos(v); C3 = math.cos(w)
        S1 = math.sin(u); S2 = math.sin(v); S3 = math.sin(w)
        pref = 2*A1 + 8*(K1+K2)
        D11 = pref * (2 - C1*(C2+C3)) + 4*A2*S1*S1 - 8*K1*(2*C1*C1 - C2*C2 - C3*C3) + aKe * math.pi**2 * q1*q1 * G*G
        D22 = pref * (2 - C2*(C3+C1)) + 4*A2*S2*S2 - 8*K1*(2*C2*C2 - C3*C3 - C1*C1) + aKe * math.pi**2 * q2*q2 * G*G
        D33 = pref * (2 - C3*(C1+C2)) + 4*A2*S3*S3 - 8*K1*(2*C3*C3 - C1*C1 - C2*C2) + aKe * math.pi**2 * q3*q3 * G*G
        D12 = (2*A1 - 16*K1)*S1*S2 + aKe * math.pi**2 * q1*q2 * G*G
        D13 = (2*A1 - 16*K1)*S1*S3 + aKe * math.pi**2 * q1*q3 * G*G
        D23 = (2*A1 - 16*K1)*S2*S3 + aKe * math.pi**2 * q2*q3 * G*G
        D = np.array([[D11, D12, D13],
                      [D12, D22, D23],
                      [D13, D23, D33]])
        eigvals, _ = np.linalg.eigh(D)
        freqs = np.sqrt(eigvals * 1e3 / mass_g) / (2*math.pi*1e12)
        freqs.sort()
        f.write(f"{q1:.10f}\t{q2:.10f}\t{q3:.10f}\t{freqs[0]:.6f}\t{freqs[1]:.6f}\t{freqs[2]:.6f}\n")
PYEOF

# === solve block: silver_dispersion.tsv ===
python3 /solution/compute_dispersion.py silver /app/outputs/silver_dispersion.tsv

# === solve finalize ===
# No further finalization needed
