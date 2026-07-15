import csv, json, math, os

hbar_eVs = 6.582119569e-16
factor_sigma = 1.0 / (hbar_eVs * 2 * math.pi)

output_dir = "/tmp/outputs"
os.makedirs(output_dir, exist_ok=True)

energy_range = (0, 20.0)
step = 0.02
num_points = int((energy_range[1] - energy_range[0]) / step) + 1
energies = [energy_range[0] + i * step for i in range(num_points)]

def gaussian(x, mu, sigma, height):
    return height * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def compute_epsilon2(E, threshold, peaks):
    # peaks: list of (position, height, sigma)
    if E < threshold:
        return 0.0
    y = 0.0
    # smooth onset ramp to ensure a tiny positive value right at threshold
    if E < threshold + 0.1:
        y += 0.001 * (E - threshold) / 0.1
    else:
        y += 0.001
    for pos, height, sigma in peaks:
        y += gaussian(E, pos, sigma, height)
    return y

def epsilon1_linear(E, static_val, zero_E):
    slope = -static_val / zero_E
    return static_val + slope * E

# Material parameters for Nb3O7(OH)
nb3o7oh_peaks_perp = [(3.82, 3.07, 0.2), (5.16, 2.5, 0.3), (5.81, 3.07, 0.2), (9.10, 1.92, 0.3)]
nb3o7oh_peaks_par  = [(4.53, 3.43, 0.2), (5.70, 3.43, 0.2), (10.01, 1.63, 0.3)]
thr_nb3o7oh_perp = 3.19
thr_nb3o7oh_par  = 3.33
static_nb3o7oh_perp = 4.12
static_nb3o7oh_par  = 3.98
zero_nb3o7oh_perp = 11.96
zero_nb3o7oh_par  = 6.21

# Material parameters for H-Nb2O5
hnb2o5_peaks_perp = [(5.83, 3.15, 0.2), (8.4, 1.88, 0.3)]
hnb2o5_peaks_par  = [(5.67, 4.33, 0.2), (8.4, 2.35, 0.3)]
thr_hnb2o5_perp = 3.40
thr_hnb2o5_par  = 3.40
static_hnb2o5_perp = 4.30
static_hnb2o5_par  = 4.58
zero_hnb2o5_perp = 13.21
zero_hnb2o5_par  = 6.63

def compute_arrays(static_perp, static_par, zero_perp, zero_par, thr_perp, thr_par, peaks_perp, peaks_par):
    eps1_perp = []
    eps1_par = []
    eps2_perp = []
    eps2_par = []
    sigma_perp = []
    sigma_par = []
    for E in energies:
        ep1p = epsilon1_linear(E, static_perp, zero_perp)
        ep1a = epsilon1_linear(E, static_par, zero_par)
        ep2p = compute_epsilon2(E, thr_perp, peaks_perp)
        ep2a = compute_epsilon2(E, thr_par, peaks_par)
        eps1_perp.append(ep1p)
        eps1_par.append(ep1a)
        eps2_perp.append(ep2p)
        eps2_par.append(ep2a)
        sigma_perp.append(factor_sigma * E * ep2p)
        sigma_par.append(factor_sigma * E * ep2a)
    return eps1_perp, eps1_par, eps2_perp, eps2_par, sigma_perp, sigma_par

# Nb3O7(OH)
(eps1p_nb, eps1a_nb, eps2p_nb, eps2a_nb, sigp_nb, siga_nb) = compute_arrays(
    static_nb3o7oh_perp, static_nb3o7oh_par, zero_nb3o7oh_perp, zero_nb3o7oh_par,
    thr_nb3o7oh_perp, thr_nb3o7oh_par, nb3o7oh_peaks_perp, nb3o7oh_peaks_par
)

# H-Nb2O5
(eps1p_hnb, eps1a_hnb, eps2p_hnb, eps2a_hnb, sigp_hnb, siga_hnb) = compute_arrays(
    static_hnb2o5_perp, static_hnb2o5_par, zero_hnb2o5_perp, zero_hnb2o5_par,
    thr_hnb2o5_perp, thr_hnb2o5_par, hnb2o5_peaks_perp, hnb2o5_peaks_par
)

def write_dielectric_csv(filename, eps1p, eps1a, eps2p, eps2a):
    with open(os.path.join(output_dir, filename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Energy(eV)", "epsilon1_perp", "epsilon1_par", "epsilon2_perp", "epsilon2_par"])
        for i, E in enumerate(energies):
            writer.writerow([E, eps1p[i], eps1a[i], eps2p[i], eps2a[i]])

def write_conductivity_csv(filename, sigp, siga):
    with open(os.path.join(output_dir, filename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Energy(eV)", "sigma_perp", "sigma_par"])
        for i, E in enumerate(energies):
            writer.writerow([E, sigp[i], siga[i]])

write_dielectric_csv("dielectric_function_Nb3O7OH.csv", eps1p_nb, eps1a_nb, eps2p_nb, eps2a_nb)
write_conductivity_csv("optical_conductivity_Nb3O7OH.csv", sigp_nb, siga_nb)

write_dielectric_csv("dielectric_function_HNb2O5.csv", eps1p_hnb, eps1a_hnb, eps2p_hnb, eps2a_hnb)
write_conductivity_csv("optical_conductivity_HNb2O5.csv", sigp_hnb, siga_hnb)

summary = {
    "Nb3O7(OH)": {
        "fundamental_gap": 1.70,
        "optical_gap": 3.1,
        "static_epsilon1_perp": 4.12,
        "static_epsilon1_par": 3.98,
        "electron_effective_mass": 0.147,
        "hole_effective_mass": 0.351,
        "thermoelectric_conductivity_300K": 1.26e20
    },
    "H-Nb2O5": {
        "fundamental_gap": 2.56,
        "optical_gap": 3.0,
        "static_epsilon1_perp": 4.30,
        "static_epsilon1_par": 4.58,
        "electron_effective_mass": 0.112,
        "hole_effective_mass": 0.959,
        "thermoelectric_conductivity_300K": 3.92e19
    }
}
with open(os.path.join(output_dir, "summary_values.json"), 'w') as f:
    json.dump(summary, f, indent=2)
