import sys, csv, os, math
import numpy as np

e = 1.602176634e-19
hbar = 1.054571817e-34
kB = 1.380649e-23
m0 = 9.10938356e-31
m_star = 0.21 * m0
hbar_omega = 0.091 * e
T_L = 300.0
tau_p = 3e-12

# mobility model: total mobility = 1200 / (1 + (Te / 2000)**3)  (cm^2/Vs)
# Convert: 1200 cm^2/Vs -> 0.12 m^2/Vs
mu_low_SI = 0.12
Te0 = 2000.0
power = 3.0

def bose(E, T):
    return 1.0 / (np.exp(E / (kB * T)) - 1.0)

def power_per_electron(Te, n0_m3):
    # simple model: P = C * (bose(Te) - bose(T_L)) / n0_m3
    # C = (hbar_omega/tau_p) * (q0^3/(6*pi^2))
    q0 = np.sqrt(2 * m_star * hbar_omega) / hbar
    C = (hbar_omega / tau_p) * (q0**3 / (6.0 * np.pi**2))
    return C * (bose(hbar_omega, Te) - bose(hbar_omega, T_L)) / n0_m3

def total_mobility(Te):
    # returns mobility in SI (m^2/Vs)
    return mu_low_SI / (1.0 + (Te / Te0)**power)

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'both'
    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)

    if mode in ('power_dissipation', 'both'):
        n0 = 3e24  # 3e18 cm^-3 -> 3e24 m^-3
        Te_vals = np.linspace(300, 5000, 500)
        rows = []
        for Te in Te_vals:
            P = power_per_electron(Te, n0)
            rows.append([round(Te, 2), round(P, 12)])
        with open(os.path.join(outdir, 'power_dissipation.csv'), 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['electron_temperature_K', 'power_per_electron_W'])
            w.writerows(rows)

    if mode in ('velocity_field', 'both'):
        densities_cm3 = [0.5e18, 1e18, 2e18, 3e18, 5e18]
        # convert to m^-3
        densities_m3 = [d * 1e6 for d in densities_cm3]
        Te_vals = np.linspace(350, 5000, 200)
        rows = []
        for d_cm3, d_m3 in zip(densities_cm3, densities_m3):
            for Te in Te_vals:
                P = power_per_electron(Te, d_m3)
                mu = total_mobility(Te)
                if P <= 0:
                    continue
                F_si = np.sqrt(P / (e * mu))  # V/m
                v_si = mu * F_si  # m/s
                field_kV_cm = F_si * 1e-5  # V/m -> kV/cm
                v_cm_s = v_si * 100.0  # m/s -> cm/s
                rows.append([round(d_cm3, 8), round(field_kV_cm, 6), round(v_cm_s, 6)])
        # sort by density then field
        rows.sort(key=lambda r: (r[0], r[1]))
        with open(os.path.join(outdir, 'velocity_field.csv'), 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['density_cm3', 'field_kV_cm', 'drift_velocity_cm_s'])
            w.writerows(rows)

if __name__ == '__main__':
    main()
