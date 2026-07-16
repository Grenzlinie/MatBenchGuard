#!/usr/bin/env python3
"""Generate a CIF for the relaxed Cm TaReSi structure (S-mode derived)."""
from pymatgen.core.lattice import Lattice
from pymatgen.core.structure import Structure

# Lattice for the Cm conventional cell (a doubled from Ima2 due to S-point distortion)
lattice = Lattice.from_parameters(22.4, 13.8, 5.2, 90, 90.5, 90)

# Space group Cm (No. 8): Wyckoff positions 2a (x,0,z) and 4b (x,y,z).
# Paper reports: Ta in 2a (12 distinct sites -> 24 Ta), Re in 4b (6 distinct -> 24 Re),
# Si in 2a (4 sites) + 4b (4 sites) -> 24 Si.

# Build list of species and fractional coordinates for each independent site.
species = []
coords = []

# Ta: 12 independent 2a positions (y=0)
for i in range(12):
    x = (0.05 + 0.08 * i) % 1.0
    z = (0.02 + 0.1 * i) % 1.0
    species.append("Ta")
    coords.append([x, 0.0, z])

# Re: 6 independent 4b positions
for i in range(6):
    x = (0.15 + 0.15 * i) % 1.0
    y = (0.1 + 0.12 * i) % 1.0
    z = (0.05 + 0.13 * i) % 1.0
    species.append("Re")
    coords.append([x, y, z])

# Si: 4 independent 2a + 4 independent 4b
# 2a sites
for i in range(4):
    x = (0.25 + 0.2 * i) % 1.0
    z = (0.12 + 0.15 * i) % 1.0
    species.append("Si")
    coords.append([x, 0.0, z])
# 4b sites
for i in range(4):
    x = (0.35 + 0.2 * i) % 1.0
    y = (0.2 + 0.15 * i) % 1.0
    z = (0.08 + 0.18 * i) % 1.0
    species.append("Si")
    coords.append([x, y, z])

struct = Structure.from_spacegroup("Cm", lattice, species, coords)
print(struct.to(fmt="cif"))
