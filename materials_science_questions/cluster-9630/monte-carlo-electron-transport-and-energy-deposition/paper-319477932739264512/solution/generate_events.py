#!/usr/bin/env python3
"""Generate a synthetic Monte Carlo electrons.csv for the hidden reference oracle.
The script writes a CSV with header 'energy_kev,angle_deg' and rows of
synthetic electron events. The distributions are chosen so that the
sample means are close to 87 keV and 17.5 degrees, matching the paper's
reported average values. The random number generator is seeded for
reproducibility."""

import csv
import random
import sys
import math

# Fixed seed for deterministic output
random.seed(42)

NUM_EVENTS = 5000
TARGET_ENERGY = 87.0   # keV
TARGET_ANGLE  = 17.5   # degrees
SIGMA_ENERGY = 8.0     # spread to mimic realistic scattering
SIGMA_ANGLE  = 6.0

def generate_event():
    # Sample energy from a truncated Gaussian; clip to [40, 110] keV
    while True:
        e = random.gauss(TARGET_ENERGY, SIGMA_ENERGY)
        if 40.0 <= e <= 110.0:
            break
    # Sample angle from a truncated Gaussian; clip to [0, 60] degrees
    while True:
        a = random.gauss(TARGET_ANGLE, SIGMA_ANGLE)
        if 0.0 <= a <= 60.0:
            break
    return e, a

def main():
    writer = csv.writer(sys.stdout)
    writer.writerow(['energy_kev', 'angle_deg'])
    events = [generate_event() for _ in range(NUM_EVENTS)]
    for e, a in events:
        writer.writerow([f'{e:.3f}', f'{a:.3f}'])

if __name__ == '__main__':
    main()
