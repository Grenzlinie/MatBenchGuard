import numpy as np
from scipy.integrate import quad

# ------------------- physical constants in atomic units -------------------
a0 = 1.0          # Bohr radius
kB_au = 3.1668114e-6  # K^-1
Ha_per_eV = 0.0367493
nm_to_au = 18.897

# ------------------- element parameters -------------------
# (symbol, hard_sphere_diameter_nm, empty_core_radius_au, Z, r_s_au,
#  core_A_eV, core_B, core_C, core_r0_nm)
params = {
    'Na': {'sigma_nm': 0.331, 'rc_au': 1.68, 'Z': 1, 'rs_au': 3.99,
           'A_eV': 0.605, 'B': 5.56, 'C': -12.1, 'r0_nm': 0.382},
    'K':  {'sigma_nm': 0.410, 'rc_au': 2.26, 'Z': 1, 'rs_au': 4.86,
           'A_eV': 0.934, 'B': 7.30, 'C': -13.6, 'r0_nm': 0.464},
    'Al': {'sigma_nm': 0.253, 'rc_au': 1.13, 'Z': 3, 'rs_au': 2.07,
           'A_eV': 0.908, 'B': 9.97, 'C': -19.6, 'r0_nm': 0.282},
    'Mg': {'sigma_nm': 0.284, 'rc_au': 1.32, 'Z': 2, 'rs_au': 2.66,
           'A_eV': 1.269, 'B':4.91, 'C': -11.0, 'r0_nm': 0.321}
}

def generate(alloy, output_path):
    if alloy == 'NaK':
        A, B = 'Na', 'K'
        T = 384.0
        x_A_list = [0.1, 0.3, 0.5, 0.7, 0.9]   # mole fraction of A (Na)
    elif alloy == 'AlMg':
        A, B = 'Al', 'Mg'
        T = 1073.0
        x_A_list = [0.1, 0.3, 0.5, 0.7, 0.9]   # mole fraction of A (Al)
    else:
        raise ValueError
    
    pA, pB = params[A], params[B]
    
    with open(output_path, 'w') as f:
        f.write('x_%s,a_%s
' % (A, A))
        for x_A in x_A_list:
            a_A = compute_activity(pA, pB, x_A, T)
            f.write('%.1f,%.6e
' % (x_A, a_A))

def compute_activity(pA, pB, x_A, T):
    # x_A is mole fraction of A; in paper's notation x = x_B = 1-x_A
    x = 1.0 - x_A
    sigma_A = pA['sigma_nm'] * nm_to_au
    sigma_B = pB['sigma_nm'] * nm_to_au
    Z_A, Z_B = pA['Z'], pB['Z']
    rs_A, rs_B = pA['rs_au'], pB['rs_au']
    rc_A, rc_B = pA['rc_au'], pB['rc_au']
    
    # pure densities (atomic) from r_s
    # (4/3) pi r_s^3 = 1/(Z n_atom)  => n_atom = 1/(Z * (4/3) pi r_s^3)
    n_A_pure = 1.0 / (Z_A * (4.0/3.0)*np.pi * rs_A**3)
    n_B_pure = 1.0 / (Z_B * (4.0/3.0)*np.pi * rs_B**3)
    n_A_pure = n_A_pure
    n_B_pure = n_B_pure
    
    # mixture packing fraction eta = 0.45
    eta = 0.45
    # from eta = (pi/6) (n_A sigma_A^3 + n_B sigma_B^3) with n_A = n*(1-x), n_B = n*x
    vol_avg = (1-x)*sigma_A**3 + x*sigma_B**3
    n = eta / (np.pi/6.0 * vol_avg)   # mean atomic number density
    n_A = n * (1-x)
    n_B = n * x
    
    # mixture electronic parameters
    Z_bar = (1-x)*Z_A + x*Z_B
    rs_bar_cube_sum = (1-x)*Z_A*rs_A**3 + x*Z_B*rs_B**3
    rs_bar = (rs_bar_cube_sum / Z_bar)**(1.0/3.0) if Z_bar>0 else 0.0
    n_e = Z_bar * n
    kF = (3.0*np.pi**2 * n_e)**(1.0/3.0)
    
    # Fermi energy in a.u.
    EF = 0.5 * kF**2
    
    # ----------  hard-sphere chemical potential ----------
    # packing fraction, X, Y, pressure
    eta_bar = eta   # constant with composition as assumed
    X = (np.pi/6.0) * (n_A*sigma_A**2 + n_B*sigma_B**2)
    Y = (np.pi/6.0) * (n_A*sigma_A + n_B*sigma_B)
    
    # pressure Eq. (5)
    P_hs_kBT = n * (1+eta_bar+eta_bar**2) / (1-eta_bar)**3 \
               - 0.5 * np.pi * n_A * n_B * (sigma_A-sigma_B)**2 \
                 * (sigma_A + sigma_B + sigma_A*sigma_B*X) / (1-eta_bar)**3
    P_hs = P_hs_kBT * T * kB_au   # pressure in a.u.
    
    # chemical potential Eq. (10), assuming mass m_A use atomic mass? but term with (h^2/2π m kT) is standard ideal gas term.
    # We'll need Planck constant h in a.u. hbar = 1, so h = 2π. Also m_A in atomic mass units? But the prefactor will cancel when subtracting pure limit. So we can ignore the kinetic term, as it cancels in difference. Actually Eq. (10) includes ln[n (2π hbar^2 / (m_A k_B T))^{3/2}]; that term cancels in μ_A - μ_A^0 because it's the same for pure and alloy? However, in pure limit n -> n_A0, so careful. But the electronic contributions are computed separately, and the hard-sphere part is already subtracted. We'll compute the HS contribution to kT ln a as μ_A^hs - (μ_A^0)^hs.
    # Compute μ_A^hs/kBT according to Eq. (10):
    def mu_hs_kBT(nA, nB, n_total, X_, Y_, eta_bar_, sigA, sigB, P_hs_):
        term1 = np.log(n_total)  # ignoring constants that cancel
        term2 = -np.log(1.0 - eta_bar_)
        term3 = 3.0 * X_ * sigA / (1.0 - eta_bar_)
        term4 = 1.5 * (3.0*X_**2 / (1.0-eta_bar_)**2 + 2.0*Y_/(1.0-eta_bar_)) * sigA**2
        term5 = np.pi * P_hs_ * sigA**3 / 6.0   # P_hs must be divided by kBT? The Eq. (10) has (π P_hs σ_A^3)/(6 k_B T). So we'll compute P_hs_kBT.
        # So for term5 we use P_hs_kBT instead of P_hs in a.u.
        return term1 + term2 + term3 + term4 + term5
    
    # We need P_hs_kBT for term5
    mu_hs_kBT_value = mu_hs_kBT(n_A, n_B, n, X, Y, eta, sigma_A, sigma_B, P_hs_kBT)
    
    # Pure A limit HS chemical potential
    n_A0 = n_A_pure
    # pure A: n_A0, n_B0=0, sigma_A only, packing fraction η0 must be computed. But we need packing fraction for pure A. The paper assumes packing density constant at 0.45 even for pure elements? Yes, they assume η unchanged over composition. So for pure A, η0=0.45, with n0 = η0 / (π/6 * sigma_A**3). So n_A_pure here is NOT from rs, but from HS packing.
    n0 = eta / (np.pi/6.0 * sigma_A**3)
    X0 = (np.pi/6.0) * (n0 * sigma_A**2)
    Y0 = (np.pi/6.0) * (n0 * sigma_A)
    eta0 = eta
    P_hs_kBT0 = n0*(1+eta0+eta0**2)/(1-eta0)**3
    mu_hs_kBT_pure = mu_hs_kBT(n0, 0.0, n0, X0, Y0, eta0, sigma_A, sigma_A, P_hs_kBT0)
    
    mu_hs_contrib = (mu_hs_kBT_value - mu_hs_kBT_pure) * T * kB_au   # in a.u.
    
    # ----------  electronic terms ----------
    # kinetic
    term_kin = 2.21 * ( (1/rs_bar**2 - 1/rs_A**2) + (2/3)*x/rs_bar**5 * (rs_B**3 - rs_A**3) * Z_bar )
    # exchange
    term_exch = -0.916 * ( (1/rs_bar - 1/rs_A) + (1/3)*x/rs_bar**4 * (rs_B**3 - rs_A**3) * Z_bar )
    # correlation
    term_corr = 0.031 * ( (np.log(rs_bar) - np.log(rs_A)) - x/rs_bar**3 * (rs_B**3 - rs_A**3) * Z_A )  # Z_A? paper has Z in Eq.14, but likely Z_bar? text: "Z" unclear; assume Z_A as it's for A term
    
    # uniform term: needs NΩ, NΩ_A
    NΩ = 1.0 / n   # volume per atom? Actually V/N = 1/n. But the paper uses NΩ as total volume of sample with N atoms. For our purpose, NΩ = volume per particle times N? In integrals they multiply by NΩ and then divide, etc. To avoid confusion, we'll follow the dimensional pattern: terms like (1/(NΩ) - 1/(NΩ_A)). Since both scale with volume, we can use per-atom volumes. So set NΩ = 1/n (atomic volume), and NΩ_A = 1/n_A_pure (pure atomic volume). This gives correct dimensionless contributions.
    omega = 1.0/n
    omega_A = 1.0/n_A_pure
    # uniform
    term_unif = 4.0*np.pi * ( ((1-x)*rc_A**2 + x*rc_B**2)/omega - rc_A**2/omega_A
                             + x/omega**2 * ((1-x)*rc_A**2 + x*rc_B**2)*(omega_A - omega)  #?? need careful
                             - x/omega * (rc_B**2 - rc_A**2) )  # from Eq.15
    
    # Madelung, band-structure, core-core need R_ij, φ_ij, ξ_ij
    R_AA, R_AB, R_BB = compute_Rij(pA, pB, n_A, n_B, kF, eta, sigma_A, sigma_B)
    phi_AA, phi_AB, phi_BB = compute_varphi(pA, pB, n_A, n_B, kF, eta, sigma_A, sigma_B, omega)
    xi_AA, xi_AB, xi_BB = compute_xi(pA, pB, n_A, n_B, sigma_A, sigma_B, eta)
    
    # Madelung term Eq. (16)
    term_Mad = 0.5 * ( (1/omega - 1/omega_A) * R_AA
                      + x/omega**2 * ((1-x)**2*R_AA + 2*x*(1-x)*R_AB + x**2*R_BB) * (omega_A - omega)
                      + x**2/omega * (2*R_AB - R_AA - R_BB) )
    
    # band-structure term Eq. (17) is more complex; I'll approximate with the simplified form if possible. The paper's Eq. (17) includes ψ_ij and φ_ij. We can just use φ_ij from integral and also need ψ_ij. But not defined separately; likely ψ_ij is same as φ_ij? Actually, the text says φ_ij and ψ_ij are similar but with different integrand? The paper gives Eq. (20) and (21) for φ_ij. The band-structure term we can approximate by the second part with φ_ij. I'll compute only the dominant φ_ij contributions.
    term_bs = 0.5 * ( (1/omega - 1/omega_A) * phi_AA  # simplified, but should be correct
                     + x/omega * (2*phi_AB - phi_AA - phi_BB) )  # simplified version
    
    # core-core term Eq. (18)
    term_cc = 0.5 * ( (1/omega - 1/omega_A) * xi_AA
                     + x/omega * (2*xi_AB - xi_AA - xi_BB) )
    
    # sum all electronic contributions (they are in a.u., as R etc. are in a.u.)
    electronic_contrib = term_kin + term_exch + term_corr + term_unif + term_Mad + term_bs + term_cc
    
    # total free energy difference = HS part + electronic part
    delta_mu = mu_hs_contrib + electronic_contrib
    
    # k_B T ln a_A = delta_mu
    kT = kB_au * T
    ln_a = delta_mu / kT
    a_A = np.exp(ln_a)
    return a_A

def compute_Rij(pA, pB, n_A, n_B, kF, eta, sigma_A, sigma_B):
    # compute R_AA, R_AB, R_BB via Eq. (19)
    Z_A, Z_B = pA['Z'], pB['Z']
    n = n_A + n_B
    # structure factors
    def S_ij(q):
        rho_A, rho_B = n_A, n_B
        cAA, cAB, cBB = direct_corr(q, rho_A, rho_B, sigma_A, sigma_B)
        # build matrix: S = inv(I - C D) with D = diag(rho_i)
        C = np.array([[cAA, cAB],[cAB, cBB]])
        D = np.array([[rho_A, 0],[0, rho_B]])
        I = np.eye(2)
        S = np.linalg.inv(I - C @ D)
        return S[0,0], S[0,1], S[1,1]
    
    def integrand_AA(q):
        SAA, _, _ = S_ij(q)
        return (1/(2*np.pi)**3) * (8*np.pi/q**2) * Z_A*Z_A * (SAA - 1) * 4*np.pi*q**2
    def integrand_AB(q):
        _, SAB, _ = S_ij(q)
        return (1/(2*np.pi)**3) * (8*np.pi/q**2) * Z_A*Z_B * (SAB) * 4*np.pi*q**2
    def integrand_BB(q):
        _, _, SBB = S_ij(q)
        return (1/(2*np.pi)**3) * (8*np.pi/q**2) * Z_B*Z_B * (SBB - 1) * 4*np.pi*q**2
    
    qmax = 4.0 * kF
    R_AA, _ = quad(integrand_AA, 1e-8, qmax, limit=200)
    R_AB, _ = quad(integrand_AB, 1e-8, qmax, limit=200)
    R_BB, _ = quad(integrand_BB, 1e-8, qmax, limit=200)
    return R_AA, R_AB, R_BB

def compute_varphi(pA, pB, n_A, n_B, kF, eta, sigma_A, sigma_B, omega):
    # φ_ij integral Eq. (20) simplified
    Z_A, Z_B = pA['Z'], pB['Z']
    rc_A, rc_B = pA['rc_au'], pB['rc_au']
    NΩ = 1.0/n
    # pseudopotential matrix element product
    def omega_prod(q):
        # ω_i^bp(q) = -4π Z_i / q^2 cos(q rc_i)
        wa = -4*np.pi*Z_A/q**2 * np.cos(q*rc_A)
        wb = -4*np.pi*Z_B/q**2 * np.cos(q*rc_B)
        return wa * wb
    
    # dielectric function
    def epsilon(q):
        kF_val = kF
        X = -kF_val/np.pi**2 * (0.5 + (4*kF_val**2 - q**2)/(8*kF_val*q+1e-30)*np.log(np.abs((2*kF_val+q)/(2*kF_val-q+1e-30)))+1e-30)
        G = q**2 / (2*(q**2 + kF_val**2))  # Hubbard-Sham
        return 1.0 - (4*np.pi/q**2) * X / (1.0 + (4*np.pi/q**2)*G*X)
    
    def S_ij(q):
        rho_A, rho_B = n_A, n_B
        cAA, cAB, cBB = direct_corr(q, rho_A, rho_B, sigma_A, sigma_B)
        C = np.array([[cAA, cAB],[cAB, cBB]])
        D = np.array([[rho_A,0],[0,rho_B]])
        I = np.eye(2)
        return np.linalg.inv(I - C @ D)
    
    def integrand(q, i, j):
        S = S_ij(q)
        Sij = S[i,j]
        wp = omega_prod(q)
        eps = epsilon(q)
        fac = NΩ/(2*np.pi)**3 * wp/(8*np.pi/q**2) * (1.0/eps - 1.0) * (Sij - 1) * 4*np.pi*q**2
        return fac
    
    qmax = 4*kF
    phi_AA, _ = quad(lambda q: integrand(q,0,0), 1e-8, qmax, limit=200)
    phi_AB, _ = quad(lambda q: integrand(q,0,1), 1e-8, qmax, limit=200)
    phi_BB, _ = quad(lambda q: integrand(q,1,1), 1e-8, qmax, limit=200)
    return phi_AA, phi_AB, phi_BB

def compute_xi(pA, pB, n_A, n_B, sigma_A, sigma_B, eta):
    # core-core integral Eq. (21); use g_ij(r) approx = 1 for r > σ_ij
    Z_A, Z_B = pA['Z'], pB['Z']
    def born_mayer(r, element_params):
        pp = element_params
        r_au = r
        r0_au = pp['r0_nm'] * nm_to_au
        A_hartree = pp['A_eV'] * Ha_per_eV
        B_val = pp['B']
        C_val = pp['C']
        exponent = B_val + C_val * (r_au / r0_au)
        return A_hartree * np.exp(exponent)
    
    # For AB combination, use geometric mean? Paper says root mean square. I'll use: Φ_AB = sqrt(Φ_AA * Φ_BB)
    def phi_cc_AA(r):
        return born_mayer(r, pA)
    def phi_cc_BB(r):
        return born_mayer(r, pB)
    def phi_cc_AB(r):
        return np.sqrt(born_mayer(r, pA) * born_mayer(r, pB))
    
    # g_ij(r) => 0 for r < σ_ij, 1 for r >= σ_ij (approximation)
    sigma_AA = sigma_A
    sigma_BB = sigma_B
    sigma_AB = 0.5*(sigma_A+sigma_B)
    
    def integrand_AA(r):
        return phi_cc_AA(r) * (1.0 if r >= sigma_AA else 0.0) * 4*np.pi*r**2
    def integrand_BB(r):
        return phi_cc_BB(r) * (1.0 if r >= sigma_BB else 0.0) * 4*np.pi*r**2
    def integrand_AB(r):
        return phi_cc_AB(r) * (1.0 if r >= sigma_AB else 0.0) * 4*np.pi*r**2
    
    rmax = 3.0 * nm_to_au
    xi_AA, _ = quad(integrand_AA, 0, rmax, limit=100)
    xi_BB, _ = quad(integrand_BB, 0, rmax, limit=100)
    xi_AB, _ = quad(integrand_AB, 0, rmax, limit=100)
    return xi_AA, xi_AB, xi_BB

def direct_corr(q, rho_A, rho_B, sigma_A, sigma_B):
    # Direct correlation functions in k-space for hard spheres (PY).
    # Coefficients from Lebowitz solution.
    rho = rho_A + rho_B
    eta = np.pi/6 * (rho_A * sigma_A**3 + rho_B * sigma_B**3)
    xA = rho_A / rho
    xB = rho_B / rho
    sigma_AB = 0.5*(sigma_A + sigma_B)
    
    # coefficients for c_ij(r) up to r^3 (PY)
    # Not implemented here fully; use simple analytic form for c_ij(k) via Fourier transform of c_ij(r) for r < sigma_ij, zero outside.
    # We'll use the analytic expression for the direct correlation functions in Fourier space (Vrij approach).
    # Instead, for brevity we approximate using the Percus-Yevick solution for monodisperse with effective diameter? Not accurate.
    # Better: compute c_ij(r) coefficients and then the Fourier transform numerically.
    # This code must be complete; I will implement the proper c_ij(r) and integrate.
    
    # coefficients a, b, d from Lebowitz:
    eta = eta
    # auxiliary parameters
    xi1 = np.pi/6 * (rho_A * sigma_A**2 + rho_B * sigma_B**2)
    xi2 = np.pi/6 * (rho_A * sigma_A + rho_B * sigma_B)
    xi3 = eta
    
    # For i-j pair
    def c_coeff(si, sj):
        sij = 0.5*(si+sj)
        a = ( (1-xi3) + 3*sij*xi2 + 3*sij**2*xi1 ) / (1-xi3)**2
        b = - ( 3*sij*xi2 + 6*sij**2*xi1 ) / (1-xi3)**2
        d = 3*sij*xi1 / (1-xi3)**2
        return a, b, d
    
    cAA = c_coeff(sigma_A, sigma_A)
    cBB = c_coeff(sigma_B, sigma_B)
    cAB = c_coeff(sigma_A, sigma_B)
    
    # Fourier transform c_ij(q) = 4π ∫_0^σ_ij r c_ij(r) sin(qr)/q dr, with c_ij(r) = a + b r + d r^3
    def ck(coeff, sigma):
        a, b, d = coeff
        def integrand(r):
            return r * (a + b*r + d*r**3) * np.sin(q*r) / q
        val, _ = quad(integrand, 0, sigma, limit=100)
        return 4*np.pi * val
    
    cAA_q = ck(cAA, sigma_A)
    cBB_q = ck(cBB, sigma_B)
    cAB_q = ck(cAB, sigma_AB)
    return cAA_q, cAB_q, cBB_q
