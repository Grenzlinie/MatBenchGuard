import sys
import numpy as np

output_path = sys.argv[1]

# Parameters
Es = -17.239
Ep = -6.857

# Overlap parameters (eV) – first neighbour, second neighbour
params = {
    'ss_sigma':   [-0.648, -0.089],
    'sp_sigma':   [ 1.327,  0.133],
    'pp_sigma':   [ 2.282,  0.343],
    'pp_pi':      [-0.549,  0.052]
}

# Bond length
bond_len = 2.9  # angstrom (d)

# Geometries
geometries = [
    ('linear', 0.0, 0.0),
    ('helix125', 3.25, 0.1439),
    ('helix50', 3.25, 0.3375)
]

def compute_h(R, theta):
    """Compute h = sqrt(d^2 - 4 R^2 sin^2(theta/2))"""
    if R == 0.0 or theta == 0.0:
        return bond_len  # h = d when no helical twist
    import math
    return math.sqrt(bond_len**2 - 4 * R**2 * math.sin(theta/2)**2)

def distance_and_direction(n, R, theta, h):
    """Return (dist, l, m, n_dir) for bond from atom 0 to atom n."""
    # n = 1 or 2
    if n == 0:
        raise ValueError('n must be 1 or 2')
    cos_n = np.cos(n * theta)
    sin_n = np.sin(n * theta)
    dx = R * (cos_n - 1)
    dy = R * sin_n
    dz = n * h
    dist = np.sqrt(dx**2 + dy**2 + dz**2)
    if dist == 0:
        l = m = nd = 0.0
    else:
        l = dx / dist
        m = dy / dist
        nd = dz / dist
    return dist, l, m, nd

def slater_koster(l, m, n, V_ss_sigma, V_sp_sigma, V_pp_sigma, V_pp_pi):
    """Return E_{ss}, E_{sx}, E_{sy}, E_{sz}, E_{xx}, E_{xy}, E_{xz}, E_{yy}, E_{yz}, E_{zz}"""
    Ess = V_ss_sigma
    Esx = l * V_sp_sigma
    Esy = m * V_sp_sigma
    Esz = n * V_sp_sigma
    # p-p
    ll = l*l
    mm = m*m
    nn = n*n
    Exx = ll * V_pp_sigma + (1 - ll) * V_pp_pi
    Exy = l * m * (V_pp_sigma - V_pp_pi)
    Exz = l * n * (V_pp_sigma - V_pp_pi)
    Eyy = mm * V_pp_sigma + (1 - mm) * V_pp_pi
    Eyz = m * n * (V_pp_sigma - V_pp_pi)
    Ezz = nn * V_pp_sigma + (1 - nn) * V_pp_pi
    return Ess, Esx, Esy, Esz, Exx, Exy, Exz, Eyy, Eyz, Ezz

def build_hamiltonian(k, R, theta, h):
    """Build 4x4 Hamiltonian matrix for given k."""
    H = np.zeros((4, 4), dtype=complex)
    # Sum over n=1 and n=2
    for n in [1, 2]:
        dist, l, m, nd = distance_and_direction(n, R, theta, h)
        # neighbour index (0=first, 1=second)
        idx = 0 if n == 1 else 1
        V_ss_sigma = params['ss_sigma'][idx]
        V_sp_sigma = params['sp_sigma'][idx]
        V_pp_sigma = params['pp_sigma'][idx]
        V_pp_pi    = params['pp_pi'][idx]

        if n == 2:
            # scale second-neighbour parameters with distance: (2*d / dist)^2
            ref_dist = 2 * bond_len
            if dist != 0:
                scale = (ref_dist / dist)**2
                V_ss_sigma *= scale
                V_sp_sigma *= scale
                V_pp_sigma *= scale
                V_pp_pi    *= scale

        Ess, Esx, Esy, Esz, Exx, Exy, Exz, Eyy, Eyz, Ezz = slater_koster(
            l, m, nd, V_ss_sigma, V_sp_sigma, V_pp_sigma, V_pp_pi)

        cos_n = np.cos(n * theta)
        sin_n = np.sin(n * theta)
        cos2k = np.cos(2 * np.pi * k)
        sin2k = np.sin(2 * np.pi * k)

        # Contributions to matrix elements
        H[0, 0] += 2 * cos2k * (cos_n * Exx + sin_n * Exy)
        H[1, 1] += -2 * cos2k * (sin_n * Exy - cos_n * Eyy)
        H[2, 2] += 2 * cos2k * Ezz
        H[3, 3] += 2 * cos2k * Ess

        # off-diagonal
        H[0, 1] += -2j * sin2k * (sin_n * Exx - cos_n * Exy)
        H[0, 2] += -2j * sin2k * Exz
        H[0, 3] += -2 * cos2k * Esx
        H[1, 2] += 2 * cos2k * Eyz
        H[1, 3] += -2j * sin2k * Esy
        H[2, 3] += -2j * sin2k * Esz

    # Add on-site energies
    H[0, 0] += Ep
    H[1, 1] += Ep
    H[2, 2] += Ep
    H[3, 3] += Es

    # Hermitian: fill upper triangle
    H[1, 0] = np.conj(H[0, 1])
    H[2, 0] = np.conj(H[0, 2])
    H[3, 0] = np.conj(H[0, 3])
    H[2, 1] = np.conj(H[1, 2])
    H[3, 1] = np.conj(H[1, 3])
    H[3, 2] = np.conj(H[2, 3])
    return H

def compute_bands(R, theta, h, num_k=200):
    k_vals = np.linspace(-0.5, 0.5, num_k, endpoint=True)
    all_energies = []
    for k in k_vals:
        H = build_hamiltonian(k, R, theta, h)
        evals = np.linalg.eigvalsh(H)
        evals.sort()
        for b, E in enumerate(evals):
            all_energies.append((k, b, E))
    return all_energies

# Collect all data
rows = []
for geom_name, R, theta in geometries:
    h = compute_h(R, theta)
    energies = compute_bands(R, theta, h, num_k=200)
    for k, b, E in energies:
        rows.append((k, b, E, geom_name))

# Write CSV
with open(output_path, 'w') as f:
    f.write('k,band,E,geometry\n')
    for k, b, E, geom in rows:
        f.write(f'{k:.8f},{b},{E:.10f},{geom}\n')
