import json
import sys
import numpy as np

OUTPUT = "/app/outputs/stress_results.json"

# =============================================================================
# Physical constants and common parameters
# =============================================================================
DeltaT = -1700.0          # K
sigma_a = -5.0            # GPa

# Elastic constants (Table 1)
E_BnS = 900.0
nu_BnS = 0.1
alpha_BnS = 2.8e-6

E_BnW_iso = 800.0
nu_BnW = 0.1
alpha_BnW_iso = 3.03e-6

E_BnG = 80.0
nu_BnG = 0.2
# BN_g has no tabulated alpha

# Anisotropic thermal expansion for case 3
alpha_a = 2.7e-6
alpha_c = 3.7e-6

# Transformation strains (dimensionless)
eps_tr_BNS_low_T = 3.2e-3       # case 2
eps_tr_BNG = 170.0e-3           # case 4

# =============================================================================
# Helper: isotropic stiffness in Voigt (6×6)
# =============================================================================
def isotropic_C_voigt(E, nu):
    """6×6 Voigt matrix for isotropic material."""
    c11 = (1.0 - nu) * E / ((1.0 + nu) * (1.0 - 2.0 * nu))
    c12 = nu * E / ((1.0 + nu) * (1.0 - 2.0 * nu))
    G  = E / (2.0 * (1.0 + nu))
    C = np.zeros((6, 6))
    C[0, 0] = C[1, 1] = C[2, 2] = c11
    C[0, 1] = C[0, 2] = C[1, 2] = c12
    C[1, 0] = C[2, 0] = C[2, 1] = c12
    C[3, 3] = C[4, 4] = C[5, 5] = G
    return C

def isotropic_compliance_voigt(E, nu):
    """6×6 compliance matrix (Voigt)."""
    return np.linalg.inv(isotropic_C_voigt(E, nu))

def bulk_modulus(E, nu):
    return E / (3.0 * (1.0 - 2.0 * nu))

def shear_modulus(E, nu):
    return E / (2.0 * (1.0 + nu))

# =============================================================================
# Thermal / transformation / unloading strain
# =============================================================================
def thermal_strain_iso(alpha, DT):
    """isotropic thermal strain tensor (3×3)."""
    return np.eye(3) * alpha * DT

def thermal_strain_aniso(alpha_mat, DT):
    """anisotropic thermal strain from diagonal alpha matrix (3×3)."""
    return alpha_mat * DT

def unloading_strain_iso(E, nu, sigma_a):
    K = bulk_modulus(E, nu)
    e_el = -sigma_a / (3.0 * K)   # positive expansion because sigma_a < 0
    return np.eye(3) * e_el

def eps_to_voigt(eps):
    v = np.zeros(6)
    v[0] = eps[0, 0]
    v[1] = eps[1, 1]
    v[2] = eps[2, 2]
    v[3] = 2.0 * eps[1, 2]
    v[4] = 2.0 * eps[0, 2]
    v[5] = 2.0 * eps[0, 1]
    return v

def voigt_to_eps(v):
    eps = np.zeros((3,3))
    eps[0,0] = v[0]
    eps[1,1] = v[1]
    eps[2,2] = v[2]
    eps[1,2] = eps[2,1] = 0.5 * v[3]
    eps[0,2] = eps[2,0] = 0.5 * v[4]
    eps[0,1] = eps[1,0] = 0.5 * v[5]
    return eps

# =============================================================================
# 4-th rank tensor E (Eq. 2) – isotropic spherical grains
# =============================================================================
def isotropic_E_tensor(G, nu):
    """
    Returns E_ijkl as a 3×3×3×3 numpy array.
    E_{ijkl} = \frac{1}{30 G (1 - nu)} [ 2(4 - 5 nu) I_{ijkl} - \delta_{ij} \delta_{kl} ]
    with I_{ijkl} = 0.5 (\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}).
    """
    coeff = 1.0 / (30.0 * G * (1.0 - nu))
    I = np.zeros((3,3,3,3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    I[i,j,k,l] = 0.5 * ((i==k and j==l) + (i==l and j==k))
    delta = np.eye(3)
    E = coeff * (2.0 * (4.0 - 5.0 * nu) * I - np.einsum('ij,kl->ijkl', delta, delta))
    return E

# =============================================================================
# Core model: compute sigma0 and delta_sigma for a collection of phases
# =============================================================================

def compute_statistics(phases):
    """
    phases: list of dicts, each with:
      'V'      : volume fraction
      'C_voigt': 6×6 stiffness
      'eps_voigt': 6-vector eigenstrain (thermal + transformation + unloading)
      'eps_3x3   : 3×3 eigenstrain tensor (for norm)
    Returns global parameters and for each phase:
      sigma0_33  (mean axial stress in specimen frame, GPa)
      delta_sigma33 (rms deviation, GPa)
    """
    N = len(phases)
    Vs = np.array([p['V'] for p in phases])

    # Average stiffness C+  (Voigt)
    C_plus = np.zeros((6,6))
    for p in phases:
        C_plus += p['V'] * p['C_voigt']

    # Average compliance → C-
    S_avg = np.zeros((6,6))
    for p in phases:
        S_avg += p['V'] * np.linalg.inv(p['C_voigt'])
    C_minus = np.linalg.inv(S_avg)

    # Average eigenstrain vectors
    eps_avg_vec = np.zeros(6)
    C_eps_avg_vec = np.zeros(6)
    for p in phases:
        eps_avg_vec += p['V'] * p['eps_voigt']
        C_eps_avg_vec += p['V'] * (p['C_voigt'] @ p['eps_voigt'])

    gamma_sigma = np.linalg.inv(C_plus) @ C_eps_avg_vec
    gamma_epsilon = eps_avg_vec
    epsilon_star = 0.5 * (gamma_sigma + gamma_epsilon)      # eq. (9)

    # Scalar Q = gamma_sigma : : C+ : gamma_sigma
    Q = np.dot(gamma_sigma, C_plus @ gamma_sigma)

    # Average squared norm of eigenstrain
    avg_norm2 = 0.0
    for p in phases:
        avg_norm2 += p['V'] * np.sum(p['eps_3x3']**2)

    mu = (1.0/12.0) * (avg_norm2 - Q)        # eq. (3) second term vanishes with eq. (9)

    results = []
    for p in phases:
        # mean stress vector sigma0 = C_i ( (gamma_sigma - eps_i)/2 )
        mean_stress_vec = 0.5 * (p['C_voigt'] @ (gamma_sigma - p['eps_voigt']))
        sigma0 = mean_stress_vec[2]   # component 33

        # fluctuation covariance: Sigma = (-mu/2) * E
        G = shear_modulus(p['E'], p['nu'])
        nu = p['nu']
        E_tensor = isotropic_E_tensor(G, nu)
        Sigma_tensor = (-mu / 2.0) * E_tensor

        # Cov_stress_ijkl = C_ijmn Sigma_mnpq C_klpq
        # For variance of sigma_33:
        C_full = np.zeros((3,3,3,3))
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        # Voigt → full conversion
                        # but we need C_ijmn. We can expand from isotropic form:
                        lam = p['C_voigt'][0,1]
                        mu_s = p['C_voigt'][3,3]
                        delta = np.eye(3)
                        C_full[i,j,k,l] = lam * delta[i,j]*delta[k,l] + mu_s * ( (i==k and j==l) + (i==l and j==k) )
        # however, we can compute stress_cov using einsum:
        # stress_cov_ijkl = sum_{m,n,p,q} C_ijmn Sigma_mnpq C_klpq
        # Since Sigma_mnpq is fully symmetric, we can use einsum
        stress_cov = np.einsum('ijmn,mnpq,klpq->ijkl', C_full, Sigma_tensor, C_full)
        var_s33 = stress_cov[2,2,2,2]
        delta_sigma = np.sqrt(max(0.0, var_s33))

        results.append( (p['label'], p['V'], sigma0, delta_sigma) )

    return results, mu

# =============================================================================
# Build phases for each scenario
# =============================================================================

# Common unloading strain contributions
def phase_data(E, nu, alpha_iso=None, alpha_aniso_diag=None,
               eps_tr=0.0, label=None):
    eps_th = np.zeros((3,3))
    if alpha_iso is not None:
        eps_th = thermal_strain_iso(alpha_iso, DeltaT)
    elif alpha_aniso_diag is not None:
        eps_th = thermal_strain_aniso(np.diag(alpha_aniso_diag), DeltaT)
    # unloading
    eps_ul = unloading_strain_iso(E, nu, sigma_a)
    # total eigenstrain (3×3)
    eps_tot = eps_th + eps_ul + np.eye(3)*eps_tr
    C_voigt = isotropic_C_voigt(E, nu)
    eps_voigt = eps_to_voigt(eps_tot)
    return {
        'E': E, 'nu': nu,
        'C_voigt': C_voigt,
        'eps_voigt': eps_voigt,
        'eps_3x3': eps_tot,
        'label': label
    }

# =============================================================================
# Case 1 & 2  (BN_W + BN_S)
# =============================================================================

cases_1_and_2 = {}
for case_id in ['case1', 'case2']:
    entries = []
    for V_BNS in np.arange(0.0, 1.001, 0.2):
        V_BNS = round(V_BNS, 2)
        V_BNW = 1.0 - V_BNS
        phases = []
        if V_BNW > 0:
            phases.append(phase_data(E=E_BnW_iso, nu=nu_BnW,
                                     alpha_iso=alpha_BnW_iso,
                                     eps_tr=0.0, label='BN_W'))
        if V_BNS > 0:
            eps_tr = eps_tr_BNS_low_T if case_id=='case2' else 0.0
            phases.append(phase_data(E=E_BnS, nu=nu_BnS,
                                     alpha_iso=alpha_BnS,
                                     eps_tr=eps_tr, label='BN_S'))
        # set volumes
        for p in phases:
            if p['label'] == 'BN_W': p['V'] = V_BNW
            else: p['V'] = V_BNS

        res, _ = compute_statistics(phases)
        for label, V, s0, ds in res:
            entries.append({
                "V_BNS": V_BNS if label=='BN_S' else V_BNS,  # always V_BNS for ease
                "phase": "BN_W" if label=='BN_W' else "BN_S",
                "sigma0": round(s0, 6),
                "delta_sigma": round(ds, 6)
            })
    cases_1_and_2[case_id] = entries

# =============================================================================
# Case 3  (single-phase textured BN_W)
# =============================================================================

case3 = []
# orientation sampling
N_phi = 36  # uniform azimuthal samples
phi_vals = np.linspace(0, 2*np.pi, N_phi)
for theta_deg in [0, 15, 30, 45, 60, 75, 90]:
    theta = np.deg2rad(theta_deg)
    # prepare grains
    grains = []
    for phi in phi_vals:
        # direction of c-axis
        u = np.array([np.sin(theta)*np.cos(phi),
                      np.sin(theta)*np.sin(phi),
                      np.cos(theta)])
        # rotation matrix: align z to u
        # R = R_z(phi) * R_y(theta)
        Ry = np.array([[np.cos(theta), 0, np.sin(theta)],
                       [0,             1, 0            ],
                       [-np.sin(theta),0, np.cos(theta)]])
        Rz = np.array([[np.cos(phi), -np.sin(phi), 0],
                       [np.sin(phi), np.cos(phi),  0],
                       [0,           0,            1]])
        R = Rz @ Ry
        # anisotropic thermal strain in crystal axes
        alpha_mat_cryst = np.diag([alpha_a, alpha_a, alpha_c])
        eps_th_cryst = thermal_strain_aniso(alpha_mat_cryst, DeltaT)
        # rotate to specimen frame
        eps_th_spec = R @ eps_th_cryst @ R.T
        # unloading (isotropic)
        eps_ul = unloading_strain_iso(E_BnW_iso, nu_BnW, sigma_a)
        eps_tot = eps_th_spec + eps_ul
        # prepare grain
        Cv = isotropic_C_voigt(E_BnW_iso, nu_BnW)
        grains.append({
            'V': 1.0/N_phi,
            'E': E_BnW_iso, 'nu': nu_BnW,
            'C_voigt': Cv,
            'eps_voigt': eps_to_voigt(eps_tot),
            'eps_3x3': eps_tot,
            'label': 'BN_W'
        })

    # compute global statistics
    res_all, mu_val = compute_statistics(grains)
    # For the output we report sigma0 and delta_sigma for a grain at this theta
    # (use the first grain as representative; they all have same sigma0? no, sigma0 depends on orientation)
    # Actually sigma0 from compute_statistics for each grain gives that grain's mean stress.
    # The paper likely reports the mean stress for a grain with that orientation.
    # We'll take the grain whose orientation matches theta exactly (phi=0).
    # So we should pick one specific grain.
    # But compute_statistics already returns per-grain results; we need to output the one we want.
    # The list res_all has entries for all grains; we'll filter the one with phi=0? Not possible.
    # So better: we compute the mean stress for a specific orientation separately.
    # Let's recompute for a single representative grain with phi=0 after building the global parameters.
    # We'll modify compute_statistics to also return individual stats.
    # Actually compute_statistics returns list of (label, V, sigma0, delta_sigma) per grain.
    # We'll run the whole ensemble, then pick the first grain from the list.
    # (All grains in the ensemble have the same phi sampling; their sigma0 values are stored.
    # So we can retrieve the sigma0 for the grain we want.
    # To make it deterministic, we can find the grain with specific eps_tot.
    # Simpler: after compute_statistics, we can manually compute sigma0 for a grain with phi=0 using the global gamma_sigma and mu.

    # Let's compute global quantities manually.
    Vs_all = np.array([g['V'] for g in grains])
    C_plus = np.sum([g['V']*g['C_voigt'] for g in grains], axis=0)
    S_avg = np.sum([g['V']*np.linalg.inv(g['C_voigt']) for g in grains], axis=0)
    C_minus = np.linalg.inv(S_avg)
    eps_avg_vec = np.sum([g['V']*g['eps_voigt'] for g in grains], axis=0)
    C_eps_avg_vec = np.sum([g['V']*(g['C_voigt'] @ g['eps_voigt']) for g in grains], axis=0)
    gamma_sigma = np.linalg.inv(C_plus) @ C_eps_avg_vec
    avg_norm2 = np.sum([g['V'] * np.sum(g['eps_3x3']**2) for g in grains])
    Q = np.dot(gamma_sigma, C_plus @ gamma_sigma)
    mu_val = (1/12)*(avg_norm2 - Q)

    # Now compute for a specific grain: orientation theta, phi=0
    phi0 = 0.0
    u0 = np.array([np.sin(theta)*np.cos(phi0), np.sin(theta)*np.sin(phi0), np.cos(theta)])
    Ry = np.array([[np.cos(theta), 0, np.sin(theta)],
                   [0,             1, 0            ],
                   [-np.sin(theta),0, np.cos(theta)]])
    Rz = np.eye(3)
    R0 = Rz @ Ry
    eps_th_cryst0 = thermal_strain_aniso(np.diag([alpha_a, alpha_a, alpha_c]), DeltaT)
    eps_th_spec0 = R0 @ eps_th_cryst0 @ R0.T
    eps_ul0 = unloading_strain_iso(E_BnW_iso, nu_BnW, sigma_a)
    eps_tot0 = eps_th_spec0 + eps_ul0
    eps_vec0 = eps_to_voigt(eps_tot0)
    Cv0 = isotropic_C_voigt(E_BnW_iso, nu_BnW)
    sigma0_val = 0.5 * (Cv0 @ (gamma_sigma - eps_vec0))[2]

    # delta_sigma
    G_val = shear_modulus(E_BnW_iso, nu_BnW)
    E_tns = isotropic_E_tensor(G_val, nu_BnW)
    Sigma_tns = (-mu_val/2.0) * E_tns
    lam = Cv0[0,1]
    mu_s = Cv0[3,3]
    delta = np.eye(3)
    C_full0 = np.zeros((3,3,3,3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    C_full0[i,j,k,l] = lam*delta[i,j]*delta[k,l] + mu_s*((i==k and j==l)+(i==l and j==k))
    stress_cov = np.einsum('ijmn,mnpq,klpq->ijkl', C_full0, Sigma_tns, C_full0)
    var_s33 = stress_cov[2,2,2,2]
    delta_sigma_val = np.sqrt(max(0.0, var_s33))

    case3.append({
        "angle_deg": theta_deg,
        "sigma0": round(float(sigma0_val), 6),
        "delta_sigma": round(float(delta_sigma_val), 6)
    })

# =============================================================================
# Case 4  (three-phase)
# =============================================================================

table2 = []
# compositions from Table 2
comp_list = [(0.20, 0.79, 0.01),
             (0.50, 0.49, 0.01),
             (0.49, 0.49, 0.02)]
for (V_S, V_W, V_G) in comp_list:
    phases = []
    # BN_S
    phases.append(phase_data(E=E_BnS, nu=nu_BnS, alpha_iso=alpha_BnS,
                              eps_tr=0.0, label='BN_S'))
    phases[-1]['V'] = V_S
    # BN_W
    phases.append(phase_data(E=E_BnW_iso, nu=nu_BnW, alpha_iso=alpha_BnW_iso,
                              eps_tr=0.0, label='BN_W'))
    phases[-1]['V'] = V_W
    # BN_g (no thermal expansion, but transformation strain)
    phases.append(phase_data(E=E_BnG, nu=nu_BnG, alpha_iso=0.0,
                              eps_tr=eps_tr_BNG, label='BN_G'))
    phases[-1]['V'] = V_G

    res, _ = compute_statistics(phases)
    # output only BN_g stress (Table 2)
    for label, V, s0, ds in res:
        if label == 'BN_G':
            table2.append({
                "V_BNS": V_S,
                "V_BNW": V_W,
                "V_BNG": V_G,
                "sigma0": round(s0, 6),
                "delta_sigma": round(ds, 6)
            })

# =============================================================================
# Write output
# =============================================================================
output = {
    "case1": cases_1_and_2["case1"],
    "case2": cases_1_and_2["case2"],
    "case3": case3,
    "case4": {"table2": table2}
}

with open(OUTPUT, 'w') as f:
    json.dump(output, f, indent=2)
