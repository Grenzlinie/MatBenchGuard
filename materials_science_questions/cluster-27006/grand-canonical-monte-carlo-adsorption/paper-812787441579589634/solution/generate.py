#!/usr/bin/env python3
"""Generate reference oracle artifacts for the TBA/TOL nanoconfinement task."""
import sys
import math
import csv

def generate_profile():
    writer = csv.writer(sys.stdout)
    writer.writerow(["composition", "radial_distance_angstrom", "density_TBA", "density_TOL"])

    # radial grid from 0 to 12.0 Å, step 0.2 Å
    r_values = [i*0.2 for i in range(61)]

    # ---- composition x_TBA = 0.49 ----
    for r in r_values:
        # TBA: low in core, Gaussian peak near r=10.5 (wall)
        d_TBA = 0.01 + 0.69 * math.exp(-0.5 * ((r - 10.5) / 1.0) ** 2)
        # TOL: high in core (r < 8), falling off near wall
        # logistic function: core high, wall low
        d_TOL = 0.7 * (1.0 - 1.0 / (1.0 + math.exp(-(r - 8.0) / 0.5)))
        writer.writerow(["0.49", f"{r:.1f}", f"{d_TBA:.6f}", f"{d_TOL:.6f}"])

    # ---- composition x_TBA = 0.71 ----
    for r in r_values:
        # TBA: negligible in core, then rises to a plateau near the wall
        if r <= 8.0:
            d_TBA = 0.01
        elif r <= 9.0:
            d_TBA = 0.01 + (r - 8.0) * (0.7 - 0.01)   # linear to 0.7 at r=9
        elif r <= 11.0:
            d_TBA = 0.7
        elif r <= 12.0:
            d_TBA = 0.7 - (r - 11.0) * (0.7 - 0.01)   # linear down to 0.01 at r=12
        else:
            d_TBA = 0.01
        # TOL: low everywhere, but a small core plateau for completeness
        d_TOL = 0.1 * (1.0 - 1.0 / (1.0 + math.exp(-(r - 8.0) / 0.5)))
        writer.writerow(["0.71", f"{r:.1f}", f"{d_TBA:.6f}", f"{d_TOL:.6f}"])

def generate_shell():
    print("e_shell_angstrom = 4.0")
    print("N_TBA_shell = 56")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: generate.py profile|shell", file=sys.stderr)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "profile":
        generate_profile()
    elif cmd == "shell":
        generate_shell()
    else:
        print(f"Unknown command {cmd}", file=sys.stderr)
        sys.exit(1)