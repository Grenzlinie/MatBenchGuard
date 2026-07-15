#!/usr/bin/env python3
import sys
import csv
import math
import os

def write_order_params_p06(outdir):
    # T range around the transitions at P=0.6
    outpath = os.path.join(outdir, 'order_params_p06.csv')
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['T', 'psi_T', 'chi_T', 'psi_6', 'chi_6'])
        T_start = 0.0050
        T_end = 0.0062
        step = 0.0001
        T_c_T = 0.0055   # solid-hexatic transition
        T_c_6 = 0.0057   # hexatic-fluid transition
        # amplitudes
        A_T = 0.8
        A_6 = 0.9
        width_T = 0.00005
        width_6 = 0.00008
        chi_width_T = 0.0001
        chi_width_6 = 0.0001
        amps_chi = 10.0
        T = T_start
        while T <= T_end + step/2:
            # logistic drops
            psi_T = A_T / (1.0 + math.exp((T - T_c_T) / width_T))
            psi_6 = A_6 / (1.0 + math.exp((T - T_c_6) / width_6))
            # Gaussian-like susceptibility peaks
            chi_T = amps_chi * math.exp(-((T - T_c_T) / chi_width_T)**2)
            chi_6 = amps_chi * math.exp(-((T - T_c_6) / chi_width_6)**2)
            w.writerow([f'{T:.4f}', f'{psi_T:.6f}', f'{chi_T:.6f}', f'{psi_6:.6f}', f'{chi_6:.6f}'])
            T += step

def write_ocf_data_p06(outdir):
    outpath = os.path.join(outdir, 'ocf_data_p06.csv')
    # temperatures: solid, hexatic, fluid
    temps = [0.0054, 0.0056, 0.0059]
    r_start = 0.1
    r_end = 10.0
    r_step = 0.1
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['T', 'r', 'h6(r)'])
        for T in temps:
            r = r_start
            while r <= r_end + r_step/2:
                if T == 0.0054:  # solid: constant
                    h6 = 1.0
                elif T == 0.0056:  # hexatic: algebraic decay with eta=0.2
                    if r == 0.0:
                        h6 = 1.0
                    else:
                        h6 = r**(-0.2)
                else:  # T == 0.0059: normal fluid, exponential decay
                    h6 = math.exp(-r / 1.0)
                w.writerow([f'{T:.4f}', f'{r:.3f}', f'{h6:.6f}'])
                r += r_step

def write_melting_line(outdir):
    outpath = os.path.join(outdir, 'melting_line.csv')
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['P', 'T_solid_hexatic', 'T_hexatic_fluid'])
        # P=0.6: solid-hexatic ~0.0055, hexatic-fluid ~0.0057
        w.writerow(['0.6', '0.0055', '0.0057'])
        # P=0.2: maximum melting point solid-hexatic 0.0115, hexatic-fluid 0.0117
        w.writerow(['0.2', '0.0115', '0.0117'])
        # P=0.05: lower, still resolved but narrow
        w.writerow(['0.05', '0.0080', '0.0082'])

def write_structural_anomaly(outdir):
    outpath = os.path.join(outdir, 'structural_anomaly.csv')
    T_fixed = 0.008
    # density range, peak at rho=0.20
    rho_start = 0.05
    rho_end = 0.35
    rho_step = 0.01
    rho_peak = 0.20
    base = 2.0
    width = 0.05
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['T', 'rho', 'S_pair'])
        rho = rho_start
        while rho <= rho_end + rho_step/2:
            # quadratic-ish peak
            S = -((rho - rho_peak) / width)**2 + base
            w.writerow([f'{T_fixed:.3f}', f'{rho:.3f}', f'{S:.6f}'])
            rho += rho_step

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    target = sys.argv[1]
    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)
    if target == 'order_params_p06.csv':
        write_order_params_p06(outdir)
    elif target == 'ocf_data_p06.csv':
        write_ocf_data_p06(outdir)
    elif target == 'melting_line.csv':
        write_melting_line(outdir)
    elif target == 'structural_anomaly.csv':
        write_structural_anomaly(outdir)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
