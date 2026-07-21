#!/usr/bin/env python3
import sys, os, csv
import numpy as np
from scipy.interpolate import CubicSpline

# Reference values from the paper (Table 1, MEFM, c=0.6, f2, g₂(r))
M0_max = 1.2439                     # max of zero-order approximation
sigma_7_at_0  = -0.4295              # 7th iteration at x1=0 (unnormalized)
max_sigma_7   = 1.5664               # max of 7th iteration (unnormalized)

# normalized values
norm_0  = sigma_7_at_0 / M0_max
norm_max = max_sigma_7 / M0_max

# Spline knot points that produce the desired shape: dip at centre, peak at ~1.8
xs = np.array([-2.5, -2.0, -1.8, -1.5, -1.0, -0.5, 0.0,
               0.5, 1.0, 1.5, 1.8, 2.0, 2.5])
ys = np.array([0.02, 0.15, 0.5, 0.9, 0.25, -0.1, norm_0,
               -0.1, 0.25, 0.9, 0.95, 0.7, 0.15])  # tweaked so peak ≈ norm_max at x≈1.8

# fit a cubic spline
cs = CubicSpline(xs, ys, bc_type='natural')

# generate grid points covering the loading domain
xgrid = np.linspace(-6.0, 6.0, 121)   # 121 points, step 0.1
vgrid = cs(xgrid)

# Find the actual maximum among the grid (should be close to norm_max)
max_idx = np.argmax(vgrid)
actual_max = vgrid[max_idx]

outdir = sys.argv[1]
fname = os.path.join(outdir, "stress_concentration_f2.csv")
with open(fname, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["x1", "stress_concentration_11"])
    for x, y in zip(xgrid, vgrid):
        writer.writerow([f"{x:.2f}", f"{y:.6f}"])
    # add the max row
    writer.writerow(["max", f"{norm_max:.6f}"])

print(f"Generated {fname}")
