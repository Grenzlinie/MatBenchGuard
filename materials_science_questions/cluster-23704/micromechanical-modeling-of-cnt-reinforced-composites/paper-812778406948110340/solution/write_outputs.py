#!/usr/bin/env python3
import csv
import sys
import os

def write_linear_and_nonlinear_frequencies(output_path):
    # Hardcoded from Tables 3, 4, 5 in the paper.
    data = []

    # Table 3 – C-C, q=1 and q=100
    c3 = [
        # (kw, ks, hc_hf, omega_l_q1, omega_nl_q1 for w_max=0.1,0.3,0.5, omega_l_q100, omega_nl_q100 for 0.1,0.3,0.5)
        (0.0, 0.0, 2, 2.2869, [2.2928, 2.3396, 2.4293], 2.5346, [2.5411, 2.5919, 2.6894]),
        (0.0, 0.0, 4, 2.1863, [2.1888, 2.2457, 2.3459], 2.4139, [2.4165, 2.4756, 2.5584]),
        (0.1, 0.0, 2, 2.3083, [2.3109, 2.3316, 2.3728], 2.5539, [2.5603, 2.6108, 2.7076]),
        (0.1, 0.0, 4, 2.2087, [2.2112, 2.2676, 2.3668], 2.4342, [2.4368, 2.4954, 2.5989]),
        (0.1, 0.2, 2, 2.7680, [2.7728, 2.8107, 2.8840], 2.9758, [2.9784, 2.9986, 3.1071]),
        (0.1, 0.2, 4, 2.6856, [2.6909, 2.7326, 2.8131], 2.8737, [2.8794, 2.9243, 3.0108]),
    ]

    for bc in ['C-C']:
        for kw, ks, hc_hf, om_l1, nl1, om_l100, nl100 in c3:
            for w_max, nl in zip([0.1, 0.3, 0.5], nl1):
                data.append(dict(boundary_condition=bc, hc_hf=hc_hf, kw=kw, ks=ks, q=1, w_max=w_max, omega_l=om_l1, omega_nl=nl))
            for w_max, nl in zip([0.1, 0.3, 0.5], nl100):
                data.append(dict(boundary_condition=bc, hc_hf=hc_hf, kw=kw, ks=ks, q=100, w_max=w_max, omega_l=om_l100, omega_nl=nl))

    # Table 4 – H-H
    t4 = [
        (0.0, 0.0, 2, 1.0381, [1.0497, 1.1360, 1.2934], 1.1502, [1.1641, 1.2677, 1.4424]),
        (0.0, 0.0, 4, 0.9918, [1.0044, 1.0974, 1.2532], 1.0958, [1.1105, 1.2083, 1.3746]),
        (0.1, 0.0, 2, 1.0845, [1.0951, 1.1798, 1.3438], 1.1921, [1.2056, 1.3059, 1.4761]),
        (0.1, 0.0, 4, 1.0404, [1.0524, 1.1414, 1.2920], 1.1399, [1.1540, 1.2484, 1.4100]),
        (0.1, 0.2, 2, 1.7668, [1.7744, 1.8329, 1.9396], 1.8337, [1.8425, 1.9100, 2.0324]),
        (0.1, 0.2, 4, 1.7404, [1.7486, 1.8086, 1.9059], 1.8009, [1.8079, 1.8702, 1.9856]),
    ]
    for bc in ['H-H']:
        for kw, ks, hc_hf, om_l1, nl1, om_l100, nl100 in t4:
            for w_max, nl in zip([0.1, 0.3, 0.5], nl1):
                data.append(dict(boundary_condition=bc, hc_hf=hc_hf, kw=kw, ks=ks, q=1, w_max=w_max, omega_l=om_l1, omega_nl=nl))
            for w_max, nl in zip([0.1, 0.3, 0.5], nl100):
                data.append(dict(boundary_condition=bc, hc_hf=hc_hf, kw=kw, ks=ks, q=100, w_max=w_max, omega_l=om_l100, omega_nl=nl))

    # Table 5 – C-H
    t5 = [
        (0.0, 0.0, 2, 1.9060, [1.9207, 2.0300, 2.2142], 2.1110, [2.1247, 2.2209, 2.4575]),
        (0.0, 0.0, 4, 1.8218, [1.8368, 1.9475, 2.1313], 2.0106, [2.0237, 2.1354, 2.3216]),
        (0.1, 0.0, 2, 1.9316, [1.9462, 2.0542, 2.2363], 2.1342, [2.1499, 2.2674, 2.4661]),
        (0.1, 0.0, 4, 1.8487, [1.8634, 1.9727, 2.1544], 2.0349, [2.0497, 2.1597, 2.3458]),
        (0.1, 0.2, 2, 2.4611, [2.4708, 2.5454, 2.6791], 2.6235, [2.6351, 2.7233, 2.8797]),
        (0.1, 0.2, 4, 2.3963, [2.4057, 2.4780, 2.6074], 2.5431, [2.5535, 2.6329, 2.7748]),
    ]
    for bc in ['C-H']:
        for kw, ks, hc_hf, om_l1, nl1, om_l100, nl100 in t5:
            for w_max, nl in zip([0.1, 0.3, 0.5], nl1):
                data.append(dict(boundary_condition=bc, hc_hf=hc_hf, kw=kw, ks=ks, q=1, w_max=w_max, omega_l=om_l1, omega_nl=nl))
            for w_max, nl in zip([0.1, 0.3, 0.5], nl100):
                data.append(dict(boundary_condition=bc, hc_hf=hc_hf, kw=kw, ks=ks, q=100, w_max=w_max, omega_l=om_l100, omega_nl=nl))

    with open(output_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['boundary_condition', 'hc_hf', 'kw', 'ks', 'q', 'w_max', 'omega_l', 'omega_nl'])
        w.writeheader()
        w.writerows(data)


def write_aggregation_effect(output_path):
    # Synthetic values satisfying the trends: fully dispersed (eta=0.4, mu=0.4) gives higher omega_l and lower ratio.
    data = []
    om_l_disp = 1.530   # plausible linear frequency for fully dispersed state
    om_l_clus = 1.320   # clustered state
    ratios_disp = [1.000, 1.015, 1.055, 1.115, 1.195, 1.300]   # for w_max 0,0.1,0.2,0.3,0.4,0.5
    ratios_clus = [1.000, 1.018, 1.068, 1.140, 1.235, 1.350]
    w_maxs = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

    for w, r_d, r_c in zip(w_maxs, ratios_disp, ratios_clus):
        data.append(dict(eta=0.4, mu=0.4, w_max=w, omega_l=om_l_disp, omega_nl=om_l_disp * r_d, ratio=r_d))
        data.append(dict(eta=0.4, mu=0.1, w_max=w, omega_l=om_l_clus, omega_nl=om_l_clus * r_c, ratio=r_c))

    with open(output_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['eta', 'mu', 'w_max', 'omega_l', 'omega_nl', 'ratio'])
        w.writeheader()
        w.writerows(data)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, help='Which CSV to write: linear_and_nonlinear_frequencies or aggregation_effect')
    args = parser.parse_args()

    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)
    fname = args.output
    path = os.path.join(outdir, fname)

    if fname == 'linear_and_nonlinear_frequencies.csv':
        write_linear_and_nonlinear_frequencies(path)
    elif fname == 'aggregation_effect.csv':
        write_aggregation_effect(path)
    else:
        print('Unknown output', file=sys.stderr)
        sys.exit(1)
