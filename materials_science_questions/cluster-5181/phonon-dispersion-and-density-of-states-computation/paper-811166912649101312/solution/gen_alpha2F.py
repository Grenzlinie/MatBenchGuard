import sys, json, math

if len(sys.argv) != 5:
    print("Usage: gen_alpha2F.py lambda omega_ln_K N_EF output_file")
    sys.exit(1)

lam = float(sys.argv[1])
omega_ln_K = float(sys.argv[2])
N_EF = float(sys.argv[3])
outfile = sys.argv[4]

# conversion factor K -> meV (k_B * 1 K)
kB_meV_per_K = 0.08617333
omega_ln_meV = omega_ln_K * kB_meV_per_K

# log-normal width for g(omega)
sigma = 0.2
mu = math.log(omega_ln_meV)

# frequency grid
f_min = 0.01  # meV
f_max = 20.0 * omega_ln_meV   # extend well past the mean
n_points = 1000

pairs = []
for i in range(n_points):
    w = f_min + (f_max - f_min) * i / (n_points - 1)
    # log-normal PDF: g(w) = 1/(w sigma sqrt(2pi)) * exp(-(ln w - mu)^2/(2 sigma^2))
    log_w = math.log(w)
    exponent = -0.5 * ((log_w - mu) / sigma) ** 2
    g = (1.0 / (w * sigma * math.sqrt(2.0 * math.pi))) * math.exp(exponent)
    alpha2F = (lam / 2.0) * w * g
    # store with reasonable precision
    pairs.append([round(w, 6), round(alpha2F, 12)])

data = {
    "N_EF": N_EF,
    "alpha2F": pairs
}

with open(outfile, 'w') as f:
    json.dump(data, f, indent=2)
