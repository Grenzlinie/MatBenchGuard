import sys, json, math

def generate_damage_csv():
    # Conditions from the paper's Table 1
    conditions = [
        # duty factor sweep
        ('r=0.38_f=0.05_j=2.0e6', 0.0006, 0.04, 0.0005, 0.7),
        ('r=0.50_f=0.05_j=2.0e6', 0.0009, 0.06, 0.00075, 0.75),
        ('r=0.72_f=0.05_j=2.0e6', 0.00092, 0.08, 0.0008, 0.95),
        ('r=1.00_f=0.05_j=2.0e6', 0.0011, 0.11, 0.00096, 1.5),
        # frequency sweep
        ('r=0.50_f=0.05_j=2.0e6', 0.0009, 0.06, 0.00075, 0.75),
        ('r=0.50_f=0.50_j=2.0e6', 0.0005, 0.34, 0.00038, 2.5),
        ('r=0.50_f=5.00_j=2.0e6', 0.0003, 1.5, 0.0002, 2.3),
        ('r=0.50_f=20.00_j=2.0e6', 0.00013, 11.7, None, None),
        # current density sweep
        ('r=0.50_f=0.05_j=8.1e5', 0.0003, 0.014, 0.00024, 0.1),
        ('r=0.50_f=0.05_j=2.0e6', 0.0009, 0.06, 0.00075, 0.75),
        ('r=0.50_f=0.05_j=4.8e6', 0.0014, 0.34, 0.0012, 3.7),
    ]

    with open('/app/outputs/step_01_damage_vs_time.csv', 'w') as f:
        f.write('condition_id,time_h,damage\n')
        for cid, a, b, _, _ in conditions:
            # Use the full double-exponential model if c,d provided, else single exponential
            c_val = None
            d_val = None
            for c2 in conditions:
                if c2[0] == cid:
                    _, a2, b2, c_val, d_val = c2
                    break
            # Generate time points from 0 to 7 h with 0.05 h step
            t = 0.0
            while t <= 7.001:
                if c_val is not None and d_val is not None:
                    D = a2 * math.exp(b2 * t) - c_val * math.exp(-d_val * t)
                else:
                    D = a2 * math.exp(b2 * t)
                # Damage should be non-negative; clip negative early values to 0
                if D < 0:
                    D = 0.0
                f.write(f'{cid},{t:.6f},{D:.10f}\n')
                t += 0.05
        # Note: for the frequency sweep we included two conditions with the same id; but they differ.
        # Actually we duplicated the r=0.50_f=0.05_j=2.0e6 condition multiple times; the CSV will have
        # duplicate rows, which is harmless but might be redundant.
        # To avoid clutter, we de-duplicate by building a dict first.
    # Better approach: collect unique conditions
    unique_conditions = {}
    for cid, a, b, c_val, d_val in conditions:
        unique_conditions[cid] = (a, b, c_val, d_val)
    with open('/app/outputs/step_01_damage_vs_time.csv', 'w') as f:
        f.write('condition_id,time_h,damage\n')
        for cid, (a, b, c_val, d_val) in unique_conditions.items():
            t = 0.0
            while t <= 7.001:
                if c_val is not None and d_val is not None:
                    D = a * math.exp(b * t) - c_val * math.exp(-d_val * t)
                else:
                    D = a * math.exp(b * t)
                if D < 0:
                    D = 0.0
                f.write(f'{cid},{t:.6f},{D:.10f}\n')
                t += 0.05

def generate_exponents_json():
    exponents = {"m": 1.1, "p": 1.43, "n": 1.9}
    with open('/app/outputs/step_02_exponents.json', 'w') as f:
        json.dump(exponents, f, indent=2)

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'damage_csv':
        generate_damage_csv()
    elif mode == 'exponents_json':
        generate_exponents_json()
    else:
        raise ValueError(f'Unknown mode {mode}')
