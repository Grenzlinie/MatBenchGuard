#!/usr/bin/env python3
"""Generate CNT volume fraction histograms for the oracle.

Usage:
    python generate_histograms.py --type {initial,evolved} --output <file.csv>
"""
import argparse
import csv
import math

def make_initial_histogram(cell_z_nm=3000.0, bin_width_nm=10.0, avg_volfrac=0.005):
    """Return list of (z_center, volume_fraction) uniform distribution."""
    num_bins = int(cell_z_nm / bin_width_nm)
    data = []
    for i in range(num_bins):
        z_center = (i + 0.5) * bin_width_nm
        data.append((z_center, avg_volfrac))
    return data

def make_evolved_histogram(cell_z_nm=3000.0, bin_width_nm=10.0, avg_volfrac=0.005):
    """Return list of (z_center, volume_fraction) with near‑wall enrichment and subsurface dip.

    The profile is symmetric with respect to the two walls: peaks at each wall,
    a depletion zone 30‑100 nm from the wall, and a smooth return to the average.
    """
    num_bins = int(cell_z_nm / bin_width_nm)
    data = []
    for i in range(num_bins):
        z_center = (i + 0.5) * bin_width_nm
        # distance to the nearest confining wall
        d_to_wall = min(z_center, cell_z_nm - z_center)
        if d_to_wall <= 30.0:
            # Linear decrease from 0.015 at wall to 0.010 at 30 nm
            volfrac = 0.015 - 0.005 * (d_to_wall / 30.0)
        elif d_to_wall <= 100.0:
            # Depleted layer with low volume fraction
            volfrac = 0.0025
        elif d_to_wall <= 200.0:
            # Ramp back to the average value
            volfrac = 0.0025 + (avg_volfrac - 0.0025) * ((d_to_wall - 100.0) / 100.0)
        else:
            volfrac = avg_volfrac
        data.append((z_center, volfrac))
    return data

def write_histogram(output_path, rows):
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['z_bin_center', 'volume_fraction'])
        for z, v in rows:
            writer.writerow([f"{z:.6f}", f"{v:.6f}"])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', required=True, choices=['initial', 'evolved'])
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    if args.type == 'initial':
        rows = make_initial_histogram()
    else:
        rows = make_evolved_histogram()
    write_histogram(args.output, rows)