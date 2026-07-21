import sys, math, csv

def u(t, t1, t2, t3, k):
    """Trapezoidal area ratio u(t) = f(t)/F."""
    if t <= 0:
        return 0.0
    if t <= t1:
        return (k * k / t1) * t if t1 > 0 else 0.0
    if t <= t2:
        return k * k
    if t <= t3:
        # linear decrease
        seg = t3 - t2
        return k * k * (t3 - t) / seg if seg > 0 else 0.0
    return 0.0

def compute(cv, k, epsilon=1e-15):
    """Compute max response and ratio for given coefficient of velocity cv and dimension k."""
    # Fixed physical parameters
    v = 1.0
    R = 1.0
    mu_x = 0.05 * 0.1
    factor = math.exp(mu_x) - 1.0   # e^{μ x} - 1
    # Time constant from cv = 2R/(vτ) => τ = 2R/(v*cv)
    tau = 2.0 * R / (v * cv)
    t1 = 2.0 * k * R / v
    t2 = 2.0 * R / v
    t3 = 2.0 * (R + k * R) / v
    k2 = k * k
    if k2 < epsilon:
        return 0.0, 0.0

    # Numerical integration to find V_max
    dt = min(0.005, tau / 200.0, (t3 + 3 * tau) / 5000.0)
    T_max = t3 + 3 * tau
    n = int(T_max / dt) + 2
    V_max = 0.0
    integral = 0.0
    t_prev = 0.0
    for i in range(1, n):
        t = i * dt
        ds = t - t_prev
        u_prev = u(t_prev, t1, t2, t3, k)
        u_curr = u(t, t1, t2, t3, k)
        u_avg = (u_prev + u_curr) * 0.5
        exp_prev = math.exp(t_prev / tau)
        exp_curr = math.exp(t / tau)
        integrand = (exp_prev * u_prev + exp_curr * u_curr) * 0.5 * ds
        integral += integrand
        V = math.exp(-t / tau) * integral / tau
        if V > V_max:
            V_max = V
        t_prev = t

    delta_max = V_max * factor
    # stationary max: V0 = k^2 (response to constant u = k^2)
    ratio = V_max / k2
    return delta_max, ratio

def main():
    mode = sys.argv[1]
    outpath = sys.argv[2]

    cv_list = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    k_list = [0.1, 0.5, 1.0, 2.0, 5.0]

    if mode == "csv":
        with open(outpath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["coefficient_of_velocity", "coefficient_of_dimension", "delta_N_N_max", "ratio_v_to_v0"])
            for cv in cv_list:
                for k in k_list:
                    delta, ratio = compute(cv, k)
                    writer.writerow([cv, k, delta, ratio])
    elif mode == "txt":
        # compute threshold and worst-case reduction
        # cache results
        data = {}
        for cv in cv_list:
            for k in k_list:
                delta, ratio = compute(cv, k)
                data[(cv, k)] = (delta, ratio)
        sorted_cv = sorted(cv_list)
        threshold = None
        for i, cv0 in enumerate(sorted_cv):
            ref_ratios = {}
            for k in k_list:
                ref_ratios[k] = data[(cv0, k)][1]
            ok = True
            for cv_other in sorted_cv[i+1:]:
                for k in k_list:
                    ratio_other = data[(cv_other, k)][1]
                    if abs((ratio_other - ref_ratios[k]) / ref_ratios[k]) > 0.01:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                threshold = cv0
                break
        if threshold is None:
            threshold = max(sorted_cv)
        # worst-case at threshold
        min_ratio = float('inf')
        for k in k_list:
            _, ratio = data[(threshold, k)]
            if ratio < min_ratio:
                min_ratio = ratio
        worst_case = min_ratio
        with open(outpath, "w") as f:
            f.write(f"threshold = {threshold}\n")
            f.write(f"worst_case_reduction = {worst_case:.6f}\n")
    else:
        print("Unknown mode", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()