import sys, csv, math

def gen_spatial():
    B_vals = [0.0, 0.1, 0.3, 0.5]
    distances = list(range(64))
    total_obs = 10000
    peak1, peak2, sigma = 15, 49, 3
    # baseline flat distribution
    base = total_obs / len(distances)   # ~156.25
    raw = {}
    for b in B_vals:
        if b == 0:
            raw[b] = [base] * 64
        else:
            # scale peak height with B
            peak_scale = b * 350
            sigma_eff = sigma if b <= 0.3 else 2.5
            arr = [base] * 64
            for i, d in enumerate(distances):
                add = peak_scale * (math.exp(-((d - peak1)**2) / (2 * sigma_eff**2)) +
                                    math.exp(-((d - peak2)**2) / (2 * sigma_eff**2)))
                arr[i] += add
            raw[b] = arr
    # normalise each histogram to sum to total_obs
    print("B_ratio,distance,count")
    for b in B_vals:
        arr = raw[b]
        s = sum(arr)
        norm = total_obs / s
        counts = [int(round(v * norm)) for v in arr]
        # adjust to exact sum
        diff = total_obs - sum(counts)
        if diff != 0:
            counts[32] += diff
        for d, c in zip(distances, counts):
            if c > 0:
                print(f"{b},{d},{c}")

def gen_size():
    B_vals = [0.0, 0.1, 0.3, 0.5]
    total_obs = 10000
    sizes = list(range(1, 101))
    means = {0.0: 5, 0.1: 7, 0.3: 10, 0.5: 13}
    sigma = 5
    print("B_ratio,size,count")
    for b in B_vals:
        mu = means[b]
        # Gaussian weights
        weights = [math.exp(-((sz - mu) ** 2) / (2 * sigma ** 2)) for sz in sizes]
        w_sum = sum(weights)
        norm = total_obs / w_sum
        counts = [int(round(w * norm)) for w in weights]
        diff = total_obs - sum(counts)
        # adjust at modal index
        if diff != 0:
            idx = int(round(mu - 1))   # size index
            idx = max(0, min(idx, len(sizes) - 1))
            counts[idx] += diff
        for sz, c in zip(sizes, counts):
            if c > 0:
                print(f"{b},{sz},{c}")

def gen_order():
    vals = [(0.0, 0.0), (0.1, 0.0), (0.3, 0.0), (0.5, -0.1)]
    print("B_ratio,order_parameter")
    for b, p in vals:
        print(f"{b},{p}")

def gen_melting():
    B_vals = [0.0, 0.1, 0.3, 0.5]
    phi_vals = [i / 10.0 for i in range(1, 11)]  # 0.1 .. 1.0
    T0 = 3.5
    print("B_ratio,volume_fraction_C,melting_temperature")
    for b in B_vals:
        for phi in phi_vals:
            if b == 0:
                Tm = T0
            else:
                # increase proportional to dilution and B
                Tm = T0 + b * (1 - phi) * 2.0
            print(f"{b},{phi},{Tm:.4f}")

if __name__ == "__main__":
    arg = sys.argv[1]
    if arg == "spatial":
        gen_spatial()
    elif arg == "size":
        gen_size()
    elif arg == "order":
        gen_order()
    elif arg == "melting":
        gen_melting()
    else:
        print("Unknown argument", file=sys.stderr)
        sys.exit(1)
