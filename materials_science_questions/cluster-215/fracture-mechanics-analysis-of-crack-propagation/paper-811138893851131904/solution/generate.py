import csv
import math

def compute_epsilon_t(B, K_Ic, mu, f, d_mm, R):
    d_m = d_mm / 1000.0
    K_Ic3 = K_Ic ** 3
    s = math.sqrt(1 + mu**2)
    denom = s - mu - R * (mu + s)
    if denom <= 0:
        return None
    return B * K_Ic3 / (f * (d_m ** 1.5) * denom)

def main():
    out_path = '/app/outputs/transition_strain_rates.csv'
    header = ['condition_id', 'd_mm', 'R', 'material', 'temperature_C', 'epsilon_t_1_per_s']
    rows = []

    K_Ic = 0.1
    f = 0.015

    # Conditions
    conditions = [
        ('fresh', -10, 4.3e-7, 0.5, [1.0, 4.0, 10.0], [0.0, 0.1, 0.2]),
        ('saline', -10, 5.1e-6, 0.5, [1.0, 4.0, 10.0], [0.0, 0.1, 0.2]),
        ('fresh', -40, 3.5e-8, 0.8, [1.0, 4.0, 10.0], [0.0, 0.05, 0.1])
    ]

    for material, tempC, B, mu, d_list, R_list in conditions:
        for d in d_list:
            for R in R_list:
                eps = compute_epsilon_t(B, K_Ic, mu, f, d, R)
                if eps is None:
                    continue
                cond_id = f"{material}_{tempC}_d{int(d) if d.is_integer() else d}_R{R}"
                rows.append([cond_id, d, R, material, float(tempC), eps])

    with open(out_path, 'w', newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        writer.writerows(rows)

if __name__ == '__main__':
    main()
