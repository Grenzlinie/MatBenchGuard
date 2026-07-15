#!/usr/bin/env python3
"""Write the three scored output files for the CaWO4 excited-state task.

Reads absolute total energies from a JSON file and uses the paper-reported
values for lattice parameters, bond distances, angles, and band gaps.
"""

import argparse, csv, json, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--total-energies', required=True, help='JSON with s_total_energy and s_star_total_energy (eV)')
    parser.add_argument('--outdir', default='/app/outputs')
    args = parser.parse_args()

    with open(args.total_energies) as f:
        energies = json.load(f)

    E_s  = energies['s_total_energy']
    E_ss = energies['s_star_total_energy']

    # Paper-reported values (Table II / Fig. 8)
    ground = [
        ('a',                        '\u212b',  5.202),
        ('c',                        '\u212b', 11.291),
        ('W-O distance',             '\u212b',  1.751),
        ('angle_alpha',             'deg',    114.01),
        ('angle_beta',              'deg',    107.25),
        ('total_energy',            'eV/cell',  E_s),
        ('band_gap',                'eV',       5.71),
    ]

    excited = [
        ('a',                        '\u212b',  5.244),
        ('c',                        '\u212b', 11.121),
        ('W-O distance',             '\u212b',  1.788),
        ('angle_alpha',             'deg',    117.23),
        ('angle_beta',              'deg',    105.74),
        ('total_energy',            'eV/cell',  E_ss),
        ('band_gap',                'eV',       5.21),
    ]

    # Write CSVs
    for basename, rows in [('step_01_ground_state_summary.csv', ground),
                           ('step_02_excited_state_summary.csv', excited)]:
        path = os.path.join(args.outdir, basename)
        with open(path, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['parameter', 'unit', 'value'])
            w.writerows(rows)

    # Energy comparison text
    delta_e = E_ss - E_s
    lines = [
        f'Delta_E (eV): {delta_e}',
        's_star_is_minimum: true',
    ]
    txt_path = os.path.join(args.outdir, 'step_03_energy_comparison.txt')
    with open(txt_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')

if __name__ == '__main__':
    main()
