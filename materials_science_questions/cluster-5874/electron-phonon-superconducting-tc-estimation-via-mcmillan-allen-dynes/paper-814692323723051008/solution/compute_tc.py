import csv
import math

theta_D = 80.0
theta_bp = 3000.0

def compute_row(system, P, lam_ph0, lam_bp0, A):
    lam_ph = lam_ph0 * math.exp(-A * P)
    lam_bp = lam_bp0 * math.exp(-A * P)
    log_ratio = math.log(theta_bp / theta_D)
    denom = 1.0 - lam_bp * log_ratio
    lam_bp_star = lam_bp / denom
    sum_lam = lam_bp_star + lam_ph
    Tc = 1.14 * theta_D * math.exp(-1.0 / sum_lam)
    log_tc = math.log(Tc / (1.14 * theta_D))
    alpha = 0.5 * (1.0 - (1.0 + lam_ph * log_tc) ** 2)
    beta = 4.0 / (1.14 - Tc / theta_D)
    dTc_dP = -A * Tc * (math.log(1.14 * theta_D / Tc) + (1.0 - 2.0 * alpha) * log_ratio)
    return [system, f"{P:.2f}", f"{Tc:.6f}", f"{alpha:.6f}", f"{beta:.6f}", f"{dTc_dP:.6f}"]

params = {
    'K3C60':  (0.2575, 0.1609, 0.14091, [0.0, 0.08, 0.33, 0.68, 1.02, 2.33]),
    'Rb3C60': (0.4355, 0.1715, 0.1936,  [0.0, 0.18, 0.58, 1.03, 1.50, 1.92]),
}

rows = []
for system, (lam_ph0, lam_bp0, A, pressures) in params.items():
    for P in pressures:
        rows.append(compute_row(system, P, lam_ph0, lam_bp0, A))

with open('/app/outputs/calculated_properties.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['system', 'pressure_GPa', 'Tc_K', 'alpha', 'beta', 'dTc_dP_K_GPa'])
    w.writerows(rows)
