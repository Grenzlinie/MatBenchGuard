#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
mkdir -p /app/outputs

# === solve block: force_depth_parabolic.csv ===
python3 <<'PYEOF'
import sys, numpy as np
sys.path.insert(0, '/solution')
from solver import get_hat_Q, get_indenter, solve_contact, compute_force

E = 70e9
nu = 0.3
N = 64
Rs = [0.25e-6, 1e-6]
Ls = [5e-6, 10e-6, 25e-6]
depths = np.arange(0, 201, 1) * 1e-9

rows = []
for R in Rs:
    for L in Ls:
        hat_Q, _, _ = get_hat_Q(N, L, E, nu)
        u_ind = get_indenter(R, L, N)
        for depth in depths:
            p = solve_contact(u_ind, depth, hat_Q)
            F = compute_force(p, L)
            rows.append([R*1e6, L*1e6, depth*1e9, F*1e9])

with open('/app/outputs/force_depth_parabolic.csv', 'w') as f:
    f.write('R_um,L_um,depth_nm,force_nN\n')
    for row in rows:
        f.write(f'{row[0]},{row[1]},{row[2]},{row[3]}\n')
PYEOF

# === solve block: stress_slice_parabolic.csv ===
python3 <<'PYEOF'
import sys, numpy as np
sys.path.insert(0, '/solution')
from solver import get_hat_Q, get_indenter, solve_contact, compute_stress_slice

E = 70e9
nu = 0.3
R = 1e-6
L = 5e-6
d = 100e-9
N = 64
z = np.arange(-2e-6, 0, 0.01e-6)

hat_Q, _, _ = get_hat_Q(N, L, E, nu)
u_ind = get_indenter(R, L, N)
p = solve_contact(u_ind, d, hat_Q)
sigma_zz = compute_stress_slice(p, L, z, E, nu)

rows = zip(z * 1e6, sigma_zz)
with open('/app/outputs/stress_slice_parabolic.csv', 'w') as f:
    f.write('z_um,sigma_zz_Pa\n')
    for zv, sz in rows:
        f.write(f'{zv},{sz}\n')
PYEOF

# === solve block: convergence_mse.csv ===
python3 <<'PYEOF'
import sys, numpy as np
sys.path.insert(0, '/solution')
from solver import get_hat_Q, get_indenter, solve_contact, compute_stress_slice

E = 70e9
nu = 0.3
R = 1e-6
L = 5e-6
d = 100e-9
Ns = [32, 64, 128, 256, 512, 1024]
z = np.arange(-2e-6, 0, 0.01e-6)

sigmas = {}
for N in Ns:
    hat_Q, _, _ = get_hat_Q(N, L, E, nu)
    u_ind = get_indenter(R, L, N)
    p = solve_contact(u_ind, d, hat_Q)
    sigma = compute_stress_slice(p, L, z, E, nu)
    sigmas[N] = sigma

ref = sigmas[1024]
ref_mean_sq = np.mean(ref ** 2)
rows = []
for N in Ns[:-1]:
    mse = np.mean((ref - sigmas[N]) ** 2) / ref_mean_sq
    rows.append((N, mse))

with open('/app/outputs/convergence_mse.csv', 'w') as f:
    f.write('grid_size,MSE\n')
    for gs, m in rows:
        f.write(f'{gs},{m}\n')
PYEOF
