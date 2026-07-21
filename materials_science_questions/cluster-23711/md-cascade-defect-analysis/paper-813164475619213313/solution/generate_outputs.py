import sys
import math
import csv

def write_cascade(out):
    writer = csv.writer(out)
    writer.writerow(["time_ps", "kinetic_norm", "potential_norm"])
    T0 = 0.35  # equipartition time (ps)
    for i in range(101):
        t = i * 0.02
        if t <= T0:
            base_k = 1.0 - 0.5 * (t / T0)
        else:
            base_k = 0.5
        potential_norm = 1.0 - base_k   # energy shift so potential_norm starts at 0
        noise_k = 0.01 * math.sin(2 * math.pi * t / 0.3)
        noise_p = -noise_k
        kinetic_norm = base_k + noise_k
        potential_norm = potential_norm + noise_p
        writer.writerow([round(t, 2), round(kinetic_norm, 6), round(potential_norm, 6)])

def write_thermal_spike(out):
    writer = csv.writer(out)
    writer.writerow(["time_ps", "kinetic_norm", "potential_norm"])
    for i in range(101):
        t = i * 0.02
        kin = 0.98 + 0.02 * math.sin(2 * math.pi * t / 0.7)
        pot = 0.02 + 0.01 * math.cos(2 * math.pi * t / 0.5)
        writer.writerow([round(t, 2), round(kin, 6), round(pot, 6)])

def write_max_volume(out):
    writer = csv.writer(out)
    writer.writerow(["energy_keV", "max_volume_nm3"])
    pi = math.pi
    e = math.e
    C = math.sqrt(3 / (2 * pi * e**3))
    kB = 1.380649e-23
    Tm = 3120.0
    Teq = 700.0
    deltaT = Tm - Teq
    rho_mass_g_cm3 = 10.92   # approximate density of UO2 at 700 K from Fink (2000)
    rho_mass_kg_m3 = rho_mass_g_cm3 * 1000.0
    M = 0.27003  # kg/mol (UO2)
    N_A = 6.02214076e23
    n = (rho_mass_kg_m3 / M) * N_A   # atomic number density (atoms/m^3)
    denom = n * 1.5 * kB * deltaT
    energies = [0.2, 1.0, 5.0, 10.0, 20.0]
    for E_keV in energies:
        E_J = E_keV * 1.602176634e-16   # keV to J
        V_m3 = C * E_J / denom
        V_nm3 = V_m3 * 1e27
        writer.writerow([E_keV, round(V_nm3, 6)])

def main():
    step = sys.argv[1]
    if step == "step_01":
        write_cascade(sys.stdout)
    elif step == "step_02":
        write_thermal_spike(sys.stdout)
    elif step == "step_03":
        write_max_volume(sys.stdout)
    else:
        raise ValueError("Unknown step")

if __name__ == "__main__":
    main()
