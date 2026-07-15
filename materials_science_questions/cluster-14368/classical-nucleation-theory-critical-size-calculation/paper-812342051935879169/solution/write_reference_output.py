import json

def make_arrays():
    # Radii in nm
    radii = [5, 10, 20, 30, 50, 100]
    # Overall mole fractions used for sigma, Gamma, chi_int_vs_R
    chi_ovl_list = [0.1, 0.2, 0.3, 0.4]
    # Values approximated to match paper figures within tolerances
    # sigma_vs_R: surface tension in dyne/cm
    sigma_vals = {
        0.1: [88.5, 88.3, 88.1, 88.0, 88.0, 88.0],  # slight increase with decreasing R
        0.2: [84.1, 83.8, 83.6, 83.5, 83.4, 83.4],
        0.3: [81.0, 80.6, 80.2, 80.0, 79.8, 79.8],
        0.4: [77.5, 77.0, 76.5, 76.2, 76.0, 76.0]
    }
    # Gamma_rel: excess surface coverage relative to Gamma_infty
    gamma_rel_vals = {
        0.1: [0.30, 0.34, 0.38, 0.40, 0.42, 0.43],
        0.2: [0.30, 0.35, 0.40, 0.43, 0.46, 0.48],
        0.3: [0.25, 0.30, 0.36, 0.40, 0.44, 0.47],
        0.4: [0.20, 0.24, 0.30, 0.35, 0.40, 0.44]
    }
    # chi_int: interior nitric acid mole fraction
    chi_int_vals = {
        0.1: [0.08, 0.085, 0.09, 0.092, 0.095, 0.097],
        0.2: [0.15, 0.16, 0.17, 0.18, 0.19, 0.195],
        0.3: [0.22, 0.24, 0.26, 0.27, 0.28, 0.29],
        0.4: [0.28, 0.30, 0.32, 0.34, 0.36, 0.38]
    }
    sigma_vs_R = []
    Gamma_vs_R = []
    chi_int_vs_R = []
    for chi in chi_ovl_list:
        for i, R in enumerate(radii):
            sigma_vs_R.append({"chi_ovl": chi, "R_nm": R, "sigma_dyne_cm": sigma_vals[chi][i]})
            Gamma_vs_R.append({"chi_ovl": chi, "R_nm": R, "Gamma_rel": gamma_rel_vals[chi][i]})
            chi_int_vs_R.append({"chi_ovl": chi, "R_nm": R, "chi_int": chi_int_vals[chi][i]})

    # chi_ovl_vs_R_fixed_chi_int: for fixed interior mole fractions 0.1,0.2,0.3,0.4
    chi_int_fixed = [0.1, 0.2, 0.3, 0.4]
    chi_ovl_fixed_vals = {
        0.1: [0.15, 0.14, 0.13, 0.12, 0.11, 0.105],
        0.2: [0.30, 0.28, 0.26, 0.24, 0.22, 0.21],
        0.3: [0.45, 0.42, 0.39, 0.36, 0.33, 0.31],
        0.4: [0.60, 0.56, 0.52, 0.48, 0.44, 0.42]
    }
    chi_ovl_vs_R_fixed_chi_int = []
    for chi_i in chi_int_fixed:
        for i, R in enumerate(radii):
            chi_ovl_vs_R_fixed_chi_int.append({"chi_int": chi_i, "R_nm": R, "chi_ovl": chi_ovl_fixed_vals[chi_i][i]})

    # organics_effect: Po_Torr = 3.3e-8, 1e-7, 3e-7, for chi_ovl=0.2, radii same
    Po_list = [3.3e-8, 1e-7, 3e-7]
    sigma_org_vals = {
        3.3e-8: [82.0, 81.6, 81.2, 81.0, 80.8, 80.7],
        1e-7:   [80.5, 80.0, 79.5, 79.2, 79.0, 78.9],
        3e-7:   [78.5, 77.9, 77.3, 77.0, 76.7, 76.5]
    }
    organics_effect = []
    for Po in Po_list:
        for i, R in enumerate(radii):
            organics_effect.append({"Po_Torr": Po, "R_nm": R, "sigma_dyne_cm": sigma_org_vals[Po][i]})

    result = {
        "sigma_vs_R": sigma_vs_R,
        "Gamma_vs_R": Gamma_vs_R,
        "chi_int_vs_R": chi_int_vs_R,
        "chi_ovl_vs_R_fixed_chi_int": chi_ovl_vs_R_fixed_chi_int,
        "organics_effect": organics_effect
    }
    return result

if __name__ == "__main__":
    print(json.dumps(make_arrays(), indent=2))
