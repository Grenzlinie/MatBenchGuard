#!/usr/bin/env python3
"""Synthesise the reference output for the kinetic Monte Carlo task.
This script is the hidden oracle; it writes the expected scored artifacts
directly from the paper's reported transition points and qualitative behaviour."""

import csv
import math
import sys

def write_kinetic_curves():
    """Write kinetic_curves.csv with exactly the declared columns."""
    # Data derived from the paper:
    # - flat (ZGB): continuous transition at YA=0.39, first‑order jump at 0.52,
    #   reaction window [0.39,0.52], peak at ~0.45.
    # - rough_T500_spillover: no sharp transitions, continuous onset at ~0.15,
    #   rate zero until YA=0.4, then peaks (~0.45) and drops.
    # - rough_T500_no_spillover: narrow window, peak at YA=0.37, shape change.

    # YA sampling (more points around features)
    ya_flat = [0.0,0.1,0.2,0.3,0.38,0.39,0.40,0.42,0.44,0.45,0.46,0.48,0.50,0.51,0.52,0.53,0.55,0.6,0.7,0.8,1.0]
    ya_spill = [0.0,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.42,0.45,0.48,0.5,0.55,0.6,0.7,0.8,1.0]
    ya_nospill = [0.0,0.1,0.2,0.25,0.3,0.35,0.37,0.4,0.45,0.5,0.55,0.6,0.7,0.8,1.0]

    # Helper: build a row
    def row(c, y, a, b, r):
        return {'condition': c, 'YA': y, 'theta_A': a, 'theta_B': b, 'reaction_rate': r}

    rows = []

    # ---- FLAT (ZGB model) ----
    # piecewise: YA<0.39 -> theta_B=1, theta_A=0, rate=0
    # 0.39-0.52: smooth change, then jump at 0.52
    # 0.52+ -> theta_A=1, theta_B=0, rate=0
    for ya in ya_flat:
        if ya < 0.39:
            ta, tb, rr = 0.0, 1.0, 0.0
        elif ya == 0.39:
            ta, tb, rr = 0.0, 1.0, 0.0   # start of continuous transition
        elif ya < 0.52:
            # linear interpolation between (0.39,0) and (0.51,0.15) for A, (1 -> 0.85) for B
            frac = (ya - 0.39) / (0.52 - 0.39)
            ta = 0.15 * min(frac, 0.923)  # keep plateau near 0.15 until very close to 0.52
            tb = 1.0 - 0.15 * min(frac, 0.923)
            # triangular reaction rate: peak 18 at 0.45
            if ya <= 0.45:
                rr = 18.0 * (ya - 0.39) / (0.45 - 0.39)
            else:
                rr = 18.0 * (0.52 - ya) / (0.52 - 0.45)
            rr = max(rr, 0.0)
        elif ya == 0.52:
            ta, tb, rr = 1.0, 0.0, 0.0
        else:
            ta, tb, rr = 1.0, 0.0, 0.0
        rows.append(row('flat', ya, round(ta,6), round(tb,6), round(rr,4)))

    # ---- ROUGH_T500_SPILLOVER (rigid surface, spillover, no metal diffusion) ----
    # smooth, no unit B region, rate zero for YA<0.4, then non‑zero, sum<1 in active window
    # key points:
    ya_key_sp = [0.0,0.15,0.4,0.45,0.5,0.6,1.0]
    theta_B_key = [1.0,0.95,0.65,0.5,0.35,0.2,0.0]
    theta_A_key = [0.0,0.05,0.35,0.3,0.2,0.65,1.0]
    rate_key = [0.0,0.0,0.0,15.0,5.0,0.0,0.0]
    # interpolate for sampled ya
    def interp(x, xs, ys):
        # linear interpolation
        for i in range(len(xs)-1):
            if xs[i] <= x <= xs[i+1]:
                frac = (x - xs[i]) / (xs[i+1] - xs[i])
                return ys[i] + frac * (ys[i+1] - ys[i])
        return ys[-1]
    for ya in ya_spill:
        ta = round(interp(ya, ya_key_sp, theta_A_key),6)
        tb = round(interp(ya, ya_key_sp, theta_B_key),6)
        rr = round(interp(ya, ya_key_sp, rate_key),4)
        rows.append(row('rough_T500_spillover', ya, ta, tb, rr))

    # ---- ROUGH_T500_NO_SPILLOVER (metal diffusion, no support A) ----
    # narrow window, peak at 0.37, zero before 0.2 and after 0.55
    ya_key_ns = [0.0,0.2,0.3,0.37,0.4,0.45,0.5,0.55,1.0]
    theta_B_key_ns = [1.0,0.9,0.6,0.35,0.3,0.25,0.2,0.15,0.0]
    theta_A_key_ns = [0.0,0.1,0.35,0.45,0.55,0.6,0.55,0.7,1.0]
    rate_key_ns = [0.0,0.0,5.0,10.0,7.0,2.0,0.0,0.0,0.0]
    for ya in ya_nospill:
        ta = round(interp(ya, ya_key_ns, theta_A_key_ns),6)
        tb = round(interp(ya, ya_key_ns, theta_B_key_ns),6)
        rr = round(interp(ya, ya_key_ns, rate_key_ns),4)
        rows.append(row('rough_T500_no_spillover', ya, ta, tb, rr))

    # Write CSV
    writer = csv.DictWriter(sys.stdout, fieldnames=['condition','YA','theta_A','theta_B','reaction_rate'])
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

def write_shape():
    """Write shape_T500_no_spillover.csv: height map at YA=0.37.
    The particle becomes taller and narrower. We create a Gaussian‑like mound
    centred at (100,100) with max height 18 and effective radius ~15 cells."""
    N = 200
    cx, cy = 100, 100
    max_height = 18
    # height = max(0, round(max_height - (dx^2+dy^2)/12.5))
    # The factor 12.5 gives base radius sqrt(max_height*12.5)=sqrt(225)=15.
    writer = csv.DictWriter(sys.stdout, fieldnames=['x','y','height'])
    writer.writeheader()
    for x in range(N):
        for y in range(N):
            dx = x - cx
            dy = y - cy
            h = max_height - (dx*dx + dy*dy) / 12.5
            h = max(0, round(h))
            writer.writerow({'x': x, 'y': y, 'height': int(h)})

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'kinetic':
        write_kinetic_curves()
    elif mode == 'shape':
        write_shape()
    else:
        raise SystemExit("Usage: generate.py [kinetic|shape]")
