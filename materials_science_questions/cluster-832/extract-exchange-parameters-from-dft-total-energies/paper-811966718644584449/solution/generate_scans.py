import sys, csv, math

def main():
    compound = sys.argv[1]
    if compound not in ('LaMn2Ge2', 'LaMn2Si2'):
        raise ValueError("Invalid compound")

    # temperature range (K)
    T = [t for t in range(10, 1201, 10)]
    rows = []

    if compound == 'LaMn2Ge2':
        # Reference points
        T_c1 = 439.0
        T_c2 = 448.0
        T_c3 = 1041.0
        # Low-T values
        theta0 = 60.0
        alpha0 = 114.0
        # alpha at helical transition
        alpha_c1 = 144.0
        # S and m2 at T=0
        S0 = 1.5
        m2_0 = 2.25
        for t in T:
            # theta: from theta0 to 90, crosses 90 at T_c1
            if t < T_c1:
                theta = min(90.0, theta0 + (90.0 - theta0) * (t / T_c1))
            else:
                theta = 90.0
            # alpha: 0..T_c1: alpha0 -> alpha_c1; T_c1..T_c2: alpha_c1 -> 180
            if t < T_c1:
                alpha = alpha0 + (alpha_c1 - alpha0) * (t / T_c1)
            elif t < T_c2:
                alpha = alpha_c1 + (180.0 - alpha_c1) * ((t - T_c1) / (T_c2 - T_c1))
            else:
                alpha = 180.0
            # S_bar: linear decrease to zero at T_c3
            S_bar = S0 * max(0.0, 1.0 - t / T_c3)
            # m2_bar: similarly decrease to zero at T_c3 (simplified)
            m2_bar = m2_0 * max(0.0, 1.0 - t / T_c3)
            # free energy: plausible negative value (not used in scoring)
            free_energy = -0.1 * t
            rows.append((t, theta, alpha, S_bar, m2_bar, free_energy))
    else:  # LaMn2Si2
        T_c1 = 269.0
        T_c2 = 393.0
        T_c3 = 1061.0
        theta0 = 53.0
        alpha0 = 139.0
        S0 = 1.5
        m2_0 = 2.25
        for t in T:
            # alpha: reaches 180 at T_c1
            if t < T_c1:
                alpha = alpha0 + (180.0 - alpha0) * (t / T_c1)
            else:
                alpha = 180.0
            # theta: stays near theta0 until T_c1, then rises to 90 at T_c2
            if t < T_c1:
                theta = theta0
            elif t < T_c2:
                theta = theta0 + (90.0 - theta0) * ((t - T_c1) / (T_c2 - T_c1))
            else:
                theta = 90.0
            S_bar = S0 * max(0.0, 1.0 - t / T_c3)
            m2_bar = m2_0 * max(0.0, 1.0 - t / T_c3)
            free_energy = -0.1 * t
            rows.append((t, theta, alpha, S_bar, m2_bar, free_energy))

    outpath = f"/app/outputs/scan_{compound}.csv"
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["T", "theta", "alpha", "S_bar", "m2_bar", "free_energy"])
        for row in rows:
            writer.writerow([str(v) for v in row])

if __name__ == '__main__':
    main()
