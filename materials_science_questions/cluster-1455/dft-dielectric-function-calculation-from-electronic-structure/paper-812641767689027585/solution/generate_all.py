import argparse
import csv
import json
import math
import sys


def summary_table(outpath):
    rows = [
        {"Material": "MgS", "Lattice_constant_a(Angstrom)": 4.41,
         "Buckling_delta(Angstrom)": 2.27, "Bond_length_MgX(Angstrom)": 2.49,
         "Cohesive_energy(eV/atom)": 3.85, "HSE06_band_gap(eV)": 4.70},
        {"Material": "MgSe", "Lattice_constant_a(Angstrom)": 4.52,
         "Buckling_delta(Angstrom)": 2.67, "Bond_length_MgX(Angstrom)": 2.63,
         "Cohesive_energy(eV/atom)": 3.40, "HSE06_band_gap(eV)": 4.51},
    ]
    fieldnames = ["Material", "Lattice_constant_a(Angstrom)",
                  "Buckling_delta(Angstrom)", "Bond_length_MgX(Angstrom)",
                  "Cohesive_energy(eV/atom)", "HSE06_band_gap(eV)"]
    with open(outpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def zero_strain_gaps(outpath):
    data = {
        "MgS": {"PBE_gap": 3.69, "HSE06_gap": 4.70},
        "MgSe": {"PBE_gap": 4.01, "HSE06_gap": 4.51}
    }
    with open(outpath, 'w') as f:
        json.dump(data, f, indent=2)


def strain_gaps(outpath):
    strains = [-8, -6, -4, -2, 0, 2, 4, 6, 8]
    # MgS: monotonic decrease from zero in both directions
    mgs_gaps = [3.50, 3.55, 3.60, 3.65, 3.69, 3.64, 3.55, 3.45, 3.35]
    # MgSe: increase up to -6%, then decrease
    mgse_gaps = [4.02, 4.07, 4.05, 4.03, 4.01, 3.95, 3.85, 3.75, 3.65]
    rows = []
    for mat, gaps in [("MgS", mgs_gaps), ("MgSe", mgse_gaps)]:
        for s, g in zip(strains, gaps):
            rows.append({"Material": mat, "Strain_percent": s, "PBE_band_gap(eV)": g})
    fieldnames = ["Material", "Strain_percent", "PBE_band_gap(eV)"]
    with open(outpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def lorentz_dielectric(energy_eV, eps_inf, oscillators):
    eps1 = eps_inf
    eps2 = 0.0
    for omega0, strength, gamma in oscillators:
        denom = (omega0**2 - energy_eV**2)**2 + (gamma * energy_eV)**2
        eps1 += strength * omega0**2 * (omega0**2 - energy_eV**2) / denom
        eps2 += strength * omega0**2 * gamma * energy_eV / denom
    return eps1, eps2


def dielectric_csv(material, outpath):
    if material == "MgS":
        eps_inf = 0.8
        osci = [
            (5.83, 0.8, 1.0),   # first peak
            (6.22, 0.53, 1.0),   # second peak
        ]
    elif material == "MgSe":
        eps_inf = 0.9
        osci = [
            (6.65, 0.7, 1.0),
            (7.60, 0.56, 1.0),
        ]
    else:
        raise ValueError("Unknown material")
    energy = [i * 0.1 for i in range(0, 151)]   # 0 .. 15 eV
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Energy_eV", "real_eps_ZZ", "imag_eps_ZZ"])
        for e in energy:
            eps1, eps2 = lorentz_dielectric(e, eps_inf, osci)
            writer.writerow([e, eps1, eps2])


def absorption_reflectivity_csv(material, outpath):
    if material == "MgS":
        eps_inf = 0.8
        osci = [
            (5.83, 0.8, 1.0),
            (6.22, 0.53, 1.0),
        ]
    elif material == "MgSe":
        eps_inf = 0.9
        osci = [
            (6.65, 0.7, 1.0),
            (7.60, 0.56, 1.0),
        ]
    else:
        raise ValueError("Unknown material")
    energy = [i * 0.1 for i in range(0, 151)]
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Energy_eV", "absorption_coeff_cm-1", "reflectivity_fraction"])
        for e in energy:
            eps1, eps2 = lorentz_dielectric(e, eps_inf, osci)
            eps_abs = math.sqrt(eps1**2 + eps2**2)
            n = math.sqrt((eps_abs + eps1) / 2)
            k = math.sqrt((eps_abs - eps1) / 2) if eps_abs > eps1 else 0.0
            if k > 0 and e > 0:
                alpha = 101283.0 * e * k   # cm^-1
            else:
                alpha = 0.0
            R = ((n - 1)**2 + k**2) / ((n + 1)**2 + k**2)
            writer.writerow([e, alpha, R])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['summary_table', 'zero_strain_gaps',
                        'strain_gaps', 'dielectric', 'absorption_reflectivity'])
    parser.add_argument('--material', help='MgS or MgSe')
    parser.add_argument('--out', required=True, help='output file path')
    args = parser.parse_args()
    if args.command == 'summary_table':
        summary_table(args.out)
    elif args.command == 'zero_strain_gaps':
        zero_strain_gaps(args.out)
    elif args.command == 'strain_gaps':
        strain_gaps(args.out)
    elif args.command == 'dielectric':
        if args.material not in ('MgS', 'MgSe'):
            print("--material must be MgS or MgSe", file=sys.stderr)
            sys.exit(1)
        dielectric_csv(args.material, args.out)
    elif args.command == 'absorption_reflectivity':
        if args.material not in ('MgS', 'MgSe'):
            print("--material must be MgS or MgSe", file=sys.stderr)
            sys.exit(1)
        absorption_reflectivity_csv(args.material, args.out)


if __name__ == '__main__':
    main()
