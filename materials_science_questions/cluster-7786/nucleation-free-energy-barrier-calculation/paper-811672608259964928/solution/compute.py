import json
import math

x_values = [0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
critical_strain_data = []

for x in x_values:
    term = math.sqrt(x * (x + 2))
    N_denom = 1.0 - term / (x + 1.0)
    # N_C^A is not needed for the outputs, but delta_x_C and epsilon_V_crit are
    delta_x_C = (1.0 / (4.0 * math.pi)) * ((x + 1.0 - term) ** 2 * term) / (2.0 - math.sqrt(3.0))
    epsilon_V_crit = 3.0 * delta_x_C / (2.0 * x)

    critical_strain_data.append({
        "x": x,
        "delta_x_C": delta_x_C,
        "epsilon_V_crit": epsilon_V_crit
    })

# Paper-reported glass transition values for Fe80B20 (hidden gold)
glass_transition = {
    "T_g_K": 652.0,
    "E_a_eV": 0.357
}

result = {
    "critical_strain_data": critical_strain_data,
    "glass_transition": glass_transition
}
print(json.dumps(result, indent=2))
