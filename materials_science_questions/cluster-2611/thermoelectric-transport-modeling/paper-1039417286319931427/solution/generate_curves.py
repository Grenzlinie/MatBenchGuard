#!/usr/bin/env python3
import csv, math, argparse, sys

def lorentzian(x, x0, gamma, A):
    return A * (gamma/2)**2 / ((x-x0)**2 + (gamma/2)**2)

def generate_transmission():
    energies = [ -2.0 + i*0.001 for i in range(4001) ]
    rows = []
    for E in energies:
        T0 = 0.02 + 0.05*E**2
        # C60: smooth baseline
        rows.append((round(E,6), 'C60', round(T0, 6)))
        # Ni@C60: two close resonances at -0.96 and -0.99 eV
        T_ni = T0 + lorentzian(E, -0.96, 0.01, 0.2) + lorentzian(E, -0.99, 0.01, 0.2)
        rows.append((round(E,6), 'Ni@C60', round(T_ni, 6)))
        # Co@C60: three resonances at -0.1, -1.08, -1.2 eV
        T_co = T0 + lorentzian(E, -0.1, 0.01, 0.3) + lorentzian(E, -1.08, 0.01, 0.2) + lorentzian(E, -1.2, 0.01, 0.2)
        rows.append((round(E,6), 'Co@C60', round(T_co, 6)))
    return rows, ['energy(eV)', 'system', 'transmission']

def generate_seebeck():
    energies = [ -2.0 + i*0.001 for i in range(4001) ]
    rows = []
    for E in energies:
        # C60: small amplitude
        S_c60 = 30 * math.sin(2*math.pi*E) * math.exp(-E**2/0.5)
        rows.append((round(E,6), 'C60', round(S_c60, 4)))
        # Ni@C60: large amplitude peaks near -0.96 and -0.99 eV
        S_ni = 192 * math.exp(-((E+0.96)**2)/(2*0.01**2)) - 172 * math.exp(-((E+0.99)**2)/(2*0.01**2))
        rows.append((round(E,6), 'Ni@C60', round(S_ni, 4)))
        # Co@C60: range +105 to -190 µV/K in window 0 to -0.3 eV, localized pulse
        win = math.exp(-((E+0.15)**2)/(2*0.1**2))  # envelope centred at -0.15 eV
        sin_val = math.sin(math.pi*(E+0.15)/0.3)
        S_co = (147.5 * sin_val - 42.5) * win
        rows.append((round(E,6), 'Co@C60', round(S_co, 4)))
    return rows, ['energy(eV)', 'system', 'seebeck_coefficient']

def generate_zt():
    energies = [ -2.0 + i*0.001 for i in range(4001) ]
    rows = []
    for E in energies:
        # C60: low peak somewhere
        ZT_c60 = 0.2 * math.exp(-((E+0.5)**2)/(2*0.1**2))
        rows.append((round(E,6), 'C60', round(ZT_c60, 6)))
        # Ni@C60: moderate peak near -0.96 eV
        ZT_ni = 0.5 * math.exp(-((E+0.96)**2)/(2*0.05**2))
        rows.append((round(E,6), 'Ni@C60', round(ZT_ni, 6)))
        # Co@C60: maximum 1.88 at 0.2 eV
        ZT_co = 1.88 * math.exp(-((E-0.2)**2)/(2*0.05**2))
        rows.append((round(E,6), 'Co@C60', round(ZT_co, 6)))
    return rows, ['energy(eV)', 'system', 'zt']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--type', required=True, choices=['transmission', 'seebeck', 'zt'])
    args = parser.parse_args()

    if args.type == 'transmission':
        rows, header = generate_transmission()
    elif args.type == 'seebeck':
        rows, header = generate_seebeck()
    elif args.type == 'zt':
        rows, header = generate_zt()
    else:
        sys.exit(1)

    with open(args.output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

if __name__ == '__main__':
    main()