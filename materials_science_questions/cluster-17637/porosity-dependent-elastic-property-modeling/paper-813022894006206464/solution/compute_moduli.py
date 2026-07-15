import numpy as np
from scipy.integrate import quad
from scipy.stats import norm
import csv

# Material properties (stainless steel)
E_host = 193.0       # GPa
nu_host = 0.27

# Pore size distribution parameters (radii in meters)
r_min = 10e-6
r_max = 100e-6
n_classes = 5
mu = 55e-6
sigma = 31.8e-6
delta_r = (r_max - r_min) / (n_classes - 1)
radii = np.array([r_min + i * delta_r for i in range(n_classes)])

# Relative frequencies from normal distribution
pdf_vals = norm.pdf(radii, loc=mu, scale=sigma)
p = pdf_vals / pdf_vals.sum()

# Host stiffness in Voigt (isotropic)
mu_host = E_host / (2.0 * (1.0 + nu_host))
lam_host = E_host * nu_host / ((1.0 + nu_host) * (1.0 - 2.0 * nu_host))

def voigt_stiffness_iso(lam, mu):
    C = np.zeros((6, 6))
    C[0, 0] = C[1, 1] = C[2, 2] = lam + 2.0 * mu
    C[0, 1] = C[0, 2] = C[1, 0] = C[1, 2] = C[2, 0] = C[2, 1] = lam
    C[3, 3] = C[4, 4] = C[5, 5] = mu
    return C

C_host = voigt_stiffness_iso(lam_host, mu_host)

def Eshelby_sphere(nu):
    S = np.zeros((6, 6))
    a = (7.0 - 5.0 * nu) / (15.0 * (1.0 - nu))
    b = (5.0 * nu - 1.0) / (15.0 * (1.0 - nu))
    c = (4.0 - 5.0 * nu) / (15.0 * (1.0 - nu))
    S[0, 0] = S[1, 1] = S[2, 2] = a
    S[0, 1] = S[0, 2] = S[1, 0] = S[1, 2] = S[2, 0] = S[2, 1] = b
    S[3, 3] = S[4, 4] = S[5, 5] = c
    return S

def Eshelby_spheroid_from_ar(ar, nu):
    """Eshelby tensor for a prolate spheroid (a=b=1, c=ar) in isotropic matrix."""
    if abs(ar - 1.0) < 1e-12:
        return Eshelby_sphere(nu)
    a = 1.0
    c = ar
    def integrand_J1(t, ai_sq, aj_sq, ak_sq):
        return 1.0 / ( (ai_sq + t) * np.sqrt((ai_sq + t) * (aj_sq + t) * (ak_sq + t)) )
    def integrand_J11(t, ai_sq, aj_sq, ak_sq):
        return 1.0 / ( (ai_sq + t)**2 * np.sqrt((ai_sq + t) * (aj_sq + t) * (ak_sq + t)) )
    def integrand_J12(t, ai_sq, aj_sq, ak_sq):
        return 1.0 / ( (ai_sq + t) * (aj_sq + t) * np.sqrt((ai_sq + t) * (aj_sq + t) * (ak_sq + t)) )

    # semi-axes squared
    a1_sq = a**2
    a2_sq = a**2
    a3_sq = c**2
    # factor = a1*a2*a3 = a*a*c = c
    factor = c
    limit = 200
    J1, _ = quad(lambda t: integrand_J1(t, a1_sq, a2_sq, a3_sq), 0, np.inf, limit=limit)
    J2, _ = quad(lambda t: integrand_J1(t, a2_sq, a1_sq, a3_sq), 0, np.inf, limit=limit)
    J3, _ = quad(lambda t: integrand_J1(t, a3_sq, a1_sq, a2_sq), 0, np.inf, limit=limit)
    J11, _ = quad(lambda t: integrand_J11(t, a1_sq, a2_sq, a3_sq), 0, np.inf, limit=limit)
    J22, _ = quad(lambda t: integrand_J11(t, a2_sq, a1_sq, a3_sq), 0, np.inf, limit=limit)
    J33, _ = quad(lambda t: integrand_J11(t, a3_sq, a1_sq, a2_sq), 0, np.inf, limit=limit)
    J12, _ = quad(lambda t: integrand_J12(t, a1_sq, a2_sq, a3_sq), 0, np.inf, limit=limit)
    J13, _ = quad(lambda t: integrand_J12(t, a1_sq, a3_sq, a2_sq), 0, np.inf, limit=limit)
    J23, _ = quad(lambda t: integrand_J12(t, a2_sq, a3_sq, a1_sq), 0, np.inf, limit=limit)
    J1 *= factor
    J2 *= factor
    J3 *= factor
    J11 *= factor
    J22 *= factor
    J33 *= factor
    J12 *= factor
    J13 *= factor
    J23 *= factor

    D = 1.0 - nu
    S = np.zeros((6, 6))
    S[0, 0] = (3.0 * a1_sq * J11 + (1.0 - 2.0 * nu) * J1) / (8.0 * np.pi * D)
    S[1, 1] = (3.0 * a2_sq * J22 + (1.0 - 2.0 * nu) * J2) / (8.0 * np.pi * D)
    S[2, 2] = (3.0 * a3_sq * J33 + (1.0 - 2.0 * nu) * J3) / (8.0 * np.pi * D)
    S[0, 1] = (a2_sq * J12 - (1.0 - 2.0 * nu) * J1) / (8.0 * np.pi * D)
    S[0, 2] = (a3_sq * J13 - (1.0 - 2.0 * nu) * J1) / (8.0 * np.pi * D)
    S[1, 0] = (a1_sq * J12 - (1.0 - 2.0 * nu) * J2) / (8.0 * np.pi * D)
    S[1, 2] = (a3_sq * J23 - (1.0 - 2.0 * nu) * J2) / (8.0 * np.pi * D)
    S[2, 0] = (a1_sq * J13 - (1.0 - 2.0 * nu) * J3) / (8.0 * np.pi * D)
    S[2, 1] = (a2_sq * J23 - (1.0 - 2.0 * nu) * J3) / (8.0 * np.pi * D)
    S[3, 3] = ((a1_sq + a2_sq) * J12 + (1.0 - 2.0 * nu) * (J1 + J2)) / (16.0 * np.pi * D)
    S[4, 4] = ((a1_sq + a3_sq) * J13 + (1.0 - 2.0 * nu) * (J1 + J3)) / (16.0 * np.pi * D)
    S[5, 5] = ((a2_sq + a3_sq) * J23 + (1.0 - 2.0 * nu) * (J2 + J3)) / (16.0 * np.pi * D)
    return S

def compute_L(S):
    I6 = np.eye(6)
    return np.linalg.inv(I6 - S)

def mt_step(C_old, phi_inst, L):
    I6 = np.eye(6)
    M = phi_inst * L + (1.0 - phi_inst) * I6
    M_inv = np.linalg.inv(M)
    C_new = (1.0 - phi_inst) * C_old @ M_inv
    return (C_new + C_new.T) / 2.0

def young_from_C(C):
    S = np.linalg.inv(C)
    return 1.0 / S[0, 0]

def compute_MT(phi_total):
    N_total = (3.0 * phi_total) / (4.0 * np.pi * np.sum(p * radii**3))
    N_i = p * N_total
    sphere_vol = (4.0 / 3.0) * np.pi * radii**3
    group_vols = N_i * sphere_vol
    # cumulative later volume
    cumul = np.zeros(n_classes)
    s = 0.0
    for i in range(n_classes - 1, -1, -1):
        cumul[i] = s
        s += group_vols[i]
    C = C_host.copy()
    for i in range(n_classes):
        phi_inst = group_vols[i] / (1.0 - cumul[i])
        S_local = np.linalg.inv(C)
        nu_curr = -S_local[0, 1] / S_local[0, 0]
        L = compute_L(Eshelby_sphere(nu_curr))
        C = mt_step(C, phi_inst, L)
    return young_from_C(C)

def compute_MMT(phi_total):
    N_total = (3.0 * phi_total) / (4.0 * np.pi * np.sum(p * radii**3))
    V_RVE = 1e-9  # m³  (1 mm³)
    N_in_RVE = N_total * V_RVE
    N_counts = p * N_in_RVE
    sphere_vol = (4.0 / 3.0) * np.pi * radii**3

    # merged probabilities
    n = len(radii)
    N_merged = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            ri = radii[i]; rj = radii[j]
            pr = (4.0 * np.pi / 3.0) * ((ri + rj)**3 - ri**3) / V_RVE
            if i == j:
                Nij_pair = N_counts[i] / 2.0
            else:
                Nij_pair = min(N_counts[i], N_counts[j])
            N_merged[i, j] = pr * N_counts[i] * Nij_pair

    # isolated counts
    N_isol = np.zeros(n)
    for i in range(n):
        total_merged = np.sum(N_merged[i, i:])
        N_isol[i] = max(N_counts[i] - total_merged, 0.0)

    # build groups (ordered: isolated of class i first, then merged of i with j>=i)
    groups = []  # (vol_total, shape, params)
    for i in range(n):
        if N_isol[i] > 1e-30:
            vol = N_isol[i] * sphere_vol[i]
            if vol > 1e-30:
                groups.append((vol, 'sphere', radii[i]))
    for i in range(n):
        for j in range(i, n):
            if N_merged[i, j] > 1e-30:
                V_pair = (4.0 / 3.0) * np.pi * (radii[i]**3 + radii[j]**3)
                vol = N_merged[i, j] * V_pair
                if vol > 1e-30:
                    ar = radii[j] / radii[i]   # >=1
                    a = ( (3.0 * V_pair) / (4.0 * np.pi * ar) )**(1.0 / 3.0)
                    c = ar * a
                    groups.append((vol, 'spheroid', ar))

    if len(groups) == 0:
        return young_from_C(C_host) * (1.0 - phi_total)

    # Scale volumes to exactly match phi_total
    total_vol = sum(g[0] for g in groups)
    scale = phi_total / total_vol if total_vol > 0 else 1.0
    for k in range(len(groups)):
        groups[k] = (groups[k][0] * scale,) + groups[k][1:]

    # cumulative later volume
    cumul = np.zeros(len(groups))
    s = 0.0
    for k in range(len(groups) - 1, -1, -1):
        cumul[k] = s
        s += groups[k][0]

    C = C_host.copy()
    for k, grp in enumerate(groups):
        vol_total, shape, *params = grp
        phi_inst = vol_total / (1.0 - cumul[k])
        S_local = np.linalg.inv(C)
        nu_curr = -S_local[0, 1] / S_local[0, 0]
        if shape == 'sphere':
            L = compute_L(Eshelby_sphere(nu_curr))
        elif shape == 'spheroid':
            ar = params[0]
            L = compute_L(Eshelby_spheroid_from_ar(ar, nu_curr))
        else:
            raise ValueError
        C = mt_step(C, phi_inst, L)
    return young_from_C(C)

def compute_OMT(phi_total):
    E_merged = compute_MMT(phi_total)
    phi_open = phi_total if phi_total >= 0.6 else 0.0
    return E_merged * (1.0 - phi_open)

# Evaluate at porosity levels 10% .. 90%
porosities = np.arange(10, 100, 10)
results = []
for pct in porosities:
    phi = pct / 100.0
    e_mt = compute_MT(phi)
    e_mmt = compute_MMT(phi)
    e_omt = compute_OMT(phi)
    results.append((int(pct), round(e_mt, 2), round(e_mmt, 2), round(e_omt, 2)))

with open('/app/outputs/predicted_moduli.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in results:
        writer.writerow(row)
