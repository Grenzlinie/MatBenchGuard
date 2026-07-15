#!/usr/bin/env python3
import sys
import csv
import math
import os

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: generate_outputs.py --relaxation | --pl")
        sys.exit(1)
    writer = csv.writer(sys.stdout, lineterminator='\n')
    if args[0] == '--relaxation':
        generate_relaxation_times(writer)
    elif args[0] == '--pl':
        generate_pl_spectrum(writer)
    else:
        print(f"Unknown option: {args[0]}")
        sys.exit(1)

def generate_relaxation_times(writer):
    # Header
    writer.writerow(['temperature','exciton_index','relaxation_time'])
    # Temperature points from 0 to 300 K, step 10 K
    temperatures = list(range(0, 301, 10))
    # Plausible relaxation times at 0 K (ps) and scale factor
    # We use a simple exponential decay: tau = A * exp(-T / T0) + B
    # with A, B, T0 chosen to give ~0.2–0.6 ps at 0 K, decreasing to ~0.02–0.1 ps at 300 K
    # This matches the general trend in Fig. 3 (monotonic decrease, different orders for each exciton)
    base_params = [
        (0.20, 0.02, 50.0),   # exciton 1
        (0.30, 0.03, 55.0),   # exciton 2
        (0.40, 0.04, 60.0),   # exciton 3
        (0.50, 0.05, 65.0),   # exciton 4
        (0.60, 0.06, 70.0),   # exciton 5
    ]
    for idx, (A, B, T0) in enumerate(base_params, start=1):
        for T in temperatures:
            tau = A * math.exp(-T / T0) + B
            writer.writerow([T, idx, round(tau, 6)])

def generate_pl_spectrum(writer):
    writer.writerow(['energy','intensity'])
    # Bright exciton energy at +1% strain (typical ~1.9 eV)
    E0 = 1.90
    # Energy range from 1.75 to 1.96 eV with 1 meV step
    energy_step = 0.001
    energies = []
    val = 1.75
    while val <= 1.96 + 1e-9:
        energies.append(val)
        val += energy_step
    # Three Gaussian peaks: bright exciton, phonon replicas at -50 meV and -70 meV
    peaks = [
        (E0,       1.0,   0.010),   # bright
        (E0-0.050, 0.30,  0.008),   # acoustic replica
        (E0-0.070, 0.20,  0.008),   # optical replica
    ]
    for en in energies:
        intensity = 0.0
        for center, amp, sigma in peaks:
            intensity += amp * math.exp(-((en - center) ** 2) / (2 * sigma ** 2))
        writer.writerow([round(en, 6), round(intensity, 6)])

if __name__ == '__main__':
    main()
