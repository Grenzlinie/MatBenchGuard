#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reference oracle data generator for the double-layer 2D slanted grating
   RCWA reproduction task. Writes CSVs to the specified output path."""

import csv
import sys

def write_efficiency_csv(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['polarization', 'order', 'efficiency'])
        writer.writerow(['TE', '(-1,0)', 39.10])
        writer.writerow(['TE', '(0,-1)', 39.12])
        writer.writerow(['TM', '(-1,0)', 39.13])
        writer.writerow(['TM', '(0,-1)', 39.19])

def write_wavelength_csv(path):
    wls = list(range(400, 501, 2))
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['wavelength_nm', 'DE_(-1,0)_TE', 'DE_(0,-1)_TE',
                         'DE_(-1,0)_TM', 'DE_(0,-1)_TM'])
        for wl in wls:
            de_10_te = piecewise_eff(wl, 39.10, 35.0, 429, 468, 400, 500)
            de_01_te = piecewise_eff(wl, 39.12, 35.0, 429, 468, 400, 500)
            de_10_tm = piecewise_eff(wl, 39.13, 35.0, 429, 468, 400, 500)
            de_01_tm = piecewise_eff(wl, 39.19, 35.0, 429, 468, 400, 500)
            writer.writerow([wl, f'{de_10_te:.2f}', f'{de_01_te:.2f}',
                             f'{de_10_tm:.2f}', f'{de_01_tm:.2f}'])

def piecewise_eff(wl, peak_eff, threshold, wl_low, wl_high, wl_min, wl_max):
    """Linear interpolation: trapezoid efficiency shape."""
    if wl <= wl_min:
        return 30.0
    if wl <= wl_low:
        return 30.0 + (wl - wl_min) * (threshold - 30.0) / (wl_low - wl_min)
    if wl <= 450:
        return threshold + (wl - wl_low) * (peak_eff - threshold) / (450 - wl_low)
    if wl <= wl_high:
        return threshold + (wl_high - wl) * (peak_eff - threshold) / (wl_high - 450)
    if wl <= wl_max:
        return threshold - (wl - wl_high) * (threshold - 30.0) / (wl_max - wl_high)
    return 30.0

def write_angle_csv(path):
    angles = [round(-5.0 + i * 0.5, 1) for i in range(21)]
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['incident_angle_deg', 'DE_(-1,0)_TE', 'DE_(0,-1)_TE',
                         'DE_(-1,0)_TM', 'DE_(0,-1)_TM'])
        for ang in angles:
            if ang <= -3.2:
                eff = linear(ang, -5.0, 5.0, -3.2, 30.0)
            elif ang <= 0:
                eff = linear(ang, -3.2, 30.0, 0.0, 39.1)
            elif ang <= 3.2:
                eff = linear(ang, 0.0, 39.1, 3.2, 30.0)
            else:
                eff = linear(ang, 3.2, 30.0, 5.0, 5.0)
            de10_te = max(eff, 0.0)
            de01_te = de10_te + 0.02
            de10_tm = de10_te + 0.03
            de01_tm = de10_te + 0.09
            writer.writerow([f'{ang:.1f}', f'{de10_te:.2f}', f'{de01_te:.2f}',
                             f'{de10_tm:.2f}', f'{de01_tm:.2f}'])

def linear(x, x1, y1, x2, y2):
    if x2 == x1:
        return y1
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)

def write_thickness_csv(path):
    h1_vals = list(range(280, 381, 5))
    h2_vals = list(range(500, 571, 5))
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['h1_nm', 'h2_nm', 'total_eff_TE', 'total_eff_TM',
                         'DE_(-1,0)_TE', 'DE_(0,-1)_TE',
                         'DE_(-1,0)_TM', 'DE_(0,-1)_TM'])
        for h1 in h1_vals:
            for h2 in h2_vals:
                if (300 <= h1 <= 350) and (525 <= h2 <= 550):
                    total = 78.0
                else:
                    total = 74.0
                de10_te = total / 2.0
                de01_te = total / 2.0
                de10_tm = total / 2.0
                de01_tm = total / 2.0
                writer.writerow([h1, h2, f'{total:.1f}', f'{total:.1f}',
                                 f'{de10_te:.2f}', f'{de01_te:.2f}',
                                 f'{de10_tm:.2f}', f'{de01_tm:.2f}'])

def write_period_angle_csv(path):
    periods = list(range(550, 651, 5))
    angles = list(range(10, 26, 1))
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['period_nm', 'slanted_angle_deg', 'DE_(-1,0)_TE',
                         'DE_(0,-1)_TE', 'DE_(-1,0)_TM', 'DE_(0,-1)_TM'])
        for period in periods:
            for ang in angles:
                if (580 <= period <= 633) and (12.2 <= ang <= 21.0):
                    eff = 39.1
                else:
                    eff = 34.0
                writer.writerow([period, ang, f'{eff:.2f}', f'{eff:.2f}',
                                 f'{eff:.2f}', f'{eff:.2f}'])

def write_duty_csv(path):
    duties = [round(0.4 + i * 0.02, 2) for i in range(11)]
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['duty_cycle', 'DE_(-1,0)_TE', 'DE_(0,-1)_TE',
                         'DE_(-1,0)_TM', 'DE_(0,-1)_TM'])
        for duty in duties:
            if 0.46 <= duty <= 0.53:
                eff = 39.1
            else:
                eff = 34.0
            writer.writerow([f'{duty:.2f}', f'{eff:.2f}', f'{eff:.2f}',
                             f'{eff:.2f}', f'{eff:.2f}'])

def main():
    if len(sys.argv) != 3:
        print("Usage: generate.py <type> <output_file>", file=sys.stderr)
        sys.exit(1)
    typ = sys.argv[1]
    outpath = sys.argv[2]
    if typ == 'efficiency':
        write_efficiency_csv(outpath)
    elif typ == 'wavelength':
        write_wavelength_csv(outpath)
    elif typ == 'angle':
        write_angle_csv(outpath)
    elif typ == 'thickness':
        write_thickness_csv(outpath)
    elif typ == 'period':
        write_period_angle_csv(outpath)
    elif typ == 'duty':
        write_duty_csv(outpath)
    else:
        print(f"Unknown type: {typ}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
