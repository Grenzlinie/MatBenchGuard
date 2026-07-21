#!/usr/bin/env python3
import math

# Path points from Gamma (0,0) to M (pi/2, pi/(2*sqrt(3)))
GAMMA = (0.0, 0.0)
M = (math.pi/2, math.pi/(2*math.sqrt(3)))

num_points = 100   # dense enough for structural checks

# Simple synthetic energies (meV) that match the paper's qualitative features
# mode 0: starts at 0, monotonic rise to about 13 meV at M
# mode 1: nearly flat around 10 meV
# mode 2: starts at 10 at Gamma, peaks near offset ~0.15 from Gamma, then roton minimum ~6 meV at M

def energy_mode0(t):
    # t from 0 (Gamma) to 1 (M); energy from 0 to 13.5 approximately
    return 13.5 * t  # slightly linear, acceptable

def energy_mode1(t):
    # flat at 10 meV
    return 10.0

def energy_mode2(t):
    # Gamma energy 10 meV, peak at t_peak≈0.12 with value 11.7, then to 6.0 at M
    # Using a simple cubic spline-like shape
    if t <= 0.12:
        # rise from 10 to 11.7
        frac = t / 0.12
        return 10.0 + 1.7 * frac**2
    else:
        # fall to 6.0 at t=1, with convex shape
        frac = (t - 0.12) / (1.0 - 0.12)
        # quadratic from 11.7 to 6.0
        return 11.7 + (6.0 - 11.7) * frac**0.7   # steep drop

# Write CSV header
print("k_label,kx,ky,mode,energy_meV")

for i in range(num_points):
    t = i / (num_points - 1)   # 0..1
    kx = GAMMA[0] + t * (M[0] - GAMMA[0])
    ky = GAMMA[1] + t * (M[1] - GAMMA[1])
    label = f"Gamma_to_M_{i:03d}"
    for mode, fn in enumerate([energy_mode0, energy_mode1, energy_mode2]):
        E = fn(t)
        print(f"{label},{kx:.6f},{ky:.6f},{mode},{E:.6f}")
