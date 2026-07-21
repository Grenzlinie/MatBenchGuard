import sys
import csv
import math

def equilibrium_P_sq(T_K, sigma, a0, T0_K, beta, gamma, Q11):
    a = a0 * (T_K - T0_K)
    a_eff = a - 2.0 * Q11 * sigma
    disc = beta**2 - 4.0 * gamma * a_eff
    if disc < 0.0:
        return 0.0
    sqrt_disc = math.sqrt(disc)
    y1 = (-beta + sqrt_disc) / (2.0 * gamma)
    y2 = (-beta - sqrt_disc) / (2.0 * gamma)
    best_G = float('inf')
    best_y = 0.0
    for y in (y1, y2):
        if y <= 0.0:
            continue
        G_val = a/2.0*y + beta/4.0*y*y + gamma/6.0*y**3 - Q11 * sigma * y
        if G_val < best_G:
            best_G = G_val
            best_y = y
    if best_y > 0.0 and best_G <= 0.0:
        return best_y
    else:
        return 0.0

def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/app/outputs/delta_T_vs_temperature.csv"
    compositions = {
        "65/35": {"T0_C": 40.0, "a0": 3.5e7, "beta": -1.5e12, "gamma": 1.9e14, "Q11": -12.0},
        "70/30": {"T0_C": 33.7, "a0": 7.5e7, "beta": -1.9e12, "gamma": 1.9e14, "Q11": -12.0},
    }
    alpha_l = 2.0e-3   # K^-1
    s11    = 3.32e-10  # m^2/N
    C      = 1.19e3    # J/(kg K)
    rho    = 1.886e3   # kg/m^3
    sigma3 = -100e6    # Pa (compressive)
    t_min, t_max, dt = 20.0, 200.0, 1.0  # °C

    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["composition", "stress_MPa", "temperature_C", "delta_T_K"])
        for name, p in compositions.items():
            T0_K = p["T0_C"] + 273.15
            a0 = p["a0"]
            beta = p["beta"]
            gamma = p["gamma"]
            Q11 = p["Q11"]
            n = int((t_max - t_min) / dt) + 1
            for i in range(n):
                T_C = t_min + i * dt
                T_K = T_C + 273.15
                P_sq_0 = equilibrium_P_sq(T_K, 0.0, a0, T0_K, beta, gamma, Q11)
                P_sq_s = equilibrium_P_sq(T_K, sigma3, a0, T0_K, beta, gamma, Q11)
                delta_S = (-0.5 * a0 * (P_sq_s - P_sq_0)
                           - 2.0 * alpha_l * s11 * sigma3**2
                           - 2.0 * alpha_l * sigma3 * Q11 * P_sq_s)
                delta_T_K = -T_K * delta_S / (C * rho)
                writer.writerow([name, -100.0, T_C, delta_T_K])

if __name__ == "__main__":
    main()