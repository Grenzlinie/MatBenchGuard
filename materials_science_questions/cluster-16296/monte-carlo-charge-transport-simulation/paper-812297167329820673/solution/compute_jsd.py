import sys, csv, math, numpy as np
from scipy.special import fresnel
from scipy.integrate import quad

# Physical constants (SI)
e = 1.602176634e-19
hbar = 1.054571817e-34
m0 = 9.10938356e-31
eV_to_J = e

# Model parameters
m = 0.3 * m0
omega0 = 0.04 * eV_to_J  # J
gamma2_J = 0.0011 * eV_to_J  # gamma^2 in J (the paper's gamma^2=1.1 meV)

def compute_icfe_k(eps_i, E_field_Vm, eps_f_arr):
    m_ = m
    hbar_ = hbar
    e_ = e
    k_i = np.sqrt(2 * m_ * eps_i) / hbar_
    k_fs = np.sqrt(np.maximum(2 * m_ * eps_f_arr, 0)) / hbar_
    # assume maximum q = k_i + k_f (both aligned with E)
    q = k_i + k_fs
    Q = e_ * E_field_Vm * q * hbar_ / m_  # units J^2
    P = eps_f_arr - eps_i - omega0
    Q_abs = np.abs(Q)
    Q_abs[Q_abs == 0] = 1e-60
    sqrt_abs_Q = np.sqrt(Q_abs)
    # Fresnel argument
    arg = P / np.sqrt(2 * Q_abs) * np.sign(Q)
    C, S = fresnel(arg)
    cos_term = np.cos(P**2 / (2 * Q_abs))
    sin_term = np.sin(P**2 / (2 * Q_abs))
    K_exact = np.sqrt(np.pi / Q_abs) * (cos_term * (1 - 2*C) + sin_term * (1 - 2*S))
    # Lorentzian approximation (eq. 15)
    term = -P - Q / (np.sqrt((2 / np.pi) * Q_abs))
    K_lorentz = 2 * np.sqrt(Q_abs / (2 * np.pi)) / ( (Q_abs / (2 * np.pi)) + term**2 )
    # Convert from 1/J to 1/eV
    K_exact_eV = K_exact * eV_to_J
    K_lorentz_eV = K_lorentz * eV_to_J
    return K_exact_eV, K_lorentz_eV

def compute_cb_k(eps_i, eps_f_arr):
    xi = eps_i / gamma2_J
    x0 = omega0 / gamma2_J
    K_vals = np.zeros_like(eps_f_arr)
    for idx, ef in enumerate(eps_f_arr):
        xfv = ef / gamma2_J
        def integrand(x):
            if x < 2 * x0:
                return 0.0
            term1 = np.sqrt(x - x0) * np.sqrt(x - 2 * x0)
            denom1 = (x - xi) ** 2 + (x - x0)
            denom2 = (x - x0 - xfv) ** 2 + (x - 2 * x0)
            return term1 / (denom1 * denom2)
        I, _ = quad(integrand, 2 * x0, np.inf, limit=200, epsabs=1e-12)
        pi_term = 0.0
        if xi > x0 and xfv < x0 and xfv > 0:
            pi_term = np.pi * np.sqrt(xfv) / ((x0 + xfv - xi) ** 2 + xfv)
        # omit delta term (point contribution)
        K_val = (2.0 / (np.pi * gamma2_J)) * (I + pi_term)
        K_vals[idx] = K_val * eV_to_J  # convert to 1/eV
    return K_vals

def main():
    output_path = sys.argv[1]
    rows = []
    # ICFE data
    fields_kVcm = [2.5, 10.0]
    E_fields_Vm = [f * 1e5 for f in fields_kVcm]
    eps_i_J = 1.0 * eV_to_J
    P_eV_range = np.linspace(-0.15, 0.1, 200)
    for E_Vm, field_kVcm in zip(E_fields_Vm, fields_kVcm):
        for P_eV in P_eV_range:
            P_J = P_eV * eV_to_J
            eps_f_J = eps_i_J + omega0 + P_J
            if eps_f_J < 0:
                continue
            K_ex, K_lo = compute_icfe_k(eps_i_J, E_Vm, np.array([eps_f_J]))
            rows.append({'type':'ICFE','field_kVcm':field_kVcm,'initial_energy_eV':'','P_eV':round(P_eV,6),'final_energy_eV':'','K':round(K_ex[0],10),'model':'exact'})
            rows.append({'type':'ICFE','field_kVcm':field_kVcm,'initial_energy_eV':'','P_eV':round(P_eV,6),'final_energy_eV':'','K':round(K_lo[0],10),'model':'lorentzian'})
    # CB data
    init_energies_eV = [0.05, 0.1, 1.0]
    final_energies_eV = np.linspace(0.01, 1.5, 100)
    for ie in init_energies_eV:
        eps_i_J = ie * eV_to_J
        eps_f_J = np.array([fe * eV_to_J for fe in final_energies_eV])
        K_cb = compute_cb_k(eps_i_J, eps_f_J)
        for fe, kv in zip(final_energies_eV, K_cb):
            rows.append({'type':'CB','field_kVcm':'','initial_energy_eV':ie,'P_eV':'','final_energy_eV':round(fe,6),'K':round(kv,10),'model':'CB'})
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['type','field_kVcm','initial_energy_eV','P_eV','final_energy_eV','K','model'])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

if __name__ == '__main__':
    main()