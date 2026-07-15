#!/usr/bin/env python3
"""Compute phonon frequencies for A3C60 from force-constant matrices."""
import sys
import csv
import numpy as np

# ----------------------------------------------------------------------
# 1. primitive cell geometry (a=1)
# ----------------------------------------------------------------------
a1 = np.array([0.0, 0.5, 0.5])
a2 = np.array([0.5, 0.0, 0.5])
a3 = np.array([0.5, 0.5, 0.0])

# basis ions (fractional coordinates in primitive lattice vectors)
# ion 1: tetrahedral  (1/4,1/4,1/4)  in conventional -> primitive (0.25,0.25,0.25)
# ion 2: tetrahedral  (3/4,1/4,1/4)  -> primitive (-0.25,0.75,0.75)
# ion 3: octahedral   (1/2,1/2,1/2)  -> primitive (0.5,0.5,0.5)
# ion 4: C60 molecule (0,0,0)         -> primitive (0,0,0)
frac_pos = np.array([
    [0.25, 0.25, 0.25],   # ion 1
    [-0.25, 0.75, 0.75],  # ion 2
    [0.5,  0.5,  0.5],    # ion 3
    [0.0,  0.0,  0.0],    # ion 4
])  # (4, 3)

# degrees of freedom per atom: translations, and libration for C60
# atoms 0,1,2 (A) have 3 DOF; atom 3 (C60) has 6 DOF: 3 trans, 3 libr
dof_per_atom = [3, 3, 3, 6]
dof_offsets = np.cumsum([0] + dof_per_atom)  # [0, 3, 6, 9, 15]

# mass matrix is identity (mA=1, M=1, I0=1)
# so D(q) = D0(q)

# ----------------------------------------------------------------------
# 2. force-constant parameters (scaled, mA=M=I0=1)
# ----------------------------------------------------------------------
params = {
    "alpha1": 1.0, "beta1": 0.2, "gamma1": 0.15, "delta1": 0.1,
    "alpha2": 1.2, "beta2": 1.1,
    "alpha3": 0.6, "beta3": 0.5,
    "alpha4": 0.4, "beta4": 0.05,
    "alpha": 0.15, "beta": 0.02, "gamma": 0.11,
    "a": 0.09, "b": 0.01, "c": 0.06,
    "p": 0.03, "q": 0.01
}

# ----------------------------------------------------------------------
# 3. reference force-constant matrices
# ----------------------------------------------------------------------
# Phi(12): tetra-tetra, bond along (1,0,0)
Phi12_ref = -np.array([
    [params["alpha1"], 0.0, 0.0],
    [0.0, params["beta1"], params["delta1"]],
    [0.0, params["delta1"], params["gamma1"]]
])

# Phi(13): tetra-octa, isotropic
Phi13_ref = -np.array([
    [params["alpha2"], params["beta2"], params["beta2"]],
    [params["beta2"], params["alpha2"], params["beta2"]],
    [params["beta2"], params["beta2"], params["alpha2"]]
])

# Phi(14): tetra-C60 (translation block only), isotropic
Phi14_tt = -np.array([
    [params["alpha3"], params["beta3"], params["beta3"]],
    [params["beta3"], params["alpha3"], params["beta3"]],
    [params["beta3"], params["beta3"], params["alpha3"]]
])

# Phi(34): octa-C60 (translation block), bond along y-axis (ref)
Phi34_tt = -np.array([
    [params["beta4"], 0.0, 0.0],
    [0.0, params["alpha4"], 0.0],
    [0.0, 0.0, params["beta4"]]
])  # note: alpha4 along the bond direction (y), beta4 perpendicular

# Phi(44): C60-C60 (6x6), bond direction (1,1,0)/(sqrt2)
Phi44 = -np.array([
    [params["alpha"], params["gamma"], 0.0, 0.0, 0.0, params["p"]],
    [params["gamma"], params["alpha"], 0.0, 0.0, 0.0, params["p"]],
    [0.0, 0.0, params["beta"], params["q"], params["q"], 0.0],
    [0.0, 0.0, params["q"], params["a"], params["c"], 0.0],
    [0.0, 0.0, params["q"], params["c"], params["a"], 0.0],
    [params["p"], params["p"], 0.0, 0.0, 0.0, params["b"]]
])

# ----------------------------------------------------------------------
# 4. Helper: rotation matrix from vector a to vector b
# ----------------------------------------------------------------------
def rot_matrix(a, b):
    """Return rotation matrix R such that R @ a = b."""
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    v = np.cross(a, b)
    s = np.linalg.norm(v)
    c = np.dot(a, b)
    if s < 1e-9:
        return np.eye(3) if c > 0 else -np.eye(3)
    k = np.array([[0, -v[2], v[1]],
                  [v[2], 0, -v[0]],
                  [-v[1], v[0], 0]])
    return np.eye(3) + k + k @ k * ((1 - c) / (s**2))

def cart_from_frac(f):
    """f: (3,) fractional in primitive basis -> Cartesian."""
    return f[0]*a1 + f[1]*a2 + f[2]*a3

# ----------------------------------------------------------------------
# 5. Neighbour enumeration
# ----------------------------------------------------------------------
# We'll collect all pairs (i, j, R) within a cutoff (in units of lattice constant a=1)
cutoff = 1.2  # includes 2nd neighbours of A and 3rd of C60

# max cell index range
max_n = 2

neighbour_pairs = []

for i in range(4):
    for j in range(4):
        for ni in range(-max_n, max_n+1):
            for nj in range(-max_n, max_n+1):
                for nk in range(-max_n, max_n+1):
                    R = np.array([ni, nj, nk])
                    # relative vector in primitive fractional coords
                    diff_frac = frac_pos[j] - frac_pos[i] + R
                    diff_cart = cart_from_frac(diff_frac)
                    dist = np.linalg.norm(diff_cart)
                    if dist == 0.0:
                        continue
                    if dist > cutoff:
                        continue
                    neighbour_pairs.append((i, j, ni, nj, nk, diff_cart, dist))

# ----------------------------------------------------------------------
# 6. Assign force-constant submatrices
# ----------------------------------------------------------------------
def get_submat(i, j, diff_cart):
    """Return np.array of shape (dof_i, dof_j) for the given pair."""
    if i < 3 and j < 3:
        # A-A
        # types of A: ion0=tetra1, ion1=tetra2, ion2=octa
        if (i == 0 or i == 1) and (j == 0 or j == 1):
            # tetra-tetra => use Phi12 rotated
            # find rotation mapping (1,0,0) to bond direction
            bond_dir = diff_cart / np.linalg.norm(diff_cart)
            R = rot_matrix(np.array([1.0,0,0]), bond_dir)
            Phi = R @ Phi12_ref @ R.T
            return Phi
        elif (i == 0 or i == 1) and j == 2:  # tetra-octa
            return Phi13_ref
        elif i == 2 and (j == 0 or j == 1):  # octa-tetra
            return Phi13_ref.T
        elif i == 2 and j == 2:  # octa-octa: no interaction given, assume zero
            return np.zeros((3,3))
        else:
            return np.zeros((3,3))
    elif i < 3 and j == 3:
        # A - C60: translation block 3x6, libration block zero
        tt = np.zeros((3,6))
        if i == 2:  # octa-C60
            # use Phi34 rotated
            bond_dir = diff_cart / np.linalg.norm(diff_cart)
            # ref matrix has alpha4 along bond direction (y), beta4 perpendicular
            # we can build directly: alpha4 * (v v^T) + beta4 * (I - v v^T)
            phi = params["beta4"] * np.eye(3) + (params["alpha4"] - params["beta4"]) * np.outer(bond_dir, bond_dir)
            tt[0:3, 0:3] = phi
            return tt
        else:  # tetra-C60
            # Phi14 isotropic
            tt[0:3, 0:3] = Phi14_tt
            return tt
    elif i == 3 and j < 3:
        # C60 - A: 6x3 block, transpose of A-C60 with swapped i,j; we use same matrix as A-C60 but transposed
        return get_submat(j, i, -diff_cart).T
    elif i == 3 and j == 3:
        # C60-C60: full 6x6
        bond_dir = diff_cart / np.linalg.norm(diff_cart)
        # reference bond direction for Phi44 is (1,1,0)/sqrt2
        ref_dir = np.array([1.0, 1.0, 0.0]) / np.sqrt(2.0)
        # find rotation R that maps ref_dir -> bond_dir
        R = rot_matrix(ref_dir, bond_dir)
        # check if determinant is -1? we'll use proper rotation always, but symmetry includes mirrors; for simplicity assume proper.
        # P = diag(R, R) because det(R)=1 for a rotation
        P = np.block([[R, np.zeros((3,3))],
                      [np.zeros((3,3)), R]])
        Phi = P @ Phi44 @ P.T
        return Phi
    else:
        return np.zeros((dof_per_atom[i], dof_per_atom[j]))

neighbours = []
for (i, j, ni, nj, nk, diff_cart, dist) in neighbour_pairs:
    sub = get_submat(i, j, diff_cart)
    neighbours.append((i, j, np.array([ni, nj, nk]), sub))

# ----------------------------------------------------------------------
# 7. Build D0(q) and diagonalize
# ----------------------------------------------------------------------
def build_D0(q):
    """q: (3,) reduced wavevector in reciprocal primitive basis."""
    D0 = np.zeros((15,15), dtype=complex)
    for (i, j, R, sub) in neighbours:
        phase = np.exp(2j * np.pi * np.dot(q, R))
        i0 = dof_offsets[i]
        i1 = i0 + dof_per_atom[i]
        j0 = dof_offsets[j]
        j1 = j0 + dof_per_atom[j]
        D0[i0:i1, j0:j1] += sub * phase
    # also add onsite term: - sum over neighbours? Actually, the force-constant matrix for i=j should ensure translational invariance.
    # For a consistent dynamical matrix, the onsite block for atom i should be negative sum of all off-diagonal blocks.
    for i in range(4):
        i0 = dof_offsets[i]
        i1 = i0 + dof_per_atom[i]
        diag_block = np.zeros((dof_per_atom[i], dof_per_atom[i]), dtype=complex)
        for (i2, j2, R2, sub2) in neighbours:
            if i2 == i:
                # contribute to sum of all interactions involving i with any j
                diag_block -= sub2  # subtract because Phi_ii = - sum_{j != i} Phi_{ij}
            if j2 == i:
                diag_block -= sub2.T
        D0[i0:i1, i0:i1] += diag_block
    return D0

def frequencies_at_q(q):
    D0 = build_D0(q)
    # D = D0 (since m^cryst = I)
    evals = np.linalg.eigvalsh(D0)  # D0 should be Hermitian
    evals = np.maximum(evals, 0.0)
    omega = np.sqrt(evals)
    omega.sort()
    return omega

# ----------------------------------------------------------------------
# 8. Main: compute for all q-points and write CSV
# ----------------------------------------------------------------------
def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "/app/outputs"
    csv_path = f"{outdir}/phonon_frequencies.csv"

    directions = {
        "Delta": np.array([1.0, 0.0, 0.0]),
        "Sigma": np.array([1.0, 1.0, 0.0]),
        "Lambda": np.array([1.0, 1.0, 1.0])
    }
    x_vals = np.linspace(0.0, 1.0, 21)

    rows = []
    for dir_name, vec in directions.items():
        for x in x_vals:
            q_red = x * vec
            freqs = frequencies_at_q(q_red)
            for branch, f in enumerate(freqs):
                rows.append([dir_name, x, branch, f])

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["direction", "q_red", "branch", "frequency"])
        writer.writerows(rows)

if __name__ == "__main__":
    main()
