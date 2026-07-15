#!/usr/bin/env python3
import argparse, csv, math, os

def write_stability(outfile):
    """Formation enthalpies per atom (eV/atom) for reference and ternary phases."""
    rows = [
        ("Cu",            0.000),
        ("Sn",            0.000),
        ("S",             0.000),
        ("Cu2S",         -0.344),
        ("SnS",          -0.560),
        ("SnS2",         -0.467),
        ("CuS",          -0.301),
        ("Cu3SnS4",      -0.420),
        ("Cu4SnS4",      -0.490),
        ("Cu2SnS3",      -0.550),
        ("Cu4Sn7S16",    -0.480),
    ]
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['compound', 'formation_enthalpy_eV_per_atom'])
        writer.writerows(rows)

def write_defect(outfile):
    """Cu-vacancy formation energies (eV) for charge states -1 and Fermi pinning ranges."""
    # Each compound: (compound, charge_state, formation_energy_eV)
    # For charge -1 (acceptor) we give a representative value at Cu-poor conditions.
    defect_rows = [
        ("Cu4SnS4",   -1, 1.60),
        ("Cu4SnS4",    0, 2.20),
        ("Cu2SnS3",   -1, 2.00),
        ("Cu2SnS3",    0, 2.60),
        ("Cu4Sn7S16", -1, 1.10),
        ("Cu4Sn7S16",  0, 1.70),
    ]
    # E_F_pin ranges (eV) relative to VBM, low then high for each compound.
    # Order: Cu4SnS4, Cu2SnS3, Cu4Sn7S16.
    pin_range_low  = [0.50, 1.63, 0.80]   # Cu-rich (lower pinning)
    pin_range_high = [0.75, 2.33, 1.05]   # Cu-poor (higher pinning)
    pin_rows = []
    for low in pin_range_low:
        pin_rows.append(("E_F_pin_range", 0, low))
    for high in pin_range_high:
        pin_rows.append(("E_F_pin_range", 0, high))
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['charge_state', 'compound', 'formation_energy_eV'])
        writer.writerows(defect_rows)
        writer.writerows(pin_rows)

def write_bandgaps(outfile):
    """GW quasiparticle band gaps (eV). Direct and indirect if applicable."""
    rows = [
        ("Cu4SnS4",   "direct",   0.82),
        ("Cu2SnS3",   "direct",   0.63),
        ("Cu4Sn7S16", "indirect", 1.23),
        ("Cu4Sn7S16", "direct",   1.27),
    ]
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['compound', 'gap_type', 'quasiparticle_gap_eV'])
        writer.writerows(rows)

def absorption_curve(energy, gap, strength, power):
    """Simple absorption model: ~ (E-Eg)^power above gap, with small tail below."""
    if energy < gap - 0.05:
        return 50.0   # very small sub-gap
    delta = energy - gap
    if delta <= 0:
        return max(50.0, strength * 0.01)
    return max(50.0, strength * (delta ** power))

def write_absorption(outfile):
    """Optical absorption coefficient vs photon energy (0–3 eV)."""
    energies = [round(i*0.05, 2) for i in range(0, 61)]  # 0.00 to 3.00 step 0.05
    compounds = [
        ("Cu2SnS3",      0.63, 1.1e5, 0.5),
        ("Cu4SnS4",      0.82, 1.0e5, 0.5),
        ("Cu4Sn7S16",    1.23, 0.9e5, 1.0),
    ]
    rows = []
    for name, gap, strength, power in compounds:
        for e in energies:
            coeff = absorption_curve(e, gap, strength, power)
            coeff = min(coeff, 2.0e5)   # cap at 2e5 cm-1
            rows.append((coeff, name, e))
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['absorption_coefficient_cm-1', 'compound', 'energy_eV'])
        writer.writerows(rows)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--outfile', required=True)
    parser.add_argument('--mode', required=True,
                        choices=['stability', 'defect', 'bandgaps', 'absorption'])
    args = parser.parse_args()
    if args.mode == 'stability':
        write_stability(args.outfile)
    elif args.mode == 'defect':
        write_defect(args.outfile)
    elif args.mode == 'bandgaps':
        write_bandgaps(args.outfile)
    elif args.mode == 'absorption':
        write_absorption(args.outfile)

if __name__ == '__main__':
    main()
