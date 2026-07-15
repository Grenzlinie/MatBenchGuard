import csv
import math
import sys

# ---- Reference values from the paper ----
# Table I lattice constants at 300 K
lattice_data = [
    {'phase': 'fcc', 'a_Angstrom': 15.50, 'c_Angstrom': '', 'c_a_ratio': ''},
    {'phase': 'hex1', 'a_Angstrom': 10.50, 'c_Angstrom': 18.42, 'c_a_ratio': 1.754},
    {'phase': 'hex2', 'a_Angstrom': 10.93, 'c_Angstrom': 17.50, 'c_a_ratio': 1.601},
]

# Temperature range: 100 K to 900 K, step 10 K
T_vals = list(range(100, 910, 10))

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def ca_hex1(T):
    # hex1: c/a increases from 1.633 at high T to 1.673 at low T
    # transition centered at 250 K, width ~30 K
    return 1.633 + 0.04 * sigmoid((250.0 - T) / 30.0)

def ca_hex2(T):
    # hex2: c/a decreases from 1.633 at high T to 1.599 at low T
    # transition midpoint at 425 K
    return 1.633 - 0.034 * sigmoid((425.0 - T) / 25.0)

def potential_fcc(T):
    # fcc orientational transition at 200 K; kink in slope
    if T <= 200.0:
        # from 100 K (-160e3) to 200 K (-155e3)
        return -160000.0 + (T - 100.0) * 50.0 / 100.0 * 5000.0  # -50 kJ rise
    else:
        # from 200 K (-155e3) to 900 K (-130e3)
        return -155000.0 + (T - 200.0) * 25000.0 / 700.0

def potential_hex1(T):
    # hex1 transitions at 100 K and 400 K
    if T <= 100.0:
        # constant? steep slope
        return -165000.0  # constant below 100 K
    elif T <= 400.0:
        # from 100 K (-165e3) to 400 K (-140e3)
        return -165000.0 + (T - 100.0) * 25000.0 / 300.0
    else:
        # from 400 K (-140e3) to 900 K (-125e3)
        return -140000.0 + (T - 400.0) * 15000.0 / 500.0

def potential_hex2(T):
    # hex2 transitions at 350 K and 500 K
    if T <= 350.0:
        # from 100 K (-162e3) to 350 K (-145e3)
        return -162000.0 + (T - 100.0) * 17000.0 / 250.0
    elif T <= 500.0:
        # from 350 K (-145e3) to 500 K (-130e3)
        return -145000.0 + (T - 350.0) * 15000.0 / 150.0
    else:
        # from 500 K (-130e3) to 900 K (-120e3)
        return -130000.0 + (T - 500.0) * 10000.0 / 400.0

def write_lattice(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['phase', 'a_Angstrom', 'c_Angstrom', 'c_a_ratio'])
        for row in lattice_data:
            writer.writerow([row['phase'], row['a_Angstrom'], row['c_Angstrom'], row['c_a_ratio']])
    print(f'Written {path}')

def write_ca_ratio(path):
    rows = []
    for T in T_vals:
        rows.append(['hex1', T, round(ca_hex1(T), 3)])
        rows.append(['hex2', T, round(ca_hex2(T), 3)])
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['phase', 'T_K', 'c_a_ratio'])
        writer.writerows(rows)
    print(f'Written {path}')

def write_potential(path):
    rows = []
    for T in T_vals:
        rows.append(['fcc', T, round(potential_fcc(T), 0)])
        rows.append(['hex1', T, round(potential_hex1(T), 0)])
        rows.append(['hex2', T, round(potential_hex2(T), 0)])
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['phase', 'T_K', 'potential_energy_per_mol_J'])
        writer.writerows(rows)
    print(f'Written {path}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: python write_data.py <output_filename>')
    basename = sys.argv[1]
    full = '/app/outputs/' + basename
    if basename == 'lattice_constants_300K.csv':
        write_lattice(full)
    elif basename == 'ca_ratio_vs_T.csv':
        write_ca_ratio(full)
    elif basename == 'potential_energy_vs_T.csv':
        write_potential(full)
    else:
        sys.exit(f'Unknown output file: {basename}')
