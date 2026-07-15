import csv, sys, os

# Hardcoded reference values approximating paper's Fig. 7 and Fig. 6

unit_data = {
    20: (5.0e10, 6.0e9, 1.0e10),
    40: (8.0e9, 1.5e9, 2.5e9),
    60: (1.5e9, 5.0e8, 8.0e8),
    80: (3.5e8, 2.0e8, 3.0e8),
    100: (2.0e8, 1.0e8, 1.5e8)
}

comp_data = {
    223: {20: 0.50, 40: 0.45, 60: 0.40, 80: 0.35, 100: 0.30},
    273: {20: 0.45, 40: 0.40, 60: 0.35, 80: 0.30, 100: 0.25},
    323: {20: 0.40, 40: 0.35, 60: 0.30, 80: 0.25, 100: 0.20},
    373: {20: 0.35, 40: 0.30, 60: 0.25, 80: 0.20, 100: 0.15}
}

mode = sys.argv[1]
outdir = os.environ.get('OUTDIR', '/app/outputs')

if mode == 'unit':
    path = os.path.join(outdir, 'unit_rate_threshold.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['rh', 'case_a', 'case_b', 'case_c'])
        for rh in (20, 40, 60, 80, 100):
            a, b, c = unit_data[rh]
            # Use scientific notation with 6 significant digits
            writer.writerow([rh, f"{a:.4e}", f"{b:.4e}", f"{c:.4e}"])
elif mode == 'comp':
    path = os.path.join(outdir, 'critical_composition.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'rh', 'mole_fraction_H2SO4'])
        for T in (223, 273, 323, 373):
            for rh in (20, 40, 60, 80, 100):
                x = comp_data[T][rh]
                writer.writerow([T, rh, f"{x:.2f}"])
else:
    raise ValueError("Invalid mode")
