#!/usr/bin/env python3
import sys, csv, numpy as np

case = sys.argv[1]
energy_grid = np.arange(-10.0, 5.01, 0.01)

if case == 'hcovered':
    peaks = [
        (-5.0, 0.2, 0.8), (-3.0, 0.4, 0.6), (-1.5, 0.6, 0.5), (-0.8, 1.0, 0.4),
        (0.8, 0.5, 0.4), (1.5, 0.8, 0.6), (2.5, 0.6, 0.8), (3.5, 0.4, 0.5)
    ]
elif case == 'dangling':
    peaks = [
        (-5.0, 0.2, 0.8), (-3.0, 0.4, 0.6), (-1.5, 0.5, 0.5), (-0.7, 1.0, 0.4),
        (0.0, 0.8, 0.5),
        (0.8, 0.4, 0.4), (1.5, 0.6, 0.6), (2.5, 0.4, 0.8), (3.5, 0.3, 0.5)
    ]
elif case == 'truncated':
    peaks = [
        (-5.0, 0.2, 0.8), (-3.0, 0.4, 0.6), (-1.5, 0.6, 0.5), (-0.9, 1.0, 0.4),
        (0.7, 0.5, 0.4), (1.5, 0.8, 0.6), (2.5, 0.6, 0.8), (3.5, 0.4, 0.5)
    ]
else:
    sys.exit(1)

dos = np.zeros_like(energy_grid)
for center, intensity, fwhm in peaks:
    sigma = fwhm / 2.355
    dos += intensity * np.exp(-0.5 * ((energy_grid - center) / sigma) ** 2)

writer = csv.writer(sys.stdout)
writer.writerow(['energy_eV', 'total_DOS'])
for e, d in zip(energy_grid, dos):
    writer.writerow([f'{e:.2f}', f'{d:.4f}'])