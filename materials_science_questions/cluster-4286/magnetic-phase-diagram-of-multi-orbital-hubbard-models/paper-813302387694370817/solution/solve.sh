#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: energy_spectrum.csv ===
cat > "$OUTDIR/energy_spectrum.csv" <<'CSVEOF'
kx,ky,E_plus,E_minus
0.0,0.0,7.21110255093,-7.21110255093
3.141592653589793,0.0,4.0,-4.0
CSVEOF

# === solve block: magnetization_value.txt ===
python3 - "$@" <<'PYEOF' > "$OUTDIR/magnetization_value.txt"
import math

U = 8.0
B = 1.5

def t_k(s, kx, ky):
    c = math.cos(kx) + math.cos(ky)
    Bk2 = 4.0 * B * B * c * c
    return math.sqrt((s * U) ** 2 + Bk2)

def Phi(s):
    if s >= 0.5:
        return 0.0
    return math.sqrt(0.25 - s * s)

def F(s):
    Nk = 300
    total = Nk * Nk
    sum_val = 0.0
    U_phi = U * Phi(s)
    for i in range(Nk):
        kx = -math.pi + (i + 0.5) * (2.0 * math.pi / Nk)
        for j in range(Nk):
            ky = -math.pi + (j + 0.5) * (2.0 * math.pi / Nk)
            tk = t_k(s, kx, ky)
            if tk >= U_phi:
                sum_val += U / tk
    avg = sum_val / total
    return avg - 1.0

# Bisection to find s in (0.001, 0.5]
a = 0.001
b = 0.5
fa = F(a)
fb = F(b)
for _ in range(50):
    m = (a + b) / 2.0
    fm = F(m)
    if fm == 0.0:
        break
    if fa * fm < 0.0:
        b = m
        fb = fm
    else:
        a = m
        fa = fm
s_sol = (a + b) / 2.0
print(s_sol)
PYEOF
