import csv, math, os

outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)

C = 302.0
# integration step (kV/cm)
de = 0.5

def integrate_g(E, T, T0_0, shift_rate, sigma, A0, neg_amp, neg_T0, neg_sigma):
    total = 0.0
    e = 0.0
    while e <= E:
        T0 = T0_0 + shift_rate * e
        g = A0 * math.exp(-((T - T0)**2) / (2*sigma**2))
        g += neg_amp * math.exp(-((T - neg_T0)**2) / (2*neg_sigma**2))
        total += g * de
        e += de
    return total

def compute_dT_dS(E, T, params):
    g_int = integrate_g(E, T, params["T0_0"], params["shift_rate"], params["sigma"],
                        params["A0"], params["neg_amp"], params["neg_T0"], params["neg_sigma"])
    dT = (T / C) * g_int
    dS = g_int
    return dT, dS

def calibrate(params, target_dT, target_E, T_guess):
    # adjust A0 to reach target peak ΔT at the given (E, T_guess)
    dT, _ = compute_dT_dS(target_E, T_guess, params)
    if abs(dT) > 1e-9:
        params["A0"] = params["A0"] * (target_dT / dT)
    return params

# Stress-free film parameters
sf_params = {
    "T0_0": 293.0,
    "shift_rate": 0.4,
    "sigma": 135.0,
    "A0": 0.001,          # to be calibrated
    "neg_amp": -0.0003,
    "neg_T0": 900.0,
    "neg_sigma": 80.0,
}
sf_params = calibrate(sf_params, 13.0, 500.0, 480.0)   # target peak ΔT = 13 K

# Strained film parameters (broader, lower peak)
st_params = {
    "T0_0": 250.0,
    "shift_rate": 0.35,
    "sigma": 160.0,
    "A0": 0.0008,
    "neg_amp": -0.0002,
    "neg_T0": 900.0,
    "neg_sigma": 100.0,
}
st_params = calibrate(st_params, 10.0, 500.0, 450.0)   # target peak ~10 K

fields = [50, 100, 200, 300, 400, 500, 600]
temperatures = list(range(5, 956, 25))   # 5, 30, ..., 955 K

def write_csv(filename, params):
    path = os.path.join(outdir, filename)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'field', 'deltaT', 'deltaS'])
        for T in temperatures:
            for field in fields:
                dT, dS = compute_dT_dS(field, T, params)
                dT = round(dT, 4)
                dS = round(dS, 4)
                writer.writerow([T, field, dT, dS])

write_csv('deltaT_stress_free.csv', sf_params)
write_csv('deltaT_strained.csv', st_params)
