import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import csv
import math

# Constants (SI)
e = 1.602176634e-19
hbar = 1.054571817e-34
kB = 1.380649e-23
m0 = 9.1093837e-31
kBeV = kB / e   # eV/K
eps0 = 8.8541878128e-12

# Material parameters for n-type Bi2Te2.7Se0.3 (x=0.3) at 500 K
T = 500.0
x = 0.3

# Band gap (eV)
Eg = 0.16*(1-x) + 0.3*x - 9.5e-5*(T-300)   # ~0.183 eV

# Offsets (eV)
dE_cb2 = 0.23   # 2nd conduction band offset above 1st CB
dE_vb2 = 0.27   # 2nd valence band offset below 1st VB (in electron energy, so it is deeper)

# Effective masses (single-valley, in m0)
m_c1 = 0.20 + 0.07*x*(1-x)   # 0.2147
m_c2 = 0.21 + 0.07*x*(1-x)   # 0.2247
m_v1 = 0.36 + 0.16*x*(1-x)   # 0.3936
m_v2 = 0.36 + 0.16*x*(1-x)   # 0.3936

# Nonparabolicities (eV^-1)
alpha_c1 = 0.0
alpha_c2 = 1.0
alpha_v1 = 0.6
alpha_v2 = 2.0

# Degeneracies
d_c = 6
d_v = 6

# Deformation potentials (eV)
Da_e = 16.0*(1-x) + 26.0*x   # 19.0
Da_h = 21.0*(1-x) + 30.0*x   # 23.7

# Elastic constant (N/m^2)
C_l = 7.1e10

# Compensation ratio
r_c = 1.0

# Static dielectric constant (relative)
eps_r = 100.0

# Lattice thermal conductivity (W/mK)
k_lat = 0.5

# Barrier parameters
E_B_eV = 10.0 * kBeV * T   # eV
w_B = 20e-9   # m

# Convert to SI
E_B = E_B_eV * e
Da_e_SI = Da_e * e
Da_h_SI = Da_h * e

# ---------- Helper functions ----------

def fermi(E, EF, T):
    """Fermi-Dirac distribution, E and EF in J"""
    if np.isinf(E):
        return 0.0
    arg = (E - EF) / (kB * T)
    # clip to avoid overflow
    if arg > 500:
        return 1e-300  # approx 0
    if arg < -500:
        return 1.0
    return 1.0 / (1.0 + np.exp(arg))

def dfermi_dE(E, EF, T):
    """-df/dE (in J^-1)"""
    f = fermi(E, EF, T)
    return f * (1.0 - f) / (kB * T)

def dos_single(E, m_star, alpha):
    """Single-valley DOS per J per m^3. E in J, alpha in J^-1, m_star in kg."""
    if E < 0:
        return 0.0
    E_J = E
    alpha_J = alpha / e   # convert eV^-1 to J^-1
    term = E_J + alpha_J * E_J**2
    if term < 0:
        return 0.0
    factor = np.sqrt(2.0) / (np.pi**2 * hbar**3)
    return factor * m_star**1.5 * np.sqrt(term) * (1.0 + 2.0 * alpha_J * E_J)

def v2_single(E, m_star, alpha):
    """Squared velocity (m^2/s^2). E in J, alpha in J^-1."""
    if E <= 0:
        return 0.0
    alpha_J = alpha / e
    num = 2.0 * E * (1.0 + alpha_J * E)
    den = 3.0 * m_star * (1.0 + 2.0 * alpha_J * E)**2
    return num / den

def tau_AC(E, m_star, alpha, Da, T):
    """Acoustic phonon scattering time (s). E in J, Da in J."""
    alpha_J = alpha / e
    if E <= 0:
        return 1e-12  # large but finite
    term = E + alpha_J * E**2
    if term <= 0:
        return 1e-12
    A = alpha_J * E * (1.0 - 1.0) / (1.0 + 2.0 * alpha_J * E)  # K=1
    B = 8.0 * alpha_J * E * (1.0 + alpha_J * E) / (3.0 * (1.0 + 2.0 * alpha_J * E)**2)
    denom = np.sqrt(2.0) * m_star**1.5 * kB * T * Da**2 * (1.0 + 2.0 * alpha_J * E) * ((1.0 - A)**2 - B)
    num = np.pi * hbar**4 * C_l / np.sqrt(term)
    return num / denom

def screening_length_rs(EF, T, bands, carrier_type='electron'):
    """Compute inverse screening length squared for electrons or holes.
    Returns 1/r_s^2 (J^-? actually m^-2)."""
    # Integrate (-df/dE) * rho_DOS dE.
    # Use same definition: for electrons, integrate over E from 0 to inf.
    # For holes, integrate over E (hole energy) from 0 to inf.
    integrand = lambda E: sum(dfermi_dE(E, EF - offset * e, T) * dos_single(E, m * m0, alpha) * d
                               for (offset, m, alpha, d) in bands)
    res, _ = quad(integrand, 0, 10*e)  # upper limit sufficient
    if res <= 0:
        return 1e-12
    return (e**2 / (eps_r * eps0)) * res

def tau_II(E, m_star, alpha, N_imp, rs2_inv):
    """Ionized impurity scattering time (s). N_imp in m^-3, rs2_inv in m^-2."""
    if E <= 0:
        return 1e-12
    alpha_J = alpha / e
    term = E + alpha_J * E**2
    if term <= 0:
        return 1e-12
    # screening parameter delta0 = 1 / (4*m*rs^2 * E) ? Actually delta0 = hbar^2 / (8 m_d* rs^2 E)
    # In the paper: delta0 = hbar^2 / (8 m_d* r0^2 E)
    # We have 1/r0^2 = rs2_inv.
    if rs2_inv <= 0:
        return 1e-12
    r0_sq = 1.0 / rs2_inv
    delta0 = hbar**2 / (8.0 * m_star * r0_sq * E)
    # tau formula: (16 sqrt(2 m_star) pi eps^2 (E+alpha E^2)^(3/2)) / (N_II e^4 (1+2alpha E)) * [ln(1+delta0) - delta0/(1+delta0)]^{-1}
    eps = eps_r * eps0
    num = 16.0 * np.sqrt(2.0 * m_star) * np.pi * eps**2 * term**1.5
    den = N_imp * e**4 * (1.0 + 2.0 * alpha_J * E)
    factor = np.log(1.0 + delta0) - delta0 / (1.0 + delta0)
    if factor <= 0:
        return 1e-12
    return num / den / factor

def transmission_WKB(E, E_barrier, w, m_star):
    """WKB barrier transmission. E and E_barrier in J."""
    if E <= 0:
        return 0.0
    if E < E_barrier:
        delta = E_barrier - E
        kappa = np.sqrt(2.0 * m_star * delta) / hbar
        den = E_barrier**2 * (np.sinh(2.0 * w * kappa))**2 + 4.0 * E * delta
        if den == 0:
            return 0.0
        return 4.0 * E * delta / den
    else:
        delta = E - E_barrier
        k = np.sqrt(2.0 * m_star * delta) / hbar
        den = E_barrier**2 * (np.sin(2.0 * w * k))**2 + 4.0 * E * delta
        if den == 0:
            return 1.0  # limit
        return min(1.0, 4.0 * E * delta / den)

# Define band lists
# Conduction bands (electrons)
cb_bands = [
    {'offset_eV': 0.0, 'm': m_c1*m0, 'alpha': alpha_c1, 'd': d_c, 'Da': Da_e_SI},
    {'offset_eV': dE_cb2, 'm': m_c2*m0, 'alpha': alpha_c2, 'd': d_c, 'Da': Da_e_SI}
]
# Valence bands (holes)
vb_bands = [
    {'offset_eV': 0.0, 'm': m_v1*m0, 'alpha': alpha_v1, 'd': d_v, 'Da': Da_h_SI},
    {'offset_eV': dE_vb2, 'm': m_v2*m0, 'alpha': alpha_v2, 'd': d_v, 'Da': Da_h_SI}
]

def calc_carrier_concentration(EF_eV, bands, carrier_type='electron', T=T):
    """Compute electron or hole concentration (m^-3). EF_eV is Fermi level relative to CB edge."""
    n = 0.0
    for band in bands:
        offset = band['offset_eV']
        if carrier_type == 'electron':
            EF_band = EF_eV - offset
        else:  # holes
            # For holes, EF_band = EF_eV + Eg + offset_in_vb?
            # offset_eV in this context for VB is the additional shift below first VB edge (which is at -Eg)
            # So band edge energy relative to CB edge: E_v = -Eg - offset_eV
            # Then EF_band_relative = EF_eV - E_v = EF_eV + Eg + offset_eV
            EF_band = EF_eV + Eg + offset
        EF_band_J = EF_band * e
        m = band['m']
        alpha = band['alpha']
        d = band['d']
        # integrand: rho_single(E) * f(E) with E in J
        integrand = lambda E: d * dos_single(E, m, alpha) * fermi(E, EF_band_J, T)
        res, _ = quad(integrand, 0, 2.0*e)  # up to ~2 eV
        n += res
    return n

def calc_transport(EF_eV, barrier=False):
    """Compute total sigma, S, kappa_elec for given EF_eV (relative to CB edge) and barrier flag.
    Returns sigma (S/m), S (V/K), kappa_elec (W/mK), kappa_bi (W/mK)."""
    sigma_e = 0.0
    Se_sigma = 0.0
    kappa_e_unipolar = 0.0
    sigma_h = 0.0
    Sh_sigma = 0.0
    kappa_h_unipolar = 0.0
    
    # Electrons
    for band in cb_bands:
        offset = band['offset_eV']
        EF_band = EF_eV - offset
        EF_band_J = EF_band * e
        m = band['m']
        alpha = band['alpha']
        d = band['d']
        Da = band['Da']
        
        def sigma_d(E):
            if E <= 0:
                return 0.0
            tau = tau_AC(E, m, alpha, Da, T)
            # Add II scattering
            N_imp = calc_carrier_concentration(EF_eV, cb_bands, 'electron', T)  # electron conc
            rs2 = screening_length_rs(EF_band, T, [(band['offset_eV'], m/m0, alpha, d)])
            if rs2 > 0:
                tau_ii = tau_II(E, m, alpha, N_imp, rs2)
                tau = 1.0 / (1.0/tau + 1.0/tau_ii)
            return e**2 * tau * v2_single(E, m, alpha) * d * dos_single(E, m, alpha) * dfermi_dE(E, EF_band_J, T)
        
        # integrate sigma
        s, _ = quad(lambda E: sigma_d(E), 0, 2*e)
        sigma_e += s
        # integrate S * sigma
        s1, _ = quad(lambda E: sigma_d(E) * (E - EF_band_J), 0, 2*e)
        Se_sigma += s1
        # kappa_elec term
        s2, _ = quad(lambda E: sigma_d(E) * (E - EF_band_J)**2, 0, 2*e)
        kappa_e_unipolar += s2
    
    if sigma_e > 0:
        Se = Se_sigma / (sigma_e * T)  # V/K, note e factor? Actually S = (1/(-e T)) * integral, so Se negative. We'll compute with proper sign.
        # The paper's formula (5) uses q = -e for electrons, so Se = (1/(-e T)) * integral/(sigma)  -> negative.
        # But we can compute total S using the proper weighted formula later. We'll compute partial S with correct sign now.
        Se = -Se_sigma / (e * T * sigma_e)  # V/K
        kappa_e_unipolar = (kappa_e_unipolar / (e**2 * T)) - (Se**2 * sigma_e * T)  # Eq (6) contributes
    else:
        Se = 0.0
        kappa_e_unipolar = 0.0
    
    # Holes
    for band in vb_bands:
        offset = band['offset_eV']
        EF_band = EF_eV + Eg + offset
        EF_band_J = EF_band * e
        m = band['m']
        alpha = band['alpha']
        d = band['d']
        Da = band['Da']
        
        # transmission factor
        if barrier:
            def T_b(E):
                return transmission_WKB(E, E_B, w_B, m)
        else:
            T_b = lambda E: 1.0
        
        def sigma_d(E):
            if E <= 0:
                return 0.0
            tau = tau_AC(E, m, alpha, Da, T)
            # II scattering for holes
            N_imp = calc_carrier_concentration(EF_eV, vb_bands, 'hole', T)
            rs2 = screening_length_rs(EF_band, T, [(band['offset_eV'], m/m0, alpha, d)])
            if rs2 > 0:
                tau_ii = tau_II(E, m, alpha, N_imp, rs2)
                tau = 1.0 / (1.0/tau + 1.0/tau_ii)
            return e**2 * tau * v2_single(E, m, alpha) * d * dos_single(E, m, alpha) * dfermi_dE(E, EF_band_J, T) * T_b(E)
        
        s, _ = quad(lambda E: sigma_d(E), 0, 2*e)
        sigma_h += s
        s1, _ = quad(lambda E: sigma_d(E) * (E - EF_band_J), 0, 2*e)
        Sh_sigma += s1
        s2, _ = quad(lambda E: sigma_d(E) * (E - EF_band_J)**2, 0, 2*e)
        kappa_h_unipolar += s2
    
    if sigma_h > 0:
        Sh = Sh_sigma / (e * T * sigma_h)  # V/K (positive)
        kappa_h_unipolar = (kappa_h_unipolar / (e**2 * T)) - (Sh**2 * sigma_h * T)
    else:
        Sh = 0.0
        kappa_h_unipolar = 0.0
    
    sigma = sigma_e + sigma_h
    if sigma > 0:
        S = (sigma_e * Se + sigma_h * Sh) / sigma
    else:
        S = 0.0
    # bipolar term
    kappa_bi = 0.0
    if sigma_e > 0 and sigma_h > 0:
        kappa_bi = (sigma_e * sigma_h / (sigma_e + sigma_h)) * (Se - Sh)**2 * T
    kappa_elec = kappa_e_unipolar + kappa_h_unipolar + kappa_bi
    return sigma, S, kappa_elec, kappa_bi

def zt_at_conc(n_cm3):
    """Given electron concentration in cm^-3, compute ZT bulk and ZT barrier."""
    n_target = n_cm3 * 1e6  # m^-3
    # Solve for EF (eV) relative to CB edge
    def f(EF):
        n_calc = calc_carrier_concentration(EF, cb_bands, 'electron', T)
        return n_calc - n_target
    # bracket
    EF_low = -0.5  # eV
    EF_high = 1.0  # eV
    try:
        EF_sol = brentq(f, EF_low, EF_high, xtol=1e-6)
    except:
        return 0.0, 0.0
    sigma_b, S_b, k_elec_b, _ = calc_transport(EF_sol, barrier=False)
    sigma_bar, S_bar, k_elec_bar, _ = calc_transport(EF_sol, barrier=True)
    zT_bulk = (S_b**2 * sigma_b * T) / (k_elec_b + k_lat) if sigma_b > 0 else 0.0
    zT_barrier = (S_bar**2 * sigma_bar * T) / (k_elec_bar + k_lat) if sigma_bar > 0 else 0.0
    return zT_bulk, zT_barrier

# Generate concentration array
n_vals = np.logspace(18, 21, 50)  # 1e18 to 1e21 cm-3
rows = []
for n in n_vals:
    zb, zbar = zt_at_conc(n)
    rows.append((n, zb, zbar))

# Write CSV
with open('/app/outputs/zT_output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['electron_concentration_cm3', 'zT_bulk', 'zT_barrier'])
    for n, zb, zbar in rows:
        writer.writerow([f'{n:.6e}', f'{zb:.6f}', f'{zbar:.6f}'])
