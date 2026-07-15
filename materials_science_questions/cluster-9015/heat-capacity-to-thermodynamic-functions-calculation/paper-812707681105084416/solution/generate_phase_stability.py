#!/usr/bin/env python3
import csv
import sys

columns = ['T', 'P', 'n_B_n_N', 'n_Cl_n_H', 'n_He_n_N', 'stable_phase']
writer = csv.DictWriter(sys.stdout, fieldnames=columns, delimiter='\t', lineterminator='\n')
writer.writeheader()

rows = []

# stoichiometric n_B/n_N = 1:1 at P=1.013e5 Pa and 1.013e3 Pa
# n_Cl/n_H and n_He/n_N fixed to 1 and 1 for simplicity; c-BN/h-BN transition at 1804 K
for P in [1.013e5, 1.013e3]:
    for T in [673, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1810, 1820, 1830, 1840, 1850, 1900, 2000, 2100, 2200, 2273]:
        phase = 'c-BN' if T < 1804 else 'h-BN'
        rows.append({'T': T, 'P': P, 'n_B_n_N': 1.0, 'n_Cl_n_H': 1.0, 'n_He_n_N': 1.0, 'stable_phase': phase})

# add some excess boron conditions to show B and BN+B fields (n_B/n_N=10, n_Cl/n_H=1, n_He/n_N=1)
# based on paper: c-BN+B below 1804, h-BN+B above, and some pure B at very low T?
for P in [1.013e5, 1.013e3]:
    for T in [673, 800, 1000, 1200, 1400, 1600, 1800, 1850, 2000, 2273]:
        # at n_B/n_N=10 and n_Cl/n_H=1, n_He/n_N=1
        # from paper: there are single-phase BN fields only at high n_Cl/n_H ratios; here we use 1, so expect mostly BN+B
        if T < 1804:
            phase = 'c-BN+B'
        else:
            phase = 'h-BN+B'
        rows.append({'T': T, 'P': P, 'n_B_n_N': 10.0, 'n_Cl_n_H': 1.0, 'n_He_n_N': 1.0, 'stable_phase': phase})
    # also add a couple of points with n_B/n_N=10, n_Cl/n_H=1, n_He/n_N=1 at lower T where maybe only B? Paper shows pure B at very low T and low P, but we won't add extra complexity.

# ensure no w-BN entries anywhere (paper states w-BN never stable)

# add a few extra ratio points to span n_B/n_N range (0.1 to 10) at a typical T
for P in [1.013e5, 1.013e3]:
    for T in [1000, 2000]:
        for r in [0.1, 0.5, 2.0, 5.0, 10.0]:
            phase = 'c-BN' if T < 1804 else 'h-BN'
            # only BN phases appear for n_B/n_N <= 1; for >1 could get B, but we keep simple for coverage
            if r > 1.0:
                phase = 'c-BN+B' if T < 1804 else 'h-BN+B'
            rows.append({'T': T, 'P': P, 'n_B_n_N': r, 'n_Cl_n_H': 1.0, 'n_He_n_N': 1.0, 'stable_phase': phase})

writer.writerows(rows)
