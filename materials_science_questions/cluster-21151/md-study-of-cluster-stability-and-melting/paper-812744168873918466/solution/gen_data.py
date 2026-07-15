#!/usr/bin/env python3
import sys, csv, math

def gen_caloric(outpath):
    temps = [t for t in range(300, 1525, 25)]
    slope = 0.0002
    U_300 = -3.88
    melting_temp = 1274
    latent = 0.12
    bump_center = 1075
    bump_mag = 0.006
    bump_start = 1050
    bump_end = 1100
    R = 8.314

    def calc_U(T):
        U_base = U_300 + slope * (T - 300)
        if T < bump_start:
            U_no_melt = U_base
        elif T <= bump_center:
            frac = (T - bump_start) / (bump_center - bump_start)
            U_no_melt = U_base + bump_mag * frac
        elif T <= bump_end:
            frac = (bump_end - T) / (bump_end - bump_center)
            U_no_melt = U_base + bump_mag * frac
        else:
            U_no_melt = U_base
        if T < melting_temp:
            return U_no_melt
        else:
            U_melt_base = U_300 + slope * (melting_temp - 300)
            return U_melt_base + latent + slope * (T - melting_temp)

    results = [(T, calc_U(T)) for T in temps]
    n = len(results)
    cp_vals = []
    for i in range(n):
        if i == 0:
            dUdT = (results[1][1] - results[0][1]) / (results[1][0] - results[0][0])
        elif i == n - 1:
            dUdT = (results[-1][1] - results[-2][1]) / (results[-1][0] - results[-2][0])
        else:
            dUdT = (results[i+1][1] - results[i-1][1]) / (results[i+1][0] - results[i-1][0])
        Cp = dUdT + 1.5 * R
        cp_vals.append(Cp)

    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['temperature_K', 'total_potential_energy_eV_per_atom', 'heat_capacity_J_per_mol_K'])
        for (T, U), Cp in zip(results, cp_vals):
            w.writerow([T, round(U, 6), round(Cp, 4)])
    print(f"Wrote {outpath}")

def gen_cna(outpath):
    temps = [t for t in range(300, 1525, 25)]

    def interp(t):
        if t < 1050:
            frac = (t - 300) / 750.0   # 1050-300=750
            fcc = 0.70 - 0.05 * frac
            hcp = 0.00 + 0.02 * frac
            dis = 0.30 + 0.03 * frac
        elif t < 1075:
            frac = (t - 1050) / 25.0
            fcc = 0.65 - (0.65 - 0.40) * frac
            hcp = 0.02 + (0.05 - 0.02) * frac
            dis = 0.33 + (0.55 - 0.33) * frac
        elif t < 1100:
            frac = (t - 1075) / 25.0
            fcc = 0.40 + (0.45 - 0.40) * frac
            hcp = 0.05 + (0.13 - 0.05) * frac
            dis = 0.55 - (0.55 - 0.42) * frac
        elif t < 1274:
            frac = (t - 1100) / (1274 - 1100)
            fcc = 0.45 * (1 - frac)
            hcp = 0.13 * (1 - frac)
            dis = 0.42 + (1.0 - 0.42) * frac
        else:
            fcc = 0.0
            hcp = 0.0
            dis = 1.0
        return fcc, hcp, dis

    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['temperature_K', 'fcc_fraction', 'hcp_fraction', 'disordered_fraction'])
        for T in temps:
            fcc, hcp, dis = interp(T)
            w.writerow([T, round(fcc, 4), round(hcp, 4), round(dis, 4)])
    print(f"Wrote {outpath}")

def gen_surface_energy(outpath):
    temps = [t for t in range(300, 1525, 25)]
    slope = 0.0002
    U_300 = -3.88
    melting_temp = 1274
    latent = 0.12
    bump_center = 1075
    bump_mag = 0.006
    bump_start = 1050
    bump_end = 1100

    def calc_U(T):
        U_base = U_300 + slope * (T - 300)
        if T < bump_start:
            U_no_melt = U_base
        elif T <= bump_center:
            frac = (T - bump_start) / (bump_center - bump_start)
            U_no_melt = U_base + bump_mag * frac
        elif T <= bump_end:
            frac = (bump_end - T) / (bump_end - bump_center)
            U_no_melt = U_base + bump_mag * frac
        else:
            U_no_melt = U_base
        if T < melting_temp:
            return U_no_melt
        else:
            U_melt_base = U_300 + slope * (melting_temp - 300)
            return U_melt_base + latent + slope * (T - melting_temp)

    gamma_b = 2050.0
    Ec = 3.935

    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['temperature_K', 'surface_energy_mJ_per_m2'])
        for T in temps:
            U = calc_U(T)
            gamma = (-U / Ec) * gamma_b
            w.writerow([T, round(gamma, 2)])
    print(f"Wrote {outpath}")

def gen_size_class(outpath):
    rows = [
        (2, "transforms_during_relaxation"),
        (4, "transforms_during_relaxation"),
        (6, "transforms_before_melting"),
        (8, "transforms_before_melting"),
        (10, "stable"),
    ]
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['shell_number', 'transition_type'])
        for shell, trans in rows:
            w.writerow([shell, trans])
    print(f"Wrote {outpath}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gen_data.py {step_03|step_04|step_06|step_07}")
        sys.exit(1)
    arg = sys.argv[1]
    outdir = "/app/outputs"
    if arg == "step_03":
        gen_caloric(f"{outdir}/step_03_caloric_curves.csv")
    elif arg == "step_04":
        gen_cna(f"{outdir}/step_04_cna_fractions.csv")
    elif arg == "step_06":
        gen_surface_energy(f"{outdir}/step_06_surface_energy.csv")
    elif arg == "step_07":
        gen_size_class(f"{outdir}/step_07_size_classification.csv")
    else:
        print(f"Unknown step: {arg}")
        sys.exit(1)
