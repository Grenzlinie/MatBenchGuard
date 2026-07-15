import csv, sys, math

def generate(molecule):
    writer = csv.writer(sys.stdout)
    writer.writerow([
        "phi_deg", "a_xx", "a_yy", "a_zz", "a_bar",
        "kappa_xx_Na", "kappa_yy_Na", "kappa_zz_Na", "kappa_bar_Na",
        "kappa_xx_355", "kappa_yy_355", "kappa_zz_355", "kappa_bar_355",
    ])
    if molecule == 'ethane':
        phis = range(0, 61, 10)
    else:
        phis = range(0, 181, 15)
    for phi_deg in phis:
        phi = math.radians(phi_deg)
        if molecule == 'hydrazine':
            A = 0.17
            a_xx = A * math.sin(2 * phi)
            a_zz = -A * math.sin(2 * phi)
            a_yy = 0.02 * math.sin(phi) * math.sin(2 * phi)
            a_bar = (a_xx + a_yy + a_zz) / 3.0
            K_Na = 0.05
            kappa_xx_Na = K_Na * math.sin(2 * phi)
            kappa_zz_Na = -K_Na * math.sin(2 * phi)
            kappa_yy_Na = 0.001 * math.sin(2 * phi)
            kappa_bar_Na = (kappa_xx_Na + kappa_yy_Na + kappa_zz_Na) / 3.0
            K_355 = 0.06
            kappa_xx_355 = K_355 * math.sin(2 * phi)
            kappa_zz_355 = -K_355 * math.sin(2 * phi)
            kappa_yy_355 = 0.001 * math.sin(2 * phi)
            kappa_bar_355 = (kappa_xx_355 + kappa_yy_355 + kappa_zz_355) / 3.0
        elif molecule == 'boranylborane':
            A = 0.12
            a_xx = A * math.sin(2 * phi)
            a_zz = -A * math.sin(2 * phi)
            a_yy = 0.0
            a_bar = (a_xx + a_yy + a_zz) / 3.0
            K_Na = 0.04
            kappa_xx_Na = K_Na * math.sin(2 * phi)
            kappa_zz_Na = -K_Na * math.sin(2 * phi)
            kappa_yy_Na = 0.0
            kappa_bar_Na = (kappa_xx_Na + kappa_yy_Na + kappa_zz_Na) / 3.0
            K_355 = 0.045
            kappa_xx_355 = K_355 * math.sin(2 * phi)
            kappa_zz_355 = -K_355 * math.sin(2 * phi)
            kappa_yy_355 = 0.0
            kappa_bar_355 = (kappa_xx_355 + kappa_yy_355 + kappa_zz_355) / 3.0
        elif molecule == 'ethane':
            A = 0.10
            a_xx = A * math.sin(3 * phi)
            a_zz = -A * math.sin(3 * phi)
            a_yy = 0.005 * math.sin(3 * phi)
            a_bar = (a_xx + a_yy + a_zz) / 3.0
            K_Na = 0.03
            kappa_xx_Na = K_Na * math.sin(3 * phi)
            kappa_zz_Na = -K_Na * math.sin(3 * phi)
            kappa_yy_Na = 0.002 * math.sin(3 * phi)
            kappa_bar_Na = (kappa_xx_Na + kappa_yy_Na + kappa_zz_Na) / 3.0
            K_355 = 0.035
            kappa_xx_355 = K_355 * math.sin(3 * phi)
            kappa_zz_355 = -K_355 * math.sin(3 * phi)
            kappa_yy_355 = 0.002 * math.sin(3 * phi)
            kappa_bar_355 = (kappa_xx_355 + kappa_yy_355 + kappa_zz_355) / 3.0
        writer.writerow([
            phi_deg,
            f"{a_xx:.10f}", f"{a_yy:.10f}", f"{a_zz:.10f}", f"{a_bar:.10f}",
            f"{kappa_xx_Na:.10f}", f"{kappa_yy_Na:.10f}", f"{kappa_zz_Na:.10f}", f"{kappa_bar_Na:.10f}",
            f"{kappa_xx_355:.10f}", f"{kappa_yy_355:.10f}", f"{kappa_zz_355:.10f}", f"{kappa_bar_355:.10f}",
        ])

if __name__ == "__main__":
    generate(sys.argv[1])
