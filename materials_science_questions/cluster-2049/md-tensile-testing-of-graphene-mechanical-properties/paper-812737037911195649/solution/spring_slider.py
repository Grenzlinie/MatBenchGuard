import argparse, math, csv, sys

# Material parameters
B = 2.38e-19        # J
E_mod = 1.0e12     # Pa
t = 0.34e-9        # m
Gamma_b = -0.232   # J/m²
L_g = 40e-9        # m
P_t_atm = 10
P_t = P_t_atm * 101325  # Pa

eta = 98.82
A_g = L_g ** 2

# Helper functions
def spring_constant(A_g):
    return 2 * B * (A_g / t**2) * math.sqrt(P_t / E_mod)

def projected_area(R_d):
    return (B * R_d / P_t)**0.25 * (math.pi * L_g / 2)

def projected_flat_area(R_d):
    return 2 * math.pi * R_d**2 * (1 - math.cos(L_g / (2 * R_d)))

def compute_theta_t(A_pr, A_def):
    if A_def == 0:
        return math.pi
    eps_s = (A_pr - A_def) / A_def
    return math.pi * (1 + eps_s)

def compute_theta_t_critical(A_pr):
    factor = (E_mod / (P_t * A_pr**2)) ** (1/9) * t**(4/9)
    return math.pi / (1 + factor)

def generate_energy_csv(output_path):
    k_s = spring_constant(A_g)
    k_b = Gamma_b / 2.0

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['curvature_1_per_nm', 'total_energy_J', 'spring_energy_J',
                         'slider_energy_J', 'potential_energy_J',
                         'rotational_angle_rad', 'critical_angle_rad'])

        # κ_d from 0 to 0.1 nm⁻¹ in 101 steps (step 0.001)
        kappas_nm = [i * 0.001 for i in range(101)]
        for kappa_nm in kappas_nm:
            if kappa_nm == 0.0:
                # flat configuration
                total = 0.0
                spring_eng = 0.0
                slider_eng = 0.0
                pot_eng = 0.0
                theta_t = math.pi
                theta_c = math.pi   # θ_c at flat state? at κ=0, A_pr infinite? We'll set to pi.
            else:
                kappa_m = kappa_nm * 1e9   # 1/m
                R_d = 1.0 / kappa_m
                A_pr = projected_area(R_d)
                A_s = projected_flat_area(R_d)
                A_def = A_pr + math.pi * A_g / 4 - A_s
                if A_def <= 0:
                    A_def = 1e-30  # avoid negative

                theta_t = compute_theta_t(A_pr, A_def)
                theta_c = compute_theta_t_critical(A_pr)

                spring_eng = 0.5 * k_s * (theta_t - math.pi)**2
                if theta_t < theta_c:
                    slider_eng = k_b * A_def * (math.sin(theta_c/2) - math.sin(theta_t/2))
                else:
                    slider_eng = 0.0

                pot_eng = P_t * ( A_def * (R_d + math.sqrt(A_def) * math.cos(theta_t/2) / 2) + A_s * R_d )
                total = spring_eng + slider_eng + pot_eng

            writer.writerow([f"{kappa_nm:.3f}", f"{total:.8e}", f"{spring_eng:.8e}",
                             f"{slider_eng:.8e}", f"{pot_eng:.8e}",
                             f"{theta_t:.6f}", f"{theta_c:.6f}"])

def generate_critical_txt(output_path):
    # Compute critical area A_g^c (m²) then convert to nm²
    A_g_c_m2 = eta * (B / P_t)**(2/3)
    A_g_c_nm2 = A_g_c_m2 * 1e18

    # To find dE/dκ root, we need a fine energy curve.
    k_s = spring_constant(A_g)
    k_b = Gamma_b / 2.0
    kappas_nm = [i * 0.0001 for i in range(1001)]  # 0 to 0.1 with step 0.0001
    energies = []
    for kappa_nm in kappas_nm:
        if kappa_nm == 0.0:
            energies.append(0.0)
            continue
        kappa_m = kappa_nm * 1e9
        R_d = 1.0 / kappa_m
        A_pr = projected_area(R_d)
        A_s = projected_flat_area(R_d)
        A_def = A_pr + math.pi * A_g / 4 - A_s
        if A_def <= 0:
            A_def = 1e-30
        theta_t = compute_theta_t(A_pr, A_def)
        theta_c = compute_theta_t_critical(A_pr)

        spring_eng = 0.5 * k_s * (theta_t - math.pi)**2
        if theta_t < theta_c:
            slider_eng = k_b * A_def * (math.sin(theta_c/2) - math.sin(theta_t/2))
        else:
            slider_eng = 0.0
        pot_eng = P_t * ( A_def * (R_d + math.sqrt(A_def) * math.cos(theta_t/2) / 2) + A_s * R_d )
        total = spring_eng + slider_eng + pot_eng
        energies.append(total)

    # Approximate derivative dE/dκ (finite differences) and find root
    root_kappa = None
    for i in range(1, len(kappas_nm)-1):
        dk = kappas_nm[i+1] - kappas_nm[i-1]
        if dk == 0:
            continue
        dE = energies[i+1] - energies[i-1]
        deriv = dE / dk
        if deriv >= 0 and i > 1 and (energies[i] - energies[i-1]) <= 0:
            # sign change from negative to positive => minimum
            root_kappa = kappas_nm[i]
            break

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"A_g_c = {A_g_c_nm2:.6f} nm²\n")
        if root_kappa is None:
            f.write("kappa_d_E = No root\n")
            # Output angles at κ_d = 0.1 nm⁻¹ for completeness
            last_kappa = kappas_nm[-1]
            kappa_m = last_kappa * 1e9
            R_d = 1.0 / kappa_m
            A_pr = projected_area(R_d)
            A_s = projected_flat_area(R_d)
            A_def = A_pr + math.pi * A_g / 4 - A_s
            if A_def <= 0:
                A_def = 1e-30
            theta_t = compute_theta_t(A_pr, A_def)
            theta_c = compute_theta_t_critical(A_pr)
            f.write(f"theta_t at kappa_d_E = {theta_t:.6f} rad\n")
            f.write(f"theta_t^c = {theta_c:.6f} rad\n")
        else:
            f.write(f"kappa_d_E = {root_kappa:.6f} nm⁻¹\n")
            # Get angles at that curvature
            kappa_m = root_kappa * 1e9
            R_d = 1.0 / kappa_m
            A_pr = projected_area(R_d)
            A_s = projected_flat_area(R_d)
            A_def = A_pr + math.pi * A_g / 4 - A_s
            if A_def <= 0:
                A_def = 1e-30
            theta_t = compute_theta_t(A_pr, A_def)
            theta_c = compute_theta_t_critical(A_pr)
            f.write(f"theta_t at kappa_d_E = {theta_t:.6f} rad\n")
            f.write(f"theta_t^c = {theta_c:.6f} rad\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-csv', help='Path to write CSV')
    parser.add_argument('--output-txt', help='Path to write TXT')
    args = parser.parse_args()
    if args.output_csv:
        generate_energy_csv(args.output_csv)
    elif args.output_txt:
        generate_critical_txt(args.output_txt)
    else:
        print("No output specified", file=sys.stderr)
        sys.exit(1)
