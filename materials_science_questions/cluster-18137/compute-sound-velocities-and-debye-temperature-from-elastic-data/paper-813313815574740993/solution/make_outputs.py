import json

# Paper reference values from Tables 2,3,4

# Elastic constants Cij (GPa)
# LaNi2P2
c11_p2 = 201.6
c12_p2 = 115.6
c13_p2 = 15.2
c33_p2 = 102.3
c44_p2 = 115.6
c66_p2 = 97.4
# LaNi2Ge2
c11_ge2 = 151.7
c12_ge2 = 87.3
c13_ge2 = 40.0
c33_ge2 = 125.7
c44_ge2 = 87.3
c66_ge2 = 90.1

# Polycrystalline moduli (GPa) from Table 3
# LaNi2P2
B_V_p2 = 64.4
B_R_p2 = 60.3
B_VRH_p2 = 62.4
G_V_p2 = 96.9
G_R_p2 = 89.2
G_VRH_p2 = 93.1
Y_p2 = 186.4
nu_p2 = 0.0017
G_over_B_p2 = 1.49

# LaNi2Ge2
B_V_ge2 = 59.1
B_R_ge2 = 64.7
B_VRH_ge2 = 61.9
G_V_ge2 = 78.1
G_R_ge2 = 70.8
G_VRH_ge2 = 74.4
Y_ge2 = 159.4
nu_ge2 = 0.0709
G_over_B_ge2 = 1.20

# Density and molar mass
# Atomic masses (g/mol)
La = 138.9055
Ni = 58.6934
P = 30.973762
Ge = 72.63

molar_mass_p2 = La + 2*Ni + 2*P
molar_mass_ge2 = La + 2*Ni + 2*Ge

# Cell volumes from VASP optimization (Table 1) in Å³
V_p2 = 153.66   # Å³
V_ge2 = 175.43  # Å³

# Density = molar_mass / (N_A * V_cell)  with V_cell in cm³, N_A = 6.02214076e23
NA = 6.02214076e23
# Convert volume to cm³: 1 Å³ = 1e-24 cm³
density_p2 = molar_mass_p2 / (NA * V_p2 * 1e-24)  # g/cm³
density_ge2 = molar_mass_ge2 / (NA * V_ge2 * 1e-24)

elastic = {
  "LaNi2P2": {
    "C11": c11_p2, "C12": c12_p2, "C13": c13_p2, "C33": c33_p2, "C44": c44_p2, "C66": c66_p2,
    "B_V": B_V_p2, "B_R": B_R_p2, "B_VRH": B_VRH_p2,
    "G_V": G_V_p2, "G_R": G_R_p2, "G_VRH": G_VRH_p2,
    "Y": Y_p2, "nu": nu_p2, "G_over_B": G_over_B_p2,
    "density_gcm3": round(density_p2, 3),
    "molar_mass_gmol": round(molar_mass_p2, 2)
  },
  "LaNi2Ge2": {
    "C11": c11_ge2, "C12": c12_ge2, "C13": c13_ge2, "C33": c33_ge2, "C44": c44_ge2, "C66": c66_ge2,
    "B_V": B_V_ge2, "B_R": B_R_ge2, "B_VRH": B_VRH_ge2,
    "G_V": G_V_ge2, "G_R": G_R_ge2, "G_VRH": G_VRH_ge2,
    "Y": Y_ge2, "nu": nu_ge2, "G_over_B": G_over_B_ge2,
    "density_gcm3": round(density_ge2, 3),
    "molar_mass_gmol": round(molar_mass_ge2, 2)
  }
}

with open("/app/outputs/elastic_and_moduli.json", "w") as f:
    json.dump(elastic, f, indent=2)

# Thermophysical data from Table 4 and Table 2
# Sound velocities (m/s)
vl_p2 = 5306.6
vt_p2 = 3753.9
vm_p2 = 4070.0
theta_p2 = 487.4

vl_ge2 = 4698.1
vt_ge2 = 3205.2
vm_ge2 = 3487.0
theta_ge2 = 386.4

# Sommerfeld coefficient gamma (mJ K^-2 mol^-1) converted to J K^-2 mol^-1
gamma_p2 = 4.556e-3
gamma_ge2 = 8.750e-3

# Lattice specific heat coefficient beta (mJ K^-4 mol^-1) converted to J K^-4 mol^-1
beta_p2 = 0.0839e-3
beta_ge2 = 0.1683e-3

T_list = [10, 20, 50, 100, 150]

def heat_cap(gamma, beta):
    return [{"T": T, "Cp": round(gamma * T + beta * (T**3), 5)} for T in T_list]

thermo = {
    "LaNi2P2": {
        "v_l": vl_p2, "v_t": vt_p2, "v_m": vm_p2,
        "theta_D": theta_p2,
        "heat_capacity": heat_cap(gamma_p2, beta_p2)
    },
    "LaNi2Ge2": {
        "v_l": vl_ge2, "v_t": vt_ge2, "v_m": vm_ge2,
        "theta_D": theta_ge2,
        "heat_capacity": heat_cap(gamma_ge2, beta_ge2)
    }
}

with open("/app/outputs/thermophysical.json", "w") as f:
    json.dump(thermo, f, indent=2)
