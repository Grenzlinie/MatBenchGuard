import json, math

# Physical constants
h = 6.62607015e-34
k = 1.380649e-23
N_A = 6.02214076e23

# Atomic weights in g/mol
AW = {"W": 183.84, "Re": 186.207, "Os": 190.23}

def avg_mass(x, y):
    return (1 - x - y) * AW["W"] + x * AW["Re"] + y * AW["Os"]  # g/mol

def compute_derived(a, C11, C12, C44, re, os):
    Cprime = (C11 - C12) / 2.0
    B = (C11 + 2 * C12) / 3.0
    # Hill shear modulus
    GV = (C11 - C12 + 3 * C44) / 5.0
    GR = 5 * (C11 - C12) * C44 / (4 * C44 + 3 * (C11 - C12))
    G = (GV + GR) / 2.0
    # Young's modulus
    E = 9 * B * G / (3 * B + G)
    # Poisson ratio
    nu = (3 * B - 2 * G) / (2 * (3 * B + G))
    B_over_G = B / G
    cp = C12 - C44
    AZ = C44 / Cprime
    # Debye temperature
    M_avg = avg_mass(re, os) * 1e-3  # kg/mol
    a_m = a * 1e-10
    V_atom = a_m ** 3 / 2.0
    rho = (M_avg / N_A) / V_atom
    v_t = math.sqrt(G * 1e9 / rho)
    v_l = math.sqrt((B + 4 * G / 3) * 1e9 / rho)
    vm = ((1.0 / 3) * (2.0 / v_t ** 3 + 1.0 / v_l ** 3)) ** (-1.0 / 3)
    n = N_A * rho / M_avg
    prefactor = (3 * n / (4 * math.pi)) ** (1.0 / 3)
    theta = (h / k) * prefactor * vm
    return {
        "shear_modulus_Hill_GPa": round(G, 2),
        "youngs_modulus_GPa": round(E, 2),
        "poisson_ratio": round(nu, 4),
        "B_over_G": round(B_over_G, 4),
        "cauchy_pressure_GPa": round(cp, 2),
        "debye_temperature_K": round(theta, 2),
        "Zener_anisotropy_AZ": round(AZ, 4),
        "Cprime_GPa": round(Cprime, 2),
        "bulk_modulus_GPa": round(B, 2),
    }

# Single‑crystal data for required compositions (from paper Tables 1,3,5 and interpolations)
data = [
    {"Re": 0.00, "Os": 0.00, "a": 3.195, "C11": 536.7, "C12": 179.9, "C44": 168.6, "ideal_tensile_strength": 26.3},
    {"Re": 0.03, "Os": 0.00, "a": 3.192, "C11": 535.3, "C12": 184.4, "C44": 168.4, "ideal_tensile_strength": 25.4},
    {"Re": 0.06, "Os": 0.00, "a": 3.1902, "C11": 533.1, "C12": 187.2, "C44": 170.26, "ideal_tensile_strength": 24.4},
    {"Re": 0.00, "Os": 0.03, "a": 3.188, "C11": 528.4, "C12": 189.0, "C44": 172.2, "ideal_tensile_strength": 24.1},
    {"Re": 0.00, "Os": 0.06, "a": 3.182, "C11": 520.2, "C12": 197.5, "C44": 176.0, "ideal_tensile_strength": 21.9},
    {"Re": 0.03, "Os": 0.03, "a": 3.188, "C11": 527.0, "C12": 192.6, "C44": 172.9, "ideal_tensile_strength": 23.2},
]

# SSH parameters from Table 6 (binary compositions only)
ssh_data = {
    (0.00, 0.06): {"eps_L": 3.698, "SSH": 0.189},
    (0.06, 0.00): {"eps_L": 2.605, "SSH": 0.118},
    (0.00, 0.03): {"eps_L": 3.768, "SSH": 0.1205},
    (0.03, 0.00): {"eps_L": 2.728, "SSH": 0.077},
}

elastic = []
derived = []

for d in data:
    re = d["Re"]
    os = d["Os"]
    a = d["a"]
    C11 = d["C11"]
    C12 = d["C12"]
    C44 = d["C44"]
    der = compute_derived(a, C11, C12, C44, re, os)

    elastic.append({
        "Re": re,
        "Os": os,
        "lattice_constant_Angstrom": round(a, 4),
        "bulk_modulus_GPa": der["bulk_modulus_GPa"],
        "C11_GPa": round(C11, 2),
        "C12_GPa": round(C12, 2),
        "C44_GPa": round(C44, 2),
        "Cprime_GPa": der["Cprime_GPa"],
    })

    base = {
        "Re": re,
        "Os": os,
        "shear_modulus_Hill_GPa": der["shear_modulus_Hill_GPa"],
        "youngs_modulus_GPa": der["youngs_modulus_GPa"],
        "poisson_ratio": der["poisson_ratio"],
        "B_over_G": der["B_over_G"],
        "cauchy_pressure_GPa": der["cauchy_pressure_GPa"],
        "debye_temperature_K": der["debye_temperature_K"],
        "Zener_anisotropy_AZ": der["Zener_anisotropy_AZ"],
        "cleavage_ratio_110": None,
        "solid_solution_hardening_misfit_epsilon_L": None,
        "solid_solution_hardening_factor": None,
        "fcc_bcc_SED_J_per_atom": None,
        "estimated_ideal_tensile_strength_001_GPa": d.get("ideal_tensile_strength"),
    }

    key = (re, os)
    if key in ssh_data:
        base["solid_solution_hardening_misfit_epsilon_L"] = round(ssh_data[key]["eps_L"], 4)
        base["solid_solution_hardening_factor"] = round(ssh_data[key]["SSH"], 4)

    derived.append(base)

with open("/app/outputs/single_crystal_elastic_constants.json", "w") as f:
    json.dump(elastic, f, indent=2)

with open("/app/outputs/derived_properties.json", "w") as f:
    json.dump(derived, f, indent=2)