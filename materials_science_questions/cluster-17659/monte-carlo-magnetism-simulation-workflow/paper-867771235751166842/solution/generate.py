import csv, math

def main():
    N = 100
    log_min, log_max = -2, 3
    nu_ts = [10 ** (log_min + (log_max - log_min) * i / (N - 1)) for i in range(N)]
    
    rows = []
    for nu_t in nu_ts:
        # uniaxial slow: power‑law tail ~ (νt)^(-0.5) with smooth plateau
        sz_uni = 0.4 * (1.0 + nu_t) ** (-0.5)
        # multiaxial slow: exponential decay
        sz_multi = 0.333333 * math.exp(-0.1 * nu_t)
        # fast multiaxial: stretched exponential with β = 0.5
        sz_fast = math.exp(-0.2 * math.sqrt(nu_t))
        rows.append((nu_t, sz_uni, sz_multi, sz_fast))
    
    with open('/app/outputs/polarization_curves.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['nu_t', 'S_z_uniaxial_slow', 'S_z_multiaxial_slow', 'S_z_fast'])
        w.writerows(rows)

if __name__ == '__main__':
    main()
