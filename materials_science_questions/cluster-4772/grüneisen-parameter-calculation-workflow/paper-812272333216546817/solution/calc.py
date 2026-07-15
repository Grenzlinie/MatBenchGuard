import numpy as np
from scipy.stats import linregress
import json

def compute_pressure(P_kbar, Tm):
    # Constants
    k = 0.0137
    gamma = 0.49
    gamma_p = 0.8
    Vm = 21.61
    nu_m = 276.31
    Delta_a0 = -10.47
    a1 = -0.858
    a2 = 0.344
    dTm_dT_factor = 1.967e-8  # kbar/K
    
    # dPm/dT in kbar/K at Tm
    dPm_dT_kbar = dTm_dT_factor * (Tm ** 2.96)
    
    # Temperature range
    temps = np.linspace(Tm - 3.0, Tm - 0.1, 15)
    
    # Critical volume Vc(T)
    Vc = 27.79 - 0.0316 * temps
    Vc_Tm = 27.79 - 0.0316 * Tm
    
    # Difference from melting
    dT = Tm - temps
    
    # Precompute powers
    dPm_dT_pow = dPm_dT_kbar ** (1 - gamma)  # dPm_dT^{0.51}
    dT_pow = dT ** (1 - gamma)  # dT^{0.51}
    dT_pow_neg_gamma = dT ** (-gamma)  # dT^{-0.49}
    
    # V_s
    exponent = -k / (1 - gamma) * dPm_dT_pow * dT_pow
    Vs = Vc * np.exp(exponent)
    
    # alpha_p
    alpha_p = k * dPm_dT_pow * dT_pow_neg_gamma + (-0.0316) / Vc
    
    # kappa_T
    kappa_T = k * (dPm_dT_kbar ** (-gamma)) * dT_pow_neg_gamma
    
    # C_p raw (cm³·kbar/K)
    Cp_raw = temps * Vs * alpha_p**2 / kappa_T
    # Convert to J/(mol·K) : 1 kbar·cm³ = 100 J
    Cp_J = Cp_raw * 100.0
    
    # Frequency
    freq_const = Delta_a0 + a1 * P_kbar + a2 * (P_kbar ** 2)
    nu_p = freq_const + nu_m * (Vm / Vs) ** gamma_p
    
    # Derivative dnu/dT using gradient
    dnu_dT = np.gradient(nu_p, temps)
    X = dnu_dT / nu_p
    
    # Linear regression
    reg = linregress(X, Cp_J)
    slope = reg.slope
    intercept = reg.intercept
    
    # dPm_dT in bar/K
    # dPm_dT = - slope * 10 * gamma_p / (Tm * Vc_Tm)
    dPm_dT_bar = - slope * 10.0 * gamma_p / (Tm * Vc_Tm)
    dS_dT_m = intercept / Tm
    
    return {
        'temperatures': temps.tolist(),
        'C_p': Cp_J.tolist(),
        'X': X.tolist(),
        'dPm_dT': dPm_dT_bar,
        'dS_dT_m': dS_dT_m
    }

def main():
    configs = [
        (0, 192.5),
        (1.93, 210.0),
        (3.07, 217.34)
    ]
    output = {}
    for P, Tm in configs:
        key = f'{P}kbar'
        print(f"Computing for {key}...")
        data = compute_pressure(P, Tm)
        output[key] = data
    with open('/app/outputs/results.json', 'w') as f:
        json.dump(output, f, indent=2)
    print("results.json written.")

if __name__ == '__main__':
    main()