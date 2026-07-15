import json, math

mu = 5.5e-6  # kg/m^2 (2*m_Te + m_Mo, with m_Te=2e-6, m_Mo=1.5e-6)
c = 2.99792458e10  # cm/s
pi = math.pi

w_shear_2 = 19.2
w_breath_2 = 27.8

# compute force constants
factor = 2 * mu * pi**2 * c**2
K_x = factor * w_shear_2**2
K_z = factor * w_breath_2**2

modes = []
Ns = [2, 3, 4, 5, 6, 7, 100]
for N in Ns:
    # shear modes
    branch = f"α={N}"
    alpha = N
    arg = (alpha - 1) * pi / N
    f = math.sqrt(1 - math.cos(arg))
    freq = w_shear_2 * f
    modes.append({"N": N, "mode_type": "shear", "branch": branch, "frequency_cm-1": round(freq, 6)})
    if N >= 4:
        branch2 = f"α={N-2}"
        alpha2 = N-2
        arg2 = (alpha2 - 1) * pi / N
        f2 = math.sqrt(1 - math.cos(arg2))
        freq2 = w_shear_2 * f2
        modes.append({"N": N, "mode_type": "shear", "branch": branch2, "frequency_cm-1": round(freq2, 6)})
    # breathing modes
    for alpha_b in range(2, N+1, 2):
        branch_b = f"α={alpha_b}"
        arg_b = (alpha_b - 1) * pi / N
        f_b = math.sqrt(1 - math.cos(arg_b))
        freq_b = w_breath_2 * f_b
        modes.append({"N": N, "mode_type": "breathing", "branch": branch_b, "frequency_cm-1": round(freq_b, 6)})

result = {
    "K_x": K_x,
    "K_z": K_z,
    "modes": modes
}

print(json.dumps(result, indent=2))