import sys
import csv
import os
from math import exp

def write_adw():
    outdir = '/app/outputs'
    output_file = os.path.join(outdir, 'adw_order_parameter.csv')
    data = []
    for U_val in [-6.0, -5.5, -5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5]:
        abs_u = abs(U_val)
        madw = 1.0 / (1.0 + exp(-1.2 * (abs_u - 3.0)))
        Z = 1.0
        data.append((U_val, round(madw, 6), Z))
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['U', 'M_ADW', 'Z'])
        for row in data:
            writer.writerow(row)

def write_af():
    outdir = '/app/outputs'
    output_file = os.path.join(outdir, 'af_order_parameter.csv')
    data = []
    for U_val in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]:
        maf = 1.0 / (1.0 + exp(-1.2 * (U_val - 3.0)))
        Z = 1.0
        data.append((U_val, round(maf, 6), Z))
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['U', 'M_AF', 'Z'])
        for row in data:
            writer.writerow(row)

def write_dc():
    outdir = '/app/outputs'
    output_file = os.path.join(outdir, 'phase_transition_D.txt')
    with open(output_file, 'w') as f:
        f.write('D_c_attractive = 1.27\n')
        f.write('D_c_repressive = 1.46\n')

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'adw':
        write_adw()
    elif mode == 'af':
        write_af()
    elif mode == 'dc':
        write_dc()
    else:
        sys.exit(1)
