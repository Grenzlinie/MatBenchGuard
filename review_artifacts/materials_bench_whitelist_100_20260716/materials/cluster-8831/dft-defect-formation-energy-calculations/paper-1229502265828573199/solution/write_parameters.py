import json, sys, os, math

if len(sys.argv) > 1:
    outfile = sys.argv[1]
else:
    outfile = "/app/outputs/arrhenius_parameters.json"

x = 0.02
nu = 8

four_x = 4 * x
four_x_sq = four_x * four_x
four_x_cb = four_x_sq * four_x
four_x_qd = four_x_cb * four_x
four_x_qn = four_x_qd * four_x

# TaC, stoichiometric (x=0), leading defects V_alpha & V_beta
tac_x0 = {
    "V_alpha":               {"prefactor": 1,           "formation_energy_eV": 1.28},
    "V_beta":                {"prefactor": 1,           "formation_energy_eV": 1.28},
    "A_beta":                {"prefactor": 1,           "formation_energy_eV": 13.44},
    "B_alpha":               {"prefactor": 1,           "formation_energy_eV": 5.93},
    "I_A":                   {"prefactor": 1,           "formation_energy_eV": 13.76},
    "I_B":                   {"prefactor": 1,           "formation_energy_eV": 5.47},
    "A_beta_B_alpha":        {"prefactor": 6,           "formation_energy_eV": 5.45},
    "V_alpha_B_alpha":       {"prefactor": 6,           "formation_energy_eV": 2.76},
    "V_beta_A_beta":         {"prefactor": 6,           "formation_energy_eV": 13.30},
    "V_alpha_V_beta":        {"prefactor": 6,           "formation_energy_eV": 2.41},
    "V_alpha_V_beta^2_T":    {"prefactor": 12,          "formation_energy_eV": 3.71},
    "V_alpha_V_beta^2_L":    {"prefactor": 3,           "formation_energy_eV": 3.57},
    "V_alpha_V_beta^3_IP":   {"prefactor": 12,          "formation_energy_eV": 5.05},
    "V_alpha_V_beta^3_OP":   {"prefactor": 8,           "formation_energy_eV": 5.07},
    "V_alpha_V_beta^4_IP":   {"prefactor": 3,           "formation_energy_eV": 6.44},
    "V_alpha_V_beta^4_OP":   {"prefactor": 12,          "formation_energy_eV": 6.41},
    "V_alpha_V_beta^5":      {"prefactor": 6,           "formation_energy_eV": 7.70},
    "V_alpha_V_beta^6":      {"prefactor": 1,           "formation_energy_eV": 9.06}
}

# TaC, metal‑rich (x=0.02), leading defects V_beta
tac_x002 = {
    "V_alpha":               {"prefactor": 1 / four_x,        "formation_energy_eV": 2.55},
    "V_beta":                {"prefactor": four_x,            "formation_energy_eV": 0.00},
    "A_beta":                {"prefactor": four_x_sq,         "formation_energy_eV": 10.90},
    "B_alpha":               {"prefactor": 1 / four_x_sq,     "formation_energy_eV": 8.48},
    "I_A":                   {"prefactor": four_x,            "formation_energy_eV": 12.48},
    "I_B":                   {"prefactor": 1 / four_x,        "formation_energy_eV": 6.74},
    "A_beta_B_alpha":        {"prefactor": 6,                 "formation_energy_eV": 5.45},
    "V_alpha_B_alpha":       {"prefactor": 6 / four_x_cb,     "formation_energy_eV": 6.58},
    "V_beta_A_beta":         {"prefactor": 6 * four_x_cb,     "formation_energy_eV": 9.47},
    "V_alpha_V_beta":        {"prefactor": 6,                 "formation_energy_eV": 2.41},
    "V_alpha_V_beta^2_T":    {"prefactor": 12 * four_x,       "formation_energy_eV": 2.43},
    "V_alpha_V_beta^2_L":    {"prefactor": 3 * four_x,        "formation_energy_eV": 2.29},
    "V_alpha_V_beta^3_IP":   {"prefactor": 12 * four_x_sq,    "formation_energy_eV": 2.50},
    "V_alpha_V_beta^3_OP":   {"prefactor": 8 * four_x_sq,     "formation_energy_eV": 2.52},
    "V_alpha_V_beta^4_IP":   {"prefactor": 3 * four_x_cb,     "formation_energy_eV": 2.61},
    "V_alpha_V_beta^4_OP":   {"prefactor": 12 * four_x_cb,    "formation_energy_eV": 2.58},
    "V_alpha_V_beta^5":      {"prefactor": 6 * four_x_qd,     "formation_energy_eV": 2.60},
    "V_alpha_V_beta^6":      {"prefactor": four_x_qn,          "formation_energy_eV": 2.68}
}

# HfC, stoichiometric (x=0), leading defects V_beta & I_B
sqrt_2nu = math.sqrt(2 * nu)
pow_2nu_15 = (2 * nu) ** 1.5
pow_2nu_2 = (2 * nu) ** 2
pow_2nu_25 = (2 * nu) ** 2.5

hfc_x0 = {
    "V_alpha":               {"prefactor": 1 / sqrt_2nu,          "formation_energy_eV": 5.34},
    "V_beta":                {"prefactor": sqrt_2nu,              "formation_energy_eV": 3.11},
    "A_beta":                {"prefactor": 2 * nu,                "formation_energy_eV": 16.00},
    "B_alpha":               {"prefactor": 1 / (2 * nu),          "formation_energy_eV": 6.93},
    "I_A":                   {"prefactor": sqrt_2nu,              "formation_energy_eV": 13.66},
    "I_B":                   {"prefactor": 1 / sqrt_2nu,          "formation_energy_eV": 3.11},
    "A_beta_B_alpha":        {"prefactor": 6,                     "formation_energy_eV": 5.00},
    "V_alpha_B_alpha":       {"prefactor": 6 / pow_2nu_15,       "formation_energy_eV": 5.03},
    "V_beta_A_beta":         {"prefactor": 12 * pow_2nu_15,      "formation_energy_eV": 18.05},
    "V_beta_B_alpha":        {"prefactor": 6 / sqrt_2nu,          "formation_energy_eV": 6.50},
    "V_beta_I_B":            {"prefactor": 8,                     "formation_energy_eV": 4.30},
    "V_alpha_V_beta":        {"prefactor": 6,                     "formation_energy_eV": 6.84},
    "V_alpha_V_beta^2_T":    {"prefactor": 12 * sqrt_2nu,        "formation_energy_eV": 8.65},
    "V_alpha_V_beta^2_L":    {"prefactor": 3 * sqrt_2nu,         "formation_energy_eV": 8.88},
    "V_alpha_V_beta^3_IP":   {"prefactor": 12 * (2 * nu),        "formation_energy_eV": 10.76},
    "V_alpha_V_beta^3_OP":   {"prefactor": 8 * (2 * nu),         "formation_energy_eV": 10.92},
    "V_alpha_V_beta^4_IP":   {"prefactor": 3 * pow_2nu_15,       "formation_energy_eV": 13.05},
    "V_alpha_V_beta^4_OP":   {"prefactor": 12 * pow_2nu_15,      "formation_energy_eV": 13.41},
    "V_alpha_V_beta^5":      {"prefactor": 6 * pow_2nu_2,         "formation_energy_eV": 15.75},
    "V_alpha_V_beta^6":      {"prefactor": pow_2nu_25,            "formation_energy_eV": 18.47}
}

# HfC, metal‑rich (x=0.02), leading defects V_beta
hfc_x002 = {
    "V_alpha":               {"prefactor": 1 / four_x,        "formation_energy_eV": 8.44},
    "V_beta":                {"prefactor": four_x,            "formation_energy_eV": 0.00},
    "A_beta":                {"prefactor": four_x_sq,         "formation_energy_eV": 9.79},
    "B_alpha":               {"prefactor": 1 / four_x_sq,     "formation_energy_eV": 13.14},
    "I_A":                   {"prefactor": four_x,            "formation_energy_eV": 10.55},
    "I_B":                   {"prefactor": 1 / four_x,        "formation_energy_eV": 6.21},
    "A_beta_B_alpha":        {"prefactor": 6,                 "formation_energy_eV": 5.00},
    "V_alpha_B_alpha":       {"prefactor": 6 / four_x_cb,     "formation_energy_eV": 14.34},
    "V_beta_A_beta":         {"prefactor": 12 * four_x_cb,    "formation_energy_eV": 8.73},
    "V_beta_B_alpha":        {"prefactor": 6 / four_x,        "formation_energy_eV": 9.60},
    "V_beta_I_B":            {"prefactor": 8,                 "formation_energy_eV": 4.30},
    "V_alpha_V_beta":        {"prefactor": 6,                 "formation_energy_eV": 6.84},
    "V_alpha_V_beta^2_T":    {"prefactor": 12 * four_x,       "formation_energy_eV": 5.54},
    "V_alpha_V_beta^2_L":    {"prefactor": 3 * four_x,        "formation_energy_eV": 5.77},
    "V_alpha_V_beta^3_IP":   {"prefactor": 12 * four_x_sq,    "formation_energy_eV": 4.55},
    "V_alpha_V_beta^3_OP":   {"prefactor": 8 * four_x_sq,     "formation_energy_eV": 4.71},
    "V_alpha_V_beta^4_IP":   {"prefactor": 3 * four_x_cb,     "formation_energy_eV": 3.73},
    "V_alpha_V_beta^4_OP":   {"prefactor": 12 * four_x_cb,    "formation_energy_eV": 4.10},
    "V_alpha_V_beta^5":      {"prefactor": 6 * four_x_qd,     "formation_energy_eV": 3.33},
    "V_alpha_V_beta^6":      {"prefactor": four_x_qn,          "formation_energy_eV": 2.95}
}

output = {
    "TaC": {"x=0": tac_x0, "x=0.02": tac_x002},
    "HfC": {"x=0": hfc_x0, "x=0.02": hfc_x002}
}

os.makedirs(os.path.dirname(outfile), exist_ok=True)
with open(outfile, 'w') as f:
    json.dump(output, f, indent=2)
