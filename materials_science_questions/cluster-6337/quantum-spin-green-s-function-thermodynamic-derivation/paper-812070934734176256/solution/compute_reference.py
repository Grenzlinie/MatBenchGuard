import sys, json, csv, os
import numpy as np
from scipy.integrate import quad

def compute_sums(p, k, n_max):
    if np.isscalar(k):
        k_arr = np.array([k])
    else:
        k_arr = np.asarray(k)
    n = np.arange(1, n_max+1)
    two_n = 2 * n[:, None]
    two_n_minus1 = (2*n - 1)[:, None]
    term_f = (1.0 / (two_n**p)) * (np.cos(two_n * k_arr[None, :]) - 1)
    f_k = 4 * np.sum(term_f, axis=0)
    term_g = (1.0 / (two_n_minus1**p)) * np.cos(two_n_minus1 * k_arr[None, :])
    g_k = 2 * np.sum(term_g, axis=0)
    alpha = 2 * np.sum(1.0 / (two_n_minus1**p))
    if np.isscalar(k):
        f_k = f_k.item()
        g_k = g_k.item()
    return f_k, g_k, alpha

def integrand(k, p, n_max):
    fk, gk, alpha = compute_sums(p, k, n_max)
    denom = (alpha - fk)**2 - gk**2
    return (alpha - fk) / denom if denom != 0 else 0.0

def compute_dispersion(p, sigma_a, n_max):
    k_vals = np.linspace(0, np.pi, 100, endpoint=True)
    fk, gk, alpha = compute_sums(p, k_vals, n_max)
    omega = sigma_a * np.sqrt((alpha - fk)**2 - gk**2)
    return k_vals, omega

def compute_TN_inverse(p, n_max):
    res, _ = quad(lambda k: integrand(k, p, n_max), 0, np.pi, limit=500, epsabs=1e-8)
    return (2/np.pi) * (2 * res)  # integral from -pi to pi = 2 * int_0^pi

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True, choices=['dispersion', 'critical'])
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    n_max = 10000
    sigma_a = 0.5

    if args.mode == 'dispersion':
        k_vals, omega = compute_dispersion(1.5, sigma_a, n_max)
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['k', 'omega_k'])
            for k, om in zip(k_vals, omega):
                writer.writerow([k, om])
        print('dispersion_k.csv written')

    elif args.mode == 'critical':
        tn_inv_1 = compute_TN_inverse(1.5, n_max)
        try:
            tn_inv_2 = compute_TN_inverse(2.5, n_max)
            if np.isfinite(tn_inv_2) and tn_inv_2 < 1e10:
                if tn_inv_2 > 1e6:
                    tn_inv_2 = 1e10
                    diverges = True
                else:
                    diverges = False
            else:
                tn_inv_2 = 1e10
                diverges = True
        except Exception:
            tn_inv_2 = 1e10
            diverges = True

        data = {
            'p1.5_TN_inverse': float(tn_inv_1),
            'p2.5_TN_inverse': float(tn_inv_2),
            'p2.5_diverges': diverges
        }
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, 'w') as f:
            json.dump(data, f)
        print('critical_temperature.json written')

if __name__ == '__main__':
    main()