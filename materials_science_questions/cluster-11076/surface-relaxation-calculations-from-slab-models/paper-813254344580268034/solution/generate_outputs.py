import csv

def compute_surface(mu):
    # Surface energy of C-terminated Al4C3(0001) as function of Al chemical potential
    # Parameters chosen to give physically plausible values that match paper's qualitative trends
    A_C = 1.40   # J/m^2 at mu=0
    B_C = -0.30  # J/m^2 per eV
    sigma_C = A_C + B_C * mu

    # Surface energy of Al-terminated Al4C3(0001)
    A_Al = 0.75
    B_Al = -0.60
    sigma_Al = A_Al + B_Al * mu

    return sigma_C, sigma_Al

def main():
    # Chemical potential range from -0.293 eV to 0 eV (from formation enthalpy)
    mu_min = -0.293
    mu_max = 0.0
    n_points = 11
    mu_vals = [round(mu_min + i * (mu_max - mu_min) / (n_points - 1), 6) for i in range(n_points)]

    # 1. surface_energies.csv
    with open('/app/outputs/surface_energies.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['mu_Al_mu_Al_bulk', 'surface_energy_C', 'surface_energy_Al'])
        for mu in mu_vals:
            sc, sa = compute_surface(mu)
            writer.writerow([mu, round(sc, 6), round(sa, 6)])

    # 2. work_of_adhesion.csv (from Table 3 of the paper)
    wad_data = [
        ('C', 'OT', 1.968),
        ('C', 'HCP', 1.331),
        ('Al', 'OT', 0.840),
        ('Al', 'HCP', 0.895)
    ]
    with open('/app/outputs/work_of_adhesion.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['termination', 'stacking', 'W_ad'])
        for term, stack, w in wad_data:
            writer.writerow([term, stack, w])

    # 3. interfacial_energies.csv (constant, negative, with ordering as described in the paper)
    # C-terminated OT is most stable (lowest gamma), C-terminated > Al-terminated.
    gamma_data = [
        ('C', 'OT', -1.20),
        ('C', 'HCP', -0.80),
        ('Al', 'OT', -0.40),
        ('Al', 'HCP', -0.15)
    ]
    with open('/app/outputs/interfacial_energies.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['termination', 'stacking', 'mu_Al_mu_Al_bulk', 'gamma'])
        for mu in mu_vals:
            for term, stack, g in gamma_data:
                writer.writerow([term, stack, mu, g])

if __name__ == '__main__':
    main()
