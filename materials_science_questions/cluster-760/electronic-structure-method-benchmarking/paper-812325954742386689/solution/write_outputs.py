import sys, csv, json, os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
mode = sys.argv[1]

geom_data = [
    ('CH2ClO2', 'MP2', 1.4546, 1.3129, 108.20, 180.00, 60.90, 60.90),
    ('CH2ClO2', 'B3LYP', 1.4538, 1.3228, 108.43, 180.00, 61.24, -61.24),
    ('CHCl2O2', 'MP2', 1.4362, 1.3231, 111.68, 180.00, 63.06, -63.06),
    ('CHCl2O2', 'B3LYP', 1.4412, 1.3253, 110.30, 0.00, 118.97, -118.97),
    ('CCl3O2', 'MP2', 1.4554, 1.3194, 111.14, 180.00, 61.11, -61.11),
    ('CCl3O2', 'B3LYP', 1.4601, 1.3184, 112.22, 180.00, 61.05, -61.05),
    ('CFCl2O2', 'MP2', 1.4397, 1.3212, 111.30, 180.00, 62.83, -62.83),
    ('CFCl2O2', 'B3LYP', 1.4451, 1.3198, 112.80, 180.00, 62.34, -62.34),
    ('CF2ClO2', 'MP2', 1.4242, 1.3329, 108.60, 180.00, 59.55, -59.55),
    ('CF2ClO2', 'B3LYP', 1.4352, 1.3315, 109.36, 180.00, 60.02, -60.02),
    ('CHFClO2', 'MP2', 1.4239, 1.3291, 110.44, -177.20, 63.67, -58.48),
    ('CHFClO2', 'B3LYP', 1.4296, 1.3289, 111.70, -175.82, 66.20, -55.94),
]

charge_data = {
    ('CH2ClO2', 'MP2'): {'dipole_moment': 2.14, 'atoms': [{'symbol': 'C', 'charge': 0.015, 'spin_density': -0.019}, {'symbol': 'O', 'charge': -0.300, 'spin_density': 0.091}, {'symbol': 'O', 'charge': -0.059, 'spin_density': 0.920}]},
    ('CH2ClO2', 'B3LYP'): {'dipole_moment': 1.90, 'atoms': [{'symbol': 'C', 'charge': -0.051, 'spin_density': -0.021}, {'symbol': 'O', 'charge': -0.144, 'spin_density': 0.287}, {'symbol': 'O', 'charge': -0.149, 'spin_density': 0.709}]},
    ('CHCl2O2', 'MP2'): {'dipole_moment': 1.67, 'atoms': [{'symbol': 'C', 'charge': 0.010, 'spin_density': -0.013}, {'symbol': 'O', 'charge': -0.289, 'spin_density': 0.053}, {'symbol': 'O', 'charge': -0.012, 'spin_density': 0.954}]},
    ('CHCl2O2', 'B3LYP'): {'dipole_moment': 1.94, 'atoms': [{'symbol': 'C', 'charge': -0.058, 'spin_density': -0.011}, {'symbol': 'O', 'charge': -0.134, 'spin_density': 0.229}, {'symbol': 'O', 'charge': -0.097, 'spin_density': 0.755}]},
    ('CCl3O2', 'MP2'): {'dipole_moment': 0.84, 'atoms': [{'symbol': 'C', 'charge': -0.014, 'spin_density': -0.013}, {'symbol': 'O', 'charge': -0.271, 'spin_density': 0.056}, {'symbol': 'O', 'charge': -0.002, 'spin_density': 0.952}]},
    ('CCl3O2', 'B3LYP'): {'dipole_moment': 1.03, 'atoms': [{'symbol': 'C', 'charge': -0.079, 'spin_density': -0.011}, {'symbol': 'O', 'charge': -0.118, 'spin_density': 0.237}, {'symbol': 'O', 'charge': -0.087, 'spin_density': 0.751}]},
    ('CFCl2O2', 'MP2'): {'dipole_moment': 0.88, 'atoms': [{'symbol': 'C', 'charge': 0.478, 'spin_density': -0.012}, {'symbol': 'O', 'charge': -0.290, 'spin_density': 0.055}, {'symbol': 'O', 'charge': -0.007, 'spin_density': 0.951}]},
    ('CFCl2O2', 'B3LYP'): {'dipole_moment': 0.86, 'atoms': [{'symbol': 'C', 'charge': 0.310, 'spin_density': -0.009}, {'symbol': 'O', 'charge': -0.140, 'spin_density': 0.234}, {'symbol': 'O', 'charge': -0.093, 'spin_density': 0.753}]},
    ('CF2ClO2', 'MP2'): {'dipole_moment': 0.70, 'atoms': [{'symbol': 'C', 'charge': 0.935, 'spin_density': -0.007}, {'symbol': 'O', 'charge': -0.324, 'spin_density': 0.040}, {'symbol': 'O', 'charge': -0.008, 'spin_density': 0.970}]},
    ('CF2ClO2', 'B3LYP'): {'dipole_moment': 0.97, 'atoms': [{'symbol': 'C', 'charge': 0.658, 'spin_density': -0.005}, {'symbol': 'O', 'charge': -0.172, 'spin_density': 0.226}, {'symbol': 'O', 'charge': -0.101, 'spin_density': 0.772}]},
    ('CHFClO2', 'MP2'): {'dipole_moment': 1.80, 'atoms': [{'symbol': 'C', 'charge': 0.486, 'spin_density': -0.010}, {'symbol': 'O', 'charge': -0.315, 'spin_density': 0.045}, {'symbol': 'O', 'charge': -0.013, 'spin_density': 0.962}]},
    ('CHFClO2', 'B3LYP'): {'dipole_moment': 2.05, 'atoms': [{'symbol': 'C', 'charge': 0.327, 'spin_density': -0.007}, {'symbol': 'O', 'charge': -0.161, 'spin_density': 0.224}, {'symbol': 'O', 'charge': -0.103, 'spin_density': 0.764}]},
}

ch_bde_data = [
    ('MP2/6-31G(d,p)', 101.1, 100.4, 96.9, 94.1, 98.8, 101.1, 98.9),
    ('B3LYP/6-31G(d,p)', 105.2, 99.1, 94.7, 92.1, 94.7, 98.5, 96.7),
]

co_bde_data = [
    ('MP2/6-31G(d,p)', 19.7, 30.3, 29.2, 25.7, 32.9, 36.1, 36.1),
    ('B3LYP/6-31G(d,p)', 30.5, 27.8, 23.3, 17.9, 25.6, 33.0, 31.1),
]

ea_data = [
    ('MP2/6-31+G(d,p)', 25.0, 43.1, 52.9, 60.5, 61.3, 58.3, 52.0),
    ('B3LYP/6-31+G(d,p)', 25.1, 66.0, 57.9, 65.9, 65.0, 61.4, 56.1),
]

if mode == 'geometries':
    path = os.path.join(OUTDIR, 'geometries.csv')
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Radical', 'Method', 'R_C1O2', 'R_O2O3', 'Angle_C1O2O3', 'Torsion_X4', 'Torsion_X5', 'Torsion_X6'])
        for row in geom_data:
            w.writerow(row)
elif mode == 'charge_spin_dipole':
    path = os.path.join(OUTDIR, 'charge_spin_dipole.json')
    out = []
    for (radical, method), d in charge_data.items():
        obj = {'radical': radical, 'method': method, 'dipole_moment': d['dipole_moment'], 'atoms': d['atoms']}
        out.append(obj)
    with open(path, 'w') as f:
        json.dump(out, f, indent=2)
elif mode == 'CH_BDEs':
    path = os.path.join(OUTDIR, 'CH_BDEs.csv')
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Level', 'CH4', 'CH3Cl', 'CH2Cl2', 'CHCl3', 'CHFCl2', 'CHF2Cl', 'CH2FCl'])
        for row in ch_bde_data:
            w.writerow(row)
elif mode == 'CO_BDEs':
    path = os.path.join(OUTDIR, 'CO_BDEs.csv')
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Level', 'CH3-O2', 'CH2Cl-O2', 'CHCl2-O2', 'CCl3-O2', 'CFCl2-O2', 'CF2Cl-O2', 'CHFCl-O2'])
        for row in co_bde_data:
            w.writerow(row)
elif mode == 'EAs':
    path = os.path.join(OUTDIR, 'EAs.csv')
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Level', 'CH3-O2', 'CH2Cl-O2', 'CHCl2-O2', 'CCl3-O2', 'CFCl2-O2', 'CF2Cl-O2', 'CHFCl-O2'])
        for row in ea_data:
            w.writerow(row)
else:
    sys.stderr.write(f'Unknown mode {mode}\n')
    sys.exit(1)
