import csv
import sys

# Matrix properties
Em = 3.22  # GPa
nu_m = 0.3
rho_m = 925  # kg/m3
Gm = Em / (2 * (1 + nu_m))

# CNT properties
E11_cnt = 600
E22_cnt = 10
G12_cnt = 5
nu_cnt = 0.19
rho_cnt = 2300

# CNT efficiency parameters: (reinf_type, CNT_vol_frac) -> (theta1, theta2)
params = {
    ('short', 0.05): (0.0253, 1.0354),
    ('short', 0.10): (0.0444, 1.2853),
    ('short', 0.15): (0.0627, 1.7799),
    ('long', 0.05): (2.1587, 1.17767),
    ('long', 0.10): (1.6346, 1.4775),
    ('long', 0.15): (1.6877, 2.0590),
}

volumes = [0.0, 0.05, 0.10, 0.15]
reinf_types = ['short', 'long']

writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(['reinforcement_type', 'CNT_volume_fraction', 'E11_GPa', 'E22_GPa', 'G12_GPa', 'nu12', 'nu21', 'rho_kgm3'])

for rtype in reinf_types:
    for vf in volumes:
        if vf == 0.0:
            E11 = Em
            E22 = Em
            G12 = Gm
            nu12 = nu_m
            nu21 = nu_m
            rho = rho_m
        else:
            theta1, theta2 = params[(rtype, vf)]
            Vcnt = vf
            Vm = 1.0 - Vcnt
            E11 = theta1 * Vcnt * E11_cnt + Vm * Em
            E22 = theta2 / (Vcnt / E22_cnt + Vm / Em)
            G12 = theta2 / (Vcnt / G12_cnt + Vm / Gm)
            nu12 = Vcnt * nu_cnt + Vm * nu_m
            nu21 = nu12 * E22 / E11
            rho = Vcnt * rho_cnt + Vm * rho_m
        writer.writerow([rtype, vf, round(E11, 6), round(E22, 6), round(G12, 6), round(nu12, 6), round(nu21, 6), round(rho, 2)])
