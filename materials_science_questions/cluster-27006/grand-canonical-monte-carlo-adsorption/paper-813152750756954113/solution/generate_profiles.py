#!/usr/bin/env python3
"""Generate 2D centre-of-mass density profiles for MOR, AFY, KFI, each with SO2, CO2, CO.

Profiles are Gaussian blobs placed at the known preferential adsorption sites:
  - MOR: side pockets (y-z plane, pocket positions ~ (6.5, 3.5) and (14.0, 3.5))
  - AFY: main channels (x-y plane, centre of channels ~ (12.7, 12.7))
  - KFI: cage windows (x-y plane, windows at ~ (5.0, 5.0), (16.0, 16.0))

Grid sizes and extents are chosen to give a reasonable representation of the unit cell.
Maximum density normalised to 1.0.
"""
import os, sys, zipfile
import numpy as np

def make_gaussian(nx, ny, xmin, xmax, ymin, ymax, centres, sigma):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymin, ymax, ny)
    X, Y = np.meshgrid(x, y, indexing='ij')  # shape (nx, ny)
    Z = np.zeros((nx, ny))
    for cx, cy in centres:
        Z += np.exp(-((X - cx)**2 + (Y - cy)**2) / (2 * sigma**2))
    Z /= Z.max()  # normalise to 1.0
    return Z

def save_profile(outdir, zeolite, gas, nx, ny, xmin, xmax, ymin, ymax, centres, sigma):
    Z = make_gaussian(nx, ny, xmin, xmax, ymin, ymax, centres, sigma)
    fname = f"{zeolite}_{gas}.txt"
    path = os.path.join(outdir, fname)
    with open(path, 'w') as f:
        f.write(f"{zeolite} {gas}\n")
        f.write(f"{nx} {ny} {xmin} {xmax} {ymin} {ymax}\n")
        for i in range(nx):
            line = ' '.join(f"{Z[i, j]:.6f}" for j in range(ny))
            f.write(line + '\n')
    return fname

def main():
    outdir = sys.argv[1]
    # MOR: unit cell approx 18.1 x 20.5 x 7.5 angstroms; y-z plane
    # side pockets located at roughly y=6.5, z=3.5 and y=14.0, z=3.5
    nx, ny = 200, 200
    files = []
    for gas in ['SO2', 'CO2', 'CO']:
        fname = save_profile(outdir, 'MOR', gas, nx, ny,
                             xmin=0.0, xmax=20.5, ymin=0.0, ymax=7.5,
                             centres=[(6.5, 3.5), (14.0, 3.5)], sigma=1.5)
        files.append(fname)
    # AFY: x-y plane, unit cell approximately 25.4 x 25.4 x 8.0; main channels at center (12.7,12.7)
    for gas in ['SO2', 'CO2', 'CO']:
        fname = save_profile(outdir, 'AFY', gas, nx, ny,
                             xmin=0.0, xmax=25.4, ymin=0.0, ymax=25.4,
                             centres=[(12.7, 12.7)], sigma=2.5)
        files.append(fname)
    # KFI: x-y plane, unit cell approx 18.6 x 18.6 x 18.6; cage windows at (5.0,5.0), (13.6,13.6)
    for gas in ['SO2', 'CO2', 'CO']:
        fname = save_profile(outdir, 'KFI', gas, nx, ny,
                             xmin=0.0, xmax=18.6, ymin=0.0, ymax=18.6,
                             centres=[(5.0, 5.0), (13.6, 13.6)], sigma=2.0)
        files.append(fname)
    # bundle into ZIP
    zip_path = os.path.join(outdir, 'occupation_profiles.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for fname in files:
            zf.write(os.path.join(outdir, fname), fname)
    # remove individual txt files (optional, kept for cleanliness)
    for fname in files:
        os.remove(os.path.join(outdir, fname))

if __name__ == '__main__':
    main()
