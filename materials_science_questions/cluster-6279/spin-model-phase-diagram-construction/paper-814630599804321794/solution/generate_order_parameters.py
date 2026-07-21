import sys, os, csv
sys.path.insert(0, '/solution')
import numpy as np
from common import J0, K0, D, solve_self

zeta = 3.0
fields = [4.5, 4.7, 5.0, 5.3]
T_vals = np.linspace(0.05, 2.5, 500)

# Compute sigma, lambda for all T
sig_lam = []
for T in T_vals:
    try:
        s, l = solve_self(T, zeta)
    except:
        if sig_lam:
            s, l = sig_lam[-1]
        else:
            s, l = (0.0, -2.0)
    sig_lam.append((s, l))

denom = 2.0 * (K0 * zeta - J0)

rows = []
for h in fields:
    for idx, T in enumerate(T_vals):
        s, l = sig_lam[idx]
        arg = (K0 * zeta - J0)**2 * (s + l)**2 - h**2
        if arg < -1e-12:
            break
        Q2 = -np.sqrt(max(arg, 0.0)) / denom
        Q0 = (3.0 * s - l) / 2.0
        S_z = h / denom
        rows.append([h, T, S_z, Q0, Q2])

outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, 'order_parameters.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['field', 'temperature', 'S_z', 'Q0', 'Q2'])
    for row in rows:
        writer.writerow(row)
