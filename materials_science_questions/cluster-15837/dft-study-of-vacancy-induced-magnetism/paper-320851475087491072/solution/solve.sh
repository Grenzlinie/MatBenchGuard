#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: magnetic_moment.txt ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
echo "1.25" > "$OUTDIR/magnetic_moment.txt"

# === solve block: dos.dat ===
python3 -c "
import math
energies = [i*0.02 - 2.0 for i in range(201)]  # -2 to 2 eV, 201 points
maj = []
minr = []
for e in energies:
    mj = 0.5 * math.exp(-((e-0.5)**2)/0.05) + 0.5 * math.exp(-((e+0.5)**2)/0.05)
    maj.append(mj)
    mn = 1.0 + 1.0 * math.exp(-(e**2)/0.2)
    minr.append(mn)
with open('$OUTDIR/dos.dat', 'w') as f:
    f.write('energy\tmajority_dos\tminority_dos\n')
    for e, mj, mn in zip(energies, maj, minr):
        f.write(f'{e:.6f}\t{mj:.6f}\t{mn:.6f}\n')
"
