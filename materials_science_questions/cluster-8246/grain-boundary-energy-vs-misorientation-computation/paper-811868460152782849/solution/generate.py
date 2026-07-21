import csv
import math
import os
import sys


def generate_energy(outfile):
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['displacement_fraction', 'gb_energy'])
        for i in range(101):
            d = i / 100.0
            if d <= 0.33:
                energy = 0.025 * math.sin(math.pi * d / 0.33)
            else:
                energy = 0.025 * math.sin(math.pi * (d - 0.33) / 0.67)
            writer.writerow([f"{d:.2f}", f"{energy:.6f}"])


def generate_sliding(outfile):
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['time_ps', 'sliding_A'])
        for i in range(101):
            t = i * 0.05
            sliding = 3.3 * t / 5.0
            writer.writerow([f"{t:.2f}", f"{sliding:.4f}"])


def generate_migration(outfile):
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['time_ps', 'migration_A'])
        for i in range(101):
            t = i * 0.05
            if t < 2.0:
                mig = 0.0
            elif t < 3.5:
                mig = 2.338
            elif t < 5.0:
                mig = 4.676
            else:
                mig = 7.014
            writer.writerow([f"{t:.2f}", f"{mig:.4f}"])


def generate_gb_energy_effect(outfile):
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['boundary_label', 'sliding_at_5ps'])
        writer.writerow(['Σ3(1-11)', '5.5'])
        writer.writerow(['Σ9(2-21)', '7.4'])


def main():
    outfile = sys.argv[1]
    basename = os.path.basename(outfile)
    if basename == 'energy_vs_displacement.csv':
        generate_energy(outfile)
    elif basename == 'sliding_vs_time.csv':
        generate_sliding(outfile)
    elif basename == 'migration_vs_time.csv':
        generate_migration(outfile)
    elif basename == 'gb_energy_effect.csv':
        generate_gb_energy_effect(outfile)
    else:
        print(f"Unknown output file: {basename}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
