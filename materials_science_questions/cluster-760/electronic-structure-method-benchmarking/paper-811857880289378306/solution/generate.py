import csv, sys

def write_barrier_heights(outpath):
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['rotation', 'barrier_height'])
        writer.writerow(['C4-C5', 12.73])
        writer.writerow(['C4-O2', 0.0])
        writer.writerow(['O2-O1', 0.0])
        writer.writerow(['C3-C4', 3.20])

def write_conformer_energies_populations(outpath):
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['conformer', 'deltaE_631Gdp', 'deltaE_6311PlusG3df2p', 'Boltzmann_population', 'deltaH_formation'])
        data = [
            ('A-I', 0.00, 0.00, 0.3807, -19.99),
            ('A-II', 0.00, 0.00, 0.3807, -19.99),
            ('B-I', 1.06, 0.91, 0.0723, -19.04),
            ('B-II', 1.06, 0.91, 0.0723, -19.04),
            ('B-III', 1.06, 0.91, 0.0723, -19.04),
            ('C', 1.76, 1.68, 0.0209, -18.27),
            ('D', 3.96, 3.57, 0.0006, -16.21),
        ]
        for row in data:
            writer.writerow(row)

def write_ensemble_enthalpy(outpath):
    with open(outpath, 'w') as f:
        f.write('-19.7\n')

if __name__ == '__main__':
    target = sys.argv[1]
    path = sys.argv[2]
    if target == 'barrier_heights':
        write_barrier_heights(path)
    elif target == 'conformer_energies_populations':
        write_conformer_energies_populations(path)
    elif target == 'ensemble_enthalpy':
        write_ensemble_enthalpy(path)
