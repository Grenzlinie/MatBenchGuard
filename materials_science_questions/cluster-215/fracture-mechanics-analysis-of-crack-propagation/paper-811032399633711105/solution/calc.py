import math

def solve_gamma(beta_rad, c1=2.5):
    # beta_rad in radians, return gamma in radians
    def f(gamma):
        return math.sin(2 * (beta_rad + gamma)) - c1 * math.cos(beta_rad) * math.cos(gamma)
    # gamma is expected near 90° (pi/2) to 120°; search in [pi/2, pi]
    lo = math.pi / 2
    hi = math.pi
    # Check if root exactly at lo
    if abs(f(lo)) < 1e-12:
        return lo
    # Ensure sign change
    f_lo = f(lo)
    f_hi = f(hi)
    # If no sign change (shouldn't happen for these parameters), expand slightly
    # Bisection
    for _ in range(100):
        mid = (lo + hi) / 2.0
        f_mid = f(mid)
        if abs(f_mid) < 1e-12:
            return mid
        if f_lo * f_mid <= 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    return (lo + hi) / 2.0

def main():
    print("beta,gamma,p")
    for beta_deg in range(0, 91, 10):
        beta = math.radians(beta_deg)
        gamma_rad = solve_gamma(beta)
        gamma_deg = math.degrees(gamma_rad)
        # Compute p = 19.0 * cot(gamma) / sin(2*(gamma+beta))
        p = 19.0 * math.cos(gamma_rad) / math.sin(gamma_rad) / math.sin(2 * (gamma_rad + beta))
        print(f"{beta_deg},{gamma_deg:.6f},{p:.6f}")

if __name__ == "__main__":
    main()
