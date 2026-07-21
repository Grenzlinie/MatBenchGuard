#!/usr/bin/env python3
import numpy as np
from scipy.special import jv, gamma as Gamma
from scipy.integrate import quad
import json
import sys

# Material constants (SI)
c11 = 12.6e10
c33 = 11.7e10
c44 = 3.53e10
c13 = 5.3e10
e31 = -6.5
e33 = 23.3
e15 = 17.0
eps11 = 151.0e-10
eps33 = 130.0e-10

def alpha_coeffs(gamma):
    """Compute α1…α19 as per the paper."""
    a1 = (c13 + c44) * eps11 + (e15 + e31) * e15
    a2 = gamma * (e15**2 + 2*e15*e31 + (2*c13 + c44) * eps11)
    a3 = gamma**2 * (e15*e31 + c13*eps11)
    a4 = e33*(e15 + e31) + eps33*(c13 + c44)
    a5 = gamma * (e31*e33 + c13*eps33)
    a6 = -(e15 + e31)**2 - c44*eps11 - c11*eps33
    a7 = -gamma * ((e15 + e31)**2 + c44*eps11 + c11*eps33)
    a8 = -c44 * eps33
    a9 = -gamma**2 * e15*e31
    a10 = -c11 * eps11
    a11 = -2*gamma * c11 * eps11
    a12 = -gamma**2 * c11 * eps11
    a13 = c44*e31 + (e15 + e31)*c13 - c11*e33
    a14 = -gamma * (-c13*(2*e15 + e31) + c11*e33)
    a15 = -c44 * e33
    a16 = gamma**2 * c13 * e15
    a17 = -c11 * e15
    a18 = -2*gamma * c11 * e15
    a19 = -gamma**2 * c11 * e15
    return (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19)

def poly_coeffs(gamma):
    """Compute a,b,c,d,e,f,g,h,w1..w4."""
    a = -c44*(e33**2 + c33*eps33)
    b = (e33*(2*c44*e31 - c11*e33) + c13**2*eps33
         - c33*((e15+e31)**2 + c44*eps11 + c11*eps33)
         + 2*c13*(e15*e33 + e31*e33 + c44*eps33))
    c = -gamma * (e33*(-2*c44*e31 + c11*e33) - c13**2*eps33
                  + c33*((e15+e31)**2 + c44*eps11 + c11*eps33)
                  - 2*c13*(e15*e33 + e31*e33 + c44*eps33))
    d = gamma**2 * (-c33*e15*e31 + c13*e15*e33 + c44*e31*e33 + c13*c44*eps33)
    e_ = (-c44*e31**2 - 2*c11*e15*e33 + c13**2*eps11 - c11*c33*eps11
          + 2*c13*(e15*(e15+e31) + c44*eps11) - c11*c44*eps33)
    f = 2*gamma * e_
    g = -gamma**2 * (c44*e31**2 + 2*c11*e15*e33 - c13**2*eps11 + c11*c33*eps11
                     - c13*(3*e15**2 + 2*e15*e31 + 3*c44*eps11) + c11*c44*eps33)
    h = gamma**3 * c13*(e15**2 + c44*eps11)
    w1 = -c11*(e15**2 + c44*eps11)
    w2 = -3*gamma * c11*(e15**2 + c44*eps11)
    w3 = -3*gamma**2 * c11*(e15**2 + c44*eps11)
    w4 = -gamma**3 * c11*(e15**2 + c44*eps11)
    return a, b, c, d, e_, f, g, h, w1, w2, w3, w4

def characteristic_roots(s, gamma, a,b,c,d,e_,f,g,h,w1,w2,w3,w4):
    """Return λ_i (i=1..3) with Re(λ_i)>0."""
    # b0, c0, d0, e0 from Eq.(30)
    b0 = a
    c0 = -(-b*s**2 + 1j*c*s + d)
    d0 = e_*s**4 - 1j*f*s**3 - g*s**2 + 1j*s*h
    e0 = w1*s**6 - 1j*w2*s**5 - w3*s**4 + 1j*w4*s**3
    # cubic: b0*z^3 - c0*z^2 + d0*z - e0 = 0
    coeffs = [b0, -c0, d0, -e0]
    z_roots = np.roots(coeffs)
    lambdas = []
    for z in z_roots:
        lam = np.sqrt(z)   # principal branch
        if lam.real < 0:
            lam = -lam
        lambdas.append(lam)
    return np.array(lambdas)

def modal_functions(s, lambdas, gamma, alphas):
    """Compute χ_i^{(1)},χ_i^{(2)},χ_i^{(3)} and β_i^{(1)},β_i^{(2)},β_i^{(3)}."""
    (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,
     a13,a14,a15,a16,a17,a18,a19) = alphas
    chi1 = []
    chi2 = []
    chi3 = []
    beta1 = []
    beta2 = []
    beta3 = []
    for lam in lambdas:
        # χ_i^(1)
        term = (-lam * (-1j*a1*s**3 - a2*s**2 + 1j*a3*s
                       + 1j*a4*lam**2 + a5*lam**2))
        chi1.append(term)
        # χ_i^(2)
        term = (-a6*s**2*lam**2 + 1j*a7*s*lam**2 + a8*lam**4 + a9*lam**2
                + a10*s**4 - a11*1j*s**3 - a12*s**2)
        chi2.append(term)
        # χ_i^(3)
        term = (-a13*s**2*lam**2 + 1j*a14*s*lam**2 + a15*lam**4 + a16*lam**2
                + a17*s**4 - a18*1j*s**3 - a19*s**2)
        chi3.append(term)
        # β_i^(1)
        b1 = 1j*s*c13*chi1[-1] - c33*lam*chi2[-1] - e33*lam*chi3[-1]
        beta1.append(b1)
        # β_i^(2)
        b2 = -lam*c44*chi1[-1] + 1j*s*c44*chi2[-1] + 1j*s*e15*chi3[-1]
        beta2.append(b2)
        # β_i^(3)
        b3 = 1j*s*e31*chi1[-1] - e33*lam*chi2[-1] + eps33*lam*chi3[-1]
        beta3.append(b3)
    return (np.array(chi1), np.array(chi2), np.array(chi3),
            np.array(beta1), np.array(beta2), np.array(beta3))

def compute_kernels(s, gamma, alphas, poly_coeffs_vals):
    """Solve 6x6 system to obtain g1,g2,g4,g5 at a given s."""
    a,b,c,d,e_,f,g,h,w1,w2,w3,w4 = poly_coeffs_vals
    lambdas = characteristic_roots(s, gamma, a,b,c,d,e_,f,g,h,w1,w2,w3,w4)
    chi1,chi2,chi3,beta1_vals,beta2_vals,beta3_vals = modal_functions(s, lambdas, gamma, alphas)
    # Build C_A (3x3) and D_A (3x3)
    C_A = np.array([chi1, beta1_vals, beta3_vals])   # rows
    D_A = np.array([chi2, chi3, beta2_vals])
    # Assemble 6x6 system: M = [[C_A, -C_A],[D_A, D_A]]
    zero3 = np.zeros((3,3))
    M = np.block([[C_A, -C_A], [D_A, D_A]])
    # RHS for (f2_bar=1, f3_bar=0) -> rhs = [0,0,0, 1,0,0]
    rhs_g1 = np.array([0.0,0,0, 1.0,0,0])
    sol1 = np.linalg.solve(M, rhs_g1)
    A1 = sol1[:3]
    # stress coefficient for g1: sum β_i^(1) * A_i
    g1_val = np.dot(beta1_vals, A1)
    # D_y coefficient for g4
    g4_val = np.dot(beta3_vals, A1)
    # RHS for (f2_bar=0, f3_bar=1)
    rhs_g2 = np.array([0.0,0,0, 0.0,1.0,0])
    sol2 = np.linalg.solve(M, rhs_g2)
    A2 = sol2[:3]
    g2_val = np.dot(beta1_vals, A2)
    g5_val = np.dot(beta3_vals, A2)
    return g1_val, g2_val, g4_val, g5_val

def beta_constants():
    """Compute asymptotic β1,β2,β4,β5 using large s and gamma=0."""
    gamma0 = 0.0
    alphas0 = alpha_coeffs(gamma0)
    poly0 = poly_coeffs(gamma0)
    s_large = 1e6
    g1, g2, g4, g5 = compute_kernels(s_large, gamma0, alphas0, poly0)
    beta1 = (g1 / s_large).real
    beta2 = (g2 / s_large).real
    beta4 = (g4 / s_large).real
    beta5 = (g5 / s_large).real
    return beta1, beta2, beta4, beta5

def G_n(n):
    """Factor G_n = 2√π (-1)^n i^n Γ(n+1+1/2)/n!"""
    return 2.0 * np.sqrt(np.pi) * ((-1)**n) * (1j**n) * Gamma(n+1+0.5) / Gamma(n+1)

def compute_graded_case(gamma_val, D0_eps_ratio, l=1.0, N=10):
    """Solve dual integral eq. via collocation, return K_I_norm, K_D_norm."""
    gamma = gamma_val / l   # since γl=gamma_val
    alphas = alpha_coeffs(gamma)
    poly = poly_coeffs(gamma)
    # asymptotic betas (same as homogeneous)
    beta1,beta2,beta4,beta5 = beta_constants()
    # s-grid for kernel precomputation
    S = 2000.0
    Ns = 20001
    s_grid = np.linspace(-S, S, Ns)
    ds = s_grid[1] - s_grid[0]
    # precompute g(s) = g1(s) + (D0/eps0)*g2(s) and similarly for D
    g_stress = []
    g_D = []
    for s in s_grid:
        if abs(s) < 1e-10:   # avoid division by zero
            s_val = 1e-10
        else:
            s_val = s
        g1,g2,g4,g5 = compute_kernels(s_val, gamma, alphas, poly)
        g_stress.append(g1 + D0_eps_ratio * g2)
        g_D.append(g4 + D0_eps_ratio * g5)
    g_stress = np.array(g_stress)
    g_D = np.array(g_D)
    # factor inside integrand: K(s) = 1/(s(i s+γ)) * g_stress
    # avoid division by zero at s=0 by using small epsilon if needed
    denom = s_grid * (1j * s_grid + gamma)
    # replace zero with small
    mask_zero = np.abs(s_grid) < 1e-10
    s_grid_safe = np.where(mask_zero, 1e-10, s_grid)
    denom = s_grid_safe * (1j * s_grid_safe + gamma)
    kernel_factor = g_stress / denom
    # collocation points x_k = -l + (k+0.5)*2l/(N+1)
    xs = -l + (np.arange(N+1) + 0.5) * 2*l / (N+1)
    # RHS: -∫_{-l}^{x} τ0(t) dt, τ0(x)=p0=1 => RHS(x) = -(x+l)
    rhs_vals = - (xs + l)
    # Build matrix A_nk = K_n(x_k)
    A = np.zeros((N+1, N+1), dtype=complex)
    for n in range(N+1):
        Gn = G_n(n)
        # J_{n+1}(s l)
        J_vals = jv(n+1, s_grid_safe * l)
        integrand = kernel_factor * J_vals
        # For each x_k, multiply by (exp(i s x_k + γ x_k) - exp(-i s l - γ l))
        exp_common = np.exp(-1j * s_grid_safe * l - gamma * l)
        for k, xk in enumerate(xs):
            exp_x = np.exp(1j * s_grid_safe * xk + gamma * xk)
            factor = exp_x - exp_common
            I_s = integrand * factor
            # integrate using trapz
            integral = np.trapz(I_s, s_grid_safe)
            A[k, n] = Gn * integral / (2*np.pi)
    # Take real part (must be real)
    A_real = A.real
    rhs_real = rhs_vals.real
    # Solve for b_n
    b_n = np.linalg.solve(A_real, rhs_real)
    # Compute K_I from Eq.(68)
    C = 2.0 * (beta1 + D0_eps_ratio * beta2) * np.exp(gamma * l) / np.sqrt(np.pi * l)
    sum_b = np.sum(b_n * Gamma(np.arange(N+1) + 1 + 0.5) / Gamma(np.arange(N+1) + 1))
    K_I = -C * sum_b   # stress intensity factor
    # normalize: K_I / (p0√l), p0=1
    K_I_norm = K_I / (1.0 * np.sqrt(l))
    # K_D from Eq.(69)
    K_D_norm = (beta4 + D0_eps_ratio * beta5) / (beta1 + D0_eps_ratio * beta2) * K_I_norm
    return K_I_norm.real, K_D_norm.real

def main():
    output_path = sys.argv[1]
    # compute beta constants
    beta1,beta2,beta4,beta5 = beta_constants()
    D0_eps0 = 4.0e8
    # homogeneous case
    K_I_hom = 1.0
    K_D_hom = (beta4 + D0_eps0 * beta5) / (beta1 + D0_eps0 * beta2)
    # graded case
    gamma_l_val = 0.4
    K_I_grad, K_D_grad = compute_graded_case(gamma_l_val, D0_eps0)
    result = {
        "homogeneous": {
            "K_I_normalized": K_I_hom,
            "K_D_normalized": K_D_hom
        },
        "graded": {
            "gamma_l": gamma_l_val,
            "D0_epsilon0": D0_eps0,
            "loading_type": "p0",
            "K_I_normalized": K_I_grad,
            "K_D_normalized": K_D_grad
        }
    }
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)
    print("intensity_factors.json written.")

if __name__ == "__main__":
    main()
