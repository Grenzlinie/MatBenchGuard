import csv
import math

e = math.e

def sr_value(w_t, t_2rho, n, mu, R, theta_deg, alpha):
    theta = math.radians(theta_deg)
    t_2rho_inv = 1.0 / t_2rho
    # Term1 = (1/(1+n)) * [ ((1+R)/sqrt(1+2R)) * t_2rho ]^(1+n)
    factor = ((1.0 + R) / math.sqrt(1.0 + 2.0 * R)) * t_2rho
    term1 = (1.0 / (1.0 + n)) * (factor ** (1.0 + n))
    # Common second factor (n/e)^n
    second = (n / e) ** n
    # Third factor
    third = (w_t / math.cos(theta)) - (t_2rho_inv + 1.0) * math.tan(theta)
    # Fourth factor
    tan_th = math.tan(theta)
    cos_th = math.cos(theta)
    sin_th = math.sin(theta)
    numer = 1.0 - cos_th + mu * sin_th * t_2rho
    denom = cos_th + mu * sin_th
    fourth = tan_th * t_2rho + (tan_th + 2.0 * mu) * numer / denom
    # SR
    sr = (t_2rho ** (-2)) * (term1 - alpha * second * third * fourth)
    return sr

def alpha_c_value(w_t, t_2rho, n, mu, R, theta_deg):
    theta = math.radians(theta_deg)
    factor = ((1.0 + R) / math.sqrt(1.0 + 2.0 * R)) * t_2rho
    term1 = (1.0 / (1.0 + n)) * (factor ** (1.0 + n))
    second = (n / e) ** n
    tan_th = math.tan(theta)
    cos_th = math.cos(theta)
    sin_th = math.sin(theta)
    t_2rho_inv = 1.0 / t_2rho
    third = (w_t / cos_th) - (t_2rho_inv + 1.0) * tan_th
    numer = 1.0 - cos_th + mu * sin_th * t_2rho
    denom = cos_th + mu * sin_th
    fourth = tan_th * t_2rho + (tan_th + 2.0 * mu) * numer / denom
    ac = term1 / (second * third * fourth)
    return ac

def lower_limit(w_t, theta_deg):
    theta = math.radians(theta_deg)
    sin_th = math.sin(theta)
    return sin_th / (w_t - sin_th)

def main():
    # Parameter grids
    wt_range = [8, 10, 12, 14]          # w/t
    t2rho_range = [0.05, 0.075, 0.1, 0.125, 0.15]  # t/2ρ
    n_range = [0.1, 0.2, 0.3, 0.4, 0.5]
    mu_range = [0.0, 0.1, 0.2]
    R_range = [0.5, 1.0, 1.5, 2.0]
    theta_range = [30, 40, 50, 60]       # degrees
    alpha_range = [round(i*0.01, 2) for i in range(21)]  # 0.00..0.20 step 0.01

    # sr_data.csv
    with open('/app/outputs/sr_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['alpha', 'w_t', 't_2rho', 'n', 'mu', 'R', 'theta', 'SR'])
        for wt in wt_range:
            for t2r in t2rho_range:
                for n in n_range:
                    for mu in mu_range:
                        for R in R_range:
                            for theta in theta_range:
                                for alpha in alpha_range:
                                    sr = sr_value(wt, t2r, n, mu, R, theta, alpha)
                                    writer.writerow([alpha, wt, t2r, n, mu, R, theta, sr])

    # alpha_c_data.csv
    with open('/app/outputs/alpha_c_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['R', 'n', 'w_t', 't_2rho', 'mu', 'theta', 'alpha_c'])
        for R in R_range:
            for n in n_range:
                for wt in wt_range:
                    for t2r in t2rho_range:
                        for mu in mu_range:
                            for theta in theta_range:
                                ac = alpha_c_value(wt, t2r, n, mu, R, theta)
                                writer.writerow([R, n, wt, t2r, mu, theta, ac])

    # lower_limit_data.csv
    wt_lower_range = list(range(8, 15, 1))   # 8..14 step 1
    theta_lower_range = list(range(30, 61, 5))  # 30..60 step 5
    with open('/app/outputs/lower_limit_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['w_t', 'theta', 'lower_limit'])
        for wt in wt_lower_range:
            for theta in theta_lower_range:
                ll = lower_limit(wt, theta)
                writer.writerow([wt, theta, ll])

if __name__ == '__main__':
    main()