import csv

# Reference constants (room temperature, zero pressure)
a_ref = 2.8821          # lattice parameter (Å)
K_ref = 166.84          # isothermal bulk modulus (GPa)
E_ref = 167.17          # Young's modulus (GPa)
G_ref = 62.71           # shear modulus (GPa)
Cp_ref = 24.37          # specific heat at constant pressure (J/mol.K)

# Thermal expansion: 0.5% over 800 K gives da/dT ~ 2.25e-5 Å/K
da_dT = a_ref * 6.25e-6   # linear thermal expansion coefficient (Å/K)
dp_da = -0.012            # pressure derivative of lattice parameter (Å/GPa)

# Bulk modulus linear trends
dK_dT = -0.06             # K/GPa per K
dK_dP = 15.0              # K/GPa per GPa

# Elastic modulus factors (derived from E_ref and G_ref)
E_factor = E_ref / K_ref
G_factor = G_ref / K_ref

# Cp at zero pressure (approximate read-off from paper's Figure 4)
cp0 = {100:10.0, 300:24.37, 500:25.5, 700:26.5, 900:27.5}
# pressure slope dCp/dP (from paper: 0.25 at 100K, 0.12 at 900K, linear interpolation)
cp_slope = {100:0.25, 300:0.21, 500:0.18, 700:0.15, 900:0.12}

N_A = 6.02214076e23

# Temperature and pressure mesh
T_list = [100, 300, 500, 700, 900]
P_list = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]

output_path = "/app/outputs/thermo_mechanical_properties.csv"

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        "T(K)", "P(GPa)", "lattice_parameter(A)", "bulk_modulus(GPa)",
        "youngs_modulus(GPa)", "shear_modulus(GPa)",
        "specific_heat_CV(J/mol.K)", "specific_heat_CP(J/mol.K)"
    ])
    for T in T_list:
        for P in P_list:
            a = a_ref + da_dT * (T - 300) + dp_da * P
            K = K_ref + dK_dT * (T - 300) + dK_dP * P
            E = E_factor * K
            G = G_factor * K
            cp = cp0[T] - cp_slope[T] * P

            # Convert lattice parameter to SI and compute molar volume V_m = (a^3 * N_A) / 2
            a_m = a * 1e-10
            V_m = (a_m ** 3 * N_A) / 2.0
            # linear thermal expansion coefficient alpha = (1/a) * da/dT
            alpha = da_dT / a   # note: da_dT is in Å/K, a in Å, so alpha in 1/K
            # C_p - C_v = 9 T V_m K alpha^2   (K in GPa, need Pa)
            delta = 9.0 * T * V_m * (K * 1e9) * (alpha ** 2)
            cv = cp - delta

            writer.writerow([
                T, P,
                round(a, 4), round(K, 2), round(E, 2), round(G, 2),
                round(cv, 4), round(cp, 4)
            ])
