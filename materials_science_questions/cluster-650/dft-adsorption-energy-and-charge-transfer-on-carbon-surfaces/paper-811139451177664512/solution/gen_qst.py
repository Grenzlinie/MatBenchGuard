import csv
import math
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate q_st^o(H) CSV')
    parser.add_argument('--out', required=True, help='Output CSV path')
    parser.add_argument('--H_start', type=float, required=True)
    parser.add_argument('--H_end', type=float, required=True)
    parser.add_argument('--step', type=float, required=True)
    parser.add_argument('--H0', type=float, required=True)  # peak position
    parser.add_argument('--max_q', type=float, required=True)  # max q_st^o
    parser.add_argument('--kT', type=float, default=0.02585)  # thermal energy
    parser.add_argument('--width', type=float, default=0.8)  # gaussian sigma
    args = parser.parse_args()
    
    # generate H values
    H_vals = []
    H = args.H_start
    while H <= args.H_end + 1e-9:
        H_vals.append(round(H, 10))  # avoid float drift
        H += args.step
    
    # compute q_st^o for each H
    # Use gaussian peak plus baseline kT
    A = args.max_q - args.kT
    with open(args.out, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['H (Å)', 'q_st^o (eV)'])
        for H in H_vals:
            q = args.kT + A * math.exp(-((H - args.H0) / args.width)**2 / 2.0)
            writer.writerow([f'{H:.1f}', f'{q:.6f}'])
    
if __name__ == '__main__':
    main()
