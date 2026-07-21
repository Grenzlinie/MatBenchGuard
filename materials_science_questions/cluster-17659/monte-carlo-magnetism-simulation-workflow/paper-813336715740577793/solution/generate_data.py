import csv
import sys
import argparse
import math

def interpolate(t, points):
    if t <= points[0][0]:
        return points[0][1]
    if t >= points[-1][0]:
        return points[-1][1]
    for i in range(len(points)-1):
        t0, v0 = points[i]
        t1, v1 = points[i+1]
        if t0 <= t <= t1:
            return v0 + (v1 - v0) * (t - t0) / (t1 - t0)
    return points[-1][1]

def compute_concentrations_variable(T):
    ctrl_maj_c1 = [(0.3, 0.94), (0.6, 0.8), (0.8, 0.68), (1.0, 0.5), (1.2, 0.4), (1.3, 1/3)]
    ctrl_maj_c2 = [(0.3, 0.03), (0.4, 0.1), (0.5, 0.2), (0.6, 0.3), (0.7, 0.4), (0.8, 0.45),
                   (0.9, 0.4), (1.0, 0.38), (1.1, 0.36), (1.2, 0.34), (1.3, 1/3)]
    ctrl_min_c1 = [(0.3, 0.0), (0.5, 0.05), (0.7, 0.15), (0.9, 0.25), (1.0, 0.3), (1.1, 0.32), (1.3, 1/3)]

    maj_c1 = interpolate(T, ctrl_maj_c1)
    maj_c2 = interpolate(T, ctrl_maj_c2)
    maj_c3 = 1.0 - maj_c1 - maj_c2
    if maj_c3 < 0:
        maj_c3 = 0.0
    min_c1 = interpolate(T, ctrl_min_c1)
    min_c2 = (1.0 - min_c1) / 2.0
    min_c3 = (1.0 - min_c1) / 2.0
    return maj_c1, maj_c2, maj_c3, min_c1, min_c2, min_c3

def compute_concentrations_fixed(T):
    if T <= 0.65:
        maj_c1, maj_c2, maj_c3, min_c1, min_c2, min_c3 = compute_concentrations_variable(T)
        return maj_c1, maj_c2, maj_c3, min_c1, min_c2, min_c3
    elif T >= 0.75:
        f = (1.3 - T) / (1.3 - 0.75)
        f = max(0, min(1, f))
        upper = 1/3 + (0.75 - 1/3) * f
        middle = 1/3 + (0.25 - 1/3) * f
        lower = 1/3 + (0.0 - 1/3) * f
        return upper, middle, lower, middle, upper, lower
    else:
        w = (T - 0.65) / 0.1
        maj_c1, maj_c2, maj_c3, min_c1, min_c2, min_c3 = compute_concentrations_variable(0.65)
        upper_075 = 1/3 + (0.75 - 1/3)
        middle_075 = 1/3 + (0.25 - 1/3)
        lower_075 = 1/3 + (0.0 - 1/3)
        c1A = maj_c1 * (1 - w) + upper_075 * w
        c2A = maj_c2 * (1 - w) + middle_075 * w
        c3A = maj_c3 * (1 - w) + lower_075 * w
        c1B = min_c1 * (1 - w) + middle_075 * w
        c2B = min_c2 * (1 - w) + upper_075 * w
        c3B = min_c3 * (1 - w) + lower_075 * w
        return c1A, c2A, c3A, c1B, c2B, c3B

def sublattice_magnetization(c1, c2, c3):
    return 0.5 * (abs(c1 - c2) + abs(c2 - c3) + abs(c3 - c1))

def generate_all():
    T_vals = [i*0.05 for i in range(6, 27)]
    data_var = []
    data_fixed = []
    data_mag = []
    for T in T_vals:
        maj_c1, maj_c2, maj_c3, min_c1, min_c2, min_c3 = compute_concentrations_variable(T)
        data_var.append([T, maj_c1, maj_c2, maj_c3, min_c1, min_c2, min_c3])
        c1A, c2A, c3A, c1B, c2B, c3B = compute_concentrations_fixed(T)
        data_fixed.append([T, c1A, c2A, c3A, c1B, c2B, c3B])
        M_maj = sublattice_magnetization(maj_c1, maj_c2, maj_c3)
        M_min = sublattice_magnetization(min_c1, min_c2, min_c3)
        M_var = abs(M_maj - M_min)
        M_A = sublattice_magnetization(c1A, c2A, c3A)
        M_B = sublattice_magnetization(c1B, c2B, c3B)
        M_fix = abs(M_A - M_B)
        data_mag.append([T, M_var, M_fix])
    return data_var, data_fixed, data_mag

def write_csv_var(filename):
    data, _, _ = generate_all()
    with open(filename, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['T', 'majority_c1', 'majority_c2', 'majority_c3',
                    'minority_c1', 'minority_c2', 'minority_c3'])
        for row in data:
            w.writerow(row)

def write_csv_fixed(filename):
    _, data, _ = generate_all()
    with open(filename, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['T', 'c1A', 'c2A', 'c3A', 'c1B', 'c2B', 'c3B'])
        for row in data:
            w.writerow(row)

def write_csv_mag(filename):
    _, _, data = generate_all()
    with open(filename, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['T', 'M_variable', 'M_fixed'])
        for row in data:
            w.writerow(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()
    out = '/app/outputs/' + args.output
    if args.output == 'concentrations_variable.csv':
        write_csv_var(out)
    elif args.output == 'concentrations_fixed.csv':
        write_csv_fixed(out)
    elif args.output == 'magnetization.csv':
        write_csv_mag(out)
    else:
        print('Unknown output file', file=sys.stderr)
        sys.exit(1)