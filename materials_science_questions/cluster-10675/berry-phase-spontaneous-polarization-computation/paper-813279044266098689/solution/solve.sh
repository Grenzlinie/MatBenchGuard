#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: epsilon_vs_T.csv ===
echo 'T (K),epsilon' > /app/outputs/epsilon_vs_T.csv
python3 -c "
import math
mu = 0.6309e-23
N = 3e21
E = 100.0
eps0 = 8.854187817e-12
kB = 1.380649e-23
J = -0.9315e-20

for T in range(100, 301, 10):
    x = mu * E / (kB * T)
    y = J / (kB * T)
    sinh_x = math.sinh(x)
    epsilon = (mu * N) / (eps0 * E) * sinh_x / math.sqrt(math.exp(-4 * y) + sinh_x ** 2)
    print(f'{T},{epsilon:.6e}')
" >> /app/outputs/epsilon_vs_T.csv
