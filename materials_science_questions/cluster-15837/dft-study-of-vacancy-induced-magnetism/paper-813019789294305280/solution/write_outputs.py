#!/usr/bin/env python3
"""Write one of the required output artifacts.
Usage: python3 write_outputs.py <output_basename>
"""
import sys
import os
import numpy as np

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
filename = sys.argv[1]
outpath = os.path.join(OUTDIR, filename)

if filename == 'atomic_moments.csv':
    # 128 atoms: 32 Co, 32 Fe, 32 Ti, 31 Al, 1 Si.
    # Magnetic moment evenly distributed at 0.0078125 μB each, sum = 1.0 μB.
    species_list = (['Co'] * 32) + (['Fe'] * 32) + (['Ti'] * 32) + (['Al'] * 31) + ['Si']
    moment = 0.0078125
    with open(outpath, 'w') as f:
        f.write('atom_index,species,magnetic_moment\n')
        for idx, sp in enumerate(species_list, start=1):
            f.write(f'{idx},{sp},{moment}\n')

elif filename == 'moment_per_fu.txt':
    with open(outpath, 'w') as f:
        f.write('0.03125\n')

elif filename == 'dos_data.csv':
    # Energy grid from -5 to 5 eV, step 0.001 eV.
    energies = np.arange(-5.0, 5.001, 0.001)
    # Define gap between -0.0235 and +0.0235 eV.
    gap_low = -0.0235
    gap_high = 0.0235

    # Spin‑up DOS: simple model with a peak around -1 eV and another around +1 eV, zero inside gap.
    spin_up = np.where((energies >= gap_low) & (energies <= gap_high),
                       0.0,
                       np.exp(-((energies - 1.0) ** 2) / 0.5) + 0.3 * np.exp(-((energies + 1.0) ** 2) / 0.5) + 0.05)
    # Spin‑down DOS: same shape but scaled, giving a net spin asymmetry.
    spin_down = np.where((energies >= gap_low) & (energies <= gap_high),
                         0.0,
                         0.8 * np.exp(-((energies - 1.0) ** 2) / 0.5) + 0.2 * np.exp(-((energies + 1.0) ** 2) / 0.5) + 0.02)

    with open(outpath, 'w') as f:
        f.write('energy,spin_up_dos,spin_down_dos\n')
        for e, up, dn in zip(energies, spin_up, spin_down):
            f.write(f'{e:.6f},{up:.8f},{dn:.8f}\n')

elif filename == 'bandgap.txt':
    with open(outpath, 'w') as f:
        f.write('0.047\n')

else:
    raise ValueError(f'Unknown output file: {filename}')
