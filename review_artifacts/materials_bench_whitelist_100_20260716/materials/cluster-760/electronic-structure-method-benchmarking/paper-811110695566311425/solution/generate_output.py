#!/usr/bin/env python3
import csv
import sys

# Hardcoded data from Table 5A and Table 6B
experimental = {
    'CH3-CH3': -84.1,
    'CH3-CH2F': -263.2,
    'CH2F-CH2F': -433.9,
    'CH3-CHF2': -500.8,
    'CH2F-CHF2': -664.8,
    'CH3-CF3': -745.6,
    'CHF2-CHF2': -877.8,
    'CH2F-CF3': -895.8,
    'CHF2-CF3': -1104.6,
    'CF3-CF3': -1342.7,
}
n_CF = {
    'CH3-CH3': 0,
    'CH3-CH2F': 1,
    'CH2F-CH2F': 2,
    'CH3-CHF2': 2,
    'CH2F-CHF2': 3,
    'CH3-CF3': 3,
    'CHF2-CHF2': 4,
    'CH2F-CF3': 4,
    'CHF2-CF3': 5,
    'CF3-CF3': 6,
}
# Raw enthalpies from Table 5A
raw = {
    'G2(MP2)': {
        'CH3-CH3': -83.1,
        'CH3-CH2F': -279.5,
        'CH2F-CH2F': -462.3,
        'CH3-CHF2': -518.3,
        'CH2F-CHF2': -691.7,
        'CH3-CF3': -775.4,
        'CHF2-CHF2': -913.2,
        'CH2F-CF3': -940.2,
        'CHF2-CF3': -1153.9,
        'CF3-CF3': -1392.9,
    },
    'G2': {
        'CH3-CH3': -86.0,
        'CH3-CH2F': -279.7,
        'CH2F-CH2F': -459.8,
        'CH3-CHF2': -516.4,
        'CH2F-CHF2': -687.0,
        'CH3-CF3': -772.1,
        'CHF2-CHF2': -906.6,
        'CH2F-CF3': -934.2,
        'CHF2-CF3': -1145.9,
        'CF3-CF3': -1383.7,
    },
    'CBS-4': {
        'CH3-CH3': -92.1,
        'CH3-CH2F': -277.7,
        'CH2F-CH2F': -447.5,
        'CH3-CHF2': -508.5,
        'CH2F-CHF2': -669.1,
        'CH3-CF3': -760.0,
        'CHF2-CHF2': -881.3,
        'CH2F-CF3': -912.0,
        'CHF2-CF3': -1116.1,
        'CF3-CF3': -1348.5,
    },
    'CBS-Q': {
        'CH3-CH3': -81.5,
        'CH3-CH2F': -274.1,
        'CH2F-CH2F': -457.5,
        'CH3-CHF2': -510.0,
        'CH2F-CHF2': -680.0,
        'CH3-CF3': -764.4,
        'CHF2-CHF2': -898.6,
        'CH2F-CF3': -925.0,
        'CHF2-CF3': -1135.2,
        'CF3-CF3': -1371.0,
    },
}
# C-F BAC parameters from Table 6B (kJ/mol)
delta_CF = {
    'G2(MP2)': -7.98,
    'G2': -6.51,
    'CBS-4': -1.28,
    'CBS-Q': -3.51,
}

methods = ['G2(MP2)', 'G2', 'CBS-4', 'CBS-Q']
molecules = list(experimental.keys())

def write_raw(filepath):
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['method', 'molecule', 'calc_Hf_abinitio'])
        for m in methods:
            for mol in molecules:
                writer.writerow([m, mol, raw[m][mol]])

def write_corrected(filepath):
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['method', 'molecule', 'n_CF', 'calc_Hf_abinitio', 'dev_abinitio', 'calc_Hf_BAC', 'dev_BAC'])
        for m in methods:
            d = delta_CF[m]
            for mol in molecules:
                exp = experimental[mol]
                calc = raw[m][mol]
                dev_ab = calc - exp
                nc = n_CF[mol]
                corr = nc * d
                calc_bac = calc + corr
                dev_bac = calc_bac - exp
                writer.writerow([m, mol, nc, calc, dev_ab, calc_bac, dev_bac])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: generate_output.py {raw_enthalpies.csv|corrected_enthalpies_and_errors.csv}', file=sys.stderr)
        sys.exit(1)
    target = sys.argv[1]
    if target == 'raw_enthalpies.csv':
        write_raw(target)
    elif target == 'corrected_enthalpies_and_errors.csv':
        write_corrected(target)
    else:
        print(f'Unknown target: {target}', file=sys.stderr)
        sys.exit(1)
