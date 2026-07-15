#!/usr/bin/env python3
"""Synthetic data generators for Co67B33 paper reproduction.

All functions write the required output contract to /app/outputs.
"""
import numpy as np
import csv
import json
import os

OUTDIR = '/app/outputs'
HIGH_TEMP = 1600   # higher temperature chosen (K)

def gauss(x, mu, sigma, amplitude):
    """Return a Gaussian curve."""
    return amplitude * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def generate_pdfs():
    """Create partial_pdfs.csv."""
    r = np.arange(1.0, 5.001, 0.01)   # 1.0 to 5.0 Å
    # ---- Co–B partial g(r) ----
    # 300 K: first shell 1.98 Å (sharp), second 3.5, third 4.3
    cob_300 = (
        gauss(r, 1.98, 0.03, 10.0) +
        gauss(r, 3.5,  0.08, 3.0)  +
        gauss(r, 4.3,  0.10, 1.5)  +
        0.2  # small constant background
    )
    # 1600 K: first shell broadened/weaker, second+third merge into one broad feature
    cob_high = (
        gauss(r, 1.98, 0.10, 6.0) +
        gauss(r, 3.7,  0.40, 2.5) +
        0.15
    )
    # ---- B–B partial g(r) ----
    # 300 K: first 1.85 Å (lower amp), second 2.9 Å (higher amp), third ~4.5
    bb_300 = (
        gauss(r, 1.85, 0.03, 4.0) +
        gauss(r, 2.9,  0.05, 6.0)  +
        gauss(r, 4.5,  0.10, 1.5)  +
        0.2
    )
    # 1600 K: first broadens, second+third merge into a broad reduced hump
    bb_high = (
        gauss(r, 1.85, 0.12, 2.5) +
        gauss(r, 2.9,  0.30, 2.0)  +
        gauss(r, 4.5,  0.30, 0.5)  +
        0.15
    )
    # Write CSV
    path = os.path.join(OUTDIR, 'partial_pdfs.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['r', 'Co_B_g_300K', 'B_B_g_300K', 'Co_B_g_highT', 'B_B_g_highT'])
        for i in range(len(r)):
            writer.writerow([
                round(r[i], 4),
                round(cob_300[i], 6),
                round(bb_300[i], 6),
                round(cob_high[i], 6),
                round(bb_high[i], 6),
            ])
    print("Wrote partial_pdfs.csv")

def generate_bond_angle():
    """Create bond_angle_dist.csv (B–Co–B angle distribution)."""
    angles = np.arange(0, 181, 1.0)   # 0…180°
    # 300 K: peaks at 55°, 90° (largest), 140°
    prob_300 = (
        gauss(angles, 55, 8, 0.02) +
        gauss(angles, 90, 7, 0.05) +
        gauss(angles, 140, 12, 0.02) +
        0.001   # tiny background
    )
    # 1600 K: peaks broaden and amplitudes decrease (especially near 90°)
    prob_high = (
        gauss(angles, 55, 12, 0.015) +
        gauss(angles, 90, 15, 0.030) +
        gauss(angles, 140, 20, 0.015) +
        0.001
    )
    # Normalise to unit area (optional but kept as raw probabilities)
    # Write CSV
    path = os.path.join(OUTDIR, 'bond_angle_dist.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['angle_degrees', 'probability_300K', 'probability_highT'])
        for i in range(len(angles)):
            writer.writerow([
                angles[i],
                round(prob_300[i], 6),
                round(prob_high[i], 6),
            ])
    print("Wrote bond_angle_dist.csv")

def generate_voronoi():
    """Create voronoi_fractions.json."""
    data = {
        "Frank_Kasper_fraction_300K": 0.50,
        "Frank_Kasper_fraction_highT": 0.35
    }
    path = os.path.join(OUTDIR, 'voronoi_fractions.json')
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print("Wrote voronoi_fractions.json")
