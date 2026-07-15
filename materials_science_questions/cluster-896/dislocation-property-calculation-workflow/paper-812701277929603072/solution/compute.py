import json, math

C11 = 195.9e9   # Pa
C12 = 117.7e9
C44 = 129.3e9
a_Ang = 3.6      # Å
b_Ang = a_Ang / math.sqrt(2)
b_m = b_Ang * 1e-10
sum_DV2_Ang6 = 0.43    # Å^6
sum_DV2_SI = sum_DV2_Ang6 * (1e-10)**6

mu_111_110 = (C11 - C12 + C44) / 3.0
mu_Voigt   = (C11 - C12 + 3*C44) / 5.0
K          = (C11 + 2*C12) / 3.0
nu_Voigt   = (3*K - 2*mu_Voigt) / (2*(3*K + mu_Voigt))
CF         = mu_Voigt * (1+nu_Voigt) / (1-nu_Voigt)

Gamma_SI = (1.0/8.0) * mu_111_110 * b_m**2

pref_Eb_J = 1.22 * (CF)**(2.0/3.0) * (sum_DV2_SI * Gamma_SI * b_m)**(1.0/3.0)
delta_Eb_eV = pref_Eb_J / 1.602176634e-19

pref_tau_Pa = 1.01 * (CF)**(4.0/3.0) * (sum_DV2_SI**2 / (Gamma_SI * b_m**10))**(1.0/3.0)
tau_y0_GPa = pref_tau_Pa * 1e-9

wc_g2o3   = 1.277
tau_dim   = 0.01758

delta_Eb = delta_Eb_eV * wc_g2o3
tau_y0   = tau_y0_GPa * tau_dim   # GPa

T = 293.0
k_eVK   = 8.617333262145e-5
eps_dot = 1e-3
eps0    = 1e4
kT_eV   = k_eVK * T
exponent = (kT_eV / delta_Eb) * math.log(eps0 / eps_dot)
tau_y = tau_y0 * max(0.0, 1.0 - exponent**(2.0/3.0))   # GPa
sigma_y_GPa = 3.06 * tau_y
sigma_y_MPa = sigma_y_GPa * 1000.0
tau_y0_MPa  = tau_y0 * 1000.0

result = {
    "delta_E_b": round(delta_Eb, 6),
    "tau_y0":     round(tau_y0_MPa, 6),
    "sigma_y":    round(sigma_y_MPa, 6)
}

with open('/app/outputs/results.json', 'w') as f:
    json.dump(result, f)
