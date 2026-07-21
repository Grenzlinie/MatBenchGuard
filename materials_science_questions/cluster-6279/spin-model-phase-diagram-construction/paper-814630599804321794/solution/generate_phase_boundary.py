import sys, os, csv
sys.path.insert(0, '/solution')
import numpy as np
from common import J0, K0, D, solve_self

zeta = 3.0
T_vals = np.linspace(0.05, 2.5, 500)
rows = []
for T in T_vals:
    try:
        s, l = solve_self(T, zeta)
    except:
        continue
    h_c = (K0 * zeta - J0) * (s + l)
    if h_c > 0:
        rows.append([h_c, T])

outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, 'phase_boundary.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['field', 'critical_temperature'])
    for h, T in rows:
        writer.writerow([h, T])
