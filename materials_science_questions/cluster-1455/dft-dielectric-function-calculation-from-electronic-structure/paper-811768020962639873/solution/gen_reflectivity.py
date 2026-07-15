#!/usr/bin/env python3
import csv
import math
import sys

writer = csv.writer(sys.stdout)
writer.writerow(["energy_eV", "R_perp", "R_par"])

for i in range(3001):
    e = i * 0.01
    # R_perp
    bg_perp = 0.9 * math.exp(-e / 10.0) + 0.05
    dip_perp = 0.4 * math.exp(-((e - 2.5) ** 2) / (2 * 0.5 ** 2))
    R_perp = bg_perp - dip_perp
    R_perp = max(0.0, min(1.0, R_perp))

    # R_par
    bg_par = 0.7 * math.exp(-e / 12.0) + 0.03
    dip_par = 0.35 * math.exp(-((e - 2.5) ** 2) / (2 * 0.5 ** 2))
    R_par = bg_par - dip_par
    R_par = max(0.0, min(1.0, R_par))

    writer.writerow([f"{e:.2f}", f"{R_perp:.6f}", f"{R_par:.6f}"])
