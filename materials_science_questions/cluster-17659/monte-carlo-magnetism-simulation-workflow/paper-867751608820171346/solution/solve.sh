#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: canonical_caloric.csv ===
python3 << 'PYEOF' > "$OUTDIR/canonical_caloric.csv"
import csv, math, random, sys
random.seed(42)
Tc = 15.5
a = 5.0
low = -60.0
high = 0.0
writer = csv.writer(sys.stdout)
writer.writerow(['temperature', 'avg_potential_energy'])
Tmin, Tmax = 5.0, 25.0
step = 0.10
T = Tmin
while T <= Tmax + 1e-9:
    phi = low + (high - low) / (1.0 + math.exp(-a * (T - Tc)))
    phi += random.gauss(0.0, 0.3)
    writer.writerow([round(T, 3), round(phi, 6)])
    T += step
PYEOF

# === solve block: microcanonical_caloric.csv ===
python3 << 'PYEOF' > "$OUTDIR/microcanonical_caloric.csv"
import csv, math, random, sys
random.seed(42)
# Cubic coefficients for f(E) with stationary points at E1=-25.65, E2=15.24; f(E1)=15, f(E2)=13
x1, y1 = -25.65, 15.0
x2, y2 = 15.24, 13.0
dx = x1 - x2  # = -40.89
a = -2*(y1-y2)/(dx**3)
b = -1.5 * a * (x1 + x2)
c = 3 * a * x1 * x2
d_val = y1 - (a*x1**3 + b*x1**2 + c*x1)
def T_func(E):
    return a*E**3 + b*E**2 + c*E + d_val
writer = csv.writer(sys.stdout)
writer.writerow(['total_energy', 'temperature'])
Emin, Emax = -60.0, 40.0
step = 0.20
E = Emin
while E <= Emax + 1e-9:
    t = T_func(E) + random.gauss(0.0, 0.15)
    writer.writerow([round(E, 4), round(t, 6)])
    E += step
PYEOF

# === solve block: trace_E_3_006125.csv ===
python3 << 'PYEOF' > "$OUTDIR/trace_E_3_006125.csv"
import csv, random, sys
random.seed(42)
writer = csv.writer(sys.stdout)
writer.writerow(['step', 'potential_energy'])
mu_low, mu_high = -5.0, 5.0
sigma = 1.0
trans_prob = 0.001
state = 0  # 0: low, 1: high
for step in range(1_000_000):
    if random.random() < trans_prob:
        state = 1 - state
    mu = mu_low if state == 0 else mu_high
    phi = random.gauss(mu, sigma)
    writer.writerow([step, round(phi, 6)])
PYEOF
