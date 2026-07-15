#!/usr/bin/env python3
import numpy as np
import sys, os, math
from scipy.optimize import fsolve

# ----- Material parameters (Case II) -----
T0 = -17.5          # reference temperature (°C)
T = 20.0            # test temperature (°C)
deltaT = T - T0

lambda_A = 29e9     # Pa
lambda_M = 15e9     # Pa
mu_A = 19e9         # Pa
mu_M = 12e9         # Pa
kappa_A = -0.1e6    # Pa/°C
kappa_M = -0.1e6    # Pa/°C
kappa = kappa_A     # constant (both equal)

M0s = -22.0
M0f = -24.0
A0s = -17.0
A0f = -13.0

sigma_s = 250e6
C_A = 6e6
C_M = 4.8e6
C0 = -0.5e6
C1f = 20e6
C1r = 30e6
sigma_bar = 40e6
D0f = 200e6
D0r = 200e6

epsilon_Lt = 0.055
epsilon_m = math.sqrt(1.5) * epsilon_Lt

p_asym = 0.8
Y_R = 0.155  # not used in uniaxial tension (reorientation limit remains inactive)

L, M, N = 1.0, 2.04, 2.04

# ----- Helper functions: Reuss mixing and derivatives -----
def compute_Z(Z_A, Z_M, xi):
    if abs(Z_M - Z_A) < 1e-6:
        return Z_A
    deltaZ = Z_A * Z_M / (Z_M - Z_A)
    inv = 1.0/Z_A - xi/deltaZ
    return 1.0/inv

def dZ_dxi(Z_A, Z_M, xi):
    if abs(Z_M - Z_A) < 1e-6:
        return 0.0
    Z = compute_Z(Z_A, Z_M, xi)
    deltaZ = Z_A * Z_M / (Z_M - Z_A)
    return Z*Z / deltaZ

# Phase-dependent elastic constants
lam = lambda xi: compute_Z(lambda_A, lambda_M, xi)
mu  = lambda xi: compute_Z(mu_A, mu_M, xi)
kap = lambda xi: kappa

dlam_dxi = lambda xi: dZ_dxi(lambda_A, lambda_M, xi)
dmu_dxi  = lambda xi: dZ_dxi(mu_A, mu_M, xi)
dkap_dxi = lambda xi: 0.0

# ----- Preferred direction and its norm -----
n0 = np.array([[ math.sqrt(2/3), 0, 0],
               [ 0, -1/math.sqrt(6), 0],
               [ 0, 0, -1/math.sqrt(6)]])

def compute_a0():
    # D matrix (a=b=1, theta=0 => A=I)
    # B = diag(sqrt(L), sqrt(M), sqrt(N))
    D_diag = np.array([1.0, 1.0, 1.0, math.sqrt(L), math.sqrt(M), math.sqrt(N)])
    n_voigt = np.array([n0[0,0], n0[1,1], n0[2,2], 0.0, 0.0, 0.0])
    Dn = n_voigt * D_diag
    norm_Dn = math.sqrt(Dn[0]*Dn[0] + Dn[1]*Dn[1] + Dn[2]*Dn[2])
    det_Dn = Dn[0] * Dn[1] * Dn[2]
    I3 = 3*math.sqrt(6) * det_Dn / (norm_Dn**3)
    
    def g(x):
        arg = 1.0 - p_asym * (1.0 - x)
        arg = max(-1.0, min(1.0, arg))
        return math.cos( math.acos(arg) / 3.0 )
    g_m1 = g(-1.0)
    g_negI3 = g(-I3)
    a = g_m1 / (norm_Dn * g_negI3)
    return a

a0 = compute_a0()

# ----- Kinetic functions -----
def C0_f(Tcur):
    if Tcur > M0s:
        return sigma_s - C_M*M0s + C_A*T0 + (C_M - C_A)*Tcur
    else:
        return sigma_s - C0*M0s + C_A*T0 + (C0 - C_A)*Tcur

def C0_r(Tcur):
    if Tcur > M0s:
        return C_A*(A0f - T0)
    else:
        return C_A*(A0f - M0s - T0) + C0*M0s + (C_A - C0)*Tcur

def Y_S_forward(xi):
    c0 = C0_f(T)
    ln = math.log(1 - xi + math.exp(-7))
    return c0 - C1f * xi * ln + D0f*(1 - a0)

def Y_S_reverse(xi):
    c0 = C0_r(T)
    ln = math.log(1 - xi + math.exp(-7))
    extra = (C_A*(A0s - A0f) + sigma_bar) * xi
    return c0 - C1r * xi * ln + extra + D0r*(1 - a0)

# ----- Tensor helpers -----
def N_tensor(a):
    return a * n0

def Ci_inv(xi, a):
    N = N_tensor(a)
    Ci = np.eye(3) + 2*epsilon_m * xi * N
    return np.linalg.inv(Ci)

def compute_S(F, xi, a):
    Ci_inv_ = Ci_inv(xi, a)
    C = F.T @ F
    tr_Ci1C = np.trace(Ci_inv_ @ C)
    lam_val = lam(xi)
    mu_val = mu(xi)
    kap_val = kap(xi)
    coef = 0.5*lam_val*tr_Ci1C - 1.5*lam_val - 3*kap_val*deltaT - mu_val
    S = coef * Ci_inv_ + mu_val * (Ci_inv_ @ C @ Ci_inv_)
    return S

def compute_sigma(F, xi, a):
    S = compute_S(F, xi, a)
    J = np.linalg.det(F)
    sigma = (1/J) * F @ S @ F.T
    return sigma

def compute_Lambda(F, xi, a):
    Ci_inv_ = Ci_inv(xi, a)
    C = F.T @ F
    OC = C @ Ci_inv_
    trOC = np.trace(OC)
    trOC2 = np.trace(OC @ OC)
    part1 = (0.125*trOC*trOC - 0.75*trOC + 1.125) * dlam_dxi(xi)
    part2 = (0.25*trOC2 - 0.5*trOC + 0.75) * dmu_dxi(xi)
    part3 = 1.5 * (3 - trOC) * deltaT * dkap_dxi(xi)
    return part1 + part2 + part3

def compute_Q_S(F, xi, a):
    S = compute_S(F, xi, a)
    Ci_inv_ = Ci_inv(xi, a)
    C = F.T @ F
    M = S @ C @ Ci_inv_
    I = np.eye(3)
    MD = M - (1/3)*np.trace(M)*I
    N = N_tensor(a)
    term1 = np.tensordot(MD, N)  # double contraction
    Lambda_val = compute_Lambda(F, xi, a)
    term2 = (1/epsilon_m)*Lambda_val + C_A*deltaT + sigma_bar*xi
    return term1 - term2

# ------ Single-point solver ------
def solve_elastic(lambda1, lambda2_guess, xi_fixed):
    def eq(lambda2):
        F = np.diag([lambda1, lambda2[0], lambda2[0]])
        sigma = compute_sigma(F, xi_fixed, a0)
        return sigma[1,1]
    lambda2_sol = fsolve(eq, [lambda2_guess], xtol=1e-12)
    return lambda2_sol[0]

def solve_step(lambda1, lambda2_guess, xi_guess, is_loading):
    # unknowns: lambda2, xi
    def equations(vars):
        lambda2, xi = vars
        F = np.diag([lambda1, lambda2, lambda2])
        sigma = compute_sigma(F, xi, a0)
        eq1 = sigma[1,1]
        QS = compute_Q_S(F, xi, a0)
        if is_loading:
            YS = Y_S_forward(xi)
            eq2 = QS - YS
        else:
            YS = Y_S_reverse(xi)
            eq2 = -QS - YS   # F_S = 0 with sgn(Q) for reverse (Q neg -> -Q - Y_r = 0)
        return [eq1, eq2]
    sol = fsolve(equations, [lambda2_guess, xi_guess], maxfev=1000, xtol=1e-12)
    return sol[0], sol[1]

# ------ Main simulation ------
def main():
    # strain path
    strain_loading = np.linspace(0, 0.08, 200)
    strain_unloading = np.linspace(0.08, 0, 200)
    strains = list(strain_loading) + list(strain_unloading[1:])
    
    xi_S = 0.0
    lambda2 = 1.0
    loading_phase = True
    results = []
    
    for e in strains:
        lambda1 = 1.0 + e
        if loading_phase and e >= 0.0799:
            loading_phase = False
        
        if loading_phase:
            # Elastic trial
            lambda2_el = solve_elastic(lambda1, lambda2, xi_S)
            F_tmp = np.diag([lambda1, lambda2_el, lambda2_el])
            QS_trial = compute_Q_S(F_tmp, xi_S, a0)
            if QS_trial - Y_S_forward(xi_S) < 0:
                lambda2 = lambda2_el
            else:
                lambda2, xi_S = solve_step(lambda1, lambda2_el, xi_S, True)
        else:
            # Unloading (reverse)
            lambda2_el = solve_elastic(lambda1, lambda2, xi_S)
            F_tmp = np.diag([lambda1, lambda2_el, lambda2_el])
            QS_trial = compute_Q_S(F_tmp, xi_S, a0)
            if -QS_trial - Y_S_reverse(xi_S) < 0:
                lambda2 = lambda2_el
            else:
                lambda2, xi_S = solve_step(lambda1, lambda2_el, xi_S, False)
        
        # Compute stress for output
        F_final = np.diag([lambda1, lambda2, lambda2])
        sigma = compute_sigma(F_final, xi_S, a0)
        stress_MPa = sigma[0,0] / 1e6
        xi_T = 0.0
        N_norm = a0
        results.append([e, stress_MPa, xi_S, xi_T, N_norm])
    
    # Write CSV
    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, 'step_01_stress_strain.csv')
    with open(path, 'w') as f:
        f.write('strain,stress_MPa,xi_S,xi_T,N_norm\n')
        for row in results:
            f.write(','.join(str(v) for v in row) + '\n')
    print(f"CSV written to {path}")

if __name__ == '__main__':
    main()