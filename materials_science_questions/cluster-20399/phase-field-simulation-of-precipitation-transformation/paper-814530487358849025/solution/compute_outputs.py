import csv, json, math, sys, os
import numpy as np
from scipy.integrate import quad

sigma_A = 1.0
xi_A = 0.5e-9  # half width (m)
R = 8.314
T = 1273.0
v_m = 1.06e-5
beta = v_m / (R * T)
omega_A = sigma_A / (2.0 * xi_A)
beta_omega_A = beta * omega_A

alpha_list = [2, 3, 4]

def u_g_from_u_m(u_m, alpha):
    K = math.exp(alpha * beta_omega_A)
    return K * u_m / (1.0 - u_m + K * u_m)

def u_m_ct_alpha(alpha):
    num = math.exp(beta_omega_A) - 1.0
    den = math.exp(alpha * beta_omega_A) - 1.0
    u_m_ct = num / den
    u_g_ct = (math.exp(alpha * beta_omega_A) * num) / (math.exp(beta_omega_A) * den)
    return u_m_ct, u_g_ct

def modelI_integrand(phi, u_m_e, alpha):
    g = 4.0 * phi * (1.0 - phi)
    C = alpha * beta_omega_A
    q = u_m_e / (1.0 - u_m_e)
    u = q * math.exp(C * g) / (1.0 + q * math.exp(C * g)) if u_m_e > 0 else 0.0
    inv_bw = 1.0 / beta_omega_A
    arg = g + inv_bw * math.log((1.0 - u) / (1.0 - u_m_e))
    return math.sqrt(max(arg, 0.0))

def modelI_sigma(u_m_e, alpha):
    result, _ = quad(lambda phi: modelI_integrand(phi, u_m_e, alpha), 0.0, 1.0, limit=200)
    return (4.0 / math.pi) * sigma_A * result

def modelII_sigma(u_m_e, alpha):
    u_g = u_g_from_u_m(u_m_e, alpha)
    inv_bw = 1.0 / beta_omega_A
    log_term = math.log((1.0 - u_g) / (1.0 - u_m_e))
    omega_e_over_omega_A = max(1.0 + inv_bw * log_term, 0.0)
    return sigma_A * math.sqrt(omega_e_over_omega_A)

def classical_sigma(u_m_e, alpha):
    u_g = u_g_from_u_m(u_m_e, alpha)
    inv_bw = 1.0 / beta_omega_A
    log_term = math.log((1.0 - u_g) / (1.0 - u_m_e))
    omega_e_over_omega_A = 1.0 + inv_bw * log_term
    return sigma_A * omega_e_over_omega_A

def generate_u_m_e_grid():
    vals = []
    x = 0.001
    while x <= 0.15 + 1e-10:
        vals.append(round(x, 10))
        x += 0.005
    if abs(vals[-1] - 0.15) > 1e-9:
        vals.append(0.15)
    return sorted(vals)

def write_common_gb_composition(output_path):
    rows = []
    for alpha in alpha_list:
        u_m_ct, u_g_ct = u_m_ct_alpha(alpha)
        grid = generate_u_m_e_grid()
        for u_m_e in grid:
            u_g = u_g_from_u_m(u_m_e, alpha)
            rows.append((alpha, u_m_e, u_g))
        rows.append((alpha, u_m_ct, u_g_ct))
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['alpha', 'u_m_e', 'u_g_e'])
        for r in rows:
            w.writerow(r)

def write_modelI_gb_energy(output_path):
    rows = []
    for alpha in alpha_list:
        u_m_ct, u_g_ct = u_m_ct_alpha(alpha)
        grid = generate_u_m_e_grid()
        if u_m_ct not in grid:
            grid.append(u_m_ct)
        grid = sorted(grid)
        for u_m_e in grid:
            if u_m_e <= u_m_ct + 1e-12:
                sigma = modelI_sigma(u_m_e, alpha)
                rows.append((alpha, u_m_e, sigma, u_m_ct, u_g_ct))
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['alpha', 'u_m_e', 'sigma', 'u_m_ct', 'u_g_ct'])
        for r in rows:
            w.writerow(r)

def write_modelII_gb_energy(output_path):
    rows = []
    for alpha in alpha_list:
        u_m_ct, _ = u_m_ct_alpha(alpha)
        grid = generate_u_m_e_grid()
        if u_m_ct not in grid:
            grid.append(u_m_ct)
        grid = sorted(grid)
        for u_m_e in grid:
            if u_m_e <= u_m_ct + 1e-12:
                sigma = modelII_sigma(u_m_e, alpha)
                rows.append((alpha, u_m_e, sigma))
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['alpha', 'u_m_e', 'sigma'])
        for r in rows:
            w.writerow(r)

def write_classical_two_phase_gb_energy(output_path):
    rows = []
    for alpha in alpha_list:
        u_m_ct, _ = u_m_ct_alpha(alpha)
        grid = generate_u_m_e_grid()
        if u_m_ct not in grid:
            grid.append(u_m_ct)
        grid = sorted(grid)
        for u_m_e in grid:
            if u_m_e <= u_m_ct + 1e-12:
                sigma = classical_sigma(u_m_e, alpha)
                rows.append((alpha, u_m_e, sigma))
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['alpha', 'u_m_e', 'sigma'])
        for r in rows:
            w.writerow(r)

def write_modelII_analytic_results(output_path):
    epsilon = (4.0 / math.pi) * math.sqrt(xi_A * sigma_A)
    u_m_sample = 0.09
    alpha_sample = 3
    sigma_sample = modelII_sigma(u_m_sample, alpha_sample)
    u_g_sample = u_g_from_u_m(u_m_sample, alpha_sample)
    inv_bw = 1.0 / beta_omega_A
    log_term = math.log((1.0 - u_g_sample) / (1.0 - u_m_sample))
    omega_e_over_omega_A = 1.0 + inv_bw * log_term
    omega_e = omega_A * omega_e_over_omega_A
    ratio1 = sigma_sample / sigma_A
    ratio2 = sigma_sample / (2.0 * xi_A * omega_e) if omega_e > 1e-20 else 1.0
    data = {
        'sigma_A': sigma_A,
        'xi_A': xi_A,
        'epsilon': epsilon,
        'omega_A': omega_A,
        'sigma': sigma_sample,
        'sigma_over_sigma_A': ratio1,
        'sigma_over_xi_omega': ratio2
    }
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    out = '/app/outputs'
    write_common_gb_composition(os.path.join(out, 'common_gb_composition.csv'))
    write_modelI_gb_energy(os.path.join(out, 'modelI_gb_energy.csv'))
    write_modelII_gb_energy(os.path.join(out, 'modelII_gb_energy.csv'))
    write_classical_two_phase_gb_energy(os.path.join(out, 'classical_two_phase_gb_energy.csv'))
    write_modelII_analytic_results(os.path.join(out, 'modelII_analytic_results.json'))