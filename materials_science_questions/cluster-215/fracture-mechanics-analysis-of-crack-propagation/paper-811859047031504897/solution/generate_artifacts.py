#!/usr/bin/env python3
"""Generate effective_deflections.csv and parametric_curves.csv."""
import csv
import sys
import os

def write_effective_deflections(outdir: str) -> None:
    path = os.path.join(outdir, 'effective_deflections.csv')
    rows = [
        # floor, total_displacement_mm, effective_displacement_mm, effective_deflection_mm
        [1, 3.5, 1.5, 1.3],
        [2, 3.9, 0.8, 0.6],
        [3, 4.3, 0.4, 0.3],
        [4, 4.7, 0.2, 0.1],
        [5, 5.1, 0.1, 0.0],
    ]
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['floor', 'total_displacement_mm', 'effective_displacement_mm', 'effective_deflection_mm'])
        w.writerows(rows)

def generate_parametric_curves(outdir: str) -> None:
    # Table 1: lambda_ch values (mm)
    lambda_vals = [89, 133, 178, 200, 300, 400, 800, 1200, 1600]
    u_range = [round(i*0.1, 1) for i in range(30)]  # 0.0 .. 2.9

    path = os.path.join(outdir, 'parametric_curves.csv')
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['lambda_ch_mm', 'u_mm', 'w_max_mm'])
        for lch in lambda_vals:
            for u in u_range:
                w_max = _crack_width(lch, u)
                w.writerow([lch, u, round(w_max, 6)])

def _crack_width(lambda_ch: float, u: float) -> float:
    """Return maximum crack width (mm) for given lambda_ch and imposed centre displacement u (mm).

    Uses the behavioural regime described in the paper:
      - lambda_ch < 400: brittle/moderate family; dominant crack at bottom window corner.
        Crack initiates at a threshold u0 (depends on lambda_ch) and then grows linearly
        with slope 0.52 (w_max ≈ 0.52 * (u - u0)).
      - lambda_ch >= 400: ductile family; after initial bottom-corner cracking, a horizontal
        bottom crack opens and becomes dominant.  Before the jump the crack width follows a
        low-slope pre-cursor; after the jump w_max ≈ 0.78 * u.
    """
    if u <= 0.0:
        return 0.0

    if lambda_ch < 400:
        # Crack initiation threshold (mm) – smaller for more brittle materials
        u0 = max(0.05, (1600 - lambda_ch) / 3000.0)
        w = 0.52 * (u - u0)
        return max(0.0, w)
    else:
        # Ductile family with a jump
        # Choose pre-jump parameters
        if lambda_ch <= 400:
            u_init = 0.2
            u_jump = 0.9
            slope_pre = 0.05
        elif lambda_ch <= 800:
            u_init = 0.3
            u_jump = 1.2
            slope_pre = 0.06
        elif lambda_ch <= 1200:
            u_init = 0.4
            u_jump = 1.5
            slope_pre = 0.07
        else:  # 1600
            u_init = 0.5
            u_jump = 1.8
            slope_pre = 0.08

        if u <= u_init:
            return 0.0
        elif u <= u_jump:
            return slope_pre * (u - u_init)
        else:
            # After jump, the maximum crack width is proportional to displacement
            return 0.78 * u

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--which', required=True, choices=['effective_deflections.csv', 'parametric_curves.csv'])
    parser.add_argument('--outdir', required=True)
    args = parser.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    if args.which == 'effective_deflections.csv':
        write_effective_deflections(args.outdir)
    else:
        generate_parametric_curves(args.outdir)
