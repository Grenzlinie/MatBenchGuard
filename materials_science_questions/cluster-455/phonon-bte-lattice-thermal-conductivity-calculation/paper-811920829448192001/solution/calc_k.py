import numpy as np
import json

# Physical constants
hbar = 1.054571817e-34
kB = 1.380649e-23

# -------------------------------------------------------------------------
# Material parameters for AlN (ΓA and ΓK) and Ge
# -------------------------------------------------------------------------

def material_aln_GA():
    vL = 10500.0      # m/s
    vT = 6300.0
    a = 3.11e-10
    V_atom = 1.0425e-29    # volume per atom (wurtzite, 4 atoms per cell)
    M = 20.5 * 1.660539e-27   # average atomic mass
    gammaL = 1.2
    gammaT = 0.8
    vO = 4000.0        # average optical phonon velocity (approx)
    d = 0.002          # effective diameter (2 mm)
    # Debye frequencies from V_atom and velocities
    n = 1.0 / V_atom
    pref = (6 * np.pi**2 * n)**(1.0/3.0)
    omegaD_L = pref * vL
    omegaD_T = pref * vT
    thetaD_L = hbar * omegaD_L / kB
    thetaD_T = hbar * omegaD_T / kB
    # frequency window for optical decay (120 cm^-1 to Debye)
    c_cm = 2.99792458e10   # cm/s
    omega_low = 2.0 * np.pi * c_cm * 120.0
    omega_high = omegaD_L   # use Debye frequency as upper bound
    return {
        'vL': vL, 'vT': vT, 'a3': a**3, 'V_atom': V_atom, 'M': M,
        'gammaL': gammaL, 'gammaT': gammaT, 'vO': vO, 'd': d,
        'thetaD_L': thetaD_L, 'thetaD_T': thetaD_T,
        'omega_low': omega_low, 'omega_high': omega_high
    }

def material_aln_GK():
    vL = 10200.0
    vT = 6100.0
    a = 3.11e-10
    V_atom = 1.0425e-29
    M = 20.5 * 1.660539e-27
    gammaL = 1.2
    gammaT = 0.8
    vO = 4000.0
    d = 0.002
    n = 1.0 / V_atom
    pref = (6 * np.pi**2 * n)**(1.0/3.0)
    omegaD_L = pref * vL
    omegaD_T = pref * vT
    thetaD_L = hbar * omegaD_L / kB
    thetaD_T = hbar * omegaD_T / kB
    c_cm = 2.99792458e10
    omega_low = 2.0 * np.pi * c_cm * 170.0   # 170 cm^-1 for ΓK
    omega_high = omegaD_L
    return {
        'vL': vL, 'vT': vT, 'a3': a**3, 'V_atom': V_atom, 'M': M,
        'gammaL': gammaL, 'gammaT': gammaT, 'vO': vO, 'd': d,
        'thetaD_L': thetaD_L, 'thetaD_T': thetaD_T,
        'omega_low': omega_low, 'omega_high': omega_high
    }

def material_ge():
    # Ge (diamond structure)
    a_Ge = 5.66e-10
    V_atom = a_Ge**3 / 8.0   # volume per atom
    vL = 5000.0
    vT = 3000.0
    M = 72.6 * 1.660539e-27
    gammaL = 1.5
    gammaT = 0.8
    vO = 3500.0
    d = 0.005          # 0.5 cm
    n = 1.0 / V_atom
    pref = (6 * np.pi**2 * n)**(1.0/3.0)
    omegaD_L = pref * vL
    omegaD_T = pref * vT
    thetaD_L = hbar * omegaD_L / kB
    thetaD_T = hbar * omegaD_T / kB
    # For Ge, optical decay window: use lower bound 100 cm^{-1} (reasonable)
    c_cm = 2.99792458e10
    omega_low = 2.0 * np.pi * c_cm * 100.0
    omega_high = omegaD_L
    return {
        'vL': vL, 'vT': vT, 'a3': a_Ge**3, 'V_atom': V_atom, 'M': M,
        'gammaL': gammaL, 'gammaT': gammaT, 'vO': vO, 'd': d,
        'thetaD_L': thetaD_L, 'thetaD_T': thetaD_T,
        'omega_low': omega_low, 'omega_high': omega_high
    }

# -------------------------------------------------------------------------
# Scattering rates as functions of x, T, and material
# -------------------------------------------------------------------------
def tau_inv_total(x, T, mat, Gamma, B_L, B_T, branch):
    """
    branch = 'L' or 'T'
    Returns total inverse relaxation time (scattering rate).
    """
    if branch == 'L':
        v = mat['vL']
        thetaD = mat['thetaD_L']
        gamma = mat['gammaL']
        B_fit = B_L
        # normal scattering prefactor
        B_N = (kB**5 * gamma**2 * mat['V_atom']) / (mat['M'] * hbar**4 * v**5)
    else:
        v = mat['vT']
        thetaD = mat['thetaD_T']
        gamma = mat['gammaT']
        B_fit = B_T
        B_N = (kB**5 * gamma**2 * mat['V_atom']) / (mat['M'] * hbar**4 * v**5)

    # boundary
    inv_B = v / mat['d']
    # point defect
    B_I = (mat['V_atom'] * kB**4 * Gamma) / (4 * np.pi * hbar**4 * v**3)
    inv_I = B_I * x**4 * T**4
    # normal three-phonon
    if branch == 'L':
        inv_N = B_N * x**2 * T**5
    else:
        inv_N = B_N * x * T**5
    # umklapp
    B_U = (kB**2 * gamma**2) / (mat['M'] * hbar * v**2 * thetaD)
    inv_U = B_U * x**2 * T**3 * np.exp(-thetaD / (3.0 * T))
    # anharmonic optical decay rate (Eq. 5)
    inv_anh = (5.0 * mat['a3'] * kB**5 * gamma**2) / (8.0 * np.pi * mat['M'] * hbar**4 * mat['vO']**5) \
              * x**5 * T**5 * (1.0 / np.tanh(x / 4.0))   # coth(z) = 1/tanh(z)
    # generation term (Eq. 6)
    inv_G = B_fit * np.sqrt(inv_anh) * np.sqrt(x * T) * Gamma

    # apply generation only within the allowed frequency window
    omega = x * kB * T / hbar
    if not (mat['omega_low'] <= omega <= mat['omega_high']):
        inv_G = 0.0

    total_inv = inv_B + inv_I + inv_N + inv_U - inv_G
    if total_inv <= 0:
        total_inv = 1e-30
    return total_inv

# -------------------------------------------------------------------------
# Thermal conductivity integration
# -------------------------------------------------------------------------
def compute_k(T, mat, Gamma, B_L, B_T):
    """
    Compute k in W/(m K) at a single temperature T.
    """
    k_total = 0.0
    for branch in ['L', 'T']:
        if branch == 'L':
            v = mat['vL']
            thetaD = mat['thetaD_L']
        else:
            v = mat['vT']
            thetaD = mat['thetaD_T']
        xD = thetaD / T
        xmax = min(xD, 30.0)   # avoid overflow
        if xmax <= 0:
            continue
        # integrand
        xs = np.logspace(-3, np.log10(xmax), 200)  # log-spaced for better low-x resolution
        integrand = np.zeros_like(xs)
        for i, x in enumerate(xs):
            inv_tot = tau_inv_total(x, T, mat, Gamma, B_L, B_T, branch)
            tau_eff = 1.0 / inv_tot
            fx = tau_eff * x**4 * np.exp(x) / (np.exp(x) - 1.0)**2
            integrand[i] = fx
        integral = np.trapz(integrand, xs)
        prefactor = (kB**4 * T**3) / (2.0 * np.pi**2 * v**3 * hbar**3)
        k_total += prefactor * integral
    return k_total

# -------------------------------------------------------------------------
# Main: produce thermal_conductivity.json
# -------------------------------------------------------------------------
T_values = np.logspace(0, 3, 100)   # 1 to 1000 K, 100 points

# Fitting parameters (hardcoded for oracle)
B_L_aln = 0.08
B_T_aln = 0.08
B_L_ge = 0.05
B_T_ge = 0.05

# Define cases
cases = {
    'AlN_GammaA_Gamma0.03': (material_aln_GA(), 0.03, B_L_aln, B_T_aln),
    'AlN_GammaA_Gamma0.13': (material_aln_GA(), 0.13, B_L_aln, B_T_aln),
    'AlN_GammaA_Gamma0.42': (material_aln_GA(), 0.42, B_L_aln, B_T_aln),
    'AlN_GammaK_Gamma0.03': (material_aln_GK(), 0.03, B_L_aln, B_T_aln),
    'AlN_GammaK_Gamma0.13': (material_aln_GK(), 0.13, B_L_aln, B_T_aln),
    'AlN_GammaK_Gamma0.42': (material_aln_GK(), 0.42, B_L_aln, B_T_aln),
    'Ge_isotropic':        (material_ge(), 2.0e-4, B_L_ge, B_T_ge)
}

result = {}
for key, (mat, Gamma, BL, BT) in cases.items():
    print(f'Computing {key} ...')
    k_vals = []
    for T in T_values:
        k = compute_k(T, mat, Gamma, BL, BT)
        k_vals.append({'T': round(T, 2), 'k': round(k, 6)})
    result[key] = k_vals

with open('/app/outputs/thermal_conductivity.json', 'w') as f:
    json.dump(result, f, indent=2)

print('thermal_conductivity.json written successfully.')
