#!/usr/bin/env python3
"""Generate ZT CSV files for the ordered alternating DNA ladder.

Synthesises a transmission function modelled as two Fano resonances
at the inner band edges, then evaluates ZT via Landauer integrals.
"""
import argparse
import csv
import math

# Physical constants
K_B = 8.617333262145e-5  # eV/K

# Energy grid
EMIN, EMAX, DE = -3.0, 3.0, 0.01
E_GRID = [round(EMIN + i * DE, 10) for i in range(int((EMAX - EMIN) / DE) + 1)]

# Transmission function parameters (Fano model)
# Two resonances: left band and right band
A_AMP = 0.01          # overall amplitude
WIDTH = 0.02          # Fano width (eV)
Q_LEFT = -1.0
Q_RIGHT = 1.0
ZERO_LEFT = -1.0      # location of the zero for left band (inner edge)
ZERO_RIGHT = 1.0      # location of the zero for right band (inner edge)
BACKGROUND = 0.001    # small constant background conductance

def center_from_zero(zero, q, width):
    """Return the Fano centre such that T(E)=0 at E=zero."""
    return zero - q * width

CENTER_LEFT = center_from_zero(ZERO_LEFT, Q_LEFT, WIDTH)
CENTER_RIGHT = center_from_zero(ZERO_RIGHT, Q_RIGHT, WIDTH)

def fano(e, center, width, q):
    """Fano profile: (q+eps)^2/(1+eps^2) where eps=(e-center)/width."""
    eps = (e - center) / width
    return (q + eps) ** 2 / (1.0 + eps ** 2)

def transmission(e):
    """Total transmission probability."""
    t = BACKGROUND
    t += A_AMP * fano(e, CENTER_LEFT, WIDTH, Q_LEFT)
    t += A_AMP * fano(e, CENTER_RIGHT, WIDTH, Q_RIGHT)
    return t

def landauer_zt(Ef, T):
    """Compute ZT for a single Fermi energy and temperature."""
    kT = K_B * T
    L0 = L1 = L2 = 0.0
    for E in E_GRID:
        TE = transmission(E)
        if TE <= 0.0:
            continue
        arg = (E - Ef) / kT
        # Avoid overflow in exp(arg)
        if arg > 50.0:
            fderiv = 0.0
        elif arg < -50.0:
            fderiv = 0.0
        else:
            exp_part = math.exp(arg)
            fderiv = exp_part / (kT * (1.0 + exp_part) ** 2)
        # dE weight
        w = DE * fderiv
        diff = E - Ef
        L0 += TE * w
        L1 += TE * diff * w
        L2 += TE * diff * diff * w

    # Avoid division by zero
    if L1 == 0.0 or abs(L1) < 1e-30:
        return 0.0
    denom = (L0 * L2) / (L1 * L1) - 1.0
    if denom <= 0.0:
        return 0.0
    return 1.0 / denom

def write_single_temperature(filename, T):
    """Write CSV with columns Ef (eV), ZT."""
    with open(filename, 'w', newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(['Ef (eV)', 'ZT'])
        for Ef in E_GRID:
            zt = landauer_zt(Ef, T)
            writer.writerow([f"{Ef:.4f}", f"{zt:.6f}"])

def write_multi_temperature(filename, temperatures):
    """Write CSV with columns Ef (eV), ZT_200K, ZT_300K, ZT_400K."""
    # temperatures expected as list of ints (200,300,400)
    with open(filename, 'w', newline='') as fh:
        writer = csv.writer(fh)
        cols = ['Ef (eV)'] + [f"ZT_{T}K" for T in temperatures]
        writer.writerow(cols)
        zt_data = {T: [] for T in temperatures}
        for Ef in E_GRID:
            for T in temperatures:
                zt_data[T].append(landauer_zt(Ef, T))
        for i, Ef in enumerate(E_GRID):
            row = [f"{Ef:.4f}"]
            for T in temperatures:
                row.append(f"{zt_data[T][i]:.6f}")
            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--temp', type=int, default=None,
                        help='Build zt_ordered_<temp>K.csv')
    parser.add_argument('--all', action='store_true',
                        help='Build zt_ordered_temperatures.csv at 200,300,400 K')
    parser.add_argument('--output', required=True, help='Output CSV path')
    args = parser.parse_args()

    if args.temp is not None:
        write_single_temperature(args.output, args.temp)
    elif args.all:
        write_multi_temperature(args.output, [200, 300, 400])
    else:
        raise SystemExit("Specify --temp or --all")

if __name__ == '__main__':
    main()
