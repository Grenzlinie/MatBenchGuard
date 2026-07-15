import csv, math, numpy as np

# Parameters
HOLLOMON = {
    'ferrite':   {'K': 581.0, 'n': 0.30},
    'austenite': {'K': 2936.0, 'n': 0.67},
    'martensite':{'K': 2652.0, 'n': 0.08},
}

OC = {
    600: {'alpha': 5.75, 'beta': 2.5, 'm': 3},
    625: {'alpha': 18.6, 'beta': 1.86, 'm': 2},
    650: {'alpha': 49.5, 'beta': 1.8, 'm': 2},
}

INITIAL = {
    600: {'V_a0': 0.318, 'V_f0': 0.682, 'V_m0': 0.000},
    625: {'V_a0': 0.379, 'V_f0': 0.621, 'V_m0': 0.000},
    650: {'V_a0': 0.443, 'V_f0': 0.528, 'V_m0': 0.029},
}

def compute_curve(T):
    params = OC[T]
    init = INITIAL[T]
    alpha, beta, m = params['alpha'], params['beta'], params['m']
    V_a0, V_f, V_m0 = init['V_a0'], init['V_f0'], init['V_m0']
    K_f, n_f = HOLLOMON['ferrite']['K'], HOLLOMON['ferrite']['n']
    K_a, n_a = HOLLOMON['austenite']['K'], HOLLOMON['austenite']['n']
    K_m, n_m = HOLLOMON['martensite']['K'], HOLLOMON['martensite']['n']

    eps_true = np.arange(0.0, 1.0+1e-6, 0.0001)  # fine grid
    f_prime = 1.0 - np.exp(-beta * (1.0 - np.exp(-alpha * eps_true))**m)
    V_a = V_a0 * (1.0 - f_prime)
    V_m = V_m0 + V_a0 * f_prime
    # ferrite stress (avoid 0**0 issue, first element 0 anyway)
    sigma_f = K_f * np.power(np.maximum(eps_true, 1e-30), n_f)
    sigma_a = K_a * np.power(np.maximum(eps_true, 1e-30), n_a)
    sigma_m = K_m * np.power(np.maximum(eps_true, 1e-30), n_m)
    sigma_c = sigma_f * V_f + sigma_a * V_a + sigma_m * V_m

    eps_eng = np.exp(eps_true) - 1.0
    sigma_eng = sigma_c * np.exp(-eps_true)

    # find instability (max engineering stress)
    idx_max = np.argmax(sigma_eng)
    UTS = sigma_eng[idx_max]
    UE = eps_eng[idx_max]

    # keep points up to instability
    eps_eng = eps_eng[:idx_max+1]
    sigma_eng = sigma_eng[:idx_max+1]

    return UTS, UE, eps_eng, sigma_eng

def main():
    temps = [600, 625, 650]
    prop_rows = []
    curve_rows = []
    for T in temps:
        UTS, UE, eps_eng, sigma_eng = compute_curve(T)
        prop_rows.append([T, round(UTS, 2), round(UE, 6)])
        for e, s in zip(eps_eng, sigma_eng):
            curve_rows.append([T, round(e, 6), round(s, 2)])

    # write predicted_properties.csv
    with open('/app/outputs/predicted_properties.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['annealing_temperature_C', 'predicted_UTS_MPa', 'predicted_uniform_elongation'])
        w.writerows(prop_rows)

    # write stress_strain_curves.csv
    with open('/app/outputs/stress_strain_curves.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['annealing_temperature_C', 'engineering_strain', 'engineering_stress_MPa'])
        w.writerows(curve_rows)

if __name__ == '__main__':
    main()
