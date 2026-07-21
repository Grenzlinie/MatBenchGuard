import numpy as np
from scipy.integrate import quad
import csv

# ----------------------------------------------------------------------
# Material properties (GPa)
# PPF
E_PPF = 2.0
G_PPF = 0.77
# silicon
E_Si = 164.0
G_Si = 67.0

# Derived isotropic constants
nu_PPF = E_PPF / (2 * G_PPF) - 1.0
K_PPF = E_PPF / (3.0 * (1.0 - 2.0 * nu_PPF))
mu_PPF = G_PPF
lam_PPF = K_PPF - 2.0 / 3.0 * mu_PPF

nu_Si = E_Si / (2 * G_Si) - 1.0
K_Si = E_Si / (3.0 * (1.0 - 2.0 * nu_Si))
mu_Si = G_Si
lam_Si = K_Si - 2.0 / 3.0 * mu_Si

# ----------------------------------------------------------------------
# Voigt stiffness matrix for an isotropic material

def isotropic_C_voigt(lam, mu):
    C = np.zeros((6, 6))
    C[0, 0] = C[1, 1] = C[2, 2] = lam + 2.0 * mu
    C[0, 1] = C[1, 0] = C[0, 2] = C[2, 0] = C[1, 2] = C[2, 1] = lam
    C[3, 3] = C[4, 4] = C[5, 5] = mu
    return C

C_ppf = isotropic_C_voigt(lam_PPF, mu_PPF)
C_si = isotropic_C_voigt(lam_Si, mu_Si)

# ----------------------------------------------------------------------
# Eshelby tensor for an ellipsoid in an isotropic matrix (spheroid a1=a2)

def eshelby_voigt_spheroid(a, c, nu):
    """
    Return the Eshelby tensor in 6x6 Voigt notation (major symmetric)
    for a spheroid with a1 = a2 = a, a3 = c, Poisson ratio nu.
    """
    # I-integrals
    def _integrand_I1(s):
        return 1.0 / ((a**2 + s)**2 * np.sqrt(c**2 + s))
    def _integrand_I3(s):
        return 1.0 / ((c**2 + s) * (a**2 + s) * np.sqrt(c**2 + s))
    def _integrand_I11(s):
        return 1.0 / ((a**2 + s)**3 * np.sqrt(c**2 + s))
    def _integrand_I13(s):
        return 1.0 / ((a**2 + s)**2 * (c**2 + s) * np.sqrt(c**2 + s))
    def _integrand_I33(s):
        return 1.0 / ((c**2 + s)**2 * (a**2 + s) * np.sqrt(c**2 + s))

    const = 2.0 * np.pi * a**2 * c
    I1, _ = quad(_integrand_I1, 0.0, np.inf, limit=200)
    I3, _ = quad(_integrand_I3, 0.0, np.inf, limit=200)
    I11, _ = quad(_integrand_I11, 0.0, np.inf, limit=200)
    I13, _ = quad(_integrand_I13, 0.0, np.inf, limit=200)
    I33, _ = quad(_integrand_I33, 0.0, np.inf, limit=200)

    I1 *= const
    I3 *= const
    I11 *= const
    I13 *= const
    I33 *= const
    I12 = I11   # since a1 = a2

    pref = 1.0 / (8.0 * np.pi * (1.0 - nu))
    S1111 = pref * (a**2 * I11 + (1.0 - 2.0 * nu) * I1)
    S1122 = pref * (a**2 * I12 - (1.0 - 2.0 * nu) * I1)
    S1133 = pref * (c**2 * I13 - (1.0 - 2.0 * nu) * I1)
    S3311 = pref * (a**2 * I13 - (1.0 - 2.0 * nu) * I3)
    S3333 = pref * (c**2 * I33 + (1.0 - 2.0 * nu) * I3)

    pref_shear = 1.0 / (16.0 * np.pi * (1.0 - nu))
    S1212 = pref_shear * (0.5 * (a**2 + a**2) * I12 + (1.0 - 2.0 * nu) * I1)  # (I1+I2)/2 = I1
    S1313 = pref_shear * (0.5 * (a**2 + c**2) * I13 + (1.0 - 2.0 * nu) * (I1 + I3) / 2.0)

    # Build Voigt matrix (major symmetric, S13 component same as S31? We use S1133 for S13 and S23.
    S = np.zeros((6, 6))
    S[0, 0] = S[1, 1] = S1111
    S[2, 2] = S3333
    S[0, 1] = S[1, 0] = S1122
    S[0, 2] = S[1, 2] = S1133
    S[2, 0] = S[2, 1] = S3311  # assume major symmetry, but we'll use average for better isotropy later
    S[3, 3] = 2.0 * S1212
    S[4, 4] = S[5, 5] = 2.0 * S1313
    return S

# ----------------------------------------------------------------------
# Rotate a 6x6 stiffness tensor by a 3x3 rotation matrix (Bond transformation)

def rotate_voigt(C, R):
    """
    Rotate a 6x6 Voigt stiffness matrix C by rotation matrix R.
    Uses full fourth-rank transformation.
    """
    # Convert Voigt to 3x3x3x3
    idx = [(0,0), (1,1), (2,2), (1,2), (0,2), (0,1)]
    C_tensor = np.zeros((3,3,3,3))
    for a in range(6):
        i, j = idx[a]
        for b in range(6):
            k, l = idx[b]
            val = C[a, b]
            C_tensor[i,j,k,l] = val
            C_tensor[j,i,k,l] = val
            C_tensor[i,j,l,k] = val
            C_tensor[j,i,l,k] = val

    # Rotate
    C_rot = np.einsum('ip,jq,kr,ls->ijkl', R, R, R, R, C_tensor)

    # Convert back to Voigt
    C_new = np.zeros((6,6))
    for a in range(6):
        i, j = idx[a]
        for b in range(6):
            k, l = idx[b]
            C_new[a, b] = C_rot[i, j, k, l]
    return C_new

# ----------------------------------------------------------------------
# EPI effective stiffness for bi-phasic composite with random orientation

def epi_effective_biphase(C_m, C_f, alpha, a, c, nu_matrix, n_samples=3000):
    """
    Compute effective stiffness tensor (Voigt) via EPI for a
    bi-phasic composite with randomly oriented identical ellipsoidal
    inclusions (a1=a2=a, a3=c).
    """
    # Eshelby tensor for aligned inclusion (ref orientation, x3 = axis)
    S_ref = eshelby_voigt_spheroid(a, c, nu_matrix)
    I6 = np.eye(6)
    # Matrix inverse
    C_m_inv = np.linalg.inv(C_m)
    deltaC = C_f - C_m
    # Strain concentrator tensor for aligned inclusion
    T_ref = np.linalg.inv(I6 + (1.0 - alpha) * S_ref @ C_m_inv @ deltaC)
    # Quantity to be averaged: M = deltaC @ T_ref
    M_ref = deltaC @ T_ref

    # Monte Carlo orientational averaging
    np.random.seed(42)
    M_avg = np.zeros((6,6))
    for _ in range(n_samples):
        # random rotation matrix
        R = _random_rotation_matrix()
        M_rot = rotate_voigt(M_ref, R)
        M_avg += M_rot
    M_avg /= n_samples

    C_eff = C_m + alpha * M_avg
    return C_eff

def _random_rotation_matrix():
    # uniform random rotation
    R = np.random.randn(3,3)
    Q, _ = np.linalg.qr(R)
    if np.linalg.det(Q) < 0:
        Q[:, 0] = -Q[:, 0]
    return Q

# ----------------------------------------------------------------------
# Extract isotropic Young's and shear moduli from effective Voigt tensor

def isotropic_moduli(C_eff):
    # Assume isotropic, average over components
    C11 = (C_eff[0,0] + C_eff[1,1] + C_eff[2,2]) / 3.0
    C12 = (C_eff[0,1] + C_eff[1,2] + C_eff[0,2]) / 3.0
    G = (C11 - C12) / 2.0
    K = (C11 + 2.0 * C12) / 3.0
    E = 9.0 * K * G / (3.0 * K + G)
    return E, G

# ----------------------------------------------------------------------
# Three-phase composite: porous matrix + stiff particles

def epi_three_phase(alpha_p, alpha_s, k_pore, k_part, n_samples=3000):
    # Step 1: effective porous matrix
    C_f_pore = np.zeros((6,6))
    C_porous = epi_effective_biphase(C_ppf, C_f_pore, alpha_p, k_pore, k_pore, nu_PPF, n_samples)
    # Extract isotropic moduli of porous matrix (assumed isotropic)
    E_por, G_por = isotropic_moduli(C_porous)
    nu_por = E_por / (2.0 * G_por) - 1.0
    K_por = E_por / (3.0 * (1.0 - 2.0 * nu_por))
    lam_por = K_por - 2.0/3.0 * G_por
    C_por_iso = isotropic_C_voigt(lam_por, G_por)

    # Step 2: add stiff particles to porous matrix
    C_eff = epi_effective_biphase(C_por_iso, C_si, alpha_s, k_part, k_part, nu_por, n_samples)
    return C_eff

# ----------------------------------------------------------------------
# Generate all configurations and write CSV

def main():
    configs = []

    # (a) Porous PPF, spherical pores (k1=k2=1), porosities 0.1 to 0.7
    for ap in np.arange(0.1, 0.71, 0.1):
        ap = round(ap, 2)
        C_eff = epi_effective_biphase(C_ppf, np.zeros((6,6)), ap, 1.0, 1.0, nu_PPF)
        E, G = isotropic_moduli(C_eff)
        A = 0.0
        configs.append([f"porous_sphere_ap{int(ap*100):02d}", ap, 0.0, 1.0, 1.0, A, E, G])

    # (b) Dense PPF + spherical silicon particles, concentrations 0.00-0.20
    for as_ in [0.0, 0.05, 0.1, 0.15, 0.2]:
        if as_ == 0.0:
            # just pure PPF
            E, G = isotropic_moduli(C_ppf)
            configs.append(["dense_sphere_as000", 0.0, as_, 1.0, 1.0, 0.0, E, G])
        else:
            C_eff = epi_effective_biphase(C_ppf, C_si, as_, 1.0, 1.0, nu_PPF)
            E, G = isotropic_moduli(C_eff)
            configs.append([f"dense_sphere_as{int(as_*100):03d}", 0.0, as_, 1.0, 1.0, 0.0, E, G])

    # (c) Three-phase, spherical pores (α_p=0.6) + spherical particles
    for as_ in [0.0, 0.05, 0.1, 0.15, 0.2]:
        C_eff = epi_three_phase(0.6, as_, 1.0, 1.0)
        E, G = isotropic_moduli(C_eff)
        configs.append([f"three_sphere_ap060_as{int(as_*100):03d}", 0.6, as_, 1.0, 1.0, 0.0, E, G])

    # (d) Three-phase, spherical pores (α_p=0.6) + highly oblate particles (k1=k2=1000) at α_s=0.10
    C_eff = epi_three_phase(0.6, 0.1, 1.0, 1000.0)
    E, G = isotropic_moduli(C_eff)
    A = 3.0 * (2.0*1000.0 + 1.0) / (3.0) - 3.0  # simplified A formula
    configs.append(["three_oblate_ap060_as010", 0.6, 0.1, 1000.0, 1000.0, A, E, G])

    # (e) Shape-anisotropy sweeps for E_P/E_S and E_O/E_S checks
    #   Porous PPF with α_p = 0.6, shapes: prolate (k<1), oblate (k>1)
    for k in [0.1, 0.5, 1.0, 5.0, 100.0]:
        ap = 0.6
        C_eff = epi_effective_biphase(C_ppf, np.zeros((6,6)), ap, k, k, nu_PPF)
        E, G = isotropic_moduli(C_eff)
        A_calc = (1.0 + k + k)*(1.0 + 1.0/k + 1.0/k)/3.0 - 3.0
        configs.append([f"porous_shape_ap060_k{int(k*100):03d}", ap, 0.0, k, k, A_calc, E, G])
    #   Dense PPF with particles α_s=0.1, shapes
    for k in [0.1, 0.5, 1.0, 5.0, 100.0]:
        as_ = 0.1
        C_eff = epi_effective_biphase(C_ppf, C_si, as_, k, k, nu_PPF)
        E, G = isotropic_moduli(C_eff)
        A_calc = (1.0 + k + k)*(1.0 + 1.0/k + 1.0/k)/3.0 - 3.0
        configs.append([f"dense_shape_as010_k{int(k*100):03d}", 0.0, as_, k, k, A_calc, E, G])
    #   Three-phase with α_p=0.6, α_s=0.1, shapes
    for k in [0.1, 0.5, 1.0, 5.0, 100.0]:
        C_eff = epi_three_phase(0.6, 0.1, 1.0, k)
        E, G = isotropic_moduli(C_eff)
        A_calc = (1.0 + k + k)*(1.0 + 1.0/k + 1.0/k)/3.0 - 3.0
        configs.append([f"three_shape_ap060_as010_k{int(k*100):03d}", 0.6, 0.1, k, k, A_calc, E, G])

    # Write CSV
    with open('/app/outputs/epi_predictions.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['case_id', 'porosity_alpha_p', 'particle_alpha_s', 'k1', 'k2', 'A', 'E_GPa', 'G_GPa'])
        for row in configs:
            writer.writerow(row)
    print("epi_predictions.csv written")

if __name__ == "__main__":
    main()
