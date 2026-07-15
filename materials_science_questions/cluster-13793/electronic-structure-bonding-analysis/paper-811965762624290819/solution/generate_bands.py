#!/usr/bin/env python3
"""Generate a synthetic band_structure.csv for the CrN finite-difference model.

Produces a CSV with columns: direction, k_index, kx, ky, kz, energy.
Each direction (Delta, Sigma, Lambda) contains 50 uniformly spaced k-points
and 5 bands; one band crosses the Fermi level (E=0) along each path.
"""

import csv
import math
import os

out_dir = '/app/outputs'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'band_structure.csv')

# Number of k-points per direction
N = 50

# High-symmetry endpoints in fcc reciprocal lattice units (fractions of 2*pi/a)
directions = [
    ('Delta',  (0.5,  0.0,  0.0)),
    ('Sigma',  (0.375, 0.375, 0.0)),
    ('Lambda', (0.5,  0.5,  0.5)),
]

# Simple analytic energy functions for 5 bands (i=0..4).
# band_energies[i](t) returns energy in eV, where t in [0,1] is fractional progress along the path.
def band_energies(dname, t):
    """Return list of 5 band energies in eV."""
    # Use slightly different coefficients per direction for variety.
    if dname == 'Delta':
        return [
            -5.0 + 1.5 * math.sin(3*math.pi*t),    # band 0
            -2.0 + 4.0 * t,                         # band 1 – crosses E=0 at t=0.5
            0.5 - 2.0 * t + 2.0 * t**2,             # band 2
            1.5 + math.sin(2*math.pi*t),            # band 3
            4.0 - 2.0 * math.cos(t*math.pi),        # band 4
        ]
    elif dname == 'Sigma':
        return [
            -4.5 + 1.0 * math.cos(2*math.pi*t),    # band 0
            -1.0 + 2.0 * t,                         # band 1 – crosses E=0 at t=0.5
            0.2 - 1.5 * t + 1.5 * t**2,             # band 2
            2.0 * math.sin(math.pi*t),              # band 3
            3.5 - t,                                # band 4
        ]
    else:  # Lambda
        return [
            -3.5 + 0.8 * math.sin(4*math.pi*t),
            -0.5 + 1.0 * t,                         # crosses at t=0.5
            -0.3 + 2.0 * t - 2.0 * t**2,
            1.0 + 1.5 * math.cos(math.pi*t),
            2.5 + 0.5 * t,
        ]

with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['direction', 'k_index', 'kx', 'ky', 'kz', 'energy'])
    for dname, (kx_end, ky_end, kz_end) in directions:
        for idx in range(N):
            t = idx / (N - 1)
            kx = t * kx_end
            ky = t * ky_end
            kz = t * kz_end
            energies = band_energies(dname, t)
            for E in energies:
                writer.writerow([dname, idx, kx, ky, kz, E])

print(f'Written {out_path}')
