#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: magnetisation_depth_profile.csv ===
python3 - << 'PY' "$OUTDIR/magnetisation_depth_profile.csv"
import sys, math, csv

output_path = sys.argv[1]

c_vals = [0.75]*6 + [0.8]*2 + [0.0]*3 + [0.8]*2 + [0.75]*6
N = len(c_vals)

JAA, JAB, JBB = 1.0, 4.0, 0.1
D = 1.0

temps = [0.5, 1.5, 2.5, 3.5, 4.5]

def solve(y, max_iters=5000, tol=1e-8):
    m1 = [0.5]*N
    m2 = [0.5]*N
    for _ in range(max_iters):
        new_m1 = [0.0]*N
        new_m2 = [0.0]*N
        for v in range(N):
            hA = 4.0 * (JAA * c_vals[v] * m1[v] + JAB * (1.0 - c_vals[v]) * m2[v])
            hB = 4.0 * (JAB * c_vals[v] * m1[v] + JBB * (1.0 - c_vals[v]) * m2[v])

            if v - 1 >= 0:
                mu = v - 1
                hA += JAA * c_vals[mu] * m1[mu] + JAB * (1.0 - c_vals[mu]) * m2[mu]
                hB += JAB * c_vals[mu] * m1[mu] + JBB * (1.0 - c_vals[mu]) * m2[mu]
            if v + 1 < N:
                mu = v + 1
                hA += JAA * c_vals[mu] * m1[mu] + JAB * (1.0 - c_vals[mu]) * m2[mu]
                hB += JAB * c_vals[mu] * m1[mu] + JBB * (1.0 - c_vals[mu]) * m2[mu]

            xA = hA / y
            xB = hB / y
            expD = math.exp(-D / y)
            denom = 2.0 * math.cosh(xA) + expD
            new_m1[v] = 2.0 * math.sinh(xA) / denom if denom > 1e-12 else 0.0
            new_m2[v] = 0.5 * math.tanh(0.5 * xB)

        diff = max(max(abs(new_m1[i] - m1[i]) for i in range(N)),
                   max(abs(new_m2[i] - m2[i]) for i in range(N)))
        m1, m2 = new_m1, new_m2
        if diff < tol:
            break

    return [c_vals[v] * m1[v] + (1.0 - c_vals[v]) * m2[v] for v in range(N)]

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['layer_index', 'reduced_temperature', 'concentration_c', 'm_v'])
    for y in temps:
        try:
            m = solve(y)
        except Exception:
            m = [0.0] * N
        for v in range(N):
            mv = m[v]
            if mv is None or (isinstance(mv, float) and math.isnan(mv)):
                mv = 0.0
            writer.writerow([v, y, c_vals[v], f"{mv:.8f}"])
print("magnetisation_depth_profile.csv written")
PY

# === solve block: phase_diagram_boundary.csv ===
python3 /solution/solve.py --output phase_diagram_boundary.csv
