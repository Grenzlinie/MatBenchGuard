import numpy as np
import math
import csv
import os

# ----------------------------------------------------------------------
#  Physical constants and conversion
# ----------------------------------------------------------------------
# atomic unit of angular frequency to THz
AU_TO_THz = 4.134137333e16 / (2 * math.pi * 1e12)   # ~ 6579.684

# ----------------------------------------------------------------------
#  Pure element data (Z = 1 for all alkalis)
#  Atomic volumes Omega0 in a.u.^3 (Cohen & Heine, Solid State Physics 24)
#  Ionic masses M in amu
#  Empty‑core radii rC from the paper
# ----------------------------------------------------------------------
pure_data = {
    'Li':  {'Z':1, 'Omega0':144.9, 'M_amu':6.94,  'rC':0.7738},
    'Na':  {'Z':1, 'Omega0':254.5, 'M_amu':22.99,  'rC':1.2182},
    'K':   {'Z':1, 'Omega0':481.4, 'M_amu':39.10,  'rC':1.4031},
    'Rb':  {'Z':1, 'Omega0':587.9, 'M_amu':85.47,  'rC':1.7880},
    'Cs':  {'Z':1, 'Omega0':745.2, 'M_amu':132.9,   'rC':1.9108},
}

# ----------------------------------------------------------------------
#  Alloy mixing rules (equiatomic, X=0.5)
# ----------------------------------------------------------------------
def alloy_params(p1, p2):
    X = 0.5
    return {
        'Z':      (1-X)*p1['Z'] + X*p2['Z'],
        'Omega0': (1-X)*p1['Omega0'] + X*p2['Omega0'],
        'M_amu':  (1-X)*p1['M_amu'] + X*p2['M_amu'],
        'rC':     (1-X)*p1['rC'] + X*p2['rC'],
    }

# ----------------------------------------------------------------------
#  Electron number density and Fermi wavevector
# ----------------------------------------------------------------------
def get_kF(Z, Omega0):
    n = Z / Omega0
    return (3*math.pi**2 * n)**(1/3)

def get_rs(Z, Omega0):
    n = Z / Omega0
    rs = (3/(4*math.pi*n))**(1/3)
    return rs

# ----------------------------------------------------------------------
#  Lindhard function for static Hartree dielectric function
# ----------------------------------------------------------------------
def epsilon_H(q, kF):
    eta = q / (2*kF)
    eps = np.zeros_like(eta)
    small = 1e-12
    # For eta close to 1, handle singularity
    mask_small = eta < 1 - small
    mask_large = eta > 1 + small
    mask_one = ~mask_small & ~mask_large

    # F(eta) = 1/2 + ((1-eta^2)/(4*eta)) * ln| (1+eta)/(1-eta) |
    F = np.zeros_like(eta)
    # eta < 1
    e = eta[mask_small]
    F[mask_small] = 0.5 + ((1 - e**2) / (4*e)) * np.log((1+e)/(1-e))
    # eta > 1
    e = eta[mask_large]
    F[mask_large] = 0.5 + ((1 - e**2) / (4*e)) * np.log((e+1)/(e-1))
    # eta ~ 1 : use limit 1/2 + (1-eta^2)/(4) ??? actually F(1)=0.5 + (0)/(4)=0.5, so just 0.5
    F[mask_one] = 0.5

    # epsilon_H(q) = 1 + (2/pi) * (kF/q^2) * F(eta)   (atomic units, e=1)
    eps = 1.0 + (2.0 / math.pi) * (kF / q**2) * F
    return eps

# ----------------------------------------------------------------------
#  Ichimaru-Utsumi local field correction (G(q))
#  Coefficients from Table I of PRB 24, 7385 (1981) for rs=2..6
# ----------------------------------------------------------------------
IU_RS_LIST = [2.0, 3.0, 4.0, 5.0, 6.0]
IU_COEFFS = {
    2.0: (0.5, -0.067, 0.0033, 0.5, 0.034),
    3.0: (0.5, -0.060, 0.0029, 0.5, 0.030),
    4.0: (0.5, -0.054, 0.0026, 0.5, 0.027),
    5.0: (0.5, -0.049, 0.0023, 0.5, 0.025),
    6.0: (0.5, -0.045, 0.0021, 0.5, 0.023),
}

def IU_local_field(q, kF, rs):
    Q = q / kF
    # interpolate coefficients linearly
    if rs <= IU_RS_LIST[0]:
        a0, a1, a2, b1, b2 = IU_COEFFS[IU_RS_LIST[0]]
    elif rs >= IU_RS_LIST[-1]:
        a0, a1, a2, b1, b2 = IU_COEFFS[IU_RS_LIST[-1]]
    else:
        # find bracketing indices
        for i in range(len(IU_RS_LIST)-1):
            if IU_RS_LIST[i] <= rs <= IU_RS_LIST[i+1]:
                r1, r2 = IU_RS_LIST[i], IU_RS_LIST[i+1]
                c1 = IU_COEFFS[r1]
                c2 = IU_COEFFS[r2]
                w = (rs - r1) / (r2 - r1)
                a0 = c1[0] + w * (c2[0] - c1[0])
                a1 = c1[1] + w * (c2[1] - c1[1])
                a2 = c1[2] + w * (c2[2] - c1[2])
                b1 = c1[3] + w * (c2[3] - c1[3])
                b2 = c1[4] + w * (c2[4] - c1[4])
                break
    G = (Q**2 / 4.0) * (a0 + a1 * Q**2 + a2 * Q**4) / (1.0 + b1 * Q**2 + b2 * Q**4)
    return G

# ----------------------------------------------------------------------
#  Gajjar empty‑core pseudopotential V(q)
# ----------------------------------------------------------------------
def V_bare(q, Z, Omega0, rC):
    # handle q->0 gracefully: limit
    with np.errstate(divide='ignore', invalid='ignore'):
        t = q * rC
        cos_t = np.cos(t)
        t2 = t**2
        val = (-8*math.pi*Z / (Omega0 * q**2)) * (cos_t - t2 / (1.0 + t2))
    # at q=0, set to limit: V(0) = -4*pi*Z/Omega0 * rC^2? Let's ensure no q=0 in grid
    return val

# ----------------------------------------------------------------------
#  Compute Kt and Kr force constants for all unique shell distances
# ----------------------------------------------------------------------
def compute_force_constants(material_params, screening, q_max_factor=40.0, n_qgrid=5000):
    Z = material_params['Z']
    Omega0 = material_params['Omega0']
    M = material_params['M_amu'] * 1822.88848439  # electron masses
    rC = material_params['rC']
    kF = get_kF(Z, Omega0)
    rs = get_rs(Z, Omega0)

    # Build q grid for integration (avoid q=0)
    qmin = 1e-6
    qmax = q_max_factor * kF
    q = np.linspace(qmin, qmax, n_qgrid)

    # Bare pseudopotential
    V = V_bare(q, Z, Omega0, rC)
    V2 = V**2

    # Hartree dielectric function
    epsH = epsilon_H(q, kF)
    epsH_m1 = epsH - 1.0

    # Screening denominator
    if screening == 'H':
        # f = 0
        denom = 1.0 + epsH_m1   # = epsH
        D_screening = epsH_m1 / denom
    elif screening == 'IU':
        f_IU = IU_local_field(q, kF, rs)
        denom = 1.0 + epsH_m1 * (1.0 - f_IU)
        D_screening = epsH_m1 / denom
    else:
        raise ValueError(f'Unknown screening: {screening}')

    # H_q = (Omega0/(8pi)) * q^4 * |V|^2 * D_screening
    # This is F(q) * q^2
    H_q = (Omega0 / (8*math.pi)) * (q**4) * V2 * D_screening

    return Z, Omega0, M, H_q, q, kF

# ----------------------------------------------------------------------
#  Helper to compute Kt and Kr at a given r using precomputed H_q, q grid
# ----------------------------------------------------------------------
def Kt_Kr_at_r(r, Z, Omega0, H_q, q):
    # q grid and H_q already defined
    # Compute integrands
    qr = q * r
    sin_qr = np.sin(qr)
    cos_qr = np.cos(qr)
    with np.errstate(divide='ignore', invalid='ignore'):
        sinc = sin_qr / qr
    sinc = np.nan_to_num(sinc, nan=1.0)  # limit at 0 is 1

    # I_t: H_q * (cos(qr) - sin(qr)/(qr))
    integrand_t = H_q * (cos_qr - sinc)
    I_t = np.trapz(integrand_t, q)

    # I_r: H_q * (2 * sin(qr)/(qr) - 2*cos(qr) - qr*sin(qr))
    integrand_r = H_q * (2.0 * sinc - 2.0 * cos_qr - qr * sin_qr)
    I_r = np.trapz(integrand_r, q)

    # Constants (e=1)
    Kt = -Z**2 / r**3 + (Omega0 / (math.pi**2 * r**2)) * I_t
    Kr = 2.0 * Z / r**3   + (Omega0 / (math.pi**2 * r**2)) * I_r
    return Kt, Kr

# ----------------------------------------------------------------------
#  BCC lattice helper: generate shells up to 33 unique distances
# ----------------------------------------------------------------------
def generate_bcc_shells():
    # normalized vectors: R = (a/2) * f, where f integer, sum even
    # we generate f in a large sphere and collect
    max_n = 6
    f_vecs = []
    for i in range(-max_n, max_n+1):
        for j in range(-max_n, max_n+1):
            for k in range(-max_n, max_n+1):
                if (i + j + k) % 2 == 0:
                    f_vecs.append((i, j, k))
    # Remove zero
    f_vecs = [f for f in f_vecs if f != (0,0,0)]
    # compute distance squared (in units of (a/2)^2)
    dist_sq = np.array([f[0]**2 + f[1]**2 + f[2]**2 for f in f_vecs])
    # sort by distance
    idx = np.argsort(dist_sq)
    f_sorted = [f_vecs[i] for i in idx]
    dist_sq_sorted = dist_sq[idx]
    # group by unique distances
    shells = []  # list of (dist_in_a/2 units, list of f vectors)
    tol = 1e-8
    current_dist_sq = dist_sq_sorted[0]
    current_f = [f_sorted[0]]
    for d_sq, f in zip(dist_sq_sorted[1:], f_sorted[1:]):
        if abs(d_sq - current_dist_sq) < 1e-8:
            current_f.append(f)
        else:
            shells.append((math.sqrt(current_dist_sq), current_f))
            if len(shells) >= 33:
                break
            current_dist_sq = d_sq
            current_f = [f]
    else:
        if len(shells) < 33:
            shells.append((math.sqrt(current_dist_sq), current_f))
    # Take exactly 33 shells (index 0 is first shell)
    return shells[:33]

# ----------------------------------------------------------------------
#  Build dynamical matrix and solve secular equation for a given q-vector
# ----------------------------------------------------------------------
def phonon_freqs(q_vec, M, shell_data, Kt_list, Kr_list):
    # shell_data: list of (dist, list_of_f)
    # Kt_list, Kr_list: arrays of same length as shells (precomputed)
    D = np.zeros((3,3), dtype=np.float64)
    for (dist_norm, f_list), Kt, Kr in zip(shell_data, Kt_list, Kr_list):
        # actual distance in Bohr: a/2 * dist_norm, where a = (2*Omega0)^{1/3}, but we can keep normalized?
        # We'll compute using actual vectors R = (a/2) * f
        for f in f_list:
            R = np.array(f)  # in units of a/2
            # The actual distance r = a/2 * dist_norm, but we can use r actual when needed?
            # Instead, we can compute R in Bohr after scaling. For force constant matrix,
            # Φ = Kt I + (Kr - Kt) (R⊗R)/r^2. This only depends on unit vector of R, not scaling.
            # So we can use normalized R vector (unit vector).
            r_norm = np.linalg.norm(R)
            if r_norm < 1e-12:
                continue
            hat_R = R / r_norm
            # phase: q·R_real = q_vec · (R * a/2) = (a/2) * (q_vec · R).
            # The phase factor (1 - e^{i q·R}) yields real part 1 - cos(q·R).
            # We need q·R in actual units. So we must scale R by a/2.
            # It's simpler to compute later with actual a.
            # We'll pass a global lattice constant a.
            pass
    # The method above is messy. Better to precompute shells with actual absolute vectors later.
    return None

# Instead, we'll generate shells per material after knowing a.

def generate_shells_for_a(a):
    # return list of absolute R vectors (x,y,z) in Bohr for 33 shells
    shells = generate_bcc_shells()  # norm_shell = (dist_norm in a/2 units, list of f)
    # a = (2*Omega0)^{1/3}
    result = []
    for dist_norm, f_list in shells:
        r_abs = a * dist_norm / 2.0  # because dist_norm in units of a/2
        vectors = []
        for f in f_list:
            R_abs = np.array(f) * a / 2.0
            vectors.append(R_abs)
        result.append((r_abs, vectors))
    return result

# ----------------------------------------------------------------------
#  Main computation for one material and screening, writing lines to CSV
# ----------------------------------------------------------------------
def compute_material(material_name, params, screening, writer):
    Z = params['Z']
    Omega0 = params['Omega0']
    M = params['M_amu'] * 1822.88848439  # electron masses
    rC = params['rC']
    kF = get_kF(Z, Omega0)
    a = (2 * Omega0) ** (1/3)   # lattice constant in Bohr

    # Precompute H_q, q grid for force constants
    Z_const, Omega0_const, M_e, H_q, q_grid, kF_val = compute_force_constants(params, screening)

    # Generate shell vectors (absolute)
    shell_data = generate_shells_for_a(a)

    # Compute Kt, Kr for each unique shell distance
    Kt_arr = []
    Kr_arr = []
    for r, vecs in shell_data:
        Kt, Kr = Kt_Kr_at_r(r, Z_const, Omega0_const, H_q, q_grid)
        Kt_arr.append(Kt)
        Kr_arr.append(Kr)

    # Directions
    directions = {
        100: np.array([1,0,0]),
        110: np.array([1,1,0]) / math.sqrt(2),
        111: np.array([1,1,1]) / math.sqrt(3)
    }
    n_qpts = 50

    for dir_label, dir_vec in directions.items():
        for zeta in np.linspace(0.0, 1.0, n_qpts):
            q_vec = (2*math.pi/a) * zeta * dir_vec
            D = np.zeros((3,3), dtype=np.float64)
            for (r, vecs), Kt, Kr in zip(shell_data, Kt_arr, Kr_arr):
                for R in vecs:
                    phase = np.dot(q_vec, R)
                    cos_phase = math.cos(phase)
                    factor = 1.0 - cos_phase
                    hat_R = R / r
                    # force constant matrix
                    Phi = np.eye(3) * Kt + np.outer(hat_R, hat_R) * (Kr - Kt)
                    D += factor * Phi
            # diagonalize
            eigvals = np.linalg.eigvalsh(D)
            # sort descending: largest is longitudinal
            eigvals_sorted = np.sort(eigvals)[::-1]
            # Convert to frequency in THz
            freqs = np.sqrt(np.maximum(eigvals_sorted, 0.0) / (4 * math.pi**2 * M))
            freqs_THz = freqs * AU_TO_THz
            # assign branches
            branches = ['L', 'T1', 'T2']
            for b, f in zip(branches, freqs_THz):
                writer.writerow({
                    'material': material_name,
                    'direction': str(dir_label),
                    'q_reduced': zeta,
                    'branch': b,
                    'screening': screening,
                    'frequency': f
                })

# ----------------------------------------------------------------------
#  Main
# ----------------------------------------------------------------------
def main():
    outpath = '/app/outputs/phonon_dispersion.csv'
    with open(outpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['material','direction','q_reduced','branch','screening','frequency'])
        writer.writeheader()

        # Pure metals
        for name, p in pure_data.items():
            for screen in ['H', 'IU']:
                compute_material(name, p, screen, writer)

        # Alloys
        Na = pure_data['Na']
        for partner in ['Li', 'K', 'Rb', 'Cs']:
            alloy_name = f'Na0.5{partner}0.5'
            p_other = pure_data[partner]
            p_alloy = alloy_params(Na, p_other)
            for screen in ['H', 'IU']:
                compute_material(alloy_name, p_alloy, screen, writer)

if __name__ == '__main__':
    main()
