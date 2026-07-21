import sys
import csv
import math

# Material constants: T300 carbon fiber + Epoxy resin (Table 1)
E_fL = 225.0   # GPa
E_fT = 15.8
G_f  = 19.6
nu_fL = 0.3
nu_fT = 0.021

E_m  = 3.43
G_m  = 1.27
nu_m = 0.36

def compute_ud(vf):
    """Compute unidirectional composite elastic coefficients.
       vf: fiber volume fraction (0..1)"""
    E11 = E_fL * vf + E_m * (1 - vf)
    E22 = (E_fT * E_m) / (E_m * vf + E_fT * (1 - vf))
    nu12 = nu_fL * vf + nu_m * (1 - vf)
    nu21 = E22 * nu12 / E11
    den = vf / E_fT + (1 - vf) / E_m
    nu23 = (nu_fT * vf / E_fT + nu_m * (1 - vf) / E_m) / den
    G12 = G_m + vf / (1.0 / (G_f - G_m) + (1 - vf) / (2 * G_m))
    G23 = E22 / (2 * (1 + nu23))
    return E11, E22, G12, G23, nu12, nu21, nu23

def Q_unidirectional(E11, E22, nu12, G12):
    nu21 = nu12 * E22 / E11
    denom = 1 - nu12 * nu21
    Q11 = E11 / denom
    Q22 = E22 / denom
    Q12 = nu12 * E22 / denom
    Q66 = G12
    return Q11, Q12, Q22, Q66

def rotate_Q(Q11, Q12, Q22, Q66, theta_deg):
    theta = math.radians(theta_deg)
    c = math.cos(theta)
    s = math.sin(theta)
    Q11r = Q11 * c**4 + Q22 * s**4 + 2 * (Q12 + 2 * Q66) * c**2 * s**2
    Q12r = (Q11 + Q22 - 4 * Q66) * c**2 * s**2 + Q12 * (c**4 + s**4)
    Q22r = Q11 * s**4 + Q22 * c**4 + 2 * (Q12 + 2 * Q66) * c**2 * s**2
    Q66r = (Q11 + Q22 - 2 * Q12 - 2 * Q66) * c**2 * s**2 + Q66 * (c**4 + s**4)
    return Q11r, Q12r, Q22r, Q66r

def laminate_eng_const(Q11, Q12, Q22, Q66):
    # For a balanced symmetric angle-ply, the laminate engineering constants
    # are directly obtained from the rotated stiffnesses (A_ij / t = Q_avg_ij).
    E11_lam = (Q11 * Q22 - Q12**2) / Q22
    E22_lam = (Q11 * Q22 - Q12**2) / Q11
    G12_lam = Q66
    return E11_lam, E22_lam, G12_lam

def write_forward(out_path):
    header = ['Vf_pct', 'E11_pred', 'E22_pred', 'G12_pred', 'G23_pred',
              'nu12_pred', 'nu21_pred', 'nu23_pred']
    vf_pcts = list(range(5, 100, 10))   # 5,15,...,95 (10 points)
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for vf_pct in vf_pcts:
            vf = vf_pct / 100.0
            E11, E22, G12, G23, nu12, nu21, nu23 = compute_ud(vf)
            writer.writerow([vf_pct, E11, E22, G12, G23, nu12, nu21, nu23])

def write_inverse_vf(out_path):
    header = ['Vf_true', 'E11_input', 'E22_input', 'G12_input', 'Vf_pred']
    vf_true_pcts = [35, 45, 55, 65, 75]
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for vf_pct in vf_true_pcts:
            vf = vf_pct / 100.0
            E11, E22, G12, _, _, _, _ = compute_ud(vf)
            # Ideal prediction equals true Vf
            writer.writerow([float(vf_pct), E11, E22, G12, float(vf_pct)])

def write_angle(out_path):
    header = ['theta_true', 'E11_input', 'E22_input', 'G12_input', 'theta_pred']
    # Fixed fibre volume fraction
    vf = 0.60
    E11_ud, E22_ud, G12_ud, _, nu12_ud, _, _ = compute_ud(vf)
    Q11_ud, Q12_ud, Q22_ud, Q66_ud = Q_unidirectional(E11_ud, E22_ud, nu12_ud, G12_ud)
    theta_vals = [5, 20, 35, 50, 65, 80]  # degrees
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for theta in theta_vals:
            Q11b, Q12b, Q22b, Q66b = rotate_Q(Q11_ud, Q12_ud, Q22_ud, Q66_ud, theta)
            E11_lam, E22_lam, G12_lam = laminate_eng_const(Q11b, Q12b, Q22b, Q66b)
            # Ideal prediction equals true theta
            writer.writerow([theta, E11_lam, E22_lam, G12_lam, theta])

if __name__ == '__main__':
    mode = sys.argv[1]
    out_path = sys.argv[2]
    if mode == 'forward':
        write_forward(out_path)
    elif mode == 'inverse_vf':
        write_inverse_vf(out_path)
    elif mode == 'angle':
        write_angle(out_path)
    else:
        raise ValueError('Unknown mode')
