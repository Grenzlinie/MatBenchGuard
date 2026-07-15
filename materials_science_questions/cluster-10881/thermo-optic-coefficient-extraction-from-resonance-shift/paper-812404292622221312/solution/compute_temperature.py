import math, os

def I(t, tm):
    if t <= 0.0:
        return 0.0
    x = t / tm
    return 40.0 * x**2 * math.exp(-2.0 * x + 2.0)

def P(t, tm):
    return 1.4 * I(t, tm)

def main():
    os.makedirs("/app/outputs", exist_ok=True)
    output_file = "/app/outputs/temperature_values.csv"
    rho = 5370.0
    c = 320.0
    V = 1.4e-13
    rho_c_V = rho * c * V
    dt = 1e-10           # 0.1 ns
    t_max = 150e-9
    targets_ns = [20, 40, 60, 80, 100]
    tm_ns = [30, 50, 70, 90]

    all_columns = {}
    for tm_ns_val in tm_ns:
        tm = tm_ns_val * 1e-9
        N = int(t_max / dt) + 1
        deltaT = [0.0] * N
        for n in range(1, N):
            sum_prev = 0.0
            t_n = n * dt
            for i in range(1, n):
                t_mid = (i - 0.5) * dt
                t_arg = t_n - t_mid
                P_val = P(t_arg, tm)
                sum_prev += P_val * (deltaT[i] - deltaT[i-1])
            P_mid = P(0.5 * dt, tm)
            denom = rho_c_V - P_mid
            if denom == 0.0:
                deltaT[n] = deltaT[n-1]
            else:
                deltaT[n] = (sum_prev - P_mid * deltaT[n-1]) / denom
        temps = []
        for t_ns in targets_ns:
            t = t_ns * 1e-9
            idx = min(int(round(t / dt)), N-1)
            temps.append(deltaT[idx])
        col_name = f"tm_{tm_ns_val}_K"
        all_columns[col_name] = temps

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ["t_ns"] + [f"tm_{v}_K" for v in tm_ns]
        writer.writerow(header)
        for row_idx, t_ns in enumerate(targets_ns):
            row = [t_ns]
            for tm_ns_val in tm_ns:
                col_name = f"tm_{tm_ns_val}_K"
                row.append(f"{all_columns[col_name][row_idx]:.6f}")
            writer.writerow(row)

if __name__ == "__main__":
    main()