#!/usr/bin/env python3
import csv, math

# Target measured spacing d = 11.9 a (atomistic result for Cu).
# We model the displacement profile with two arctan sigmoids:
#   delta_u_x(x) = (atan((x - x1)/w) + atan((x - x2)/w) + π) / π
# where x1, x2 are the centers of the two Shockley partials.
# For w=1.5 a, the measured d' (distance between points where
# delta=1/3 and 4/3) is approximately d - 2*0.577*w.  To
# obtain d' = 11.9a we set the center separation to
# d_centers = 11.9 + 2*0.577*1.5 ≈ 13.631 a.
d_meas = 11.9
w_core  = 1.5
delta_w = 0.577 * 2.0  # empirical correction factor
center_half_sep = (d_meas + delta_w * w_core) / 2.0  # ≈ 6.8155
x1 = -center_half_sep
x2 =  center_half_sep

# Generate 201 points from -25a to 25a
x_min, x_max = -25, 25
npts = 201
dx = (x_max - x_min) / (npts - 1)

header = ['x', 'delta_u_x']
writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(header)

for i in range(npts):
    x = x_min + i * dx
    f = (math.atan((x - x1)/w_core) + math.atan((x - x2)/w_core) + math.pi) / math.pi
    writer.writerow([round(x, 6), round(f, 6)])
