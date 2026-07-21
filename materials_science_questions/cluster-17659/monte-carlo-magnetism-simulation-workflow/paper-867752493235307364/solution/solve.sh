#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p $OUTDIR
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: idealized_magnetization.csv ===
python3 << 'EOF'
import numpy as np

p = 3
N = 101
s_vals = np.linspace(0, 1, N)
tau_vals = np.linspace(0, 1, N)
m_grid = np.linspace(0, 1, 20001)

rows = []
for s in s_vals:
    for tau in tau_vals:
        a = s * p * m_grid**(p-1)
        f = s * (p-1) * m_grid**p - (1 - tau) * np.sqrt(a**2 + 1) - tau * a
        m = m_grid[np.argmin(f)]
        rows.append([s, tau, m])

outpath = '/app/outputs/idealized_magnetization.csv'
np.savetxt(outpath, rows, delimiter=',', header='s,tau,m', comments='', fmt='%.15g')
print('Written', len(rows), 'rows to', outpath)
EOF

# === solve block: finiteT_magnetization.csv ===
python3 /solution/compute.py finiteT

# === solve block: jump_magnetization.csv ===
python3 /solution/compute.py jump

# === solve block: SVMC_magnetization.csv ===
python3 /solution/compute.py svmc

# === solve block: SA_magnetization.csv ===
python3 /solution/compute.py sa
