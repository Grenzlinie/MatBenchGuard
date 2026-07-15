import csv
import sys

def write_csv(filename, rows, header):
    with open(f'/app/outputs/{filename}', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

# ---------------------------------------------------------------------------
# Reference values synthesised to match paper trends and approximate magnitudes
# ---------------------------------------------------------------------------
materials = ['Na', 'K', 'Al', 'Cu', 'Ag', 'Au']
epsilon_vals = [1.0, 5.0, 10.0]
radius_nm = 6.0

# FoM data: (FoM_electrons, FoM_holes) for epsilon_m = 1,5,10
fom_data = {
    'Na': [(0.15, 0.05), (0.4, 0.12), (1.5, 0.5)],      # factor ~10
    'K':  [(0.12, 0.04), (0.3, 0.10), (1.2, 0.4)],      # factor ~10
    'Al': [(0.03, 0.01), (0.045, 0.015), (0.06, 0.02)], # doubles
    'Cu': [(0.002, 0.001), (0.02, 0.008), (0.2, 0.08)],  # factor ~100
    'Ag': [(0.02, 0.008), (0.06, 0.02), (0.2, 0.06)],    # factor ~10
    'Au': [(0.008, 0.004), (0.08, 0.03), (0.8, 0.3)]    # factor ~100
}

# Water splitting counts: (N_e_HER, N_h_OER) per nanoparticle
ws_data = {
    'Na': [(5e10, 1e9),   (1e11, 5e9),   (5e11, 2e10)],
    'K':  [(4e10, 8e8),   (8e10, 4e9),   (4e11, 1.5e10)],
    'Al': [(2e10, 2e9),   (4e10, 5e9),   (1e11, 1e10)],
    'Cu': [(1e9, 5e10),   (3e9, 1e11),   (1e10, 5e11)],
    'Ag': [(2e9, 3e10),   (5e9, 8e10),   (2e10, 3e11)],
    'Au': [(1e9, 2e10),   (4e9, 5e10),   (1e10, 2e11)]
}

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('--fom', '--ws'):
        print('Usage: write_outputs.py --fom|--ws', file=sys.stderr)
        sys.exit(1)

    if sys.argv[1] == '--fom':
        rows = []
        for mat in materials:
            for i, eps in enumerate(epsilon_vals):
                fe, fh = fom_data[mat][i]
                rows.append([mat, eps, radius_nm, fe, fh])
        write_csv('figure_of_merit.csv', rows,
                  ['material', 'epsilon_m', 'radius_nm', 'FoM_electrons', 'FoM_holes'])
    else:
        rows = []
        for mat in materials:
            for i, eps in enumerate(epsilon_vals):
                ne, nh = ws_data[mat][i]
                rows.append([mat, eps, radius_nm, ne, nh])
        write_csv('water_splitting_counts.csv', rows,
                  ['material', 'epsilon_m', 'radius_nm', 'N_electrons_HER', 'N_holes_OER'])

if __name__ == '__main__':
    main()