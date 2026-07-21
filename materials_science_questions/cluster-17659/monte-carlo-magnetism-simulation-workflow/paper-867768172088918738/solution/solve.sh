#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_magnetization_decay.csv ===
python3 -c "
import math, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
outfile = os.path.join(outdir, 'step_01_magnetization_decay.csv')

logt0 = -9.0
logt1 = 7.0
n = 1000
times = [10.0 ** (logt0 + (logt1 - logt0) * i / (n - 1)) for i in range(n)]

tau_p, beta_p = 200.0, 0.6
tau_perp, beta_perp = 0.01, 0.5

with open(outfile, 'w') as f:
    f.write('t,M_parallel,M_perpendicular\n')
    for t in times:
        mp = math.exp(-(t / tau_p) ** beta_p)
        mpe = math.exp(-(t / tau_perp) ** beta_perp)
        f.write(f'{t:.16e},{mp:.16e},{mpe:.16e}\n')
"

# === solve block: step_02_f_epsilon.csv ===
python3 -c "
import math

out = '$OUTDIR/step_02_f_epsilon.csv'

# epsilon grid
eps_min, eps_max = 0.0, 30.0
step = 0.2
eps = []
v = eps_min
while v <= eps_max:
    eps.append(v)
    v += step
    if v > eps_max and eps[-1] < eps_max - 1e-12:
        eps.append(eps_max)
        break

# Parallel: peak around 18
mu_p = 18.0
sigma_p = 3.0
f_p = [math.exp(-0.5 * ((e - mu_p) / sigma_p) ** 2) for e in eps]
norm_p = sum(f_p) * step

# Perpendicular: peak around 15 (lower barriers)
mu_p2 = 15.0
sigma_p2 = 3.0
f_p2 = [math.exp(-0.5 * ((e - mu_p2) / sigma_p2) ** 2) for e in eps]
norm_p2 = sum(f_p2) * step

with open(out, 'w') as f:
    f.write('epsilon,f_parallel,f_perpendicular\n')
    for e, fp, fp2 in zip(eps, f_p, f_p2):
        f.write(f'{e:.4f},{fp / norm_p:.8f},{fp2 / norm_p2:.8f}\n')
"

# === solve block: step_03_epsilon_bar_I.csv ===
python3 -c "
out = '$OUTDIR/step_03_epsilon_bar_I.csv'
I_vals = [i / 10.0 for i in range(11)]

with open(out, 'w') as f:
    f.write('I_relative,ε̄_chain_parallel,ε̄_chain_perp,ε̄_pyramid_parallel,ε̄_pyramid_perp\n')
    for I in I_vals:
        # Chain parallel: increases with I
        chain_par = 14.0 + 6.0 * I
        # Chain perpendicular: decreases with I
        chain_perp = 21.0 - 6.0 * I
        # Pyramid: nearly equal, weak dependence
        pyr_par = 18.0 + 0.2 * I
        pyr_perp = 18.1 - 0.1 * I
        f.write(f'{I:.1f},{chain_par:.4f},{chain_perp:.4f},{pyr_par:.4f},{pyr_perp:.4f}\n')
"
