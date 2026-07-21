import numpy as np
from scipy.linalg import eig
import json
import sys

# Physical parameters (all in Kelvin unless noted)
S = 0.78
Jb = 120.0
Js = 70.0
# JI not used for a single film
Dpar = 0.6
Dperp = 0.0   # not used

# Lattice neighbour counts
n_parallel = 6
n_perp = 3
n_up = 3       # not used
n_planes = 8   # thickness

# Dipolar parameters (standard Co values)
# omega_M = gamma * mu0*M_s, approximated from typical Co data
omega_M = 2.37   # K
# Demagnetisation factor for in‑plane magnetisation
Nz = 1.0

# Derived constants
delta_dip = 0.25 * omega_M               # contribution to on‑site energy
A_dip0 = -0.5 * omega_M                  # dipolar part for anomalous term

def lambda_k(kx):
    """In‑plane structural factor for a hexagonal lattice, k_y = 0."""
    return 2.0 * (np.cos(kx) + 2.0 * np.cos(kx / 2.0))

# k‑point grid (at least 20 points)
k_vals = np.linspace(0.0, np.pi, 21)

all_results = []

for kx in k_vals:
    lk = lambda_k(kx)

    # On‑site (diagonal) and anomalous (pairing) matrices
    H11 = np.zeros((n_planes, n_planes))
    H12 = np.zeros((n_planes, n_planes))

    # Off‑diagonal hopping strength (uniform across the film)
    V = -2.0 * Jb * S * n_perp

    for i in range(n_planes):
        if i == 0 or i == n_planes - 1:
            # surface layers
            diag = (2.0 * S * (Js * (n_parallel - lk) + Jb * n_perp)
                    + 2.0 * S * Dpar
                    + delta_dip)
            H11[i, i] = diag
            H12[i, i] = 2.0 * S * Dpar + A_dip0   # anomalous coupling
        else:
            # interior (bulk) layers
            diag = (2.0 * S * Jb * ((n_parallel - lk) + 2.0 * n_perp)
                    + delta_dip)
            H11[i, i] = diag
            # no anomalous term for bulk planes

        if i < n_planes - 1:
            H11[i, i + 1] = V
            H11[i + 1, i] = V

    # Build the non‑Hermitian dynamic matrix from the bogoliubov Hamiltonian
    M = np.block([[H11, H12], [-H12, -H11]])

    # Eigenvalues of M come in +/- pairs; take the positive ones
    vals, _ = eig(M)
    vals = np.real(vals)
    # keep only positive and discard tiny numerical noise
    pos = vals[vals > 1e-4]

    # Exactly n positive branches expected
    if len(pos) != n_planes:
        # fallback: take the n smallest positive values
        pos_ordered = np.sort(vals)
        pos = pos_ordered[pos_ordered > 1e-4][:n_planes]

    pos_sorted = np.sort(pos)

    # Output each branch with index 1 (lowest energy) … n_planes
    for idx, energy in enumerate(pos_sorted, start=1):
        all_results.append({
            "k_x": round(float(kx), 10),
            "branch_index": idx,
            "energy": round(float(energy), 6)
        })

# Write JSON to stdout (the solve block redirects to the output file)
json.dump(all_results, sys.stdout, indent=2)
