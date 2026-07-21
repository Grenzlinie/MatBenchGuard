import numpy as np
import sys
import csv
import os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')

# Physical constants
z = 6
chi0 = 1.0 / z          # constant at half-filling for parabolic band
Lambda2 = 8 * np.pi / np.sqrt(3)
Lambda = np.sqrt(Lambda2)
area = np.pi * Lambda2
xi = 1.2
t_c = 1.0
U = 1.0

# k-mesh for radial integration
Nk = 200
ks = np.linspace(1e-6, Lambda, Nk)
dk = ks[1] - ks[0]
weights = 2 * np.pi * ks * dk / area

def compute_chi_cf(Phi, td_div_U, V2_div_U, T=0.001):
    td = td_div_U * U
    V = np.sqrt(V2_div_U)
    Vf = V * Phi
    T_f = 4 * td**2 * chi0
    eps_f = 1.5 * T_f * (ks**2 - Lambda2/2)
    eps_c = 1.5 * t_c * (ks**2 - xi * Lambda2/2)
    delta = eps_f - eps_c
    denom = np.sqrt((delta/2)**2 + Vf**2)
    E1 = 0.5*(eps_f + eps_c) + denom
    E2 = 0.5*(eps_f + eps_c) - denom
    n1 = 1.0 / (1.0 + np.exp(E1 / T))
    n2 = 1.0 / (1.0 + np.exp(E2 / T))
    integrand = -0.5 * (n1 - n2) / denom
    return np.sum(integrand * weights)

def solve_Phi(td_div_U, V2_div_U):
    if V2_div_U == 0:
        return 0.0
    lo, hi = 0.0, 0.9999
    def eq(Phi):
        if Phi == 0:
            return 0.0
        LHS = (1/8)*(1/np.sqrt(1-Phi**2) - 8*z*td_div_U*chi0)
        chi_cf = compute_chi_cf(Phi, td_div_U, V2_div_U)
        RHS = V2_div_U * chi_cf
        return LHS - RHS
    f_lo = eq(lo)
    f_hi = eq(hi)
    if f_lo * f_hi > 0:
        return 0.0
    for _ in range(50):
        mid = (lo+hi)/2
        f_mid = eq(mid)
        if f_mid == 0:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    return (lo+hi)/2

def compute_ldos_meanfield(td_div_U, V2_div_U, omega_min, omega_max, omega_step, eta=0.01):
    Phi = solve_Phi(td_div_U, V2_div_U)
    td = td_div_U
    V2 = V2_div_U
    V = np.sqrt(V2)
    Vf = V * Phi
    T_f = 4 * td**2 * chi0
    eps_f = 1.5 * T_f * (ks**2 - Lambda2/2)
    eps_c = 1.5 * t_c * (ks**2 - xi * Lambda2/2)
    delta = eps_f - eps_c
    denom = np.sqrt((delta/2)**2 + Vf**2)
    E1 = 0.5*(eps_f + eps_c) + denom
    E2 = 0.5*(eps_f + eps_c) - denom
    cos2alpha = delta / (2*denom)
    cos2 = 0.5*(1+cos2alpha)
    sin2 = 0.5*(1-cos2alpha)
    omegas = np.arange(omega_min, omega_max, omega_step)
    A = np.zeros_like(omegas)
    for idx, w in enumerate(omegas):
        l1 = eta / ((w - E1)**2 + eta**2)
        l2 = eta / ((w - E2)**2 + eta**2)
        integrand = cos2 * l1 + sin2 * l2
        A[idx] = np.sum(integrand * weights) / np.pi
    return omegas, A

def write_ldos_anderson_zeroT():
    omegas, A = compute_ldos_meanfield(0.0, 0.5, -1.5, 1.5, 0.005)
    with open(os.path.join(OUTDIR, 'ldos_anderson_zeroT.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['omega', 'A(omega)'])
        for o, a in zip(omegas, A):
            writer.writerow([o, a])

def write_ldos_finite_td():
    omegas, A = compute_ldos_meanfield(0.04, 0.35, -1.5, 1.5, 0.005)
    with open(os.path.join(OUTDIR, 'ldos_finite_td.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['omega', 'A(omega)'])
        for o, a in zip(omegas, A):
            writer.writerow([o, a])

def compute_broadened_ldos(td_div_U, V2_div_U, T, gamma0=0.05, omega_min=-1.5, omega_max=1.5, omega_step=0.005):
    Phi = solve_Phi(td_div_U, V2_div_U)
    td = td_div_U
    V2 = V2_div_U
    V = np.sqrt(V2)
    Vf = V * Phi
    T_f = 4 * td**2 * chi0
    eps_f = 1.5 * T_f * (ks**2 - Lambda2/2)
    eps_c = 1.5 * t_c * (ks**2 - xi * Lambda2/2)
    delta = eps_f - eps_c
    denom = np.sqrt((delta/2)**2 + Vf**2)
    E1 = 0.5*(eps_f + eps_c) + denom
    E2 = 0.5*(eps_f + eps_c) - denom
    cos2alpha = delta / (2*denom)
    cos2 = 0.5*(1+cos2alpha)
    sin2 = 0.5*(1-cos2alpha)
    W_sp = 1.5 * T_f * Lambda2
    D_c = 0.75 * t_c * Lambda2
    T_K = 2 * Vf**2 / D_c if D_c > 0 else 0.0
    E0 = np.sqrt(T_K**2 + W_sp**2)
    omegas = np.arange(omega_min, omega_max, omega_step)
    A = np.zeros_like(omegas)
    for idx, w in enumerate(omegas):
        gamma_tot = gamma0 + (w**2 + (np.pi*T)**2) / (2 * np.pi * E0)
        l1 = gamma_tot / ((w - E1)**2 + gamma_tot**2)
        l2 = gamma_tot / ((w - E2)**2 + gamma_tot**2)
        integrand = cos2 * l1 + sin2 * l2
        A[idx] = np.sum(integrand * weights) / np.pi
    return omegas, A

def write_ldos_anderson_broadened():
    omegas, A = compute_broadened_ldos(0.0, 0.5, T=0.05, gamma0=0.05, omega_min=-1.5, omega_max=1.5, omega_step=0.005)
    with open(os.path.join(OUTDIR, 'ldos_anderson_broadened.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['omega', 'A(omega)'])
        for o, a in zip(omegas, A):
            writer.writerow([o, a])

def half_max_width(omegas, A):
    idx_max = np.argmax(A)
    A_max = A[idx_max]
    half = A_max / 2.0
    zero_idx = np.argmin(np.abs(omegas))
    for i in range(zero_idx, len(omegas)):
        if A[i] <= half:
            if i == 0:
                return abs(omegas[0])
            omega_i = omegas[i]
            omega_prev = omegas[i-1]
            A_i = A[i]
            A_prev = A[i-1]
            if A_i == A_prev:
                return abs(omega_i)
            return abs(omega_prev + (half - A_prev) / (A_i - A_prev) * (omega_i - omega_prev))
    return None

def write_width_vs_T():
    Ts = [0.01, 0.02, 0.05, 0.1, 0.2]
    with open(os.path.join(OUTDIR, 'width_vs_T.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T_div_tc', 'half_max_width'])
        for T in Ts:
            omegas, A = compute_broadened_ldos(0.0, 0.5, T=T, gamma0=0.05, omega_min=-1.5, omega_max=1.5, omega_step=0.001)
            w = half_max_width(omegas, A)
            writer.writerow([T, w])

def write_phase_diagram():
    td_vals = np.arange(0, 0.155, 0.005)
    V2_vals = np.arange(0, 2.02, 0.02)
    with open(os.path.join(OUTDIR, 'phase_diagram.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['t_d_div_U', 'V2_div_U', 'Phi'])
        for td in td_vals:
            td = round(td, 10)
            for V2 in V2_vals:
                V2 = round(V2, 10)
                phi = solve_Phi(td, V2)
                writer.writerow([td, V2, phi])

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'phase':
        write_phase_diagram()
    elif cmd == 'ldos_anderson_zeroT':
        write_ldos_anderson_zeroT()
    elif cmd == 'ldos_finite_td':
        write_ldos_finite_td()
    elif cmd == 'ldos_anderson_broadened':
        write_ldos_anderson_broadened()
    elif cmd == 'width_vs_T':
        write_width_vs_T()
    else:
        print('Unknown command')
        sys.exit(1)
