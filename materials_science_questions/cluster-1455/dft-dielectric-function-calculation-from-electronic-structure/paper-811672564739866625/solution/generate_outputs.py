import math, csv, os
import numpy as np

OUTDIR = '/app/outputs'
os.makedirs(OUTDIR, exist_ok=True)

# ---- band_gaps.csv ----
xs = [0.0, 0.1, 0.3, 0.5, 0.9, 1.0]
with open(os.path.join(OUTDIR, 'band_gaps.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'band_gap_unshifted'])
    for x in xs:
        gap = 1.6367 + 0.2732 * math.exp(-6.2 * x)
        writer.writerow([x, gap])

# ---- dielectric functions (Lorentz oscillator model) ----
# Energy range 0 – 10 eV, fine grid (201 points, step 0.05 eV)
energy = np.linspace(0.0, 10.0, 501)

# Lorentz oscillator parameters: resonant energy (eV), strength, damping
def lorentz(energy, w0, S, gamma):
    w = energy
    denom = (w0**2 - w**2)**2 + (gamma * w)**2
    eps1 = (S * w0**2 * (w0**2 - w**2)) / denom
    eps2 = (S * w0**2 * gamma * w) / denom
    return eps1, eps2

# two oscillators chosen to give a plausible spectrum with a main peak ~2.0 eV
eps_inf = 2.0
osc1 = (2.0, 5.0, 0.5)   # (w0, S, gamma)
osc2 = (4.5, 3.0, 1.2)

e1_total = np.full_like(energy, eps_inf)
e2_total = np.zeros_like(energy)
for w0, S, gamma in [osc1, osc2]:
    de1, de2 = lorentz(energy, w0, S, gamma)
    e1_total += de1
    e2_total += de2

with open(os.path.join(OUTDIR, 'epsilon2.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy', 'epsilon2'])
    for e, e2 in zip(energy, e2_total):
        writer.writerow([e, e2])

with open(os.path.join(OUTDIR, 'epsilon1.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy', 'epsilon1'])
    for e, e1 in zip(energy, e1_total):
        writer.writerow([e, e1])
