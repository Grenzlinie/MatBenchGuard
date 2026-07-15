#!/usr/bin/env python3
"""Generate a placeholder Ima2 TaReSi structure CIF."""
from pymatgen.core.lattice import Lattice
from pymatgen.core.structure import Structure

# Approximate lattice parameters for Ima2 TaReSi (conventional cell)
lattice = Lattice.from_parameters(11.2, 13.8, 5.2, 90, 90, 90)

# Space group Ima2 (No. 46), all atoms in general 8c positions to get 8 formula units per cell.
# Each 8c site yields 8 atoms; we place three distinct sites for Ta, Re, Si.
# Coordinates are rough but yield a valid Ima2 structure.
species = ["Ta", "Re", "Si"]
coords = [
    [0.1, 0.1, 0.1],
    [0.6, 0.1, 0.1],
    [0.1, 0.6, 0.1]
]

struct = Structure.from_spacegroup("Ima2", lattice, species, coords)
print(struct.to(fmt="cif"))
