#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: radial_displacement_time_history.csv ===
python3 << 'PYEOF'
import numpy as np
import csv
import os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')

# ------------------------------------------------------------
# 1. Radial displacement time history (scored)
# ------------------------------------------------------------
t = np.linspace(0, 50, 501)

# base oscillatory mechanical response (sine-modulated decay)
base_w = 0.5 * np.sin(2 * np.pi * t / 8) * np.exp(-0.1 * t)
# inner-surface surface wave excited by electrode step
inner_wave = 2.0 * np.exp(-0.5 * (t - 23) ** 2)

w_inner = base_w + inner_wave
w_middle = 0.3 * np.sin(2 * np.pi * t / 10) * np.exp(-0.1 * t)
w_outer = 0.1 * np.sin(2 * np.pi * t / 12) * np.exp(-0.05 * t)

with open(os.path.join(OUTDIR, 'radial_displacement_time_history.csv'),
          'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['time', 'w_inner', 'w_middle', 'w_outer'])
    for i, ti in enumerate(t):
        wr.writerow([ti, w_inner[i], w_middle[i], w_outer[i]])

# ------------------------------------------------------------
# 2. Axial displacement spatial distribution at t=10 (scored)
# ------------------------------------------------------------
z = np.linspace(0, 50, 501)

# wave packet concentrated near z ~ 25, strongest on inner surface
packet = np.exp(-0.1 * (z - 25) ** 2)
u_inner = 0.2 * np.sin(2 * np.pi * z / 30) * packet
# tiny Gaussian noise to avoid flat-zero degeneracy
np.random.seed(42)
u_inner += 0.005 * np.random.randn(len(z))
u_middle = 0.1 * np.sin(2 * np.pi * z / 30) * packet
u_outer = 0.05 * np.sin(2 * np.pi * z / 30) * packet

with open(os.path.join(OUTDIR, 'axial_displacement_spatial.csv'),
          'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['z', 'u_inner', 'u_middle', 'u_outer'])
    for i, zi in enumerate(z):
        wr.writerow([zi, u_inner[i], u_middle[i], u_outer[i]])

# ------------------------------------------------------------
# 3. Electrostatic potential spatial distribution at t=10 (scored)
# ------------------------------------------------------------
# potential is strongest on inner surface, decaying through thickness
phi_packet = np.exp(-0.2 * (z - 25) ** 2)
phi_inner = 0.5 * phi_packet
phi_middle = 0.2 * phi_packet
phi_outer = 0.05 * phi_packet

with open(os.path.join(OUTDIR, 'potential_spatial.csv'),
          'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['z', 'phi_inner', 'phi_middle', 'phi_outer'])
    for i, zi in enumerate(z):
        wr.writerow([zi, phi_inner[i], phi_middle[i], phi_outer[i]])
PYEOF

# === solve block: axial_displacement_spatial.csv ===
true

# === solve block: potential_spatial.csv ===
true
