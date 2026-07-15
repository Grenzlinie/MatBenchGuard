import csv, math, sys

def lorentzian(h, q0, kappa, amp):
    return amp / ((h - q0)**2 + kappa**2)

def write_lattice_parameters():
    writer = csv.writer(sys.stdout)
    writer.writerow(["condition_id", "epsilon_aa", "a", "b", "c", "epsilon_bb", "epsilon_cc"])
    a0 = 3.880
    b0 = 3.880
    c0 = 9.500
    nu_ba = 0.16
    nu_ca = 0.11
    conditions = [
        ("0%", 0.0),
        ("0.05%", -0.0005),
        ("0.2%", -0.002),
        ("0.5%", -0.005),
        ("1.1%", -0.011),
    ]
    for cond_id, eps_aa in conditions:
        eps_bb = -nu_ba * eps_aa
        eps_cc = -nu_ca * eps_aa
        a = a0 * (1.0 + eps_aa)
        b = b0 * (1.0 + eps_bb)
        c = c0 * (1.0 + eps_cc)
        writer.writerow([cond_id, eps_aa, round(a, 6), round(b, 6), round(c, 6), round(eps_bb, 6), round(eps_cc, 6)])

def write_poisson():
    writer = csv.writer(sys.stdout)
    writer.writerow(["ratio", "value", "uncertainty"])
    writer.writerow(["ν_ba", 0.16, 0.01])
    writer.writerow(["ν_ca", 0.11, 0.01])

def write_linecuts():
    writer = csv.writer(sys.stdout)
    writer.writerow(["condition_id", "peak_label", "H", "intensity"])
    # strain sweep at T = 78 K
    strain_conditions = [
        ("0%_78K", 0.0),
        ("0.05%_78K", 0.8),
        ("0.2%_78K", 1.0),
        ("0.5%_78K", 1.0),
        ("1.1%_78K", 1.0),
    ]
    # temperature sweep at 1.1 % strain
    temp_conditions = [
        ("1.1%_30K", 1.0),
        ("1.1%_101K", 1.0),
    ]
    conditions = strain_conditions + temp_conditions
    peak_labels = ["(412)", "(4̄12)"]   # both reflections
    h_min, h_max, step = 2.5, 5.5, 0.01
    h_points = []
    h = h_min
    while h <= h_max + 1e-9:
        h_points.append(h)
        h += step
    # Bragg peak at H=4
    A_bragg = 100.0
    sigma = 0.02
    # satellite Lorentzians
    q0_left, q0_right = 3.53, 4.48
    kappa = 0.25
    amp_left_base, amp_right_base = 5.0, 5.0
    background = 0.5
    for cond_id, amp_factor in conditions:
        amp_left = amp_left_base * amp_factor
        amp_right = amp_right_base * amp_factor
        for peak_label in peak_labels:
            for h_val in h_points:
                bragg = A_bragg * math.exp(-(h_val - 4.0)**2 / (2.0 * sigma**2))
                left = lorentzian(h_val, q0_left, kappa, amp_left)
                right = lorentzian(h_val, q0_right, kappa, amp_right)
                intensity = bragg + left + right + background
                writer.writerow([cond_id, peak_label, round(h_val, 4), round(intensity, 4)])

def write_fitting():
    writer = csv.writer(sys.stdout)
    writer.writerow(["condition_id", "peak_label", "q0", "q0_uncertainty", "κ", "κ_uncertainty", "ξ", "ξ_uncertainty"])
    fit_conditions = [
        "0.05%_78K", "0.2%_78K", "0.5%_78K", "1.1%_78K",
        "1.1%_30K", "1.1%_101K"
    ]
    peaks = [
        ("H~3.53", 3.53, 0.04),
        ("H~4.48", 4.48, 0.02),
    ]
    kappa = 0.25
    kappa_unc = 0.01
    xi = 4.0
    xi_unc = 0.2
    for cond in fit_conditions:
        for peak_label, q0, q0_unc in peaks:
            writer.writerow([cond, peak_label, q0, q0_unc, kappa, kappa_unc, xi, xi_unc])

if __name__ == "__main__":
    cmd = sys.argv[1]
    {"lattice": write_lattice_parameters,
     "poisson": write_poisson,
     "linecuts": write_linecuts,
     "fitting": write_fitting}[cmd]()
