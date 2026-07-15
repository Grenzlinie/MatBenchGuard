import argparse
import csv
import sys

def generate_mlg(output_path):
    rows = []
    # strain 0 to 0.12, step 0.005
    for i in range(0, 25):
        strain = i * 0.005
        if strain <= 0.1:
            force = 5.0 * strain
        else:
            force = 0.5 - 20.0 * (strain - 0.1)
        strain_energy = strain * strain + 0.5 * strain  # eV, arbitrary
        rows.append((strain, force, strain_energy))
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['strain', 'force', 'strain_energy'])
        writer.writerows(rows)

def generate_gh(output_path):
    rows = []
    # strain 0 to 12.5, step 0.5
    for i in range(0, 26):
        strain = i * 0.5
        force = 0.2 * strain          # increasing, no peak
        strain_energy = 0.5 * strain * strain
        rows.append((strain, force, strain_energy))
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['strain', 'force', 'strain_energy'])
        writer.writerows(rows)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--material', required=True, choices=['MLG', 'GH'])
    args = parser.parse_args()
    if args.material == 'MLG':
        generate_mlg(args.output)
    else:
        generate_gh(args.output)
