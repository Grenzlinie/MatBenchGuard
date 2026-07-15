import csv
import math
import sys
import argparse

def gaussian(x, mu, sigma, amp):
    return amp * math.exp(-((x - mu) / sigma) ** 2 / 2.0)

def generate_energy(min_e, max_e, step):
    n = int((max_e - min_e) / step + 1.5)
    return [min_e + i*step for i in range(n)]

def write_dos_csv(output_path, energies, dos_up, dos_down):
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy_eV', 'dos_up', 'dos_down'])
        for i, e in enumerate(energies):
            writer.writerow(["{:.6f}".format(e), "{:.6f}".format(dos_up[i]), "{:.6f}".format(dos_down[i])])

def gen_cr_ainp():
    energies = generate_energy(-2.0, 4.0, 0.05)
    dos_up = []
    dos_down = []
    shift = 0.0  # ainp: gap centred
    gap_lo = -1.0 - shift
    gap_hi = 1.0 - shift
    for e in energies:
        up = gaussian(e, -1.5, 1.0, 5.0) + gaussian(e, 0.5, 1.5, 1.5) + 0.1
        if gap_lo <= e <= gap_hi:
            down = 0.0
        else:
            down = gaussian(e, 2.0, 0.8, 6.0) + gaussian(e, -2.5, 0.5, 0.5)
        dos_up.append(up)
        dos_down.append(down)
    return energies, dos_up, dos_down

def gen_cr_azb():
    energies = generate_energy(-2.0, 4.0, 0.05)
    shift = 0.5   # Fermi shifted towards conduction band
    dos_up = []
    dos_down = []
    for e in energies:
        e_b = e - shift
        up = gaussian(e_b, -1.5, 1.0, 5.0) + gaussian(e_b, 0.5, 1.5, 1.5) + 0.1
        if -1.0 <= e_b <= 1.0:
            down = 0.0
        else:
            down = gaussian(e_b, 2.0, 0.8, 6.0) + gaussian(e_b, -2.5, 0.5, 0.5)
        dos_up.append(up)
        dos_down.append(down)
    return energies, dos_up, dos_down

def gen_p_ainp():
    energies = generate_energy(-2.0, 4.0, 0.05)
    dos_up = []
    dos_down = []
    for e in energies:
        up = gaussian(e, 0.0, 0.4, 4.0) + gaussian(e, -1.0, 0.8, 2.0) + 0.2
        down = gaussian(e, 0.0, 0.4, 4.0) + gaussian(e, 0.5, 0.6, 1.5) + 0.2
        dos_up.append(up)
        dos_down.append(down)
    return energies, dos_up, dos_down

def gen_p_azb():
    energies = generate_energy(-2.0, 4.0, 0.05)
    dos_up = []
    dos_down = []
    for e in energies:
        up = gaussian(e, 0.2, 0.4, 3.5) + gaussian(e, -0.8, 0.8, 2.0) + 0.2
        down = gaussian(e, 0.2, 0.4, 3.5) + gaussian(e, 0.7, 0.6, 1.5) + 0.2
        dos_up.append(up)
        dos_down.append(down)
    return energies, dos_up, dos_down

def gen_mag():
    data = [
        ("Cr", 5.89, "Cr", "S", 3.68),
        ("Cr", 5.89, "P", "S-1", -0.33),
        ("Cr", 5.89, "Cr", "C", 3.35),
        ("Cr", 5.89, "P", "C", -0.35),
        ("Cr", 5.48, "Cr", "S", 3.57),
        ("Cr", 5.48, "P", "S-1", -0.24),
        ("Cr", 5.48, "Cr", "C", 3.22),
        ("Cr", 5.48, "P", "C", -0.22),
        ("P", 5.89, "P", "S", -0.76),
        ("P", 5.89, "Cr", "S-1", 2.73),
        ("P", 5.89, "P", "C", -0.35),
        ("P", 5.89, "Cr", "C", 3.35),
        ("P", 5.48, "P", "S", -0.55),
        ("P", 5.48, "Cr", "S-1", 2.30),
        ("P", 5.48, "P", "C", -0.22),
        ("P", 5.48, "Cr", "C", 3.22),
    ]
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--type', required=True)
    args = parser.parse_args()
    if args.type == 'mag':
        data = gen_mag()
        with open(args.output, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['termination','lattice_constant_A','atom','layer','magnetic_moment_muB'])
            for row in data:
                writer.writerow(row)
    else:
        if args.type == 'cr_ainp':
            energies, dos_up, dos_down = gen_cr_ainp()
        elif args.type == 'cr_azb':
            energies, dos_up, dos_down = gen_cr_azb()
        elif args.type == 'p_ainp':
            energies, dos_up, dos_down = gen_p_ainp()
        elif args.type == 'p_azb':
            energies, dos_up, dos_down = gen_p_azb()
        else:
            raise ValueError(f"Unknown type {args.type}")
        write_dos_csv(args.output, energies, dos_up, dos_down)

if __name__ == '__main__':
    main()