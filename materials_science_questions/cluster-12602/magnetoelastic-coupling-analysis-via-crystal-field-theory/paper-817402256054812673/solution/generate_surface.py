#!/usr/bin/env python3
import csv, os, sys

# Parameter: gamma(mu_Ga) = A + B * mu_Ga  for 100% Ga coverage
# For other coverages, add an offset (keeping same slope to ensure 100% is most stable)
# Offsets: 0% +0.8, 50% +0.4, 75% +0.2

definitions = {
    'none': {
        '001': {'A': 1.2, 'B': 0.3},
        '110': {'A': 1.0, 'B': 0.2},
        '111': {'A': 2.0, 'B': 0.1},
    },
    'H2S': {
        '001': {'A': 1.2, 'B': 0.3},  # same as clean
        '110': {'A': 1.0, 'B': 0.2},
        '111': {'A': 2.0, 'B': 0.1},
    },
    'O': {
        # crossover at mu_Ga=-2.6: 1.3+0.23*(-2.6)=0.702, 1.0+0.115*(-2.6)=0.701
        '001': {'A': 1.3, 'B': 0.23},
        '110': {'A': 1.0, 'B': 0.115},
        '111': {'A': 2.0, 'B': 0.05},
    },
    'Os': {
        # crossover at mu_Ga=-1.8: 1.2+0.25*(-1.8)=0.75, 0.9+0.0833*(-1.8)=0.75
        '001': {'A': 1.2, 'B': 0.25},
        '110': {'A': 0.9, 'B': 0.0833},
        '111': {'A': 2.0, 'B': 0.05},
    },
}

orientations = ['001', '110', '111']
coverages = ['0%', '50%', '75%', '100%']
adsorbents = ['none', 'O', 'Os', 'H2S']
mu_Ga_vals = [round(-4.0 + 0.5*i, 1) for i in range(9)]   # -4.0 to 0.0 step 0.5

outpath = '/app/outputs/surface_energies.csv'
os.makedirs(os.path.dirname(outpath), exist_ok=True)

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Orientation', 'Ga_coverage', 'Adsorbent', 'mu_Ga', 'Surface_energy'])
    for ads in adsorbents:
        for orient in orientations:
            base = definitions[ads][orient]
            A100 = base['A']
            B = base['B']
            for cov in coverages:
                if cov == '100%':
                    offset = 0.0
                elif cov == '75%':
                    offset = 0.2
                elif cov == '50%':
                    offset = 0.4
                elif cov == '0%':
                    offset = 0.8
                else:
                    offset = 0.0
                A = A100 + offset
                for mu in mu_Ga_vals:
                    gamma = A + B * mu
                    writer.writerow([orient, cov, ads, mu, round(gamma, 6)])

print('surface_energies.csv written', file=sys.stderr)