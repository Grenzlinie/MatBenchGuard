#!/usr/bin/env python3
import csv
import math
import sys

def gauss(e, center, sigma, amp):
    return amp * math.exp(-0.5 * ((e - center) / sigma) ** 2)

def main(outpath):
    # energy grid
    energies = [-5.0 + i * 0.05 for i in range(261)]  # -5 to 8 eV step 0.05

    # Define atoms/orbitals per layer and synthetic peaks (center, sigma, amplitude)
    # Ti d orbitals: x2-y2, xz, yz, xy, 3z2-r2
    # O p orbitals: x, y, z
    atoms_orbitals = [
        # Layer 0
        (0, "Ti1", "x2-y2", [(2.85, 0.2, 1.5), (3.6, 0.3, 0.8)]),
        (0, "Ti1", "xz",   [(3.05, 0.25, 1.0), (4.0, 0.35, 0.6)]),
        (0, "Ti1", "yz",   [(3.1, 0.25, 1.0)]),
        (0, "Ti1", "xy",   [(3.3, 0.3, 0.7), (5.0, 0.4, 0.4)]),
        (0, "Ti1", "3z2-r2", [(3.4, 0.3, 0.9), (4.2, 0.35, 0.5)]),
        (0, "Ti2", "x2-y2", [(3.2, 0.25, 0.8)]),
        (0, "Ti2", "xz",   [(3.1, 0.25, 1.1)]),
        (0, "Ti2", "yz",   [(3.1, 0.25, 1.1)]),
        (0, "Ti2", "xy",   [(3.5, 0.3, 0.6)]),
        (0, "Ti2", "3z2-r2", [(3.6, 0.3, 0.7)]),
        (0, "O1", "x",  [(-1.0, 0.3, 0.5), (-2.2, 0.3, 0.4)]),
        (0, "O1", "y",  [(-0.8, 0.3, 0.6)]),
        (0, "O1", "z",  [(-1.5, 0.3, 0.5), (-2.5, 0.3, 0.3)]),
        (0, "O2", "x",  [(-1.1, 0.3, 0.5), (-2.3, 0.3, 0.4)]),
        (0, "O2", "y",  [(-0.9, 0.3, 0.6)]),
        (0, "O2", "z",  [(-1.4, 0.3, 0.5), (-2.4, 0.3, 0.3)]),
        # Layer 1
        (1, "O3", "x",  [(-2.55, 0.25, 0.8)]),
        (1, "O3", "y",  [(-2.7, 0.25, 0.5)]),
        (1, "O3", "z",  [(-3.2, 0.25, 0.9)]),
        # Layer 2
        (2, "O4", "x",  [(-2.6, 0.3, 0.5)]),
        (2, "O4", "y",  [(-2.8, 0.3, 0.3)]),
        (2, "O4", "z",  [(-3.15, 0.3, 0.6)]),
    ]

    with open(outpath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["layer", "atom", "orbital", "energy", "dos"])
        for layer, atom, orb, peaks in atoms_orbitals:
            for e in energies:
                dos = sum(gauss(e, c, s, a) for c, s, a in peaks)
                # Force oxygen DOS in the band gap [0, 3] eV to be negligible
                if atom.startswith("O") and 0.0 <= e <= 3.0:
                    dos = 0.0
                writer.writerow([layer, atom, orb, f"{e:.6f}", f"{dos:.8f}"])

    print(f"Written {outpath}")

if __name__ == "__main__":
    main(sys.argv[1])
