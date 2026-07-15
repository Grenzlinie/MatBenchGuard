import csv
import math

def main():
    deltas = [0.02, 0.04]
    Us = [0.0, 0.125, -0.125]
    # theta = E/kT from 0.5 to 2.0 step 0.1
    thetas = [round(i * 0.1, 2) for i in range(5, 21)]  # 0.5,0.6,...,2.0
    rows = []
    for delta in deltas:
        for U in Us:
            for theta in thetas:
                w0 = math.exp(theta * (-6 + delta * (19 - 7 * U)))
                w1_1 = math.exp(theta * (-5.5 - 0.5 * U + 18 * delta - 6 * delta * U))
                w1_2 = math.exp(theta * (-5 + delta * (17 - 7 * U)))
                w1_3 = math.exp(theta * (-4.5 - 0.5 * U + 16 * delta - 6 * delta * U))
                sum_w1 = w1_1 + w1_2
                term_w1 = 14 * w1_3 + 25 * sum_w1
                exp_factor_B = math.exp(-4 * theta * (1 - U) * (1 - 2 * delta))

                f_B = (2 * delta * term_w1 +
                       8 * (1 - 15 * delta) * w0 +
                       (2 * (1 - 15 * delta) * w0 / delta) * exp_factor_B)

                D_B_star = ((4 * delta * term_w1 +
                             16 * (1 - 15 * delta) * w0 +
                             (4 * (1 - 15 * delta) * w0 / delta) * exp_factor_B) /
                            (1 + 2 * delta))

                w1_sum_A = w1_3 + 1.5 * sum_w1
                exp_factor_A1 = math.exp(theta * (1 - U) * (4 - 7 * delta))
                exp_factor_A2 = math.exp(theta * delta * (1 - U))

                f_A = (24.1 * delta**2 / (1 - 2 * delta) * w1_sum_A * exp_factor_A1 +
                       8 * (1 - 15 * delta) * w0 / (1 - 2 * delta) *
                       (delta * exp_factor_A1 + exp_factor_A2))

                D_A_star = ((24.1 * delta**2 * w1_sum_A +
                             8 * (1 - 15 * delta) * w0 +
                             (8 * (1 - 15 * delta) * w0 / delta) * exp_factor_B) /
                            (1 - 2 * delta))

                rows.append([delta, U, theta, f_A, f_B, D_A_star, D_B_star])

    with open('/app/outputs/tracer_diffusion_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['delta', 'U_param', 'E_over_kT', 'f_A', 'f_B', 'D_A_star', 'D_B_star'])
        writer.writerows(rows)

if __name__ == '__main__':
    main()