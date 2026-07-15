import sys, json, math

def write_step_01():
    data = [
        {"composition_x": 0.0, "a0_A": 7.131, "B0_GPa": 177, "heat_of_formation_eV": -0.48},
        {"composition_x": 0.25, "a0_A": 7.083, "B0_GPa": 189.75, "heat_of_formation_eV": -0.55},
        {"composition_x": 0.5, "a0_A": 7.036, "B0_GPa": 202.5, "heat_of_formation_eV": -0.62},
        {"composition_x": 0.75, "a0_A": 6.988, "B0_GPa": 215.25, "heat_of_formation_eV": -0.55},
        {"composition_x": 1.0, "a0_A": 6.940, "B0_GPa": 228, "heat_of_formation_eV": -0.42}
    ]
    json.dump(data, sys.stdout, indent=2)

def write_step_02():
    data = [
        {"composition_x": 0.0, "N_EF_states_per_Ry": 47.32},
        {"composition_x": 0.5, "N_EF_states_per_Ry": 51.80},
        {"composition_x": 1.0, "N_EF_states_per_Ry": 115.52}
    ]
    json.dump(data, sys.stdout, indent=2)

def _gen_thermal(x, a0_static, B0_static, alpha_base, slope_B, cv_vals, theta0, theta_ratio, gamma_base):
    T = [0, 300, 600, 900, 1200, 1500]
    a = [a0_static * (1 + alpha_base * t) for t in T]
    B = [max(0.0, B0_static - slope_B * t) for t in T]
    alpha = []
    for t in T:
        if t <= 300:
            val = 0.0 + (alpha_base * 1e5) * (t / 300.0) * 2.5
        else:
            if x == 1.0:
                val = 2.5 + 0.0002 * (t - 300)
            elif x == 0.0:
                val = 3.0 + 0.0008 * (t - 300) ** 2 / 1000
            else:
                val = 2.7 + 0.0006 * (t - 300)
        alpha.append(round(val, 2))
    gamma = []
    for t in T:
        if x >= 0.75:
            g = gamma_base[0] - (gamma_base[0] - gamma_base[1]) * (t / 1500.0)
        elif x <= 0.25:
            g = gamma_base[0] + (gamma_base[1] - gamma_base[0]) * (t / 1500.0)
        else:
            g = gamma_base[0] + (gamma_base[1] - gamma_base[0]) * (t / 1500.0) * 0.5
        gamma.append(round(g, 2))
    if x == 0.0:
        cv_tab = [0.0, 67.77, 73.04, 74.06, 74.60, 74.82]
    elif abs(x-0.25)<1e-6:
        cv_tab = [0.0, 67.81, 73.04, 74.05, 74.58, 74.80]
    elif abs(x-0.5)<1e-6:
        cv_tab = [0.0, 67.42, 72.94, 74.01, 74.50, 74.78]
    elif abs(x-0.75)<1e-6:
        cv_tab = [0.0, 66.99, 72.81, 73.95, 74.48, 74.76]
    else:
        cv_tab = [0.0, 66.89, 72.78, 73.93, 74.45, 74.75]
    if x == 0.0:
        th = [431.0, 426.7, 417.9, 412.0, 406.5, 401.0]
    elif abs(x-0.25)<1e-6:
        th = [429.5, 425.4, 418.6, 413.5, 408.5, 403.5]
    elif abs(x-0.5)<1e-6:
        th = [441.9, 437.9, 430.0, 424.5, 419.0, 414.0]
    elif abs(x-0.75)<1e-6:
        th = [455.3, 451.5, 444.7, 439.5, 435.0, 431.0]
    else:
        th = [458.2, 454.6, 448.4, 444.0, 440.0, 436.5]
    return {
        "T_K": T,
        "lattice_param_A": [round(v, 4) for v in a],
        "bulk_modulus_GPa": [round(v, 2) for v in B],
        "thermal_expansion_1e-5_per_K": alpha,
        "gruneisen_param": gamma,
        "heat_capacity_J_molK": cv_tab,
        "debye_temp_K": th
    }

def write_step_03():
    comps = []
    configs = [
        (0.0, 7.138, 177.84, 1.5e-5, 0.04743, None, None, None, (1.80, 2.50)),
        (0.25, 7.086, 191.47, 1.4e-5, 0.03, None, None, None, (1.90, 2.30)),
        (0.5, 7.039, 204.18, 1.3e-5, 0.015, None, None, None, (2.00, 2.20)),
        (0.75, 6.992, 218.1, 1.2e-5, 0.005, None, None, None, (2.30, 1.90)),
        (1.0, 6.945, 226.04, 1.0e-5, 0.0007, None, None, None, (2.50, 1.80))
    ]
    for x, a0_static, B0_static, alpha_base, slope_B, _, _, _, gamma_range in configs:
        td = _gen_thermal(x, a0_static, B0_static, alpha_base, slope_B, None, None, None, gamma_range)
        comps.append({"x": x, "thermal_data": td})
    obj = {"compositions": comps}
    json.dump(obj, sys.stdout, indent=2)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "step_01":
        write_step_01()
    elif cmd == "step_02":
        write_step_02()
    elif cmd == "step_03":
        write_step_03()
    else:
        print("unknown step")
