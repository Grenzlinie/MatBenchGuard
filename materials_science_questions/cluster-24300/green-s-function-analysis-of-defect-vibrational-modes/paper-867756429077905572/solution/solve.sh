#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: harmonic_spectrum.csv ===
echo 'Computing harmonic emission spectrum...'
python3 << 'PYEOF'
import numpy as np
from scipy.fft import fft, fftfreq
import csv
from pathlib import Path

outdir = Path("/app/outputs")
outdir.mkdir(parents=True, exist_ok=True)

# ---- parameters ----
g = 3.5
theta = 1.2
E0 = 2.0
omega = 0.2
N_cycles = 5
Delta = 6.0
q = 1.0
m = 1.0

# time array
tau = 2 * np.pi * N_cycles / omega
dt = 0.01
t_arr = np.arange(0, tau + dt, dt)
Nt = len(t_arr)

A_arr = -E0 / (2 * omega) * np.sin(omega * t_arr)

sh = np.sinh(theta)
ch = np.cosh(theta)

# reflection amplitude R(t) and R(-theta)
D_arr = 1 - 1j * (q / 4) * (4 / g**2 + 1 + A_arr**2) * sh
R_arr = -ch / D_arr

D_neg_arr = 1 + 1j * (q / 4) * (4 / g**2 + 1 + A_arr**2) * sh
R_neg_arr = -ch / D_neg_arr   # R(-theta)

# transmission amplitude T(t)
term1 = 4 / g - 1j * (4 / g**2 + 1 + A_arr**2) * sh
num = 1j * (1 + (A_arr - 2j / g)**2) * sh * term1
T_arr = num / D_arr

# ---- spatial setup ----
vg = np.tanh(theta)
x0 = 20.0
L = 60.0
dx = 0.2
x = np.arange(0, L, dx)
nx = len(x)

u_plus = np.array([np.exp(-theta / 2), np.exp(theta / 2)]) / np.sqrt(2)
u_minus = np.array([np.exp(theta / 2), np.exp(-theta / 2)]) / np.sqrt(2)

# ---- dipole moment expectation ----
d_arr = np.zeros(Nt)
dx = x[1] - x[0]

for idx in range(Nt):
    t = t_arr[idx]
    A = A_arr[idx]
    T = T_arr[idx]
    Rneg = R_neg_arr[idx]

    xc = x0 + vg * t
    G = np.exp(-(x - xc)**2 / (2 * Delta**2))
    laser = np.exp(1j * x * A)
    exp_ipx = np.exp(1j * sh * x)
    exp_minus_ipx = np.exp(-1j * sh * x)

    f1 = u_plus[:, None] * exp_ipx[None, :]
    f2 = u_minus[:, None] * exp_minus_ipx[None, :]
    phi = laser[None, :] * G[None, :] * T * (f1 + Rneg * f2)

    prob = np.sum(np.abs(phi)**2, axis=0)
    # manual trapezoidal integration (compatible with all numpy versions)
    norm = 0.5 * np.sum((prob[:-1] + prob[1:]) * dx)
    integrand = x * prob
    dipole = 0.5 * np.sum((integrand[:-1] + integrand[1:]) * dx) / norm
    d_arr[idx] = dipole

# ---- spectrum ----
d_centered = d_arr - np.mean(d_arr)
amp = np.abs(fft(d_centered))
freqs = fftfreq(Nt, d=dt)

omega_multiples = np.arange(0, 21)
intensity_vals = np.zeros(len(omega_multiples))
for i, n in enumerate(omega_multiples):
    target = n * omega
    idx_f = np.argmin(np.abs(freqs - target))
    intensity_vals[i] = amp[idx_f] if idx_f < len(amp) else 0.0

max_intensity = np.max(intensity_vals)
if max_intensity > 0:
    intensity_vals /= max_intensity

with open(outdir / "harmonic_spectrum.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["omega_multiples", "intensity"])
    for n, val in zip(omega_multiples, intensity_vals):
        writer.writerow([float(n), float(val)])
print("harmonic_spectrum.csv written.")
PYEOF
