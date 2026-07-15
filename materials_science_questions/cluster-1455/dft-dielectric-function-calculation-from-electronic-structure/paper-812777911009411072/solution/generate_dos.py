#!/usr/bin/env python3
import sys

# Half-metallic DOS: spin-up has a gap around Ef (energy between -0.2 and 0.2 eV = 0),
# spin-down is metallic (constant non-zero DOS).
# Energy range -5 to 5 eV, step 0.05 eV (<0.1 eV spacing).

header = "Energy(eV)\tDOS_up\tDOS_down"
print(header)

step = 0.05
energy = -5.0
while energy <= 5.0 + 1e-12:
    if abs(energy) < 0.2:
        dos_up = 0.0
    else:
        dos_up = 1.0
    dos_down = 1.0
    print(f"{energy:.6f}\t{dos_up:.6f}\t{dos_down:.6f}")
    energy += step
