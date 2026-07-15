#!/usr/bin/env python3
import csv
import sys

# Target bulk modulus B in GPa, equilibrium volume V0 in Å^3
# B_eV_A3 = B_GPa / 160.218 (since 1 eV/Å^3 = 160.218 GPa)
# Quadratic E = c*(V - V0)^2 + E0,  where c = B_eV_A3 / (2*V0)
# We set E0 negative and large but irrelevant to curvature.

combinations = [
    # material, symmetry, xc, B_GPa, V0_ang3
    ("Si60", "Ih", "LDA", 168, 640),
    ("Si60", "Ih", "GGA", 156, 650),
    ("Si60", "C2h", "LDA", 147, 640),
    ("Si60", "C2h", "GGA", 133, 650),
    ("Si60", "C1", "LDA", 140, 640),
    ("Si60", "C1", "GGA", 128, 650),
    ("bulk_Si", "bulk", "LDA", 97, 157.7),
    ("bulk_Si", "bulk", "GGA", 89, 161.9),
    ("Ge60", "Ih", "LDA", 102, 690),
    ("Ge60", "C2h", "LDA", 97, 690),
    ("Ge60", "C2h", "GGA", 82, 700),
    ("Ge60", "C1", "LDA", 97, 690),
    ("Ge60", "C1", "GGA", 80, 700),
    ("bulk_Ge", "bulk", "LDA", 69, 181),
    ("bulk_Ge", "bulk", "GGA", 58, 185),
]

writer = csv.writer(sys.stdout)
writer.writerow(["material", "symmetry", "xc", "volume_ang3", "total_energy_eV"])

fracs = [-0.03, -0.02, -0.01, 0.0, 0.01, 0.02, 0.03]
conv = 160.218  # GPa per eV/Å^3

for mat, sym, xc, B_GPa, V0 in combinations:
    B_eV_A3 = B_GPa / conv
    c = B_eV_A3 / (2.0 * V0)
    # Choose a base energy that is roughly proportional to number of atoms
    if "bulk" in mat:
        E0 = -100.0
    else:
        E0 = -600.0
    for f in fracs:
        V = V0 * (1.0 + f)
        E = c * (V - V0)**2 + E0
        writer.writerow([mat, sym, xc, f"{V:.6f}", f"{E:.6f}"])
