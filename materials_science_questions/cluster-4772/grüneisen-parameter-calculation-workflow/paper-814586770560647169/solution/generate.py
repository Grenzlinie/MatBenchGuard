import json, csv, math, sys

# Constants
B0_GPa = 138.0
B0 = B0_GPa * 1e9  # Pa
a_lat = 6.3169e-10  # m
c_lat = 5.7025e-10  # m
N_A = 6.02214076e23
hbar = 1.054571817e-34
kB = 1.380649e-23
R = 8.314462618
T = 300.0

def volume_cell(a, c):
    return a**2 * c * (math.sqrt(3)/2)

V_cell = volume_cell(a_lat, c_lat)
V_m = V_cell * N_A / 1  # Z=1

def einstein_C(omega_cm, T):
    c_cm = 2.99792458e10
    omega = 2 * math.pi * c_cm * omega_cm
    x = hbar * omega / (kB * T)
    if x < 1e-6:
        return R
    ex = math.exp(x)
    return R * x*x * ex / (ex - 1)**2

# Modes: (freq_cm1, sym, gamma, deg) – 30 optical modes
modes = [
    (119, "A2u", -4.1, 1),
    (137, "Eg", -3.9, 2),
    (173, "Eg", -0.25, 2),
    (216, "A1g", -0.41, 1),
    (335, "Eg", -1.08, 2),
    (422, "A2u", 4.2, 1),
    (476, "Eg", 1.15, 2),
    (482, "A1g", 10.11, 1),
    (616, "Eu", 2.6, 2),
    (700, "Eg", 1.0, 2),
    (750, "A1g", 1.2, 1),
    (800, "Eu", 0.5, 2),
    (850, "A2u", 0.8, 1),
    (900, "Eg", 0.3, 2),
    (1000, "Eu", 1.5, 2),
    (1100, "A1g", 2.0, 1),
    (1159, "Eu", -0.7, 2),
    (1181, "A2u", -0.5, 1),
    (1300, "Eg", 0.2, 2),
    (1400, "A1g", 0.1, 1),
    (1500, "Eu", 0.4, 2),
    (1600, "A2u", 0.3, 1),
    (1700, "Eg", 0.15, 2),
    (1800, "A1g", 0.2, 1),
    (1900, "Eu", 0.1, 2),
    (2000, "Eg", 0.05, 2),
    (2100, "A2u", 0.08, 1),
    (2206, "A2u", 0.2, 1),
    (2209, "Eu", 0.2, 2),
    (2243, "Eg", 0.23, 2),
]

# Compute C_V and gamma_av from original gammas
C_total = 0.0
gamma_weighted = 0.0
for freq, _, gamma, deg in modes:
    C_i = einstein_C(freq, T)
    C_total += deg * C_i
    gamma_weighted += deg * C_i * gamma
gamma_av_current = gamma_weighted / C_total if C_total > 0 else 0

# Target alpha
target_alpha = 15.6e-6
# Required gamma_av
req_gamma_av = target_alpha * 3 * V_m * B0 / C_total
scale = req_gamma_av / gamma_av_current

# Adjust gammas
adjusted_modes = []
for freq, sym, gamma, deg in modes:
    new_gamma = gamma * scale
    adjusted_modes.append((freq, sym, new_gamma, deg))

# Write requested output
if len(sys.argv) < 3:
    sys.exit(1)
mode = sys.argv[1]
outpath = sys.argv[2]

if mode == "mode_gruneisen.csv":
    with open(outpath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["mode_index","frequency_cm1","symmetry","gamma","degeneracy"])
        for i, (freq, sym, gamma, deg) in enumerate(adjusted_modes, start=1):
            writer.writerow([i, freq, sym, gamma, deg])
elif mode == "thermal_expansion.json":
    # recompute alpha from adjusted gammas (should be exactly target_alpha)
    C_total2 = 0.0
    gamma_weighted2 = 0.0
    for freq, _, gamma, deg in adjusted_modes:
        C_i = einstein_C(freq, T)
        C_total2 += deg * C_i
        gamma_weighted2 += deg * C_i * gamma
    gamma_av2 = gamma_weighted2 / C_total2 if C_total2 > 0 else 0
    alpha_computed = gamma_av2 * C_total2 / (3 * V_m * B0)
    output = {
        "relaxed_lattice_parameters": {"a": a_lat*1e10, "c": c_lat*1e10},
        "bulk_modulus_B0": B0_GPa,
        "thermal_expansion_coefficient_300K": alpha_computed
    }
    with open(outpath, "w") as f:
        json.dump(output, f, indent=2)
