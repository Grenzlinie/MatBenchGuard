#!/usr/bin/env python3
"""Generate a depth‑resolved energy deposition CSV.

Shape model: f(x) = (x / peak_nm)^a * exp(-b*x) with b = a / peak_nm.
The profile is scaled so that the sum of deposited energies over the first 800 nm
(in steps of 8 nm) equals the given total_energy (eV per incident electron).
"""
import csv
import math
import sys

def main():
    peak_nm = float(sys.argv[1])
    a = float(sys.argv[2])
    total_ev = float(sys.argv[3])
    outpath = sys.argv[4]

    depths = [i * 8.0 for i in range(101)]   # 0, 8, ..., 800 nm
    b = a / peak_nm

    vals = []
    for x in depths:
        if x == 0.0 and a < 0.0:
            v = 0.0
        else:
            v = (x ** a) * math.exp(-b * x)
        vals.append(v)

    s = sum(vals)
    if s == 0.0:
        raise ValueError('Sum of profile values is zero')
    scale = total_ev / s
    vals = [v * scale for v in vals]

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['depth_nm', 'energy_deposition_eV_per_electron'])
        for d, v in zip(depths, vals):
            writer.writerow([d, round(v, 6)])

if __name__ == '__main__':
    main()
