#!/usr/bin/env python3
"""Generate cs_bicrystal.xyz for Σ5(013)[100] tilt boundary in Al (Morse params).
Rotation axis [100] (x), misorientation 36.87°, dimensions 80a×20a×40a.
The bicrystal is built by placing two fcc slabs, each rotated by ±θ/2 about x,
and selecting atoms inside the block."""
import math, sys

# Lattice constant and basis
a = 4.05  # Å
r1 = 0.707 * a  # ≈2.8635 Å (not used here)

# Dimensions in units of a
Nx = 80   # along boundary plane (x)
Ny = 20   # along misorientation axis (y)
Nz = 40   # perpendicular to boundary plane (z); total from -20a to +20a

# Rotations: half angle = 36.87°/2 = 18.435°
theta2 = math.radians(18.435)
cos_t = math.cos(theta2)
sin_t = math.sin(theta2)

# fcc basis positions (conventional cubic cell)
basis = [
    (0.0, 0.0, 0.0),
    (0.0, 0.5, 0.5),
    (0.5, 0.0, 0.5),
    (0.5, 0.5, 0.0)
]

def rotate_x(px, py, pz, cos_t, sin_t):
    """Rotate point by +angle about x-axis."""
    ny = cos_t * py - sin_t * pz
    nz = sin_t * py + cos_t * pz
    return (px, ny, nz)

def generate_slab(x_min, x_max, y_min, y_max, z_min, z_max, cos_t, sin_t):
    atoms = []
    # Loop over unit cells
    ix0 = int(math.floor(x_min))
    ix1 = int(math.ceil(x_max))
    iy0 = int(math.floor(y_min))
    iy1 = int(math.ceil(y_max))
    iz0 = int(math.floor(z_min))
    iz1 = int(math.ceil(z_max))
    for ix in range(ix0, ix1):
        for iy in range(iy0, iy1):
            for iz in range(iz0, iz1):
                for bx, by, bz in basis:
                    px = (ix + bx) * a
                    py = (iy + by) * a
                    pz = (iz + bz) * a
                    # rotate
                    rx, ry, rz = rotate_x(px, py, pz, cos_t, sin_t)
                    # check bounds
                    if x_min <= rx <= x_max and y_min <= ry <= y_max and z_min <= rz <= z_max:
                        atoms.append((rx, ry, rz))
    return atoms

# Define block (Cartesian)
x_min, x_max = 0.0, Nx * a
y_min, y_max = 0.0, Ny * a
z_half = (Nz/2) * a

# Slab 1: rotated by +theta2 (upper half, z from 0 to +20a)
slab1 = generate_slab(x_min, x_max, y_min, y_max, 0.0, z_half, cos_t, sin_t)
# Slab 2: rotated by -theta2 (lower half, z from -20a to 0)
slab2 = generate_slab(x_min, x_max, y_min, y_max, -z_half, 0.0, cos_t, -sin_t)

all_atoms = slab1 + slab2

# Write XYZ
print(len(all_atoms))
print("CSL bicrystal Al Σ5(013)[100] tilt boundary")
for x, y, z in all_atoms:
    print(f"Al {x:.6f} {y:.6f} {z:.6f}")
