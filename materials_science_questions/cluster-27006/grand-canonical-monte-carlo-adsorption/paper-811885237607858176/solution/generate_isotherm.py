import csv, sys

system = sys.argv[1] if len(sys.argv) > 1 else "cu"

if system == "cu":
    outfile = "/app/outputs/cu_adsorption_isotherm.csv"
    # mu range from -3.70 to -3.53 eV (step 0.005)
    mu_range = [round(-3.70 + 0.005 * i, 4) for i in range(int((-3.53 - (-3.70)) / 0.005) + 1)]
    # stages: (mu_lower, mu_upper, N_atoms, avg_binding_energy)
    stages = [
        (-3.70, -3.64, 30, -3.72),
        (-3.64, -3.61, 60, -3.66),
        (-3.61, -3.57, 100, -3.57),
        (-3.57, -3.55, 210, -3.56),
        (-3.55, -3.535, 300, -3.55),
        (-3.535, -3.53, 380, -3.54),
        (-3.53, -3.50, 450, -3.53),
    ]
elif system == "ag":
    outfile = "/app/outputs/ag_adsorption_isotherm.csv"
    # mu range from -3.35 to -2.855 eV (step 0.005)
    mu_range = [round(-3.35 + 0.005 * i, 4) for i in range(int((-2.855 - (-3.35)) / 0.005) + 1)]
    stages = [
        (-3.35, -3.12, 20, -3.30),
        (-3.12, -3.01, 50, -3.20),
        (-3.01, -2.985, 100, -3.10),
        (-2.985, -2.87, 160, -2.92),
        (-2.87, -2.855, 260, -2.87),
    ]
else:
    raise ValueError("Unknown system")

with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["avg_binding_energy", "chemical_potential", "num_atoms"])
    for mu in mu_range:
        N_val = 0
        binding_val = 0.0
        for low, high, N, binding in stages:
            if low <= mu <= high:
                N_val = N
                binding_val = binding
                break
        if N_val > 0:
            writer.writerow([binding_val, mu, N_val])
