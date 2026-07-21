import sys, math, cmath, csv, json, numpy as np

# Material constants (Table 1 of the paper)
CdS = {'C44': 1.49e10, 'rho': 4824, 'e15': -0.21, 'eps11': 7.99e-11}
ZnO = {'C44': 4.25e10, 'rho': 5676, 'e15': -0.59, 'eps11': 7.38e-11}

# Vacuum permittivity
EPS0 = 8.854187817e-12

# Reference velocity for dimensionless scaling
C_t_CdS = math.sqrt(CdS['C44'] / CdS['rho'])

OUTDIR = '/app/outputs'
D = 1.0            # period (m), arbitrary; results independent
h = D / 4          # half‑thickness of CdS layer (h = h')
hp = D / 4         # half‑thickness of ZnO layer

def compute_T_and_block(k_parallel_D, Omega, matA, matB):
    """
    Return the 4x4 transfer matrix T, its inverse, and the 2x2 block
    M = (T+T^{-1})/2 that appears in the dispersion relation.
    matA: material for the first layer (e.g., CdS or ZnO).
    matB: material for the second layer.
    """
    k = k_parallel_D               # because D=1
    omega = 2 * math.pi * Omega * C_t_CdS

    C44A = matA['C44']; rhoA = matA['rho']; e15A = matA['e15']; eps11A = matA['eps11']
    C44B = matB['C44']; rhoB = matB['rho']; e15B = matB['e15']; eps11B = matB['eps11']

    # α^2
    denomA = C44A + e15A**2 / eps11A
    alphaA_sq = k*k - rhoA * omega*omega / denomA
    alphaA = cmath.sqrt(alphaA_sq)

    denomB = C44B + e15B**2 / eps11B
    alphaB_sq = k*k - rhoB * omega*omega / denomB
    alphaB = cmath.sqrt(alphaB_sq)

    # Appendix constants
    B_val = e15A/eps11A - e15B/eps11B

    C_val  = k * (eps11A * e15B - eps11B * e15A) / (eps11B * alphaB * (C44B + e15B**2/eps11B))
    C_prime= k * (eps11A * e15B - eps11B * e15A) / (eps11A * alphaA * (C44A + e15A**2/eps11A))

    F_val  = alphaA * (C44A + e15A**2/eps11A) / (alphaB * (C44B + e15B**2/eps11B))
    F_prime= 1.0 / F_val

    E_val  = eps11A / eps11B
    E_prime= 1.0 / E_val

    # Hyperbolic functions
    S1 = cmath.sinh(k*h); C1 = cmath.cosh(k*h)
    S1p = cmath.sinh(k*hp); C1p = cmath.cosh(k*hp)
    S1_2 = cmath.sinh(2*k*h); C1_2 = cmath.cosh(2*k*h)
    S1p_2 = cmath.sinh(2*k*hp); C1p_2 = cmath.cosh(2*k*hp)

    S2 = cmath.sinh(alphaA * h); C2 = cmath.cosh(alphaA * h)
    S2p = cmath.sinh(alphaB * hp); C2p = cmath.cosh(alphaB * hp)
    S2_2 = cmath.sinh(2 * alphaA * h); C2_2 = cmath.cosh(2 * alphaA * h)
    S2p_2 = cmath.sinh(2 * alphaB * hp); C2p_2 = cmath.cosh(2 * alphaB * hp)

    # Transfer matrix elements (from Appendix)
    T11 = C1_2*C1p_2 + 0.5*(E_val+E_prime)*S1_2*S1p_2 + 0.5*B_val*C_val*S1_2*S2p_2
    T12 = B_val*(C1p_2 - C2p_2)*C1*C2 + B_val*(E_prime*C2*S1*S1p_2 - F_val*C1*S2*S2p_2)
    T13 = -S1_2*C1p_2 - (E_val*C1**2 + E_prime*S1**2)*S1p_2 - B_val*C_val*C1**2*S2p_2
    T14 = B_val*(C2p_2 - C1p_2)*C1*S2 - B_val*E_prime*S1p_2*S1*S2 + B_val*F_val*C1*C2*S2p_2

    T21 = C_prime*C1*S2*S1p_2 - C_val*S1*C2*S2p_2 + (E_val*C_prime*C1p_2 - C_val*F_prime*C2p_2)*S1*S2
    T22 = C2_2*C2p_2 + 0.5*(F_val+F_prime)*S2_2*S2p_2 + 0.5*B_val*C_prime*S1p_2*S2_2
    T23 = C_val*C1*C2*S2p_2 - C_prime*S1*S2*S1p_2 + (C_val*F_prime*C2p_2 - C_prime*E_val*C1p_2)*C1*S2
    T24 = -C2p_2*S2_2 - (F_prime*S2**2 + F_val*C2**2)*S2p_2 - B_val*C_prime*S1p_2*S2**2

    T31 = -C1p_2*S1_2 - B_val*C_val*S2p_2*S1**2 - (E_prime*C1**2 + E_val*S1**2)*S1p_2
    T32 = B_val*(C2p_2 - C1p_2)*S1*C2 - B_val*E_prime*C1*C2*S1p_2 + B_val*F_val*S1*S2*S2p_2
    T33 = T11
    T34 = B_val*(C1p_2 - C2p_2)*S1*S2 + B_val*(E_prime*C1*S2*S1p_2 - F_val*S1*C2*S2p_2)

    T41 = C_val*S1*S2*S2p_2 - C_prime*C1*C2*S1p_2 + (C_val*F_prime*C2p_2 - C_prime*E_val*C1p_2)*C2*S1
    T42 = -C2p_2*S2_2 - B_val*C_prime*S1p_2*C2**2 - (F_prime*C2**2 + F_val*S2**2)*S2p_2
    T43 = C_prime*S1*C2*S1p_2 - C_val*C1*S2*S2p_2 + (E_val*C_prime*C1p_2 - C_val*F_prime*C2p_2)*C1*C2
    T44 = T22

    T = np.array([[T11, T12, T13, T14],
                  [T21, T22, T23, T24],
                  [T31, T32, T33, T34],
                  [T41, T42, T43, T44]], dtype=complex)

    invT = np.linalg.inv(T)
    M = 0.5 * (T + invT)
    # upper-left 2x2 block
    M11 = M[0,0].real
    M12 = M[0,1].real
    M21 = M[1,0].real
    M22 = M[1,1].real

    return T, invT, (M11, M12, M21, M22)


def eigenvalues_2x2(M11, M12, M21, M22):
    """ Return the two real eigenvalues of the 2x2 matrix. """
    tr = M11 + M22
    det = M11*M22 - M12*M21
    disc = tr*tr - 4*det
    if disc < 0:
        disc = 0.0
    sqrt_disc = math.sqrt(disc)
    lam1 = (tr + sqrt_disc) / 2.0
    lam2 = (tr - sqrt_disc) / 2.0
    return lam1, lam2


def propagation_condition(k_parallel_D, Omega):
    """ Return True if bulk waves propagate (any eigenvalue in [-1,1]). """
    _, _, (M11, M12, M21, M22) = compute_T_and_block(k_parallel_D, Omega, CdS, ZnO)
    lam1, lam2 = eigenvalues_2x2(M11, M12, M21, M22)
    return (abs(lam1) <= 1.0) or (abs(lam2) <= 1.0)


def find_band_edges(k_parallel_D, Omega_min=0.0, Omega_max=1.2, dOmega=0.0005):
    """ Return lists of (Omega_lower, Omega_upper) for consecutive bands. """
    # coarse scan
    N = int((Omega_max - Omega_min) / dOmega) + 1
    Omegas = [Omega_min + i*dOmega for i in range(N)]
    flags = [False]*N
    for i, Om in enumerate(Omegas):
        flags[i] = propagation_condition(k_parallel_D, Om)
    # Refine band edges via bisection
    edges = []
    prev = False
    for i in range(1, N):
        if flags[i] != prev:
            # bisection
            a = Omegas[i-1]
            b = Omegas[i]
            for _ in range(30):
                mid = 0.5*(a+b)
                if propagation_condition(k_parallel_D, mid):
                    b = mid
                else:
                    a = mid
            edges.append(0.5*(a+b))
        prev = flags[i]
    # edges list alternates: start, end of first band, start, end of second, etc.
    if not edges:
        return []
    # Ensure first edge is band start (propagation begins)
    if flags[0]:
        # band starts at Omega_min
        edges.insert(0, Omega_min)
    bands = []
    for i in range(0, len(edges)-1, 2):
        bands.append((edges[i], edges[i+1]))
    if len(edges) % 2 == 1:
        # last band extends to Omega_max (unlikely)
        pass
    return bands


def compute_bulk_band_edges():
    kD_vals = np.linspace(0.0, math.pi, 200)   # enough points
    with open(f'{OUTDIR}/bulk_band_edges.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['k_parallel_D', 'band1_lower', 'band1_upper', 'band2_lower', 'band2_upper'])
        for kD in kD_vals:
            bands = find_band_edges(kD, Omega_max=1.2)
            b1l = bands[0][0] if len(bands)>=1 else float('nan')
            b1u = bands[0][1] if len(bands)>=1 else float('nan')
            b2l = bands[1][0] if len(bands)>=2 else float('nan')
            b2u = bands[1][1] if len(bands)>=2 else float('nan')
            writer.writerow([kD, b1l, b1u, b2l, b2u])


def surface_det(Omega, k_parallel_D, surface_mat, other_mat, metallized):
    """
    Compute the determinant of the surface boundary condition matrix.
    surface_mat: material of the surface layer (e.g., CdS or ZnO).
    """
    T, _, _ = compute_T_and_block(k_parallel_D, Omega, surface_mat, other_mat)
    eigenvalues, eigenvectors = np.linalg.eig(T)
    # select eigenvectors with |eigenvalue| < 1 (decaying)
    retained = []
    for i in range(len(eigenvalues)):
        if abs(eigenvalues[i]) < 1.0:
            # eigenvector is eigenvectors[:,i]
            retained.append(eigenvectors[:, i])
    if len(retained) < 2:
        return 1e6   # no decaying modes

    C44 = surface_mat['C44']; e15 = surface_mat['e15']; eps11 = surface_mat['eps11']
    k = k_parallel_D
    alpha_sq_num = k*k - surface_mat['rho'] * (2*math.pi*Omega*C_t_CdS)**2 / (C44 + e15**2/eps11)
    alpha = cmath.sqrt(alpha_sq_num)
    hs = h if surface_mat is CdS else hp   # surface layer half‑thickness

    D_mat = []
    for r in range(2):
        psi = retained[r]
        P1 = psi[0]; P2 = psi[1]; Q1 = psi[2]; Q2 = psi[3]
        # sinh/cosh arguments
        arg_k = k * hs
        arg_a = alpha * hs
        sinh_k = cmath.sinh(arg_k); cosh_k = cmath.cosh(arg_k)
        sinh_a = cmath.sinh(arg_a); cosh_a = cmath.cosh(arg_a)

        D1r = e15 * k * (P1 * sinh_k + Q1 * cosh_k) + \
              alpha * (C44 + e15**2/eps11) * (P2 * sinh_a + Q2 * cosh_a)
        D2r = eps11 * k * (P1 * sinh_k + Q1 * cosh_k)
        D3r = P1 * cosh_k + Q1 * sinh_k + (e15/eps11) * (P2 * cosh_a + Q2 * sinh_a)
        if metallized:
            D_mat.append([D1r, D2r])
        else:
            D_mat.append([D1r, D2r, D3r])
    if metallized:
        # 2x2 determinant
        mat = np.array(D_mat, dtype=complex).T   # shape (2,2)
        return np.linalg.det(mat).real
    else:
        # 3x3, add third column (vacuum)
        col3 = [0.0, EPS0 * k * math.exp(-k * hs), -math.exp(-k * hs)]
        mat = np.array(D_mat + [col3], dtype=complex).T   # shape (3,3)
        return np.linalg.det(mat).real


def find_surface_omega(k_parallel_D, surface_mat, other_mat, metallized, Omega_bulk_edge):
    """
    Search for a surface wave frequency below Omega_bulk_edge.
    Returns Omega (float) or None if not found.
    """
    # scan from 0 to bulk_edge
    Om_min = 0.0
    Om_max = Omega_bulk_edge * 0.999  # slightly below edge
    if Om_max <= Om_min:
        return None
    steps = 200
    dOm = (Om_max - Om_min) / steps
    prev_det = None
    for i in range(steps+1):
        Om = Om_min + i*dOm
        det = surface_det(Om, k_parallel_D, surface_mat, other_mat, metallized)
        if prev_det is not None and prev_det * det < 0:
            # bisection
            a = Om - dOm
            b = Om
            for _ in range(25):
                mid = 0.5*(a+b)
                if surface_det(mid, k_parallel_D, surface_mat, other_mat, metallized) * prev_det < 0:
                    b = mid
                else:
                    a = mid
            Om_root = 0.5*(a+b)
            return Om_root
        prev_det = det
    return None


def compute_surface_velocities():
    kD_list = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    with open(f'{OUTDIR}/surface_phase_velocities.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['k_parallel_D', 'velocity_CdS_nonmetal', 'velocity_CdS_metal', 'velocity_ZnO_metal'])
        for kD in kD_list:
            # bulk band lower edge
            bands = find_band_edges(kD, Omega_max=1.2)
            if not bands:
                bulk_edge = 0.01   # fallback
            else:
                bulk_edge = bands[0][0]
            # CdS non-metal
            Om_non = find_surface_omega(kD, CdS, ZnO, metallized=False, Omega_bulk_edge=bulk_edge)
            # CdS metal
            Om_met = find_surface_omega(kD, CdS, ZnO, metallized=True, Omega_bulk_edge=bulk_edge)
            # ZnO metal
            Om_zmet = find_surface_omega(kD, ZnO, CdS, metallized=True, Omega_bulk_edge=bulk_edge)
            def to_velocity(Om):
                if Om is None or kD == 0:
                    return ''
                return 2*math.pi * Om / kD
            writer.writerow([kD, to_velocity(Om_non), to_velocity(Om_met), to_velocity(Om_zmet)])


def compute_effective_constants():
    x = 0.5   # equal thicknesses
    def get_vals(mat):
        C44 = mat['C44']; eps11 = mat['eps11']; e15 = mat['e15']
        Dprime = C44 * eps11 + e15**2
        A = C44 / Dprime
        B = eps11 / Dprime
        C = e15 / Dprime
        return A, B, C
    A_cds, B_cds, C_cds = get_vals(CdS)
    A_zno, B_zno, C_zno = get_vals(ZnO)
    A_avg = x*A_cds + (1-x)*A_zno
    B_avg = x*B_cds + (1-x)*B_zno
    C_avg = x*C_cds + (1-x)*C_zno
    Dprime_eff = 1.0 / (A_avg*B_avg + C_avg**2)
    C44_eff = A_avg * Dprime_eff          # N/m²
    e15_eff = C_avg * Dprime_eff          # C/m²
    eps11_eff = B_avg * Dprime_eff        # F/m
    # convert to required units: C44_eff in 10^10 N/m², e15_eff in C/m², eps11_eff in 10⁻¹¹ F/m
    result = {
        "C44_eff": C44_eff / 1e10,
        "e15_eff": e15_eff,
        "epsilon11_eff": eps11_eff / 1e-11
    }
    with open(f'{OUTDIR}/effective_constants.json', 'w') as f:
        json.dump(result, f, indent=2)


if __name__ == '__main__':
    task = sys.argv[1]
    if task == 'bulk_bands':
        compute_bulk_band_edges()
    elif task == 'surface':
        compute_surface_velocities()
    elif task == 'effective':
        compute_effective_constants()
    else:
        raise SystemExit("Unknown task: " + task)
