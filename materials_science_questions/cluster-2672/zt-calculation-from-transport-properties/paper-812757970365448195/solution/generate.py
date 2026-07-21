import csv
import math
import sys
import os

def generate_electronic_transport(outdir):
    n_values = [1e18, 2e18, 3e18, 4e18, 5e18, 6e18, 6.5e18, 7e18, 7.1e18, 8e18, 9e18, 1e19, 2e19, 3e19, 5e19, 8e19, 1e20]
    rows = []
    for n in n_values:
        # H phase
        sigma_H = 7500 * (n/6.5e18)**0.8
        S_H = 180.0 - 30.9 * math.log10(n/1e18)
        kappa_e_H = (0.094 / 7500) * sigma_H
        P_H = (S_H**2) * sigma_H * 1e-6
        # W phase
        sigma_W = 4103 * (n/7.1e18)**0.8
        S_W = 202.0 - 25.3 * math.log10(n/1e18)
        kappa_e_W = (0.062045 / 4103) * sigma_W
        P_W = (S_W**2) * sigma_W * 1e-6
        rows.append({
            'n_cm3': f"{n:.2e}",
            'sigma_H_Sm': f"{sigma_H:.1f}",
            'sigma_W_Sm': f"{sigma_W:.1f}",
            'S_H_uVK': f"{S_H:.2f}",
            'S_W_uVK': f"{S_W:.2f}",
            'kappa_e_H_WmK': f"{kappa_e_H:.6f}",
            'kappa_e_W_WmK': f"{kappa_e_W:.6f}",
            'P_H_uWmK2': f"{P_H:.2f}",
            'P_W_uWmK2': f"{P_W:.2f}",
        })
    filepath = os.path.join(outdir, 'electronic_transport.csv')
    fieldnames = ['n_cm3','sigma_H_Sm','sigma_W_Sm','S_H_uVK','S_W_uVK','kappa_e_H_WmK','kappa_e_W_WmK','P_H_uWmK2','P_W_uWmK2']
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def generate_temperature_dependence_ZT(outdir):
    data = [
        (200, 0.00280,  0.00250,  1.12),
        (300, 0.005295, 0.004794, 1.1045),
        (400, 0.00850,  0.007870, 1.080),
        (500, 0.01200,  0.011215, 1.070),
        (600, 0.01600,  0.014815, 1.080),
        (700, 0.02050,  0.018636, 1.100),
        (800, 0.02500,  0.022124, 1.130),
        (900, 0.03000,  0.025862, 1.160),
        (1000,0.03500,  0.029661, 1.180),
    ]
    filepath = os.path.join(outdir, 'temperature_dependence_ZT.csv')
    fieldnames = ['T_K','ZT_H','ZT_W','ratio_ZT_HW']
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for T, zth, ztw, ratio in data:
            writer.writerow({'T_K': T, 'ZT_H': zth, 'ZT_W': ztw, 'ratio_ZT_HW': ratio})

if __name__ == '__main__':
    outdir = sys.argv[1]
    generate_electronic_transport(outdir)
    generate_temperature_dependence_ZT(outdir)
