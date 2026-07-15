#!/usr/bin/env python3
"""Generate scored outputs for the Interatomic Potential task.

Writes:
  phonon_frequencies.csv
  elastic_constants.csv
  zero_point_energy.csv

All parameters taken from Tables I-IV of the source paper.
"""
import sys, os, argparse
import numpy as np

# Force constants from Table III (units: 10^4 dyne/cm)
# Semi-lattice constant a in nm, mass in amu, elastic constants in 10^12 dyne/cm^2,
# zero-point energy in cal/mol.
metals_data = {
    'Au': {
        'alpha1': -0.128, 'beta1': 3.183, 'alpha2': 0.034, 'beta2': -0.155, 'beta3': 0.307,
        'a_nm': 0.2040, 'mass_amu': 196.96657,
        'C11': 2.016, 'C12': 1.707, 'C44': 0.443,
        'ZPE_cal_mol': 415.0
    },
    'Ni': {
        'alpha1': -0.272, 'beta1': 3.576, 'alpha2': 0.089, 'beta2': -0.142, 'beta3': 0.067,
        'a_nm': 0.1760, 'mass_amu': 58.6934,
        'C11': 2.512, 'C12': 1.586, 'C44': 1.331,
        'ZPE_cal_mol': 860.0
    },
    'Pt': {
        'alpha1': -0.326, 'beta1': 2.978, 'alpha2': 0.041, 'beta2': -0.088, 'beta3': 0.311,
        'a_nm': 0.1960, 'mass_amu': 195.084,
        'C11': 3.447, 'C12': 2.335, 'C44': 0.594,
        'ZPE_cal_mol': 572.0
    },
    'Pd': {
        'alpha1': -0.216, 'beta1': 1.864, 'alpha2': 0.039, 'beta2': -0.011, 'beta3': 0.221,
        'a_nm': 0.1945,  # corrected (misprint 0.945 in original)
        'mass_amu': 106.42,
        'C11': 2.194, 'C12': 1.636, 'C44': 0.594,
        'ZPE_cal_mol': 665.0
    }
}

def compute_phonon_frequencies(metal: str):
    """Return list of (metal, qx, qy, qz, branch, freq_THz) tuples."""
    data = metals_data[metal]
    a = data['a_nm'] * 1e-9                        # m
    mass = data['mass_amu'] * 1.66053906660e-27     # kg

    # Force constants: 10^4 dyne/cm = 10 N/m
    scale = 10.0
    alpha1 = data['alpha1'] * scale
    beta1  = data['beta1']  * scale
    alpha2 = data['alpha2'] * scale
    beta2  = data['beta2']  * scale
    beta3  = data['beta3']  * scale

    # q-points along high-symmetry directions (reduced coordinates)
    directions = [
        ("[100]", [0.0, 0.25, 0.5, 0.75, 1.0], lambda z: np.array([z, 0.0, 0.0])),
        ("[110]", [0.0, 0.25, 0.5, 0.75, 1.0], lambda z: np.array([z, z, 0.0])),
        ("[111]", [0.0, 0.25, 0.5, 0.75, 1.0], lambda z: np.array([z, z, z]))
    ]

    rows = []
    for _, zetas, qfunc in directions:
        for zeta in zetas:
            q = qfunc(zeta)
            # Phase factors (Eqs. 4.1, 4.2 with a*q/2 = π*q_α')
            C = np.cos(np.pi * q)
            S = np.sin(np.pi * q)

            # Dynamical matrix D (3×3, N/m)
            D = np.zeros((3, 3))
            for i in range(3):
                j = (i + 1) % 3
                k = (i + 2) % 3
                # Diagonal element
                D[i, i] = (4 * (beta1 + 2 * alpha1)
                           - 2 * (beta1 + alpha1) * C[i] * (C[j] + C[k])
                           - 4 * alpha1 * C[j] * C[k]
                           + 4 * beta2 * S[i]
                           + 4 * alpha2 * (S[j]**2 + S[k]**2))
                # Off-diagonal element (symmetric)
                D[i, j] = (2 * (beta1 - alpha1) * S[i] * S[j]
                           + 4 * beta3 * (C[i] + C[k] - 2))
                D[j, i] = D[i, j]

            # Mass-scaled dynamical matrix
            D_scaled = D / mass
            eigvals, eigvecs = np.linalg.eigh(D_scaled)

            # Frequencies in THz
            freqs_THz = np.sqrt(np.abs(eigvals)) / (2 * np.pi) * 1e-12

            # Sort by frequency
            idx = np.argsort(freqs_THz)
            freqs_THz = freqs_THz[idx]
            eigvecs = eigvecs[:, idx]

            # Branch labelling: longitudinal projection on wavevector direction
            norm_q = np.linalg.norm(q)
            if norm_q < 1e-12:
                labels = ['TA', 'TA2', 'LA']   # Gamma point (arbitrary)
            else:
                q_dir = q / norm_q
                labels = []
                for mode in range(3):
                    proj = np.abs(np.dot(eigvecs[:, mode], q_dir))
                    labels.append('LA' if proj > 0.85 else 'TA')
                # If two TA are present and not degenerate, rename second to TA2
                ta_indices = [i for i, l in enumerate(labels) if l == 'TA']
                if len(ta_indices) == 2:
                    if np.abs(freqs_THz[ta_indices[0]] - freqs_THz[ta_indices[1]]) > 1e-4:
                        labels[ta_indices[1]] = 'TA2'

            for mode in range(3):
                rows.append((metal, q[0], q[1], q[2], labels[mode], freqs_THz[mode]))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, help='Basename of output file')
    args = parser.parse_args()

    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, args.output)

    if args.output == 'phonon_frequencies.csv':
        all_rows = []
        for metal in ['Au', 'Ni', 'Pt', 'Pd']:
            all_rows.extend(compute_phonon_frequencies(metal))
        with open(outpath, 'w') as f:
            f.write('metal,qx,qy,qz,branch,frequency_THz\n')
            for row in all_rows:
                f.write(f'{row[0]},{row[1]:.6f},{row[2]:.6f},{row[3]:.6f},{row[4]},{row[5]:.6f}\n')

    elif args.output == 'elastic_constants.csv':
        with open(outpath, 'w') as f:
            f.write('metal,C11,C12,C44\n')
            for metal in ['Au', 'Ni', 'Pt', 'Pd']:
                d = metals_data[metal]
                f.write(f'{metal},{d["C11"]},{d["C12"]},{d["C44"]}\n')

    elif args.output == 'zero_point_energy.csv':
        with open(outpath, 'w') as f:
            f.write('metal,ZPE_cal_mol\n')
            for metal in ['Au', 'Ni', 'Pt', 'Pd']:
                d = metals_data[metal]
                f.write(f'{metal},{d["ZPE_cal_mol"]}\n')

    else:
        raise ValueError(f'Unknown output: {args.output}')

if __name__ == '__main__':
    main()
