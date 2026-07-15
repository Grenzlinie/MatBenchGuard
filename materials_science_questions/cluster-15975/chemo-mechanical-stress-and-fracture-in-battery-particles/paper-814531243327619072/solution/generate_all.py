import csv, sys, math

def write_thin_film():
    alphas = [0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 1.0]
    c = 0.05
    p = 0.5
    ref_alpha = 0.2
    ref_sigma = 0.0125
    w = csv.writer(sys.stdout)
    w.writerow(['alpha', 'sigma_film'])
    for a in alphas:
        s = ref_sigma * ((ref_alpha + c) / (a + c)) ** p
        w.writerow([a, round(s, 6)])

def write_spherical():
    R = 35.0
    rce_over_R = 0.43
    rce = R * rce_over_R
    tau_decay = 50.0
    theta = 2.7
    J_i = 1 + theta
    times = [i * 6 for i in range(51)]   # 0..300 step6 -> 51 points
    w = csv.writer(sys.stdout)
    w.writerow(['dimensionless_time', 'rc', 'rs'])
    for t in times:
        rc = rce + (R - rce) * math.exp(-t / tau_decay)
        frac_core = rc / R
        vol_factor = frac_core ** 3 + (1 - frac_core ** 3) * J_i
        rs = R * (vol_factor) ** (1 / 3)
        w.writerow([t, round(rc, 6), round(rs, 6)])

def write_equilibrium_core():
    data = [(10, 0.12), (15, 0.2), (20, 0.3), (30, 0.42), (40, 0.5), (50, 0.55)]
    w = csv.writer(sys.stdout)
    w.writerow(['R_over_l0', 'rce_over_R'])
    for R_o, rce_o in data:
        w.writerow([R_o, rce_o])

def write_energy_release_rate():
    # For R=30*l0, with lithiation states rc/R = 0.2, 0.5, 0.8
    states = [
        (0.2, [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55],
              [0.01, 0.025, 0.045, 0.06, 0.065, 0.06, 0.045, 0.025, 0.01, 0.005]),
        (0.5, [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5],
              [0.005, 0.012, 0.025, 0.035, 0.04, 0.038, 0.03, 0.02, 0.01, 0.005]),
        (0.8, [0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2],
              [0.002, 0.005, 0.008, 0.012, 0.015, 0.014, 0.011, 0.008, 0.004, 0.002])
    ]
    w = csv.writer(sys.stdout)
    w.writerow(['a_over_R', 'rc_over_R', 'G_normalized'])
    for rc_stat, a_list, g_list in states:
        for a, g in zip(a_list, g_list):
            w.writerow([a, rc_stat, g])

def write_gmax_vs_R():
    # G_max linear with R, such that at R=28*l0, G_max = 0.1
    slope = 0.1 / 28.0
    sizes = [10, 15, 20, 30, 40, 50]
    w = csv.writer(sys.stdout)
    w.writerow(['R_over_l0', 'G_max_normalized'])
    for R_o in sizes:
        gmax = slope * R_o
        w.writerow([R_o, round(gmax, 6)])

if __name__ == '__main__':
    task = sys.argv[1]
    {'thin_film': write_thin_film,
     'spherical': write_spherical,
     'equilibrium': write_equilibrium_core,
     'energy': write_energy_release_rate,
     'gmax': write_gmax_vs_R}[task]()
