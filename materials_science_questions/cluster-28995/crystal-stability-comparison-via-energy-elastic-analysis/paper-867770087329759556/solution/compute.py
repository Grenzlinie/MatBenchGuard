import sys
import math
import numpy as np

def V_R(R, A, a1, a2, mu1, mu2):
    poly = 1.0 + a1*R + a2*R*R
    exp_term = math.exp(-mu1*R - mu2*R*R)
    return A * poly * exp_term

def dV_R_dR(R, A, a1, a2, mu1, mu2):
    f = 1.0 + a1*R + a2*R*R
    f_prime = a1 + 2.0*a2*R
    g_prime = -mu1 - 2.0*mu2*R
    exp_term = math.exp(-mu1*R - mu2*R*R)
    return A * exp_term * (f_prime + f * g_prime)

def d2V_R_dR2(R, A, a1, a2, mu1, mu2):
    f = 1.0 + a1*R + a2*R*R
    f_prime = a1 + 2.0*a2*R
    f_dprime = 2.0*a2
    g_prime = -mu1 - 2.0*mu2*R
    g_dprime = -2.0*mu2
    exp_term = math.exp(-mu1*R - mu2*R*R)
    part = f_dprime + 2.0*f_prime*g_prime + f*(g_prime*g_prime + g_dprime)
    return A * exp_term * part

def rho(R, g_rho, nu):
    return g_rho * math.exp(-nu * R)

def rho_prime(R, g_rho, nu):
    return -nu * rho(R, g_rho, nu)

def rho_dprime(R, g_rho, nu):
    return nu*nu * rho(R, g_rho, nu)

# Parameters from Table 1
A_val   = 2.10e-15  # J
a1_val  = -0.5819    # Å⁻¹
a2_val  =  0.09309   # Å⁻²
mu1_val =  3.000     # Å⁻¹
mu2_val = -0.03996   # Å⁻²
g_rho_val = 80.0
nu_val    = 3.60     # Å⁻¹

# Lattice constants (Å)
a_list = np.arange(3.8, 5.25, 0.1).tolist()  # includes 5.2

fcc_basis = np.array([[0,0,0],
                      [0,0.5,0.5],
                      [0.5,0,0.5],
                      [0.5,0.5,0]])

def compute_for_a(a):
    # max neighbor distance = a*sqrt(3)
    r_max = a * math.sqrt(3.0)
    r_max_sq = r_max * r_max
    # grid index range
    n_max = int(math.ceil(r_max / a + 0.5)) + 1
    # accumulate sums
    lambda_sum = 0.0
    alpha0_sum = 0.0
    alpha0s_sum = 0.0
    beta0_sum = 0.0
    beta0s_sum = 0.0
    # neighbor lists for second pass
    neighbors = []  # (x,y,z,R,s)
    for i in range(-n_max, n_max+1):
        for j in range(-n_max, n_max+1):
            for k in range(-n_max, n_max+1):
                for b in fcc_basis:
                    x = a * (i + b[0])
                    y = a * (j + b[1])
                    z = a * (k + b[2])
                    R2 = x*x + y*y + z*z
                    if R2 < 1e-12 or R2 > r_max_sq+1e-9:
                        continue
                    R = math.sqrt(R2)
                    s = (x**4 + y**4 + z**4) / (R2*R2)
                    neighbors.append((x,y,z,R,s))
                    # rho sums
                    rho_val = rho(R, g_rho_val, nu_val)
                    lambda_sum += rho_val
                    alpha0_sum += R * rho_prime(R, g_rho_val, nu_val)
                    alpha0s_sum += R * rho_prime(R, g_rho_val, nu_val) * s
                    beta0_sum += R*R * rho_dprime(R, g_rho_val, nu_val)
                    beta0s_sum += R*R * rho_dprime(R, g_rho_val, nu_val) * s
    if len(neighbors) == 0:
        raise RuntimeError("No neighbors found")
    # lambda is the sum of rho over all neighbors
    lambda_const = lambda_sum
    factor = math.exp(-2.0 * lambda_const)
    Omega = a**3 / 4.0  # atomic volume per atom (Å³)
    # sums for u,v,w
    sum_phi = 0.0
    sum_R_phi_prime = 0.0
    sum_R2_phi_dprime = 0.0
    sum_phi_s = 0.0
    sum_R_phi_prime_s = 0.0
    sum_R2_phi_dprime_s = 0.0
    for (x,y,z,R,s) in neighbors:
        vR = V_R(R, A_val, a1_val, a2_val, mu1_val, mu2_val)
        phi = factor * vR
        phi_prime = factor * dV_R_dR(R, A_val, a1_val, a2_val, mu1_val, mu2_val)
        phi_dprime = factor * d2V_R_dR2(R, A_val, a1_val, a2_val, mu1_val, mu2_val)
        sum_phi += phi
        sum_R_phi_prime += R * phi_prime
        sum_R2_phi_dprime += R*R * phi_dprime
        sum_phi_s += phi * s
        sum_R_phi_prime_s += R * phi_prime * s
        sum_R2_phi_dprime_s += R*R * phi_dprime * s
    inv_2Omega = 0.5 / Omega
    u = sum_phi * inv_2Omega
    v = sum_R_phi_prime * inv_2Omega
    w = sum_R2_phi_dprime * inv_2Omega
    u_s = sum_phi_s * inv_2Omega
    v_s = sum_R_phi_prime_s * inv_2Omega
    w_s = sum_R2_phi_dprime_s * inv_2Omega
    # environment parameters
    alpha0 = alpha0_sum
    alpha0_s = alpha0s_sum
    beta0 = beta0_sum
    beta0_s = beta0s_sum
    # Closed forms (units: J/Å³)
    P = (1.0/3.0) * (-v + 2.0*u*alpha0)
    delta = (4.0/9.0) * (-alpha0*v + u*alpha0*alpha0)
    P_s = (1.0/3.0) * (-v_s + 2.0*u*alpha0_s)
    K   = (1.0/3.0) * (w - 2.0*u*beta0)
    K_s = (1.0/3.0) * (w_s - 2.0*u*beta0_s)
    B   = (2.0/3.0)*P + (1.0/3.0)*K + delta
    C11 = -P + P_s + K_s + delta
    C12 = 0.5*(3.0*P + K - P_s - K_s) + delta
    C44 = 0.5*(-P + K - P_s - K_s)
    # convert from J/Å³ to GPa: 1 J/Å³ = 10^30 Pa = 10^21 GPa
    conv = 1e21
    return (P*conv, delta*conv, B*conv, C11*conv, C12*conv, C44*conv)

def main():
    outpath = sys.argv[1]
    with open(outpath, 'w') as f:
        f.write('lattice_constant_A,pressure_GPa,delta_GPa,B_GPa,C11_GPa,C12_GPa,C44_GPa\n')
        for a in a_list:
            P, delta, B, C11, C12, C44 = compute_for_a(a)
            f.write(f'{a:.1f},{P:.6f},{delta:.6f},{B:.6f},{C11:.6f},{C12:.6f},{C44:.6f}\n')

if __name__ == '__main__':
    main()