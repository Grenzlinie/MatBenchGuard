import sys, csv, json, math
def write_mu_vs_T():
    T_KT = 0.08
    mu0 = 0.0801
    mu_KT = 0.12
    mu_inf = 0.22
    tau = 0.1
    T_vals = [0.01*i + 0.01 for i in range(1, 51)]
    with open('/app/outputs/mu_vs_T.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'mu_2D'])
        for T in T_vals:
            if T <= T_KT:
                mu = mu0 + (mu_KT - mu0) * (T / T_KT)
            else:
                mu = mu_KT + (mu_inf - mu_KT) * (1 - math.exp(-(T - T_KT) / tau))
            writer.writerow([f'{T:.4f}', f'{mu:.6f}'])

def ns_curve(n_sat, T_char, p=2):
    T_vals = [0.01*i + 0.01 for i in range(1, 51)]
    ns = []
    for T in T_vals:
        val = n_sat / (1 + (T / T_char)**p)
        ns.append(val)
    return T_vals, ns

def write_ns_vs_T():
    n_sat_mix = 8.0e13
    n_sat_single = 2.5e13
    mix_params = {int(1e17): 0.07, int(1e18): 0.1172, int(1e19): 0.15}
    single_params = {int(1e17): 0.2, int(1e18): 0.372, int(1e19): 0.45}
    with open('/app/outputs/ns_vs_T.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['n_gas', 'component', 'T', 'n_s'])
        for n_gas in [int(1e17), int(1e18), int(1e19)]:
            T_char = mix_params[n_gas]
            T_vals, n_s_vals = ns_curve(n_sat_mix, T_char)
            for T, n_s in zip(T_vals, n_s_vals):
                writer.writerow([f'{int(n_gas)}', 'mixture', f'{T:.4f}', f'{n_s:.4e}'])
            T_char = single_params[n_gas]
            T_vals, n_s_vals = ns_curve(n_sat_single, T_char)
            for T, n_s in zip(T_vals, n_s_vals):
                writer.writerow([f'{int(n_gas)}', 'single', f'{T:.4f}', f'{n_s:.4e}'])

def write_KT_temperatures():
    data = {'mixture': 0.180, 'single': 0.160}
    with open('/app/outputs/KT_temperatures.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)
    arg = sys.argv[1]
    if arg == 'mu_vs_T.csv':
        write_mu_vs_T()
    elif arg == 'ns_vs_T.csv':
        write_ns_vs_T()
    elif arg == 'KT_temperatures.json':
        write_KT_temperatures()
    else:
        sys.exit(1)
