import math, random, json, sys, os

random.seed(0)

def generate_initial_microstructure(N=5000):
    sigma_ray = math.sqrt(2.0 / math.pi)
    radii = []
    for _ in range(N):
        u = max(random.random(), 1e-10)
        r = sigma_ray * math.sqrt(-2.0 * math.log(u))
        radii.append(r)
    mean_r = sum(radii) / N
    # normalize to mean=1
    radii = [r / mean_r for r in radii]
    # generate disorientation components
    comps = []
    for _ in range(N):
        u1, u2 = random.random(), random.random()
        u1 = max(u1, 1e-10)
        r1 = 3.5 * math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        u1, u2 = random.random(), random.random()
        u1 = max(u1, 1e-10)
        r2 = 3.5 * math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        u1, u2 = random.random(), random.random()
        u1 = max(u1, 1e-10)
        r3 = 3.5 * math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        comps.append((r1, r2, r3))
    cells = [{"radius": radii[i], "r1": comps[i][0], "r2": comps[i][1], "r3": comps[i][2]} for i in range(N)]
    return cells

def generate_kinetics():
    t = [i * 0.002 for i in range(126)]  # 0 to 0.25
    X = [1.0 / (1.0 + math.exp(-35.0 * (ti - 0.14))) for ti in t]
    rho_rx = []
    mean_R_rx = []
    for ti in t:
        if ti < 0.10:
            rho = 0.0025 * (ti / 0.10) ** 2
        else:
            rho = 0.0025 * math.exp(-5.0 * (ti - 0.10))
        rho_rx.append(rho)
        if ti < 0.05:
            mr = 1.0
        else:
            mr = 1.0 + (ti - 0.05) * (0.03 / (0.25 - 0.05))
        mean_R_rx.append(mr)
    return t, X, rho_rx, mean_R_rx

def maxwell_pdf(x, sigma):
    if x < 0:
        return 0.0
    return math.sqrt(2.0 / math.pi) * (x**2) / (sigma**3) * math.exp(-x**2 / (2.0 * sigma**2))

def generate_orientation_distribution():
    bin_edges = list(range(0, 21))  # 0..20
    bin_centers = [(bin_edges[i] + bin_edges[i+1]) / 2.0 for i in range(len(bin_edges)-1)]
    sigma_all = 3.5
    sigma_rec1, sigma_rec2 = 4.5, 7.0
    w_rec1 = 0.7
    # Raw densities
    all_raw = []
    rec_raw = []
    for x in bin_centers:
        p_init = maxwell_pdf(x, sigma_all)
        p_rec = w_rec1 * maxwell_pdf(x, sigma_rec1) + (1 - w_rec1) * maxwell_pdf(x, sigma_rec2)
        all_raw.append(0.5 * p_init + 0.5 * p_rec)
        rec_raw.append(p_rec)
    # Normalize
    sum_all = sum(all_raw)
    sum_rec = sum(rec_raw)
    all_frac = [v / sum_all for v in all_raw]
    rec_frac = [v / sum_rec for v in rec_raw]
    return bin_edges, all_frac, rec_frac

def generate_boundary_moments():
    t = [i * 0.002 for i in range(126)]
    mean_theta = []
    sqrt_second = []
    for ti in t:
        if ti <= 0.05:
            mt = 7.80 - 12.0 * ti
            ss = 17.0 - 30.0 * ti
        elif ti <= 0.15:
            mt = 7.20 + (ti - 0.05) * 3.0
            ss = 15.5 + (ti - 0.05) * 10.0
        else:
            mt = 7.50
            ss = 16.5
        mean_theta.append(mt)
        sqrt_second.append(ss)
    return t, mean_theta, sqrt_second

def main():
    data = {}
    data["initial_microstructure"] = generate_initial_microstructure(5000)
    t, X, rho_rx, mean_R_rx = generate_kinetics()
    data["kinetics"] = {"t": t, "X": X, "rho_rx": rho_rx, "mean_R_rx": mean_R_rx}
    bin_edges, all_frac, recryst_frac = generate_orientation_distribution()
    data["orientation"] = {
        "bin_edges": bin_edges,
        "all_grains_area_fraction": all_frac,
        "recrystallized_area_fraction": recryst_frac
    }
    t_m, mt, ss = generate_boundary_moments()
    data["boundary"] = {"t": t_m, "mean_theta": mt, "sqrt_second_moment": ss}
    with open("/tmp/oracle_data.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
