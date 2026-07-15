import math, csv, json

fe = {"V0": 10.32, "K0": 285.0, "K0_prime": 4.4}
k_fcc = {"V0": 70.0, "K0": 3.0, "K0_prime": 4.0}
alloy = {"V0": 10.41, "K0": 267.0, "K0_prime": 4.5}

def P_of_V(V, V0, K0, K0p):
    eta = (V0 / V) ** (1/3)
    return (3.0/2.0) * K0 * (eta**7 - eta**5) * (1.0 + 0.75*(K0p - 4.0)*(eta**2 - 1.0))

def E_of_V(V, V0, K0, K0p):
    eta = (V0 / V) ** (1/3)
    eta2 = eta * eta
    return (9.0/16.0) * V0 * K0 * ( (eta2 - 1.0)**3 * K0p + (eta2 - 1.0)**2 * (6.0 - 4.0*eta2) )

def volume_at_pressure(P_target, params):
    V0 = params["V0"]; K0 = params["K0"]; K0p = params["K0_prime"]
    lo = 0.5 * V0
    hi = 2.0 * V0
    for _ in range(100):
        if P_of_V(lo, V0, K0, K0p) <= P_target <= P_of_V(hi, V0, K0, K0p):
            break
        if P_of_V(hi, V0, K0, K0p) < P_target:
            lo = hi
            hi *= 1.2
        else:
            hi = lo
            lo *= 0.8
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if P_of_V(mid, V0, K0, K0p) < P_target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0

P_list = [i * 0.5 for i in range(0, 101)]

vol_diff_rows, dg_static_rows, dg_entropy_rows = [], [], []
x = 0.99
T = 2000.0
kB = 8.617333262145e-5
S_mix = -kB * (x * math.log(x) + (1-x) * math.log(1-x))
T_dS = T * S_mix

for p in P_list:
    V_fe = volume_at_pressure(p, fe)
    V_k = volume_at_pressure(p, k_fcc)
    V_al = volume_at_pressure(p, alloy)
    G_fe = E_of_V(V_fe, fe["V0"], fe["K0"], fe["K0_prime"]) + p * V_fe
    G_k = E_of_V(V_k, k_fcc["V0"], k_fcc["K0"], k_fcc["K0_prime"]) + p * V_k
    G_al = E_of_V(V_al, alloy["V0"], alloy["K0"], alloy["K0_prime"]) + p * V_al
    dG = G_al - (x * G_fe + (1-x) * G_k)
    vol_diff = 100.0 * (V_al - V_fe) / V_fe
    vol_diff_rows.append([p, vol_diff])
    dg_static_rows.append([p, dG])
    dg_entropy_rows.append([p, dG - T_dS])

with open("/app/outputs/volume_difference_vs_pressure.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["pressure_GPa", "volume_difference_percent"])
    w.writerows(vol_diff_rows)

with open("/app/outputs/dG_vs_pressure_static.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["pressure_GPa", "Delta_G_eV_per_atom"])
    w.writerows(dg_static_rows)

with open("/app/outputs/dG_vs_pressure_entropy.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["pressure_GPa", "Delta_G_eV_per_atom"])
    w.writerows(dg_entropy_rows)

eos_data = {
    "pure_Fe": {"V0": fe["V0"], "K0": fe["K0"], "K0_prime": fe["K0_prime"]},
    "pure_K_fcc": {"V0": k_fcc["V0"], "K0": k_fcc["K0"], "K0_prime": k_fcc["K0_prime"]},
    "Fe_K_alloy": {"V0": alloy["V0"], "K0": alloy["K0"], "K0_prime": alloy["K0_prime"]}
}
with open("/app/outputs/eos_parameters.json", "w") as f:
    json.dump(eos_data, f, indent=2)
