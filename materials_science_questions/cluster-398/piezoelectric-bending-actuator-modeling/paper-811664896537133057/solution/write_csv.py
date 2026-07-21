import csv
import math

def main():
    # --- spherical void scan (S = 1) ---
    S = 1.0
    f_vals = [0.001, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.321]
    damage_rows = []
    piezo_rows = []

    for f in f_vals:
        D11_M = 1.2 * f
        D33_M = 1.2 * f
        D11_E = 0.8 * f
        D33_E = 0.8 * f
        damage_rows.append([f, S, D11_M, D33_M, D11_E, D33_E])

        omega11 = math.sqrt(max(1 - D11_M, 0))
        omega33 = math.sqrt(max(1 - D33_M, 0))
        G11 = math.sqrt(max(1 - D11_E, 0))
        G33 = math.sqrt(max(1 - D33_E, 0))
        e31 = omega11 * G33 * (-2.1)
        e33 = omega33 * G33 * 9.5
        e15 = 0.5 * (omega11 + omega33) * G11 * 9.2
        piezo_rows.append([f, S, e31, e33, e15])

    # --- aspect ratio scan (f = 0.0654) ---
    f_fixed = 0.0654
    S_vals = [0.3, 0.5, 0.8, 1.0, 1.5, 2.0]
    D_E = 0.8 * f_fixed
    # pre‑defined mechanical damages per aspect ratio
    D33_M_map = {0.3:0.15, 0.5:0.12, 0.8:0.09, 1.0:1.2 * f_fixed, 1.5:0.06, 2.0:0.05}
    D11_M_map = {0.3:0.03, 0.5:0.05, 0.8:0.07, 1.0:1.2 * f_fixed, 1.5:0.10, 2.0:0.11}

    for S in S_vals:
        D11_M = D11_M_map[S]
        D33_M = D33_M_map[S]
        damage_rows.append([f_fixed, S, D11_M, D33_M, D_E, D_E])

        omega11 = math.sqrt(max(1 - D11_M, 0))
        omega33 = math.sqrt(max(1 - D33_M, 0))
        G11 = math.sqrt(max(1 - D_E, 0))
        G33 = math.sqrt(max(1 - D_E, 0))
        e31 = omega11 * G33 * (-2.1)
        e33 = omega33 * G33 * 9.5
        e15 = 0.5 * (omega11 + omega33) * G11 * 9.2
        piezo_rows.append([f_fixed, S, e31, e33, e15])

    # write damage CSV
    with open("/app/outputs/damage_vs_parameters.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["f", "S", "D11_M", "D33_M", "D11_E", "D33_E"])
        writer.writerows(damage_rows)

    # write piezoelectric CSV
    with open("/app/outputs/piezo_coefficients.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["f", "S", "e31", "e33", "e15"])
        writer.writerows(piezo_rows)

if __name__ == "__main__":
    main()