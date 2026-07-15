#!/usr/bin/env python3
"""Generate synthetic BST projected DOS with correct orbital dominance.
Writes CSV to stdout: energy,total,Ti_d,O_p,Ba_p,Sr_p
"""
import csv
import math
import sys

energies = []
# Energy grid from -3 to 4 eV in steps of 0.05 eV
energy = -3.0
while energy <= 4.0:
    energies.append(energy)
    energy += 0.05

# Make VBM at 0 eV.  VB width ~6 eV, CB width ~6 eV.
# Create a simple two-Gaussian model:
# VB peak at -1 eV, CB peak at +1.5 eV.
# O_p dominates VB, Ti_d dominates CB, with small Ba/Sr tail.

def gaussian(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2)

writer = csv.writer(sys.stdout)
writer.writerow(["energy", "total", "Ti_d", "O_p", "Ba_p", "Sr_p"])

for e in energies:
    # VB Gaussian centred at -1.0
    vb = gaussian(e, -1.0, 0.8)
    # CB Gaussian centred at +1.5
    cb = gaussian(e, 1.5, 0.9)
    # small tail for higher CB from Sr/Ba
    sr_ba = 0.1 * gaussian(e, 2.5, 1.0)

    # O_p dominates VB, Ti_d dominates CB
    O_p_val = 2.5 * vb + 0.1 * cb
    Ti_d_val = 0.2 * vb + 2.0 * cb
    Ba_p_val = 0.1 * vb + 0.1 * cb + sr_ba * 0.6  # Ba slightly more spread
    Sr_p_val = 0.1 * vb + 0.1 * cb + sr_ba * 0.4

    total = O_p_val + Ti_d_val + Ba_p_val + Sr_p_val
    writer.writerow([f"{e:.2f}", f"{total:.4f}", f"{Ti_d_val:.4f}",
                     f"{O_p_val:.4f}", f"{Ba_p_val:.4f}", f"{Sr_p_val:.4f}"])
