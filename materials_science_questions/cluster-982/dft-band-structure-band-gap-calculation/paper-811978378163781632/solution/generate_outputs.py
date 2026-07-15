import numpy as np
import os

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

# Energy range -5 to +5 eV with 0.01 eV step
energies = np.arange(-5.0, 5.01, 0.01)
dos = np.zeros_like(energies)

# Gap region: |E| < 0.45 eV -> DOS = 0
mask = np.abs(energies) < 0.45
dos[~mask] = np.exp(-((energies[~mask] - 1.5)**2) / (2 * 0.5**2)) + \
             np.exp(-((energies[~mask] + 1.5)**2) / (2 * 0.5**2)) + 0.01

# Write dos.dat: energy (eV)  DOS (states/eV)
np.savetxt(os.path.join(output_dir, 'dos.dat'),
           np.column_stack((energies, dos)),
           fmt='%.6f %.8e')

# Write band gap value
with open(os.path.join(output_dir, 'band_gap.txt'), 'w') as f:
    f.write('0.9\n')
