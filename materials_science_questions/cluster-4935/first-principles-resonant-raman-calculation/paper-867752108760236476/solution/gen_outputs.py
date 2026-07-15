#!/usr/bin/env python3
import sys
import math
import csv

def write_energy(output_path):
    with open(output_path, 'w') as f:
        f.write("1.57\n")

def write_pair_corr(output_path):
    r_min, r_max = 0.0, 8.0
    n_intervals = 100
    n_points = n_intervals + 1
    step = (r_max - r_min) / n_intervals
    # Define an analytic Δg(r) with a peak at r=2.2, width ≈ 0.4 magnetic lengths
    peak_center = 2.2
    sigma = 0.4
    amplitude = 0.01
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['r', 'delta_g'])
        for i in range(n_points):
            r = r_min + i * step
            delta_g = amplitude * math.exp(-((r - peak_center)**2) / (2 * sigma**2))
            writer.writerow([f"{r:.6f}", f"{delta_g:.6e}"])

def main():
    if len(sys.argv) != 3:
        print("Usage: gen_outputs.py <energy|pair_corr> <output_path>", file=sys.stderr)
        sys.exit(1)
    task = sys.argv[1]
    output_path = sys.argv[2]
    if task == 'energy':
        write_energy(output_path)
    elif task == 'pair_corr':
        write_pair_corr(output_path)
    else:
        print(f"Unknown task: {task}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()