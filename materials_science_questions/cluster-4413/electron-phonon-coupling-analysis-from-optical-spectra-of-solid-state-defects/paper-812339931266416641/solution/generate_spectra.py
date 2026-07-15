#!/usr/bin/env python3
"""Synthesise a vibronic spectrum as a sum of two Lorentzian lines."""
import argparse
import csv
import math

def lorentzian(e, e0, height, hwhm):
    """Return Lorentzian value at energy e (cm-1).

    Parameters
    ----------
    height : float
        Desired peak height at e0.
    hwhm : float
        Half-width at half-maximum (cm-1).  The full area under the
        line equals height * π * hwhm.
    """
    gamma = hwhm
    return height * (gamma * gamma) / ((e - e0) ** 2 + gamma * gamma)

def main():
    parser = argparse.ArgumentParser(description='Generate a two-line spectrum')
    parser.add_argument('--low', type=float, required=True, help='Start energy (cm-1)')
    parser.add_argument('--high', type=float, required=True, help='End energy (cm-1)')
    parser.add_argument('--step', type=float, required=True, help='Energy step (cm-1)')
    parser.add_argument('--center1', type=float, required=True, help='Center of line 1 (cm-1)')
    parser.add_argument('--height1', type=float, required=True, help='Peak height of line 1')
    parser.add_argument('--hwhm1', type=float, required=True, help='HWHM of line 1 (cm-1)')
    parser.add_argument('--center2', type=float, required=True, help='Center of line 2 (cm-1)')
    parser.add_argument('--height2', type=float, required=True, help='Peak height of line 2')
    parser.add_argument('--hwhm2', type=float, required=True, help='HWHM of line 2 (cm-1)')
    parser.add_argument('--outfile', required=True, help='Output CSV file')
    parser.add_argument('--title', default='', help='Optional comment (not used)')
    args = parser.parse_args()

    with open(args.outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy', 'intensity'])
        e = args.low
        while e <= args.high + 1e-9:
            intensity = (lorentzian(e, args.center1, args.height1, args.hwhm1) +
                         lorentzian(e, args.center2, args.height2, args.hwhm2))
            writer.writerow([f'{e:.1f}', f'{intensity:.6e}'])
            e += args.step

if __name__ == '__main__':
    main()