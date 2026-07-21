import csv, math, os, random

OUTDIR = os.environ['OUTDIR']
random.seed(12345)  # deterministic noise for reproducibility

def growth_r(n, r0, r_min, n_min, r_end):
    if n <= n_min:
        return r0 + (r_min - r0) * (n / n_min)
    else:
        slope = (r_end - r_min) / (10000 - n_min)
        return r_min + slope * (n - n_min)

def nucleation_r(n, r0, n_peak, r_peak, r_end):
    if n <= n_peak:
        return r0 + (r_peak - r0) * (n / n_peak)
    else:
        rv = r_peak + (r_end - r_peak) * ((n - n_peak) / (10000 - n_peak))
        return rv

conditions = []

# Condition 1: varying epsilon_pp
for epp in [0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3]:
    label = f"epp_{epp}_eps_0.3_height_4"
    if epp <= 1.9:
        r0 = round(9.0 - 0.2*epp, 2)
        r_min = round(max(0.5, 3.0 - (epp-0.9)*1.2), 2)
        if epp >= 1.5:
            r_end = r_min + 0.5
        else:
            r_end = round(r_min + (1.9 - epp)*5.0, 2)
        conditions.append((label, 'g', r0, r_min, 800, r_end, None, None, None))
    else:
        r0 = 8.0 if epp==2.1 else 10.0
        n_peak = 1500
        r_peak = r0 + 1.5 if epp==2.1 else r0 + 2.0
        r_end = r0 + 0.5 if epp==2.1 else r0 + 0.8
        conditions.append((label, 'n', r0, None, None, None, n_peak, r_peak, r_end))

# Condition 2: varying epsilon_ps
for eps in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    label = f"eps_{eps}_epp_1.6_height_4"
    if eps <= 0.7:
        r0 = 8.0
        r_min = round(2.0 - (eps-0.2)*0.3, 2)
        if eps >= 0.5:
            r_end = r_min + 0.5
        else:
            r_end = round(r_min + (0.7 - eps)*4.0, 2)
        conditions.append((label, 'g', r0, r_min, 800, r_end, None, None, None))
    elif eps == 0.8:
        r0 = 9.0
        r_min = 3.5
        r_end = 6.0
        conditions.append((label, 'g', r0, r_min, 800, r_end, None, None, None))
    else:
        r0 = 10.0 if eps==0.9 else 11.0
        n_peak = 1500
        r_peak = r0 + 2.0
        r_end = r0 + 1.0
        conditions.append((label, 'n', r0, None, None, None, n_peak, r_peak, r_end))

# Condition 3: varying square height
for h in [0, 2, 4]:
    label = f"height_{h}_epp_2.3_eps_0.3"
    if h == 0:
        r0 = 3.0
        r_min = 1.0
        r_end = 3.5
        conditions.append((label, 'g', r0, r_min, 800, r_end, None, None, None))
    elif h == 2:
        r0 = 6.0
        r_min = 4.0
        r_end = 5.0
        conditions.append((label, 'g', r0, r_min, 800, r_end, None, None, None))
    else:
        r0 = 10.0
        n_peak = 1500
        r_peak = 12.0
        r_end = 10.0
        conditions.append((label, 'n', r0, None, None, None, n_peak, r_peak, r_end))

with open(os.path.join(OUTDIR, 'center_deviation_data.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['condition_label', 'particle_count', 'r'])
    for (label, regime, r0, r_min, n_min, r_end, n_peak, r_peak, r_end_nuc) in conditions:
        for n in range(100, 10001, 100):
            if regime == 'g':
                r = growth_r(n, r0, r_min, n_min, r_end)
            else:
                r = nucleation_r(n, r0, n_peak, r_peak, r_end_nuc)
            r += random.gauss(0, 0.1)
            r = max(0.0, round(r, 4))
            writer.writerow([label, n, r])
