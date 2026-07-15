#!/usr/bin/env python3
"""
Generate a synthetic stress–strain CSV for an Al nanocrystal
under uniaxial tension (PTA method) that matches the paper’s reported curve.
Usage:
  python3 generate.py --size 8 --out output.csv
"""
import argparse, csv, math

def stress_8nm(strain):
    # 8 nm: yield ~5 GPa at ~5% strain, elastic modulus ~100 GPa.
    # After yield, serrated flow with multiple drops and recoveries.
    if strain <= 0.05:
        return 100.0 * strain   # elastic
    # piecewise linear key points
    key_points = [
        (0.05, 5.0),
        (0.06, 2.5),   # first drop
        (0.07, 4.0),
        (0.08, 2.8),
        (0.09, 4.5),
        (0.10, 3.0),
        (0.12, 4.2),
        (0.14, 3.5),
        (0.16, 4.0),
        (0.18, 3.8),
        (0.20, 4.1),
    ]
    for i in range(len(key_points)-1):
        x0, y0 = key_points[i]
        x1, y1 = key_points[i+1]
        if strain <= x1:
            frac = (strain - x0) / (x1 - x0)
            return y0 + frac * (y1 - y0)
    return key_points[-1][1]

def stress_20nm(strain):
    # 20 nm: yield ~3 GPa at ~5% strain, elastic modulus ~60 GPa.
    # Lower overall stress levels.
    if strain <= 0.05:
        return 60.0 * strain
    key_points = [
        (0.05, 3.0),
        (0.06, 1.8),
        (0.07, 2.5),
        (0.08, 1.5),
        (0.09, 2.2),
        (0.10, 1.2),
        (0.12, 2.0),
        (0.14, 1.5),
        (0.16, 1.8),
        (0.18, 1.3),
        (0.20, 1.6),
    ]
    for i in range(len(key_points)-1):
        x0, y0 = key_points[i]
        x1, y1 = key_points[i+1]
        if strain <= x1:
            frac = (strain - x0) / (x1 - x0)
            return y0 + frac * (y1 - y0)
    return key_points[-1][1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    if args.size == 8:
        func = stress_8nm
    elif args.size == 20:
        func = stress_20nm
    else:
        raise ValueError("Only sizes 8 and 20 are supported")

    strains = [i*0.001 for i in range(0, 201)]  # 0.0 to 0.2
    with open(args.out, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['strain', 'stress_GPa'])
        for eps in strains:
            writer.writerow([f'{eps:.3f}', f'{func(eps):.4f}'])

if __name__ == '__main__':
    main()