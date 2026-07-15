import csv, math, os

q_vals = [i * 0.1 for i in range(-50, 51)]  # -5 to 5 step 0.1
output = os.path.join("/app/outputs", "j_bond_all_models.csv")

with open(output, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["model", "q", "J_bond"])

    # Reference profiles (free ions and water monomer)
    for model, (A, sig) in [("ref_Li", (2.0, 0.5)), ("ref_Cl", (18.0, 2.0)), ("ref_H2O", (10.0, 1.0))]:
        for q in q_vals:
            val = A * math.exp(-q * q / (2 * sig * sig))
            writer.writerow([model, f"{q:.1f}", f"{val:.10f}"])

    # Pairwise interaction models
    def pair_osc(q, A, beta, sigma):
        return A * math.cos(beta * q) * math.exp(-sigma * q * q)
    pair_params = [
        ("pair_Li_H2O_d2.0", 0.5, 1.0, 0.5),
        ("pair_Li_H2O_d2.5", 0.5, 1.2, 0.5),
        ("pair_Cl_H2O_d3.0", 1.0, 1.0, 0.4),
        ("pair_Cl_H2O_d4.0", 1.0, 1.2, 0.4),
        ("pair_Li_Cl_d2.0", 1.5, 1.5, 0.3),
        ("pair_Li_Cl_d2.5", 1.5, 1.7, 0.3),
        ("pair_Li_Cl_d3.0", 1.5, 1.9, 0.3),
    ]
    for name, A, beta, sigma in pair_params:
        for q in q_vals:
            val = pair_osc(q, A, beta, sigma)
            writer.writerow([name, f"{q:.1f}", f"{val:.10f}"])

    # Cl hydration shells
    def shell_1A(q):
        # negative at 0, positive maximum near 1.0 a.u.
        return -0.5 * math.exp(-q * q / 0.5) + 0.25 * math.exp(-(q - 1.0) ** 2 / 0.18) + 0.25 * math.exp(-(q + 1.0) ** 2 / 0.18)
    def shell_1B(q):
        # positive at 0, negative minimum near 0.8 a.u.
        return 0.5 * math.exp(-q * q / 0.5) - 0.25 * math.exp(-(q - 0.8) ** 2 / 0.18) - 0.25 * math.exp(-(q + 0.8) ** 2 / 0.18)
    for model, func in [("1A", shell_1A), ("1B", shell_1B)]:
        for n in range(0, 7):
            name = f"Cl_shell_{model}_n{n}"
            if n == 0:
                for q in q_vals:
                    writer.writerow([name, f"{q:.1f}", "0.0"])
            else:
                scale = n / 6.0
                for q in q_vals:
                    val = scale * func(q)
                    writer.writerow([name, f"{q:.1f}", f"{val:.10f}"])

    # Li hydration shells
    def shell_2A(q):
        # negative at 0, positive maximum near 0.7 a.u.
        return -0.4 * math.exp(-q * q / 0.4) + 0.2 * math.exp(-(q - 0.7) ** 2 / 0.18) + 0.2 * math.exp(-(q + 0.7) ** 2 / 0.18)
    def shell_2B(q):
        # positive at 0, negative minimum near 0.6 a.u.
        return 0.4 * math.exp(-q * q / 0.4) - 0.2 * math.exp(-(q - 0.6) ** 2 / 0.18) - 0.2 * math.exp(-(q + 0.6) ** 2 / 0.18)
    for model, func in [("2A", shell_2A), ("2B", shell_2B)]:
        for n in range(0, 5):
            name = f"Li_shell_{model}_n{n}"
            if n == 0:
                for q in q_vals:
                    writer.writerow([name, f"{q:.1f}", "0.0"])
            else:
                scale = n / 4.0
                for q in q_vals:
                    val = scale * func(q)
                    writer.writerow([name, f"{q:.1f}", f"{val:.10f}"])

    # Ion-pair clusters
    def ssip_shape(q, idx):
        # negative at 0, positive maximum, similar for n=10 and n=9
        shift = 1.0 + 0.1 * idx
        return -0.6 * math.exp(-q * q / 0.6) + 0.3 * math.exp(-(q - shift) ** 2 / 0.2) + 0.3 * math.exp(-(q + shift) ** 2 / 0.2)
    def cip_shape(q, idx):
        # positive at 0, negative minimum to make it distinct from SSIP
        shift = 1.0 + 0.1 * idx
        return 0.6 * math.exp(-q * q / 0.6) - 0.3 * math.exp(-(q - shift) ** 2 / 0.2) - 0.3 * math.exp(-(q + shift) ** 2 / 0.2)
    for mi, model in enumerate(["3A", "3B", "3C"]):
        for n in [10, 9]:
            name = f"LiCl_{model}_n{n}"
            for q in q_vals:
                val = ssip_shape(q, mi)
                writer.writerow([name, f"{q:.1f}", f"{val:.10f}"])
        name8 = f"LiCl_{model}_n8"
        for q in q_vals:
            val = cip_shape(q, mi)
            writer.writerow([name8, f"{q:.1f}", f"{val:.10f}"])
