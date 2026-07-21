import numpy as np
import sys, os

def main(outdir):
    thicknesses_um = [20, 28, 40, 60, 80, 100, 140, 200]
    skin_um = 7.0
    eps_skin = 2.5e-11
    eps_bulk = 9e-11
    Esat_skin = 6e6  # V/m
    Esat_bulk = 16e6
    strain_scale = 5e7  # to obtain strain percentage magnitude
    E_max = 20e6  # V/m
    freq = 0.1  # Hz
    period = 1.0 / freq  # 10 s
    half_period = period / 2.0  # 5 s
    dt = 0.01
    nsteps = int(half_period / dt) + 1

    # field grid for interpolation (0–20 MV/m, 101 points)
    field_interp_MVm = np.linspace(0, 20, 101)
    field_interp_Vm = field_interp_MVm * 1e6

    strain_rows = []  # (thickness_um, field_MV_per_m, strain_percent)
    max_strains = {}  # thickness_um -> max strain percent

    record_arr = None
    first_thick = True

    for th_um in thicknesses_um:
        L_total = th_um * 1e-6
        L1 = skin_um * 1e-6
        L3 = L1
        L2 = L_total - L1 - L3
        if L2 <= 0:
            L2 = 1e-9
        # capacitance factors (A=1)
        C1 = eps_skin / L1
        C2 = eps_bulk / L2
        C3 = eps_skin / L3
        # stiffness denominator D = (1/L1 + 1/L2 + 1/L3) * L_total
        D = (1.0 / L1 + 1.0 / L2 + 1.0 / L3) * L_total

        # initial conditions
        V1, V2 = 0.0, 0.0
        t = 0.0
        applied_E_list = []
        strain_list = []

        for step in range(nsteps):
            E_applied = E_max * (t / half_period)
            V_tot = E_applied * L_total
            V3 = V_tot - V1 - V2

            E1 = V1 / L1
            E2 = V2 / L2
            E3 = V3 / L3

            P1 = eps_skin * Esat_skin * np.tanh(E1 / Esat_skin)
            P2 = eps_bulk * Esat_bulk * np.tanh(E2 / Esat_bulk)
            P3 = eps_skin * Esat_skin * np.tanh(E3 / Esat_skin)

            sum_P2 = P1**2 + P2**2 + P3**2
            fraction = sum_P2 / D
            strain_mag = -fraction * strain_scale   # positive magnitude

            applied_E_list.append(E_applied)
            strain_list.append(strain_mag)

            def sech2(x):
                return 1.0 - np.tanh(x)**2

            G1 = C1 * sech2(E1 / Esat_skin)
            G2 = C2 * sech2(E2 / Esat_bulk)
            G3 = C3 * sech2(E3 / Esat_skin)

            # guard against zero
            G1 = max(G1, 1e-30)
            G2 = max(G2, 1e-30)
            G3 = max(G3, 1e-30)

            sum_invG = 1.0 / G1 + 1.0 / G2 + 1.0 / G3
            dV_tot = E_max * L_total * dt / half_period
            dV1 = (1.0 / G1) / sum_invG * dV_tot
            dV2 = (1.0 / G2) / sum_invG * dV_tot
            V1 += dV1
            V2 += dV2
            t += dt

        E_MV_per_m = np.array(applied_E_list) / 1e6
        strain_percent = np.array(strain_list)
        interp_strain = np.interp(field_interp_MVm, E_MV_per_m, strain_percent)

        for fmv, sp in zip(field_interp_MVm, interp_strain):
            strain_rows.append((th_um, fmv, sp))

        max_strain = float(np.max(strain_percent))
        max_strains[th_um] = max_strain

        if first_thick:
            time_arr = np.linspace(0, half_period, nsteps)
            rec_dtype = [('time', float), ('E_MVm', float), ('strain_pct', float)]
            record_arr = np.zeros(nsteps, dtype=rec_dtype)
            record_arr['time'] = time_arr
            record_arr['E_MVm'] = E_MV_per_m[:nsteps]
            record_arr['strain_pct'] = strain_percent[:nsteps]
            first_thick = False

    # --- write scored artifacts ---
    csv_path = os.path.join(outdir, "strain_vs_E.csv")
    with open(csv_path, 'w') as f:
        f.write("thickness_um,field_MV_per_m,strain_percent\n")
        for th, fmv, sp in strain_rows:
            f.write(f"{th},{fmv:.4f},{sp:.6f}\n")

    max_csv_path = os.path.join(outdir, "max_strain_vs_thickness.csv")
    with open(max_csv_path, 'w') as f:
        f.write("thickness_um,max_strain_percent\n")
        for th_um in thicknesses_um:
            f.write(f"{th_um},{max_strains[th_um]:.6f}\n")

    # --- evidence record ---
    np.save(os.path.join(outdir, "simulation_record.npy"), record_arr)


if __name__ == "__main__":
    main(sys.argv[1])