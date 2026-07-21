import sys
import numpy as np

# ---------------------------- paper constants and functions ----------------------------

def _safe_log(x):
    return np.log(max(x, 1e-12))

def G_theta(cos_theta):
    # Eq. (2) of the paper: G(θ) = -1/(4π) * ( 1/2 + 4/3 cosθ + cosθ * ln[ sin^2(θ/2) ] )
    # Note: sin^2(θ/2) = (1 - cosθ) / 2
    sin2 = (1 - cos_theta) / 2.0
    # prevent log of extremely small numbers
    sin2 = max(sin2, 1e-12)
    return -(1.0 / (4 * np.pi)) * (0.5 + (4.0 / 3.0) * cos_theta + cos_theta * np.log(sin2))

def fcc_lattice_constant(phi, R_o=1.0):
    # φ = (4 * (4/3)π R_o^3) / a^3
    a = ( (16.0 * np.pi) / (3.0 * phi) ) ** (1.0/3.0) * R_o
    return a

def fcc_undeformed_neighbors(a, R_o=1.0):
    # returns list of 12 neighbor vectors (relative to a central atom)
    # neighbor separations are a/2 * (±1, ±1, 0) etc.
    half = a / 2.0
    vectors = []
    for i in (-1, 1):
        for j in (-1, 1):
            vectors.append(np.array([i, j, 0]) * half)
            vectors.append(np.array([i, 0, j]) * half)
            vectors.append(np.array([0, i, j]) * half)
    # unique list
    # the above gives each vector twice? Actually the set of 12 distinct directions is correct if we use permutations.
    # A simpler way: generate all 12 directions using permutations of (±1,±1,0).
    # We'll generate the 4! / 2! / 2! = 6 permutations of (±1,±1,0) with signs, which yields 12 distinct vectors (including sign flips).
    # Better: explicit list
    dirs = [
        (1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0),
        (1,0,1), (1,0,-1), (-1,0,1), (-1,0,-1),
        (0,1,1), (0,1,-1), (0,-1,1), (0,-1,-1)
    ]
    return [np.array(d, dtype=float) * half for d in dirs]

def compute_delta_R(r_ij, R_o=1.0):
    # contact displacement: δR_i = |r_ij|/2 - R_o
    return np.linalg.norm(r_ij) / 2.0 - R_o

def manybody_forces(r_ij_list, R_o=1.0, max_iter=50, tol=1e-8):
    n = len(r_ij_list)
    # compute unit vectors and δR
    omega = []
    delta_R = np.zeros(n)
    for i, r in enumerate(r_ij_list):
        d = np.linalg.norm(r)
        omega.append(r / d)
        delta_R[i] = d / 2.0 - R_o
    
    # precompute all G_ij for i ≠ j
    G_mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                cos_theta = np.dot(omega[i], omega[j])
                # clamp to avoid numerical issues
                cos_theta = max(-1.0, min(1.0, cos_theta))
                G_mat[i, j] = G_theta(cos_theta)
    
    # initial guess: small positive forces
    f = np.ones(n) * 0.1
    for iteration in range(max_iter):
        # assemble matrix M: M[i,i] = A_i, M[i,j] = -G_ij
        M = np.zeros((n, n))
        for i in range(n):
            f_i = max(f[i], 1e-12)  # ensure positive for log
            A_i = (1.0 / (24 * np.pi)) * (5.0 + 6.0 * np.log(f_i / (8 * np.pi)))
            M[i, i] = A_i
            for j in range(n):
                if i != j:
                    M[i, j] = -G_mat[i, j]
        # solve linear system
        try:
            new_f = np.linalg.solve(M, delta_R)
        except np.linalg.LinAlgError:
            # fallback: use pseudo-inverse
            new_f = np.dot(np.linalg.pinv(M), delta_R)
        change = np.max(np.abs(new_f - f))
        f = new_f
        if change < tol:
            break
    # return final forces (we do not allow negative forces; clamp to zero if negative)
    f = np.maximum(f, 0.0)
    return f

def compute_stress_from_one_atom(r_ij_list, forces, volume_per_atom):
    # stress tensor = (1 / (2 * V)) * sum_i f_i * n_i ⊗ r_ij
    # but for a crystal with N_atoms equivalent atoms, we can sum over one atom and multiply by N_atoms.
    # For fcc with 4 atoms per conventional cell, N_atoms=4.
    # Actually we are in a unit cell of volume V_cell.
    # We'll use the formula: sigma = (N_atoms / (2 * V_cell)) * sum_i f_i * n_i ⊗ r_ij
    sigma = np.zeros((3,3))
    for r, f in zip(r_ij_list, forces):
        if f <= 0:
            continue
        norm = np.linalg.norm(r)
        n_vec = r / norm
        sigma += f * np.outer(n_vec, r)
    return sigma

def isotropic_pressure_csv(filepath):
    phis = np.linspace(0.79, 0.85, 7)  # includes 0.79,0.81,0.83,0.85
    R_o = 1.0
    N_atoms_cell = 4.0
    with open(filepath, 'w') as f:
        f.write('phi,pressure\n')
        for phi in phis:
            a = fcc_lattice_constant(phi, R_o)
            V_cell = a**3
            r_ij_list = fcc_undeformed_neighbors(a, R_o)
            forces = manybody_forces(r_ij_list, R_o)
            sigma = compute_stress_from_one_atom(r_ij_list, forces, V_cell)
            # confinement pressure Π = - (1/3) Tr(σ) * (R_o / γ) but in our dimensionless units it's just -Tr/3
            pressure = -np.trace(sigma) * (N_atoms_cell / (2.0 * V_cell))
            f.write(f'{phi:.6f},{pressure:.8f}\n')

def uniaxial_stress_csv(filepath):
    phi0 = 0.8
    R_o = 1.0
    a = fcc_lattice_constant(phi0, R_o)
    V_cell = a**3
    # undeformed neighbors
    r0_list = fcc_undeformed_neighbors(a, R_o)
    N_atoms_cell = 4.0
    lam_vals = np.linspace(1.0, 1.15, 31)  # λ from 1 to 1.15, step 0.005
    with open(filepath, 'w') as f:
        f.write('extension_ratio_minus_one,normal_stress_difference\n')
        for lam in lam_vals:
            F = np.diag([lam**(-0.5), lam**(-0.5), lam])
            # apply deformation to neighbor vectors
            r_ij_list = [F @ r0 for r0 in r0_list]
            forces = manybody_forces(r_ij_list, R_o)
            sigma = compute_stress_from_one_atom(r_ij_list, forces, V_cell) * (N_atoms_cell / (2.0 * V_cell))
            ndiff = sigma[2,2] - sigma[0,0]  # σ33 - σ11
            f.write(f'{lam-1:.6f},{ndiff:.8f}\n')

def shear_stress_csv(filepath):
    phi0 = 0.8
    R_o = 1.0
    a = fcc_lattice_constant(phi0, R_o)
    V_cell = a**3
    r0_list = fcc_undeformed_neighbors(a, R_o)
    N_atoms_cell = 4.0
    strains = np.linspace(0.0, 0.2, 41)
    with open(filepath, 'w') as f:
        f.write('shear_strain,shear_stress\n')
        for gamma in strains:
            F = np.array([[1, 0, 0], [0, 1, 0], [gamma, 0, 1]])
            r_ij_list = [F @ r0 for r0 in r0_list]
            forces = manybody_forces(r_ij_list, R_o)
            sigma = compute_stress_from_one_atom(r_ij_list, forces, V_cell) * (N_atoms_cell / (2.0 * V_cell))
            shear = sigma[0,2]  # σ13
            f.write(f'{gamma:.6f},{shear:.8f}\n')

def main():
    if len(sys.argv) != 3:
        print('Usage: compute.py <mode> <output_path>')
        sys.exit(1)
    mode = sys.argv[1]
    outpath = sys.argv[2]
    if mode == 'isotropic':
        isotropic_pressure_csv(outpath)
    elif mode == 'uniaxial':
        uniaxial_stress_csv(outpath)
    elif mode == 'shear':
        shear_stress_csv(outpath)
    else:
        print('Unknown mode')
        sys.exit(1)

if __name__ == '__main__':
    main()