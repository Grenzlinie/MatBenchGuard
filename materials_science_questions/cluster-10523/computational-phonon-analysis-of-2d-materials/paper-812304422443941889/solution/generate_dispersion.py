#!/usr/bin/env python3
"""Generate synthetic phonon dispersion CSVs for the 2D Peierls phase.

Pattern (a): 8 branches, gap at q=16 (π/2).
Pattern (b): 16 branches, gaps at q=0 and q=8 (π/4, …).
"""

import csv
import sys
import os
import argparse


def write_dispersion(pattern: str, outpath: str) -> None:
    if pattern == 'a':
        qmax = 16
        n_branches = 8
        # Start values at q=0 (sorted)
        start_raw = [0.0, 0.2, 0.4, 0.6, 5.0, 5.2, 5.4, 5.6]
        # End values at q=16 → gap between index 3 (2.7) and index 4 (7.4)
        end_raw   = [0.4, 1.3, 2.0, 2.7, 7.4, 9.0, 10.6, 12.0]
    else:  # pattern 'b'
        qmax = 8
        n_branches = 16
        # Start values at q=0 – small gap between index 7 (1.0) and index 8 (1.5)
        start_raw = [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.0,
                     1.5, 1.7, 2.5, 2.7, 3.0, 3.3, 3.6, 4.0]
        # End values at q=8 – larger gap between index 7 (2.0) and index 8 (6.0)
        end_raw   = [0.5, 0.7, 1.0, 1.3, 1.6, 1.9, 2.0, 2.0,
                     6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5]

    start_raw.sort()
    end_raw.sort()

    fieldnames = ['q'] + [f'omega2_{i}' for i in range(n_branches)]

    with open(outpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for q in range(qmax + 1):
            frac = q / qmax
            row_vals = [start_raw[i] + (end_raw[i] - start_raw[i]) * frac
                        for i in range(n_branches)]
            row_vals.sort()
            row = {'q': q}
            for i in range(n_branches):
                row[f'omega2_{i}'] = f'{row_vals[i]:.6f}'
            writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate dispersion CSV')
    parser.add_argument('-p', '--pattern', required=True, choices=['a', 'b'])
    parser.add_argument('-o', '--outfile', required=True)
    args = parser.parse_args()
    write_dispersion(args.pattern, args.outfile)
