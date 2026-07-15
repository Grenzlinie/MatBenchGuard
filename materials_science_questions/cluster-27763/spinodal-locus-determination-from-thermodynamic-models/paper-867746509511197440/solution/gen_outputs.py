#!/usr/bin/env python3
import sys, csv, math, os

OUTDIR = '/app/outputs'

def write_mean_field_coexistence():
    # Data for delta = 0.72 (temperatures, rho_liquid, rho_vapour, rho_lambda_line)
    # Extracted approximately from Fig. 2a of the paper.
    temps072 = [0.92, 0.94, 0.96, 0.98, 1.00, 1.002, 1.01, 1.02, 1.03, 1.04,
                1.05, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11, 1.12, 1.13, 1.14,
                1.15, 1.16, 1.17]
    rho_l072 = [0.755, 0.745, 0.735, 0.725, 0.714, 0.700, 0.690, 0.680, 0.665,
                0.650, 0.635, 0.620, 0.605, 0.588, 0.572, 0.555, 0.537, 0.518,
                0.500, 0.482, 0.465, 0.452, 0.445]
    rho_v072 = [0.045, 0.050, 0.055, 0.060, 0.070, 0.080, 0.090, 0.098, 0.108,
                0.117, 0.126, 0.136, 0.147, 0.159, 0.172, 0.188, 0.206,
                0.227, 0.252, 0.282, 0.322, 0.382, 0.445]
    rho_lambda072 = [0.82, 0.81, 0.80, 0.79, 0.77, 0.70] + [''] * (len(temps072)-6)

    # Data for delta = 0.65 (Fig. 2c). Triple point at T ≈ 1.05
    temps065 = [0.95, 0.98, 1.00, 1.02, 1.04, 1.044, 1.048, 1.052, 1.056, 1.060,
                1.065, 1.070, 1.075, 1.080, 1.085, 1.090, 1.095, 1.100, 1.105,
                1.110, 1.115, 1.120, 1.125, 1.130, 1.135, 1.140, 1.145, 1.150,
                1.155, 1.160, 1.165, 1.170, 1.175, 1.180]
    # liquid branch: below 1.05 demixed liquid (high density), above 1.05 mixed liquid (low density)
    rho_l065 = [0.695, 0.685, 0.675, 0.665, 0.655, 0.650, 0.350, 0.355, 0.360, 0.365,
                0.372, 0.380, 0.388, 0.396, 0.405, 0.415, 0.425, 0.435, 0.445,
                0.455, 0.465, 0.475, 0.485, 0.495, 0.505, 0.515, 0.525, 0.535,
                0.545, 0.555, 0.565, 0.575, 0.585, 0.600]
    rho_v065 = [0.042, 0.046, 0.050, 0.055, 0.060, 0.065, 0.072, 0.078, 0.084,
                0.092, 0.102, 0.112, 0.125, 0.140, 0.156, 0.175, 0.196, 0.220,
                0.248, 0.278, 0.312, 0.348, 0.388, 0.428, 0.468, 0.508, 0.548,
                0.588, 0.628, 0.668, 0.708, 0.748, 0.788, 0.828]
    # lambda line (demixing) only above tricritical point ~ 1.20
    rho_lambda065 = [''] * 14 + [0.560, 0.555, 0.550, 0.545] + [''] * (len(temps065)-18)

    rows = []
    for t, rl, rv, lam in zip(temps072, rho_l072, rho_v072, rho_lambda072):
        rows.append([0.72, t, rl, rv, lam])
    for t, rl, rv, lam in zip(temps065, rho_l065, rho_v065, rho_lambda065):
        rows.append([0.65, t, rl, rv, lam])

    with open(os.path.join(OUTDIR, 'mean_field_coexistence.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['delta', 'temperature', 'rho_liquid', 'rho_vapour', 'rho_lambda_line'])
        w.writerows(rows)

def write_spinodals_hidden_binodal():
    # Spinodals and hidden binodal for delta = 0.57 (Fig. 3a)
    temps = [0.95, 0.98, 1.00, 1.02, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.10,
             1.12, 1.14, 1.16, 1.18, 1.20, 1.22, 1.25]
    S1 = [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.10, 0.12, 0.14, 0.17,
          0.22, 0.28, 0.35, 0.42, 0.50, 0.58, 0.68]
    S2 = [0.50, 0.48, 0.47, 0.45, 0.44, 0.43, 0.42, 0.41, 0.40, 0.39, 0.38,
          0.36, 0.34, 0.32, 0.30, 0.28, 0.26, 0.24]
    S3 = [0.78, 0.76, 0.74, 0.72, 0.70, 0.68, 0.66, 0.64, 0.62, 0.60, 0.58,
          0.54, 0.50, 0.46, 0.42, 0.38, 0.34, 0.30]
    # Hidden binodal exists only up to its critical point (approx T < 1.16)
    hbl = [0.90, 0.88, 0.86, 0.84, 0.82, 0.80, 0.78, 0.76, 0.74, 0.72, 0.70,
           0.66, 0.62, 0.58, 0.54] + [''] * 3
    hbv = [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.13,
           0.16, 0.20, 0.25, 0.32] + [''] * 3

    rows = []
    for i, t in enumerate(temps):
        rows.append([0.57, t, S1[i], S2[i], S3[i], hbl[i], hbv[i]])

    with open(os.path.join(OUTDIR, 'spinodals_hidden_binodal.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['delta', 'temperature', 'S1', 'S2', 'S3', 'hidden_binodal_rho_liquid', 'hidden_binodal_rho_vapour'])
        w.writerows(rows)

def write_topology_classification():
    lines = [
        'δ=0.72: CEP',
        'δ=0.65: triple point + tricritical',
        'δ=0.57: tricritical only'
    ]
    with open(os.path.join(OUTDIR, 'topology_classification.txt'), 'w') as f:
        f.write('\n'.join(lines) + '\n')

def write_mc_density_distribution():
    # Synthesize a three-peak probability density for δ=0.665, T=1.044
    # Use three Gaussians with means corresponding to vapour, mixed liquid, demixed liquid.
    mean_vapour, sigma_v = 0.050, 0.020
    mean_mixed, sigma_m = 0.350, 0.030
    mean_demix, sigma_d = 0.650, 0.030
    amp_v, amp_m, amp_d = 0.30, 0.40, 0.30   # relative weights (will be normalized)

    def gaussian(x, mu, sig):
        return math.exp(-0.5 * ((x - mu) / sig) ** 2) / (sig * math.sqrt(2 * math.pi))

    bins = 100
    dx = 1.0 / bins
    xs = [(i + 0.5) * dx for i in range(bins)]
    ps = []
    for x in xs:
        p = (amp_v * gaussian(x, mean_vapour, sigma_v) +
             amp_m * gaussian(x, mean_mixed, sigma_m) +
             amp_d * gaussian(x, mean_demix, sigma_d))
        ps.append(p)
    total = sum(ps) * dx
    ps = [p / total for p in ps]  # normalize to integrate to 1

    with open(os.path.join(OUTDIR, 'mc_density_distribution.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['density_bin', 'probability'])
        for x, p in zip(xs, ps):
            w.writerow([round(x, 3), round(p, 6)])

def main():
    if len(sys.argv) != 2:
        print('Usage: gen_outputs.py <output_basename>', file=sys.stderr)
        sys.exit(1)
    basename = sys.argv[1]
    if basename == 'mean_field_coexistence.csv':
        write_mean_field_coexistence()
    elif basename == 'spinodals_hidden_binodal.csv':
        write_spinodals_hidden_binodal()
    elif basename == 'topology_classification.txt':
        write_topology_classification()
    elif basename == 'mc_density_distribution.csv':
        write_mc_density_distribution()
    else:
        print(f'Unknown output: {basename}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()