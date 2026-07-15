#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: sifs_initial_crack.csv ===
# Overwrite /solution/compute.py with corrected version (signed omega)
python3 <<'PYEOF'
import textwrap
new_code = r"""
import numpy as np
from scipy.special import ellipk, ellipe

def normalize(v):
    n = np.linalg.norm(v)
    return v / n if n > 1e-15 else v

def crack_normal(alpha_deg, beta_deg):
    alpha = np.radians(alpha_deg)
    beta = np.radians(beta_deg)
    l = np.sin(beta) * np.cos(alpha)
    m = np.sin(beta) * np.sin(alpha)
    n = -np.cos(beta)
    return np.array([l, m, n])

def stresses_on_plane(l, m, n, sigma_x, sigma_y, sigma_z, P):
    sigma_n_ext = sigma_x*l**2 + sigma_y*m**2 + sigma_z*n**2
    tau = np.sqrt((sigma_x*l)**2 + (sigma_y*m)**2 + (sigma_z*n)**2 - sigma_n_ext**2)
    sigma_n_eff = P - sigma_n_ext
    tau_eff = tau
    if tau > 1e-14:
        l_tau = (sigma_x - sigma_n_ext) * l / tau
        m_tau = (sigma_y - sigma_n_ext) * m / tau
        n_tau = (sigma_z - sigma_n_ext) * n / tau
    else:
        l_tau, m_tau, n_tau = 1.0, 0.0, 0.0
    return sigma_n_ext, tau, sigma_n_eff, tau_eff, np.array([l_tau, m_tau, n_tau])

def signed_angle(u, v, n):
    # signed angle from u to v, following right-hand rule around n
    u = np.asarray(u)
    v = np.asarray(v)
    n = np.asarray(n)
    dot_uv = np.dot(u, v)
    cross_uv = np.cross(u, v)
    angle = np.arctan2(np.dot(n, cross_uv), dot_uv)
    return angle

def shear_angle(alpha_deg, beta_deg, l_tau, m_tau, n_tau):
    alpha = np.radians(alpha_deg)
    beta = np.radians(beta_deg)
    l_o = np.cos(beta) * np.cos(alpha)
    m_o = np.cos(beta) * np.sin(alpha)
    n_o = np.sin(beta)
    u = np.array([l_o, m_o, n_o])
    v = np.array([l_tau, m_tau, n_tau])
    n_vec = crack_normal(alpha_deg, beta_deg)
    omega = signed_angle(u, v, n_vec)
    return omega

def circular_sifs(phi_rad, a, sigma_n_eff, tau_eff, omega, nu):
    KI = 2 * np.sqrt(a / np.pi) * sigma_n_eff * np.ones_like(phi_rad)
    KII = -4 / (2 - nu) * np.sqrt(a / np.pi) * tau_eff * np.cos(phi_rad - omega)
    KIII = 4 * (1 - nu) / (2 - nu) * np.sqrt(a / np.pi) * tau_eff * np.sin(phi_rad - omega)
    return KI, KII, KIII

def elliptical_sifs(phi_rad, a, b, gamma, sigma_n_eff, tau_eff, omega, nu):
    k2 = 1 - (b/a)**2
    k = np.sqrt(k2) if k2>0 else 0.0
    kp = b / a
    E = ellipe(k2)
    K = ellipk(k2)
    B = (k2 - nu) * E + nu * kp**2 * K
    C = (k2 + nu * kp**2) * E - nu * kp**2 * K
    denom = (a**2 * np.sin(phi_rad)**2 + b**2 * np.cos(phi_rad)**2)**(0.25)
    KI = sigma_n_eff / E * np.sqrt(np.pi * b / a) * denom
    term2 = np.cos(omega)*np.cos(phi_rad) * (kp / B) + np.sin(omega)*np.sin(phi_rad) * (1 / C)
    KII = - tau_eff * k2 * np.sqrt(np.pi * a * b) / denom * term2
    term3 = np.cos(omega)*np.sin(phi_rad) * (1 / B) - np.sin(omega)*np.cos(phi_rad) * (kp / C)
    KIII = tau_eff * k2 * (1 - nu) * np.sqrt(np.pi * a * b) / denom * term3
    return KI, KII, KIII

def mts_critical_angle(KI, KII):
    KI = np.atleast_1d(np.asarray(KI, dtype=float))
    KII = np.atleast_1d(np.asarray(KII, dtype=float))
    theta = np.zeros_like(KI)
    mask = np.abs(KII) > 1e-15
    A = KI[mask] / KII[mask]
    sqrt_term = np.sqrt(A**2 + 8)
    root1 = (A - sqrt_term) / 4
    root2 = (A + sqrt_term) / 4
    theta1 = 2 * np.arctan(root1)
    theta2 = 2 * np.arctan(root2)
    def sigma_factor(th, KI, KII):
        c = np.cos(th/2)
        s = np.sin(th/2)
        return c**2 * (KI * c - 3 * KII * s)
    f1 = sigma_factor(theta1, KI[mask], KII[mask])
    f2 = sigma_factor(theta2, KI[mask], KII[mask])
    best = np.where(f1 >= f2, theta1, theta2)
    theta[mask] = best
    if KI.size == 1:
        return float(theta[0])
    return theta

def compute_phi_zero(a, b, gamma, omega, nu):
    k2 = 1 - (b/a)**2
    k = np.sqrt(k2) if k2>0 else 0.0
    kp = b / a
    E = ellipe(k2)
    K = ellipk(k2)
    B = (k2 - nu) * E + nu * kp**2 * K
    C = (k2 + nu * kp**2) * E - nu * kp**2 * K
    if abs(B * np.tan(omega)) < 1e-15:
        phi_zero = np.pi/2 if (-kp*C) >= 0 else 3*np.pi/2
    else:
        phi_zero = np.arctan2(-kp*C, B*np.tan(omega))
    if phi_zero < 0:
        phi_zero += 2*np.pi
    return phi_zero

def phi_actual_from_apparent(phi, a, b):
    denom = a * np.cos(phi)
    num = b * np.sin(phi)
    phi_act = np.arctan2(num, denom)
    phi_act = np.where(phi_act < 0, phi_act + 2*np.pi, phi_act)
    return phi_act

def ellipse_coords(phi, a, b, gamma):
    f = a * np.cos(phi) * np.cos(gamma) - b * np.sin(phi) * np.sin(gamma)
    g = a * np.cos(phi) * np.sin(gamma) + b * np.sin(phi) * np.cos(gamma)
    return f, g

def global_coords(f, g, h, alpha_deg, beta_deg):
    alpha = np.radians(alpha_deg)
    beta = np.radians(beta_deg)
    x = f * np.cos(beta) * np.cos(alpha) - g * np.sin(alpha) - h * np.cos(alpha) * np.sin(beta)
    y = f * np.cos(beta) * np.sin(alpha) + g * np.cos(alpha) - h * np.sin(alpha) * np.sin(beta)
    z = f * np.sin(beta) + h * np.cos(beta)
    return x, y, z

def fit_ellipse(R, phi_vals):
    a_new = np.max(R)
    b_new = np.min(R)
    max_idx = np.argmax(R)
    gamma_new = phi_vals[max_idx]
    return a_new, b_new, gamma_new

def propagate_step(alpha_deg, beta_deg, a, b, gamma, inc, sigma_x, sigma_y, sigma_z, P, nu, n_phi=360):
    l, m, n = crack_normal(alpha_deg, beta_deg)
    sigma_n_ext = sigma_x*l**2 + sigma_y*m**2 + sigma_z*n**2
    tau = np.sqrt((sigma_x*l)**2 + (sigma_y*m)**2 + (sigma_z*n)**2 - sigma_n_ext**2)
    sigma_n_eff = P - sigma_n_ext
    tau_eff = tau
    alpha = np.radians(alpha_deg)
    beta = np.radians(beta_deg)
    l_o = np.cos(beta) * np.cos(alpha)
    m_o = np.cos(beta) * np.sin(alpha)
    n_o = np.sin(beta)
    if tau > 1e-14:
        l_tau = (sigma_x - sigma_n_ext) * l / tau
        m_tau = (sigma_y - sigma_n_ext) * m / tau
        n_tau = (sigma_z - sigma_n_ext) * n / tau
    else:
        l_tau, m_tau, n_tau = 1.0, 0.0, 0.0
    # signed omega
    u_proj = np.array([l_o, m_o, n_o])
    v_shear = np.array([l_tau, m_tau, n_tau])
    omega = signed_angle(u_proj, v_shear, np.array([l, m, n]))

    phi_vals = np.linspace(0, 2*np.pi, n_phi, endpoint=False)
    if abs(b - a) < 1e-10:
        KI, KII, KIII = circular_sifs(phi_vals, a, sigma_n_eff, tau_eff, omega, nu)
    else:
        KI, KII, KIII = elliptical_sifs(phi_vals, a, b, gamma, sigma_n_eff, tau_eff, omega, nu)

    phi_zero = compute_phi_zero(a, b, gamma, omega, nu)
    phi_max1 = phi_zero + np.pi/2
    phi_max2 = phi_zero - np.pi/2
    idx_max1 = np.argmin(np.abs(phi_vals - phi_max1))
    idx_max2 = np.argmin(np.abs(phi_vals - phi_max2))
    KII_max1 = np.abs(KII[idx_max1])
    KII_max2 = np.abs(KII[idx_max2])
    if KII_max1 >= KII_max2:
        idx_max = idx_max1
        phi_max = phi_vals[idx_max1]
    else:
        idx_max = idx_max2
        phi_max = phi_vals[idx_max2]

    theta_c_all = mts_critical_angle(KI, KII)
    theta_c_max = theta_c_all[idx_max]

    h = inc * np.sin(theta_c_max) * np.cos(phi_vals - phi_max)

    if abs(b - a) < 1e-10:
        prev_len = np.full_like(phi_vals, a)
    else:
        f_prev, g_prev = ellipse_coords(phi_vals, a, b, gamma)
        prev_len = np.sqrt(f_prev**2 + g_prev**2)
        phi_actual_vals = phi_actual_from_apparent(phi_vals, a, b)

    theta_c_vals = theta_c_all
    valid = np.abs(theta_c_vals) > 1e-12
    if abs(b - a) < 1e-10:
        length = np.copy(prev_len)
        length[valid] = prev_len[valid] + h[valid] / np.tan(theta_c_vals[valid])
        length[~valid] = prev_len[~valid] + inc
    else:
        length = np.copy(prev_len)
        length[valid] = prev_len[valid] + h[valid] / np.tan(theta_c_vals[valid])
        length[~valid] = prev_len[~valid] + inc

    R = np.sqrt(length**2 + h**2)
    a_new, b_new, gamma_new = fit_ellipse(R, phi_vals)

    if abs(b - a) < 1e-10:
        f_new = length * np.cos(phi_vals)
        g_new = length * np.sin(phi_vals)
    else:
        f_new = length * np.cos(phi_actual_vals)
        g_new = length * np.sin(phi_actual_vals)
    h_new = h

    p0 = np.array([f_new[0], g_new[0], h_new[0]])
    p90_idx = n_phi//4
    p90 = np.array([f_new[p90_idx], g_new[p90_idx], h_new[p90_idx]])
    p180 = np.array([f_new[n_phi//2], g_new[n_phi//2], h_new[n_phi//2]])
    v1 = p90 - p0
    v2 = p180 - p0
    normal = np.cross(v1, v2)
    normal = normalize(normal)
    n_glob = np.array([
        normal[0] * np.cos(beta) * np.cos(alpha) - normal[1] * np.sin(alpha) - normal[2] * np.cos(alpha) * np.sin(beta),
        normal[0] * np.cos(beta) * np.sin(alpha) + normal[1] * np.cos(alpha) - normal[2] * np.sin(alpha) * np.sin(beta),
        normal[0] * np.sin(beta) + normal[2] * np.cos(beta)
    ])
    x_n, y_n, z_n = n_glob[0], n_glob[1], n_glob[2]
    r_xy = np.sqrt(x_n**2 + y_n**2)
    if r_xy < 1e-15:
        beta_new_deg = 0.0
        alpha_new_deg = 0.0
    else:
        beta_new_rad = np.pi/2 - np.abs(np.arctan(z_n / r_xy))
        beta_new_deg = np.degrees(beta_new_rad)
        if x_n != 0:
            alpha_new_deg = np.degrees(np.arctan2(y_n, x_n))
        else:
            alpha_new_deg = 90.0 if y_n >= 0 else 270.0
        if alpha_new_deg < 0:
            alpha_new_deg += 360.0
    return a_new, b_new, gamma_new, alpha_new_deg, beta_new_deg

def write_final_crack_front(output_dir):
    import os, csv
    a0 = 0.1
    alpha0 = 0.0
    beta0 = 45.0
    sigma_x = 92e6
    sigma_y = 92e6
    sigma_z = 63e6
    P = 80e6
    nu = 0.25
    inc = 0.01
    steps = 20

    a, b, gamma = a0, a0, 0.0
    alpha, beta = alpha0, beta0
    for step in range(steps):
        a, b, gamma, alpha, beta = propagate_step(alpha, beta, a, b, gamma, inc, sigma_x, sigma_y, sigma_z, P, nu, n_phi=360)

    phi_deg = np.arange(0, 351, 10)
    phi_rad = np.radians(phi_deg)
    f, g = ellipse_coords(phi_rad, a, b, gamma)
    h = np.zeros_like(f)
    x, y, z = global_coords(f, g, h, alpha, beta)
    filepath = os.path.join(output_dir, 'final_crack_front.csv')
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['phi_deg', 'x', 'y', 'z'])
        for i in range(len(phi_deg)):
            writer.writerow([phi_deg[i], f'{x[i]:.6e}', f'{y[i]:.6e}', f'{z[i]:.6e}'])
"""
with open('/solution/compute.py', 'w') as f:
    f.write(textwrap.dedent(new_code))
PYEOF

# Now compute initial SIFs with signed omega
python3 <<'EOF'
import csv, math

a = 0.1
alpha_deg = 0.0
beta_deg = 45.0
sigma_x = 92e6
sigma_y = 92e6
sigma_z = 63e6
P = 80e6
nu = 0.25

alpha = math.radians(alpha_deg)
beta = math.radians(beta_deg)

l = math.sin(beta) * math.cos(alpha)
m = math.sin(beta) * math.sin(alpha)
n = -math.cos(beta)

sigma_n_ext = sigma_x * l**2 + sigma_y * m**2 + sigma_z * n**2
tau = math.sqrt((sigma_x*l)**2 + (sigma_y*m)**2 + (sigma_z*n)**2 - sigma_n_ext**2)
sigma_n_eff = P - sigma_n_ext
tau_eff = tau

if tau > 1e-12:
    l_tau = (sigma_x - sigma_n_ext) * l / tau
    m_tau = (sigma_y - sigma_n_ext) * m / tau
    n_tau = (sigma_z - sigma_n_ext) * n / tau
else:
    l_tau, m_tau, n_tau = 1.0, 0.0, 0.0

l_o = math.cos(beta) * math.cos(alpha)
m_o = math.cos(beta) * math.sin(alpha)
n_o = math.sin(beta)

# signed omega using cross product with crack normal
# crack normal = [l, m, n]
# u = projection of dip direction: [l_o, m_o, n_o]
# v = shear direction: [l_tau, m_tau, n_tau]
def cross(u, v):
    return [u[1]*v[2] - u[2]*v[1],
            u[2]*v[0] - u[0]*v[2],
            u[0]*v[1] - u[1]*v[0]]

u = [l_o, m_o, n_o]
v = [l_tau, m_tau, n_tau]
cross_uv = cross(u, v)
dot_uv = u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
n_dot_cross = l*cross_uv[0] + m*cross_uv[1] + n*cross_uv[2]
omega = math.atan2(n_dot_cross, dot_uv)

const1 = 2.0 * math.sqrt(a / math.pi) * sigma_n_eff
const2 = -4.0 / (2.0 - nu) * math.sqrt(a / math.pi) * tau_eff
const3 = 4.0 * (1.0 - nu) / (2.0 - nu) * math.sqrt(a / math.pi) * tau_eff

rows = []
for phi_deg in range(0, 351, 10):
    phi = math.radians(phi_deg)
    KI = const1
    KII = const2 * math.cos(phi - omega)
    KIII = const3 * math.sin(phi - omega)
    rows.append([phi_deg, KI, KII, KIII])

with open('/app/outputs/sifs_initial_crack.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['phi_deg', 'KI', 'KII', 'KIII'])
    for row in rows:
        writer.writerow([f'{row[0]}', f'{row[1]:.6e}', f'{row[2]:.6e}', f'{row[3]:.6e}'])
EOF

# === solve block: final_crack_front.csv ===
python3 -c "import sys; sys.path.insert(0, '/solution'); from compute import write_final_crack_front; write_final_crack_front('/app/outputs')"
