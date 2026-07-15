#!/usr/bin/env python3
import sys
import csv
import math

def energy_spectrum():
    # Falling spectrum with a tail above 30 MeV
    header = ['energy_MeV', 'differential_flux']
    rows = []
    # Energy bins from 1 to 50 MeV
    for e in range(1, 51):
        # approximate flux shape with cut-off around 40 MeV, but non-zero beyond
        flux = 1e6 * math.exp(-e / 15.0) + 1e3 * (1 if e >= 30 else 0)
        rows.append([str(e), str(flux)])
    w = csv.writer(sys.stdout)
    w.writerow(header)
    w.writerows(rows)

def spatial_distribution():
    # Gaussian radial profile with sigma such that HWHM ~10 km
    header = ['radius_km', 'flux_per_area']
    sigma = 8.5  # km ; HWHM = sigma * sqrt(2 ln2) ≈ 8.5*1.177=10.0 km
    peak_flux = 1000.0
    rows = []
    for r_km in range(0, 51, 1):  # 0 to 50 km
        flux = peak_flux * math.exp(-r_km * r_km / (2 * sigma * sigma))
        rows.append([str(r_km), str(flux)])
    w = csv.writer(sys.stdout)
    w.writerow(header)
    w.writerows(rows)

def time_profile():
    # Two Gaussian peaks: first at 5 ms, second at 14 ms (separation 9 ms)
    header = ['time_ms', 'count_rate']
    center1, amp1, sigma1 = 5.0, 1.0, 0.8   # ms, arbitrary unit, width
    center2, amp2, sigma2 = 14.0, 0.8, 0.8
    rows = []
    for t in [x * 0.1 for x in range(0, 301)]:  # 0 to 30 ms step 0.1 ms
        v = (amp1 * math.exp(-(t - center1)**2 / (2 * sigma1**2)) +
             amp2 * math.exp(-(t - center2)**2 / (2 * sigma2**2)))
        rows.append([f"{t:.1f}", f"{v:.6f}"])
    w = csv.writer(sys.stdout)
    w.writerow(header)
    w.writerows(rows)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'energy':
        energy_spectrum()
    elif cmd == 'spatial':
        spatial_distribution()
    elif cmd == 'time':
        time_profile()
    else:
        sys.exit(1)