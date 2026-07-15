#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# Install required packages
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# Execute the computation script
python3 /solution/compute_spin_wave.py

# === solve block: results.csv ===
python3 << 'PYEOF'
import numpy as np
import csv, math
from scipy.integrate import quad

def compute_1d():
    # linear chain: z=2, BZ [-π, π]  (exact analytic energy)
    E_NJ = math.sqrt(2) / math.pi - 0.75
    n_str = "Inf"
    sq_mag = 0.0
    # out-of-plane nearest-neighbor correlation via quad (smooth)
    def integrand(k):
        S_val = 2.0 * math.cos(k)
        rad = 1.0 - S_val / 2.0
        if rad <= 0.0:
            return 0.0
        return (1.0 / (8.0 * math.pi)) * S_val * math.sqrt(rad)
    oop_corr, _ = quad(integrand, -np.pi, np.pi, limit=200)
    return E_NJ, n_str, oop_corr, sq_mag

def compute_2d(nk=600):
    z = 4
    dk = 2.0 * math.pi / nk
    # shifted (midpoint) grid to avoid the singular point at k=0
    kx = -math.pi + (np.arange(nk) + 0.5) * dk
    ky = -math.pi + (np.arange(nk) + 0.5) * dk
    KX, KY = np.meshgrid(kx, ky, indexing='ij')
    S = 2.0 * (np.cos(KX) + np.cos(KY))
    rad = 1.0 - S / z
    # energy per site
    f = np.sqrt(rad) - 1.0
    E_NJ = -z / 8.0 + (z / 4.0) * np.mean(f)
    # occupation number
    a = S / (2.0 * z)
    t = a / (1.0 - a)                     # tanh(2u)
    t_sq = t ** 2
    # cosh(2u) = 1 / sqrt(1 - tanh^2(2u)) = 1 / sqrt(1 - t^2)
    cosh2u = 1.0 / np.sqrt(1.0 - t_sq)
    sinh2_u = 0.5 * (cosh2u - 1.0)
    n_avg = np.mean(sinh2_u)
    # out-of-plane nearest-neighbor correlation
    oop_corr = (1.0 / (4.0 * z)) * np.mean(S * np.sqrt(rad))
    # squared magnetization (order parameter squared)
    sq_mag = (n_avg - 0.5) ** 2
    return E_NJ, n_avg, oop_corr, sq_mag

def compute_3d(nk=250):
    z = 6
    dk = 2.0 * math.pi / nk
    kx = -math.pi + (np.arange(nk) + 0.5) * dk
    ky = -math.pi + (np.arange(nk) + 0.5) * dk
    kz = -math.pi + (np.arange(nk) + 0.5) * dk
    KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing='ij')
    S = 2.0 * (np.cos(KX) + np.cos(KY) + np.cos(KZ))
    rad = 1.0 - S / z
    f = np.sqrt(rad) - 1.0
    E_NJ = -z / 8.0 + (z / 4.0) * np.mean(f)
    a = S / (2.0 * z)
    t = a / (1.0 - a)
    t_sq = t ** 2
    cosh2u = 1.0 / np.sqrt(1.0 - t_sq)
    sinh2_u = 0.5 * (cosh2u - 1.0)
    n_avg = np.mean(sinh2_u)
    oop_corr = (1.0 / (4.0 * z)) * np.mean(S * np.sqrt(rad))
    sq_mag = (n_avg - 0.5) ** 2
    return E_NJ, n_avg, oop_corr, sq_mag

E1, n1, oop1, sq1 = compute_1d()
E2, n2, oop2, sq2 = compute_2d()
E3, n3, oop3, sq3 = compute_3d()

with open("/app/outputs/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["lattice", "energy_per_site", "occupation_number", "out_of_plane_correlation", "squared_magnetization"])
    writer.writerow(["linear_chain", f"{E1:.12f}", n1, f"{oop1:.12f}", f"{sq1:.12f}"])
    writer.writerow(["square_lattice", f"{E2:.12f}", f"{n2:.12f}", f"{oop2:.12f}", f"{sq2:.12f}"])
    writer.writerow(["simple_cubic", f"{E3:.12f}", f"{n3:.12f}", f"{oop3:.12f}", f"{sq3:.12f}"])
PYEOF
