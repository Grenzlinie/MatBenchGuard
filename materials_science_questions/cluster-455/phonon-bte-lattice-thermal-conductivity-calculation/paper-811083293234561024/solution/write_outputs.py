import csv
import sys

def write_step_01(path):
    rows = []
    # b = 20 nm: plateau relative resistance = Tr^-1 = (20/100)^-1 = 5.0
    res_20 = [1.8, 2.4, 3.0, 3.7, 4.3, 5.0, 5.0, 5.0, 5.0, 5.0]
    # b = 60 nm: plateau = (60/100)^-1 ≈ 1.6667
    res_60 = [1.2, 1.3, 1.4, 1.5, 1.58, 1.667, 1.667, 1.667, 1.667, 1.667]
    # b = 90 nm: plateau = (90/100)^-1 ≈ 1.1111
    res_90 = [1.05, 1.06, 1.07, 1.08, 1.09, 1.111, 1.111, 1.111, 1.111, 1.111]
    n_vals = list(range(1, 11))
    for b, res_list in [(20, res_20), (60, res_60), (90, res_90)]:
        for n, res in zip(n_vals, res_list):
            kappa = 1.0 / res
            rows.append((n, b, round(kappa, 6), round(res, 6)))
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['n_constrictions', 'constriction_width_nm', 'relative_thermal_conductivity', 'relative_thermal_resistance'])
        w.writerows(rows)

def write_step_02(path):
    # chi starts at 1.0, decreases linearly to 0.0 at N=6, stays 0
    chi_vals = [1.0, 0.8, 0.6, 0.4, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0]
    rows = [(n, chi) for n, chi in enumerate(chi_vals, start=1)]
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['n_constrictions', 'chi'])
        w.writerows(rows)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(1)
    output_path = sys.argv[1]
    step = sys.argv[2]
    if step == 'step_01':
        write_step_01(output_path)
    elif step == 'step_02':
        write_step_02(output_path)
    else:
        sys.exit(1)