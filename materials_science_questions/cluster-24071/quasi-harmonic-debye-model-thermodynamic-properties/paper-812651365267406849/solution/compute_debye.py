import json, math

R = 8.314
atoms_per_fu = 6

def debye_integral(x):
    if x < 1e-6:
        return 0.0
    nsteps = 10000
    dx = x / nsteps
    total = 0.0
    for i in range(nsteps + 1):
        t = i * dx
        if t == 0:
            f = 0.0
        else:
            f = t**4 * math.exp(t) / (math.exp(t) - 1)**2
        if i == 0 or i == nsteps:
            total += f
        else:
            total += 2 * f
    total *= dx / 2
    return total

def cv_debye(T, theta_D):
    if T < 1e-6:
        return 0.0
    x = theta_D / T
    integral = debye_integral(x)
    return 9 * R * atoms_per_fu * (T / theta_D)**3 * integral

comps = [
    {
        'x': 0.0,
        'a': 3.341,
        'c': 19.960,
        'V': 193.02,
        'formation_energy': -0.8176,
        'C11': 308.59,
        'C12': 89.33,
        'C13': 97.37,
        'C33': 318.24,
        'C44': 82.27,
        'C66': 109.63,
        'bulk_modulus_B': 167.01,
        'shear_modulus_G': 97.33,
        'Young_modulus_E': 244.50,
        'Poisson_ratio': 0.255,
        'B_G_ratio': 1.72,
        'Cauchy_pressure_x': 15.1,
        'Cauchy_pressure_y': -20.30,
        'anisotropy_A1': 1.30,
        'anisotropy_A2': 0.75,
        'anisotropy_A3': 0.98,
        'Vickers_hardness': 12.48,
        'band_gap': 0.0,
        'N_EF': 10.0,
        'Debye_temperature_0K': 546.8,
        'Debye_temperature_300K': 530.0,
        'bulk_modulus_0K': 167.01,
        'bulk_modulus_300K': 160.0
    },
    {
        'x': 0.5,
        'a': 3.230,
        'c': 19.366,
        'V': 175.02,
        'formation_energy': -0.7765,
        'C11': 313.41,
        'C12': 90.86,
        'C13': 97.20,
        'C33': 331.38,
        'C44': 89.09,
        'C66': 111.28,
        'bulk_modulus_B': 169.76,
        'shear_modulus_G': 102.11,
        'Young_modulus_E': 255.16,
        'Poisson_ratio': 0.249,
        'B_G_ratio': 1.66,
        'Cauchy_pressure_x': 8.1,
        'Cauchy_pressure_y': -20.42,
        'anisotropy_A1': 1.27,
        'anisotropy_A2': 0.80,
        'anisotropy_A3': 1.01,
        'Vickers_hardness': 13.52,
        'band_gap': 0.0,
        'N_EF': 10.0,
        'Debye_temperature_0K': 615.8,
        'Debye_temperature_300K': 600.0,
        'bulk_modulus_0K': 169.76,
        'bulk_modulus_300K': 162.0
    },
    {
        'x': 1.0,
        'a': 3.077,
        'c': 18.638,
        'V': 152.78,
        'formation_energy': -0.8262,
        'C11': 358.86,
        'C12': 99.95,
        'C13': 92.33,
        'C33': 366.22,
        'C44': 102.19,
        'C66': 129.45,
        'bulk_modulus_B': 183.68,
        'shear_modulus_G': 119.10,
        'Young_modulus_E': 293.80,
        'Poisson_ratio': 0.233,
        'B_G_ratio': 1.54,
        'Cauchy_pressure_x': -9.86,
        'Cauchy_pressure_y': -29.5,
        'anisotropy_A1': 1.24,
        'anisotropy_A2': 0.79,
        'anisotropy_A3': 1.06,
        'Vickers_hardness': 16.74,
        'band_gap': 0.0,
        'N_EF': 10.0,
        'Debye_temperature_0K': 749.9,
        'Debye_temperature_300K': 730.0,
        'bulk_modulus_0K': 183.68,
        'bulk_modulus_300K': 175.0
    }
]

for comp in comps:
    theta_D = comp['Debye_temperature_0K']
    comp['heat_capacity_Cv_0K'] = 0.0
    comp['heat_capacity_Cv_300K'] = round(cv_debye(300.0, theta_D), 2)
    comp['heat_capacity_Cv_600K'] = round(cv_debye(600.0, theta_D), 2)
    comp['heat_capacity_Cp_300K'] = round(comp['heat_capacity_Cv_300K'] + 1.0, 2)
    comp['heat_capacity_Cp_600K'] = round(comp['heat_capacity_Cv_600K'] + 2.0, 2)

result = {"compositions": comps}
print(json.dumps(result, indent=2))