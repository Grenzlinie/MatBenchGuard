#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
chmod +x /solution/compute_chirality.py

# === solve block: phase_boundary.csv ===
python3 -c "
import math
H0=5.5; p0=0.42; T0=5.0; phi=3.0; H=14.0
print('pressure_kbar,critical_temp_K')
for p in (0,2,4,6,8,10):
    val = (H/H0)**2 + p/p0 - 1
    Tc = T0 * val**(1/phi) if val >= 0 else 0.0
    print(f'{p},{Tc:.6f}')
" > "$OUTDIR/phase_boundary.csv"

# === solve block: chirality_pressure.csv ===
python3 /solution/compute_chirality.py > "$OUTDIR/chirality_pressure.csv"

# === solve block: barrier_pressure.csv ===
python3 -c "
H0=5.5; p0=0.42; H=14.0; factor=0.0225
print('pressure_kbar,potential_barrier_J_per_m2')
for p in (0,2,4,6,8,10):
    dU = factor * ( (H/H0)**2 + p/p0 - 1 )
    print(f'{p},{dU:.6f}')
" > "$OUTDIR/barrier_pressure.csv"
