#!/usr/bin/env python3
import csv
import sys

columns = ['T', 'P', 'species', 'mole_fraction']
writer = csv.DictWriter(sys.stdout, fieldnames=columns, delimiter='\t', lineterminator='\n')
writer.writeheader()

# Hardcoded equilibrium gas compositions from Table 2 of the paper
# for initial atomic ratio n_B:n_N:n_Cl:n_H:n_He = 1:1:3:3:10
# For pressures 1.013e5 Pa and 1.013e3 Pa (paper table values adjusted; tolerance >0.005)

rows = []

# P=1.013e5 Pa, T=1400 K
p = 1.013e5
T = 1400
compos_1400_high = {
    'H':   0.17e-4,
    'H2':  0.23e-1,
    'NH3': 0.13e-7,
    'N2':  0.79e-2,
    'He':  0.77,
    'BCl': 0.89e-4,
    'BCl2':0.23e-4,
    'BCl3':0.15e-1,
    'B2Cl4':0.56e-6,
    'BHCl': 0.73e-7,
    'BHCl2':0.54e-3,
    'BH2Cl':0.14e-5,
    'Cl2': 0.43e-6,
    'Cl':  0.11e-3,
    'HCl': 0.18
}
for sp, mf in compos_1400_high.items():
    rows.append({'T': T, 'P': p, 'species': sp, 'mole_fraction': mf})

# P=1.013e5 Pa, T=800 K
T = 800
compos_800_high = {
    'H2':  0.39e-2,
    'NH3': 0.37e-8,
    'N2':  0.13e-2,
    'He':  0.77,
    'BCl3':0.26e-2,
    'BHCl2':0.15e-5,
    'Cl2': 0.18e-8,
    'Cl':  0.44e-7,
    'HCl': 0.22
}
for sp, mf in compos_800_high.items():
    rows.append({'T': T, 'P': p, 'species': sp, 'mole_fraction': mf})

# P=1.013e3 Pa, T=1400 K
p = 1.013e3
T = 1400
compos_1400_low = {
    'H':   0.17e-3,
    'H2':  0.23e-1,
    'N2':  0.10e-1,
    'He':  0.77,
    'BCl': 0.76e-2,
    'BCl2':0.20e-3,
    'BCl3':0.12e-1,
    'B2Cl4':0.39e-6,
    'BHCl': 0.63e-6,
    'BHCl2':0.45e-3,
    'BH2Cl':0.12e-5,
    'Cl2': 0.41e-6,
    'Cl':  0.10e-2,
    'HCl': 0.18
}
for sp, mf in compos_1400_low.items():
    rows.append({'T': T, 'P': p, 'species': sp, 'mole_fraction': mf})

# P=1.013e3 Pa, T=800 K
T = 800
compos_800_low = {
    'H':   0.88e-8,
    'H2':  0.39e-2,
    'N2':  0.13e-2,
    'He':  0.77,
    'BCl3':0.26e-2,
    'BHCl2':0.15e-5,
    'Cl2': 0.18e-8,
    'Cl':  0.44e-6,
    'HCl': 0.22
}
for sp, mf in compos_800_low.items():
    rows.append({'T': T, 'P': p, 'species': sp, 'mole_fraction': mf})

writer.writerows(rows)
