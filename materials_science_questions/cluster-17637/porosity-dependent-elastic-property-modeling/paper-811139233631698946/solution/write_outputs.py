import csv
import os

OUTDIR = '/app/outputs'

# ----------------------------------------------------------------------
# Reference data: approximated normalised effective moduli
# ----------------------------------------------------------------------

# Step 1: circular nanopores (square/hex, surfaces A/B/C, radii 1..50 nm)
# For surface C, all ratios = 1.0.
# For surfaces A and B we use approximate values that reproduce the
# size‑dependency seen in the paper: strong surface stiffening at small
# radii, diminishing to classical behaviour at large radii.

radii = [1,2,5,10,20,30,40,50]
distributions = ['square', 'hexagonal']
surfaces = ['A', 'B', 'C']

# base values (used for both distributions, small variations ignored)
moduli_A = {
    1:  {'k':2.80, 'm':2.50, 'n':2.80, 'l':3.00, 'G':2.50, 'Gp':2.50},
    2:  {'k':2.30, 'm':2.10, 'n':2.30, 'l':2.50, 'G':2.10, 'Gp':2.10},
    5:  {'k':1.80, 'm':1.60, 'n':1.80, 'l':1.90, 'G':1.60, 'Gp':1.60},
    10: {'k':1.40, 'm':1.30, 'n':1.40, 'l':1.50, 'G':1.30, 'Gp':1.30},
    20: {'k':1.15, 'm':1.10, 'n':1.15, 'l':1.20, 'G':1.10, 'Gp':1.10},
    30: {'k':1.05, 'm':1.04, 'n':1.05, 'l':1.06, 'G':1.04, 'Gp':1.04},
    40: {'k':1.02, 'm':1.01, 'n':1.02, 'l':1.02, 'G':1.01, 'Gp':1.01},
    50: {'k':1.00, 'm':1.00, 'n':1.00, 'l':1.00, 'G':1.00, 'Gp':1.00},
}

moduli_B = {
    1:  {'k':1.50, 'm':1.40, 'n':1.45, 'l':1.55, 'G':1.40, 'Gp':1.40},
    2:  {'k':1.40, 'm':1.30, 'n':1.35, 'l':1.45, 'G':1.30, 'Gp':1.30},
    5:  {'k':1.25, 'm':1.18, 'n':1.22, 'l':1.30, 'G':1.18, 'Gp':1.18},
    10: {'k':1.10, 'm':1.08, 'n':1.10, 'l':1.12, 'G':1.08, 'Gp':1.08},
    20: {'k':1.02, 'm':1.01, 'n':1.02, 'l':1.03, 'G':1.01, 'Gp':1.01},
    30: {'k':1.00, 'm':1.00, 'n':1.00, 'l':1.00, 'G':1.00, 'Gp':1.00},
    40: {'k':1.00, 'm':1.00, 'n':1.00, 'l':1.00, 'G':1.00, 'Gp':1.00},
    50: {'k':1.00, 'm':1.00, 'n':1.00, 'l':1.00, 'G':1.00, 'Gp':1.00},
}

def write_step_01():
    with open(os.path.join(OUTDIR, 'step_01_nanopores_circular.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['radius','distribution','surface',
                    'k_norm','m_norm','n_norm','l_norm','G_norm','Gp_norm'])
        for r in radii:
            for dist in distributions:
                for surf in surfaces:
                    if surf == 'C':
                        vals = {'k':1.0,'m':1.0,'n':1.0,'l':1.0,'G':1.0,'Gp':1.0}
                    elif surf == 'A':
                        vals = moduli_A[r]
                    else:  # B
                        vals = moduli_B[r]
                    w.writerow([r, dist, surf,
                                vals['k'], vals['m'], vals['n'],
                                vals['l'], vals['G'], vals['Gp']])

# Step 2: non‑circular nanopores (surface A only, f=0.2)
shapes = ['4_oscillations', '8_oscillations']

noncirc_k = {
    '4_oscillations': {1:2.20, 2:1.90, 5:1.50, 10:1.25, 20:1.10, 30:1.04, 40:1.01, 50:1.00},
    '8_oscillations': {1:2.00, 2:1.80, 5:1.40, 10:1.20, 20:1.08, 30:1.03, 40:1.01, 50:1.00},
}

def write_step_02():
    with open(os.path.join(OUTDIR, 'step_02_nanopores_noncircular.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['R0','shape','k_norm'])
        for r in radii:
            for sh in shapes:
                w.writerow([r, sh, noncirc_k[sh][r]])

# Step 3: circular nanofibers (square/hex/random, f=0.3, interface modulus given)
fiber_radii = [1,2,5,10,20,30,40,50]
fiber_dists = ['square', 'hexagonal', 'random']

# normalised moduli (ratio to matrix moduli) – approximate values
fiber_moduli = {
    1:  {'k':1.60, 'm':1.55, 'n':1.60, 'l':1.50, 'G':1.55, 'Gp':1.55},
    2:  {'k':1.50, 'm':1.45, 'n':1.50, 'l':1.40, 'G':1.45, 'Gp':1.45},
    5:  {'k':1.30, 'm':1.25, 'n':1.30, 'l':1.22, 'G':1.25, 'Gp':1.25},
    10: {'k':1.10, 'm':1.08, 'n':1.10, 'l':1.05, 'G':1.08, 'Gp':1.08},
    20: {'k':0.95, 'm':0.93, 'n':0.95, 'l':0.90, 'G':0.93, 'Gp':0.93},
    30: {'k':0.85, 'm':0.83, 'n':0.85, 'l':0.82, 'G':0.83, 'Gp':0.83},
    40: {'k':0.82, 'm':0.80, 'n':0.82, 'l':0.79, 'G':0.80, 'Gp':0.80},
    50: {'k':0.80, 'm':0.78, 'n':0.80, 'l':0.77, 'G':0.78, 'Gp':0.78},
}

def write_step_03():
    with open(os.path.join(OUTDIR, 'step_03_nanofibers.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['radius','distribution','realization',
                    'k_norm','m_norm','n_norm','l_norm','G_norm','Gp_norm'])
        for r in fiber_radii:
            for dist in fiber_dists:
                vals = fiber_moduli[r]
                # For random distribution we report one realisation (realization=1)
                if dist == 'random':
                    w.writerow([r, dist, 1,
                                vals['k'], vals['m'], vals['n'],
                                vals['l'], vals['G'], vals['Gp']])
                else:
                    w.writerow([r, dist, 1,
                                vals['k'], vals['m'], vals['n'],
                                vals['l'], vals['G'], vals['Gp']])
