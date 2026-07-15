#!/usr/bin/env python3
import csv, sys

data = [
    (15.0, 1.9),
    (18.0, 1.6),
    (25.0, 1.3),
    (35.0, 1.1)
]
writer = csv.writer(sys.stdout)
writer.writerow(['diameter_A', 'band_gap_eV'])
for d, bg in data:
    writer.writerow([f'{d}', f'{bg}'])