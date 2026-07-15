import sys, json, math

def main():
    a0_ang, C11, C12, C44 = map(float, sys.argv[1:5])
    # Density
    M = 176.983   # g/mol
    Z = 4         # formula units per conventional cubic cell
    N_A = 6.02214076e23
    vol_cm3 = (a0_ang * 1e-8)**3
    rho_gcm3 = (M * Z) / (N_A * vol_cm3)
    # Elastic moduli
    B = (C11 + 2*C12) / 3.0
    G_V = (C11 - C12 + 3*C44) / 5.0
    G_R = 5 * (C11 - C12) * C44 / (4*C44 + 3*(C11 - C12))
    G = (G_V + G_R) / 2.0
    # Sound velocities (km/s)
    Vs = math.sqrt(G / rho_gcm3)
    Vp = math.sqrt((B + 4*G/3) / rho_gcm3)
    Vm = ( (2/Vs**3 + 1/Vp**3) / 3 ) ** (-1/3)
    # Debye temperature
    h = 6.62607015e-34
    k_B = 1.380649e-23
    rho_kgm3 = rho_gcm3 * 1000
    n_formula_per_m3 = N_A * rho_kgm3 / M
    atom_density = 3 * n_formula_per_m3   # 3 atoms per formula
    Vm_ms = Vm * 1000
    Theta_D = (h / k_B) * ( (3*atom_density / (4*math.pi))**(1/3) ) * Vm_ms
    # Hardness
    k_ratio = G / B
    Hv = 2 * (k_ratio**2 * G)**0.585 - 3
    result = {
        "Vs_km_s": round(Vs, 3),
        "Vp_km_s": round(Vp, 3),
        "Vm_km_s": round(Vm, 3),
        "Debye_temperature_K": round(Theta_D, 3),
        "Hardness_Hv_GPa": round(Hv, 3)
    }
    json.dump(result, sys.stdout)

if __name__ == "__main__":
    main()
