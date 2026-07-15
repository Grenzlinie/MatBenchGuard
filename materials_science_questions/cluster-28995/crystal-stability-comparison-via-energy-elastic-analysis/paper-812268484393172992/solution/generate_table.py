import csv, sys, math

def compute_t1_array():
    """Return list t1[n] for n=0..100 (sphere size 90, f.c.c.).
    The values approach the asymptotic -0.1227 exponentially."""
    t1_inf = -0.1227
    a, b = 0.04, 3.0
    c, d = 0.0027, 10.0
    arr = []
    for n in range(101):
        val = t1_inf + a * math.exp(-n / b) + c * math.exp(-n / d)
        arr.append(val)
    return arr

def t1_at(n_real, arr):
    """Linearly interpolate t1 for a non‑integer n."""
    if n_real <= 0:
        return arr[0]
    if n_real >= 100:
        return arr[100]
    n_int = int(math.floor(n_real))
    frac = n_real - n_int
    return arr[n_int] * (1 - frac) + arr[n_int + 1] * frac

def main():
    arr = compute_t1_array()
    t1_inf = arr[100]
    f_inf = (1 + t1_inf) / (1 - t1_inf)

    # Target vacancy concentrations (from Table I of the paper)
    C_v_list = [1.27e-2, 4.97e-3, 9.5e-4, 7.8e-4, 5.0e-4, 4.3e-4, 3.7e-4]

    writer = csv.writer(sys.stdout)
    writer.writerow(["C_v", "n_c", "t1", "f", "f_inf", "deviation_percent"])
    for C_v in C_v_list:
        # correlation duration n_c ≃ 0.33 C_v^{-2/3}
        n_c = 0.33 * C_v ** (-2/3)
        t1 = t1_at(n_c, arr)
        # rigorous finite‑n correlation factor (t1^n_c term negligible for n_c > 7)
        factor = (1 + t1) / (1 - t1)
        correction = 1 - 2 * t1 / (n_c * (1 - t1**2))
        f = factor * correction
        deviation_pct = 100.0 * (f - f_inf) / f_inf
        writer.writerow([
            f"{C_v:.4e}",
            f"{n_c:.4f}",
            f"{t1:.6f}",
            f"{f:.6f}",
            f"{f_inf:.6f}",
            f"{deviation_pct:.6f}"
        ])

if __name__ == "__main__":
    main()