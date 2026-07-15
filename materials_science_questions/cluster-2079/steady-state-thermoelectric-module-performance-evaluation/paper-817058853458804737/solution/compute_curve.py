#!/usr/bin/env python3
import sys, csv, json, math

S = 0.0027
R = 1.035
Theta_th = 102.0
T_j = 353.0
Theta_a = 50.0
Q = 0.5

T_c = T_j - Theta_a * Q
T_diff = T_c

def compute_theta_thv(I):
    if I == 0.0:
        return Theta_th
    delta_T_over_theta = S * I * T_c - 0.5 * I**2 * R - Q
    delta_T = Theta_th * delta_T_over_theta
    P_tec = S * I * delta_T + I**2 * R
    A = P_tec / I**2 - R
    B = 0.5 * S * I * R - S**2 * T_diff
    theta_thv = (A * Theta_th) / (A + B * Theta_th)
    return theta_thv

def main(outdir):
    currents = [i * 0.1 for i in range(0, 16)]  # 0.0 to 1.5
    data = [(I, compute_theta_thv(I)) for I in currents]
    csv_path = f"{outdir}/theta_thv_vs_I.csv"
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["I_tec", "theta_thv"])
        writer.writerows(data)
    min_row = min(data, key=lambda x: x[1])
    minimum_value = min_row[1]
    current_at_minimum = min_row[0]
    json_path = f"{outdir}/minimum_theta_thv.json"
    with open(json_path, 'w') as f:
        json.dump({
            "minimum_value": minimum_value,
            "current_at_minimum": current_at_minimum
        }, f)

if __name__ == "__main__":
    main(sys.argv[1])
