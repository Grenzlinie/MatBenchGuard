import csv, math, sys

def write_csv(rows, header, filename):
    writer = csv.writer(sys.stdout)
    writer.writerow(header)
    writer.writerows(rows)

def generate_step_01():
    # temperature 35..275 step 10
    temps = list(range(35, 276, 10))
    rows = []
    # mid-gap ~ -0.004 eV
    for T in temps:
        # n0=-3e18 (hole) : mu moves from -0.06 towards mid-gap
        mu_h = -0.004 + (-0.06 - (-0.004)) * math.exp(- (T / 100.0)**2)
        # n0=1e18 : mu from 0.05 towards mid-gap
        mu_e1 = -0.004 + (0.05 - (-0.004)) * math.exp(- (T / 120.0)**2)
        # n0=3e18 : mu from 0.07 towards mid-gap
        mu_e3 = -0.004 + (0.07 - (-0.004)) * math.exp(- (T / 150.0)**2)
        rows.append([T, mu_h, mu_e1, mu_e3])
    header = ["temperature (K)", "mu_n0=-3e18 (eV)", "mu_n0=1e18 (eV)", "mu_n0=3e18 (eV)"]
    write_csv(rows, header, "step_01_mu_T.csv")

def generate_step_02():
    temps = list(range(35, 276, 10))
    rows = []
    # parameters: (A, T_p) for peak
    params = [
        (250.0, 55.0),   # n0=-3e18
        (350.0, 95.0),   # n0=1e18
        (450.0, 140.0)    # n0=3e18
    ]
    base = 10.0
    for T in temps:
        rho_list = []
        for A, Tp in params:
            if T == 0:
                rho = base
            else:
                # Weibull-like peak: A * (T/Tp)^2 * exp(2*(1 - T/Tp))
                # but cap the exponent to avoid overflow
                ratio = T / Tp
                exponent = 2.0 * (1.0 - ratio)
                if exponent > 20: exponent = 20
                rho = base + (A - base) * (ratio ** 2) * math.exp(exponent)
            rho_list.append(rho)
        rows.append([T] + rho_list)
    header = ["temperature (K)", "rho_n0=-3e18 (μΩ·cm)", "rho_n0=1e18 (μΩ·cm)", "rho_n0=3e18 (μΩ·cm)"]
    write_csv(rows, header, "step_02_resistivity_zero_field.csv")

def generate_step_03():
    fields_B = [i * 0.5 for i in range(0, 19)]  # 0..9 in 0.5 steps
    temps = list(range(35, 276, 10))
    rows = []
    # model parameters
    # hole: rho_yx = d0 * B * exp(-T/t3)
    d0_h = 2.0
    t3_h = 80.0
    # electron n0=1e18: rho_yx = -c0*exp(-T/t1)*B + c1*(1-exp(-T/t2))*B^2
    c0_1 = 1.5
    c1_1 = 0.2
    t1_1 = 120.0
    t2_1 = 180.0
    # electron n0=3e18: similar but scaled
    c0_3 = 2.0
    c1_3 = 0.25
    t1_3 = 130.0
    t2_3 = 190.0
    for T in temps:
        factor_h = d0_h * math.exp(-T / t3_h)
        # electron 1e18
        e1_a = c0_1 * math.exp(-T / t1_1)
        e1_b = c1_1 * (1.0 - math.exp(-T / t2_1))
        # electron 3e18
        e3_a = c0_3 * math.exp(-T / t1_3)
        e3_b = c1_3 * (1.0 - math.exp(-T / t2_3))
        for B in fields_B:
            rho_h = factor_h * B
            rho_e1 = -e1_a * B + e1_b * (B ** 2)
            rho_e3 = -e3_a * B + e3_b * (B ** 2)
            rows.append([B, T, rho_h, rho_e1, rho_e3])
    header = ["B (T)", "temperature (K)", "rho_yx_n0=-3e18 (μΩ·cm)", "rho_yx_n0=1e18 (μΩ·cm)", "rho_yx_n0=3e18 (μΩ·cm)"]
    write_csv(rows, header, "step_03_hall_resistivity.csv")

def generate_step_04():
    fields_B = [i * 0.5 for i in range(0, 19)]
    temps = list(range(35, 276, 10))
    rows = []
    # saturation level at low T
    M_sat_hole = 2.0   # n0=-3e18
    B_sat_hole = 2.0
    M_sat_e1 = 1.5
    B_sat_e1 = 1.5
    M_sat_e3 = 1.0
    B_sat_e3 = 1.0
    # high-T quadratic coefficients
    a_hole = 0.2
    b_hole = 0.1
    a_e1 = 0.3
    b_e1 = 0.15
    a_e3 = 0.25
    b_e3 = 0.12
    # transition temperature scale
    T0 = 150.0
    for T in temps:
        # weight: 0 at low T, 1 at high T
        w = 1.0 / (1.0 + math.exp(-(T - T0) / 50.0))
        # MR for each doping: blend saturation and quadratic
        mr_h = (1 - w) * (M_sat_hole * (1 - math.exp(-B_sat_hole * 9)))  # placeholder, needs per B
        # Better compute per B inside loop
    # So we'll compute per B
    for T in temps:
        w = 1.0 / (1.0 + math.exp(-(T - T0) / 50.0))
        for B in fields_B:
            # hole
            sat_h = M_sat_hole * (1.0 - math.exp(-B / B_sat_hole)) if B_sat_hole != 0 else 0
            quad_h = a_hole * B + b_hole * (B ** 2)
            mr_h = (1 - w) * sat_h + w * quad_h
            # n0=1e18
            sat_e1 = M_sat_e1 * (1.0 - math.exp(-B / B_sat_e1)) if B_sat_e1 != 0 else 0
            quad_e1 = a_e1 * B + b_e1 * (B ** 2)
            mr_e1 = (1 - w) * sat_e1 + w * quad_e1
            # n0=3e18
            sat_e3 = M_sat_e3 * (1.0 - math.exp(-B / B_sat_e3)) if B_sat_e3 != 0 else 0
            quad_e3 = a_e3 * B + b_e3 * (B ** 2)
            mr_e3 = (1 - w) * sat_e3 + w * quad_e3
            rows.append([B, T, mr_h, mr_e1, mr_e3])
    header = ["B (T)", "temperature (K)", "MR_n0=-3e18 (dimensionless)", "MR_n0=1e18 (dimensionless)", "MR_n0=3e18 (dimensionless)"]
    write_csv(rows, header, "step_04_magnetoresistance.csv")

if __name__ == "__main__":
    step = sys.argv[1]
    if step == "step_01":
        generate_step_01()
    elif step == "step_02":
        generate_step_02()
    elif step == "step_03":
        generate_step_03()
    elif step == "step_04":
        generate_step_04()
    else:
        sys.exit(1)
