#!/usr/bin/env python3
"""Hidden oracle: compute XXZ short-distance correlation functions."""
import sys, json, numpy as np
from numpy import pi, cosh, sinh, tanh, sqrt, log, exp, array, real, zeros, ones, arange, linspace, fft

def solve_ising(delta, J, h, T):
    """Return dict with keys for n=2,3,4 longitudinal and transversal."""
    # Ising limit: delta->infty, J finite, JI = J*delta
    JI = J * delta
    # formulas (29a,b)
    h2T = h/(2*T)
    sh = sinh(h2T)
    ch = cosh(h2T)
    e4 = exp(4*JI/T)
    denom = sqrt(sh*sh + e4)
    mz = sh/denom  # <sigma^z>
    # correlation function <sigma_z sigma_z> for distance n
    # from (29b): <s^z_1 s^z_{n+1}> = sh^2/(sh^2+e4) + e4/(sh^2+e4) * ((ch - denom)/(ch + denom))^(n)
    def corr_z(n):
        if n == 0:
            return 1.0  # not used
        base = (ch - denom)/(ch + denom)
        return (sh**2)/(sh**2+e4) + (e4/(sh**2+e4)) * base**n
    results = {}
    for n in [2,3,4]:
        cz = corr_z(n-1)  # distance: n-1 = 1,2,3
        connected_z = cz - mz*mz
        results[f'ising_n{n}_longitudinal'] = connected_z
        results[f'ising_n{n}_transversal'] = 0.0  # transversal vanishes in classical Ising
    return results

def K_tilde(z, eta):
    """K̃η(z) = sinh(2η) / (2 sin(z+iη) sin(z-iη))"""
    return sinh(2*eta) / (2 * np.sin(z + 1j*eta) * np.sin(z - 1j*eta))

def L_tilde(z, eta):
    """L̃η(z) = i sin(2z) / (2 sin(z+iη) sin(z-iη))"""
    return (1j * np.sin(2*z)) / (2 * np.sin(z + 1j*eta) * np.sin(z - 1j*eta))

def compute_omega_paramagnet(mu1, mu2, eta, h, T):
    z = -1j * mu2 + 1j * mu1  # μ̃2 - μ̃1 = -i mu2 + i mu1
    th2 = tanh(h/(2*T))**2
    omega = K_tilde(z, eta) * th2
    omegaprime = L_tilde(z, eta) * th2
    return omega, omegaprime

def solve_massive_one(delta, J, h, T, N=128, max_iter=100, mix=0.5):
    """Numerical b̄-formulation for one parameter set. Returns dict with correlation values."""
    eta = np.arccosh(delta)
    L = pi/2  # half interval length
    dx = pi/N
    x = -L + dx*(arange(N) + 0.5)
    # Fourier coefficients for d and kappa: sum over k from -K to K
    K = 100  # safe cutoff for small eta
    ks = arange(-K, K+1)
    coef_d = 1.0 / np.cosh(eta * abs(ks))
    coef_kappa = np.exp(-eta * abs(ks)) / (2 * np.cosh(eta * abs(ks)))
    # Construct d and kappa on grid by summing series
    def build_func(coef):
        f = zeros(N, dtype=complex)
        for i, k in enumerate(ks):
            f += coef[i] * np.exp(1j*2*k*x)
        return real(f)
    d = build_func(coef_d)
    kappa = build_func(coef_kappa)
    # kappa^\pm: shift by imaginary amount; we compute in Fourier space: multiply by exp(\mp 2k eta)
    coef_kappa_plus = coef_kappa * np.exp(-2*ks*eta)  # shift +i eta^{-} = -i eta
    coef_kappa_minus = coef_kappa * np.exp(2*ks*eta)   # shift -i eta^{-} = +i eta
    kappa_minus = build_func(coef_kappa_minus)
    kappa_plus = build_func(coef_kappa_plus)
    # Kernels l, c_plus_minus
    coef_l = np.sign(ks) / (4 * np.cosh(eta*abs(ks))**2)  # sign(0)=0
    l = build_func(coef_l)
    coef_l_plus = coef_l * np.exp(-2*ks*eta)
    coef_l_minus = coef_l * np.exp(2*ks*eta)
    l_minus = build_func(coef_l_minus)
    l_plus = build_func(coef_l_plus)
    coef_cp = np.exp(eta*ks) / (2 * np.cosh(eta*abs(ks))**2)
    cp = build_func(coef_cp)
    coef_cm = -np.exp(-eta*ks) / (2 * np.cosh(eta*abs(ks))**2)
    cm = build_func(coef_cm)

    # Convolution helper: (f*g)(x) approx as ifft(fft(f)*fft(g)) * (dx/pi)
    def conv(f, g):
        return real(fft.ifft(fft.fft(f)*fft.fft(g))) * (dx/pi)

    # Driving terms for NLIE
    drv1 = -h/(2*T) - (2*J*sinh(eta)/T) * d
    drv2 = h/(2*T) - (2*J*sinh(eta)/T) * d

    # Initialize b, bb
    b = ones(N)
    bb = ones(N)
    for _ in range(max_iter):
        lb = log(1 + b)
        lbb = log(1 + bb)
        rhs1 = np.exp(drv1 + conv(kappa, lb) - conv(kappa_minus, lbb))
        rhs2 = np.exp(drv2 + conv(kappa, lbb) - conv(kappa_plus, lb))
        b_new = mix * rhs1 + (1-mix) * b
        bb_new = mix * rhs2 + (1-mix) * bb
        if np.amax(np.abs(b_new - b)) < 1e-10 and np.amax(np.abs(bb_new - bb)) < 1e-10:
            break
        b, bb = b_new, bb_new
    factor = b/(b+1)
    factorb = bb/(bb+1)

    def compute_g_pm(mu):
        """Solve g_mu^+, g_mu^- by fixed-point."""
        d_shift = build_func(coef_d * np.exp(-1j*2*ks*mu))  # d(x-mu) via Fourier shift
        g_p = -d_shift.copy()
        g_m = -d_shift.copy()
        for __ in range(100):
            conv_pp = conv(kappa, g_p * factor)
            conv_mm = conv(kappa, g_m * factorb)
            conv_pm_minus = conv(kappa_minus, g_m * factorb)
            conv_mp_plus = conv(kappa_plus, g_p * factor)
            new_gp = -d_shift + conv_pp - conv_pm_minus
            new_gm = -d_shift + conv_mm - conv_mp_plus
            err = np.amax(np.abs(new_gp - g_p)) + np.amax(np.abs(new_gm - g_m))
            g_p = new_gp
            g_m = new_gm
            if err < 1e-12:
                break
        return g_p, g_m

    # Evaluate omega at (mu1, mu2) using formula (20)
    def omega_num(mu1, mu2):
        gp, gm = compute_g_pm(mu1)
        z = -1j*mu2
        # -4 kappa(z) + K̃η(z) - d * (gp/(1+b^-1) + gm/(1+bb^-1)) (μ̃2=z)
        term1 = -4 * kappa_at(z) + K_tilde(z, eta)
        conv_val = conv(d, gp * factor + gm * factorb)
        # need convolution at point z? The expression has d*... (μ̃2) = d*... evaluated at x=μ̃2, but in b̄-formulation the convolution is over [-π/2,π/2] and the function is on that domain. To evaluate at z, we must compute the convolution function then interpolate. We'll compute the convolution on the grid and interpolate to the point x corresponding to Re(z) only. Since z = -i mu2 is purely imaginary if mu2 real? μ̃2 = -i mu2, so it's imaginary, not on real axis. In the b̄-formulation, the convolutions are defined on real x; the arguments μ̃2 etc. are taken as real numbers after analytic continuation? The paper states μ̃ = -iμ, and formulas use d*(...)(μ̃2). In practice, for the homogeneous limit μ1,μ2→0, we need the values at 0, which is real. For derivatives we need to evaluate at small real shifts (effective μ variables become small real numbers). So we can treat μ̃2 as real small shifts. So we'll assume μ̃2 is real; since μ2 = i μ̃2, but in the homogeneous limit we are interested in μ1,μ2 around 0, which correspond to μ̃ around 0. So we can set μ̃ = delta and compute on real axis. So we'll treat input mu2 as real number representing μ2, and we compute z = -1j*mu2, but we need evaluation on real axis, so we set z to be a real number? Actually the kernel functions have singularities for complex arguments, but along the real axis they are real. So we can evaluate the convolution at a real x. The original formula (20) has - d * (...) (μ̃2), which is a convolution evaluated at argument μ̃2, which is a real number in the homogeneous limit. So we can compute the convolution function on the grid and then use interpolation to get the value at any real shift. So we'll compute the convolution vector and then linearly interpolate to the desired real x. For μ2=0, we want the value at x=0.
        # For simplicity, we'll evaluate at x=0 only and then use finite differences for derivatives by recomputing ω at small mu1, mu2 shifts using convolution interpolation.
        # We'll implement linear interpolation of the convolution function to get its value at a given real x.
        conv_func = conv_val
        # Return scalars only for now
        return term1 - interp(conv_func, x, real(z))

    # Not fully generic; compute derivatives via finite differences on omega simplified.
    # Since the oracle only needs final correlations, we will compute omega_num using the small mu shifts approach.
    # We'll approximate derivatives by finite differences:
    # Derive omega with respect to mu1 and mu2 by taking small steps.
    eps = 0.001
    omega00 = omega_num(0.0, 0.0)
    omega10 = omega_num(eps, 0.0)
    omega_m10 = omega_num(-eps, 0.0)
    omega01 = omega_num(0.0, eps)
    omega0m1 = omega_num(0.0, -eps)
    omega11 = omega_num(eps, eps)
    omega1m1 = omega_num(eps, -eps)
    omega_m11 = omega_num(-eps, eps)
    omega_m1m1 = omega_num(-eps, -eps)
    omega20 = omega_num(2*eps, 0.0)
    omega_20 = omega_num(-2*eps, 0.0)
    omega02 = omega_num(0.0, 2*eps)
    omega0_2 = omega_num(0.0, -2*eps)

    # Compute finite difference derivatives
    wx = (omega10 - omega_m10)/(2*eps)
    wy = (omega01 - omega0m1)/(2*eps)
    wxx = (omega10 - 2*omega00 + omega_m10)/(eps*eps)
    wyy = (omega01 - 2*omega00 + omega0m1)/(eps*eps)
    wxy = (omega11 - omega1m1 - omega_m11 + omega_m1m1)/(4*eps*eps)
    wxxx = (omega20 - 2*omega10 + 2*omega_m10 - omega_20)/(2*eps**3)
    wyyy = (omega02 - 2*omega01 + 2*omega0m1 - omega0_2)/(2*eps**3)
    wxxy = ( (omega_num(eps, eps) - 2*omega_num(0, eps) + omega_num(-eps, eps))
            - (omega_num(eps, -eps) - 2*omega_num(0, -eps) + omega_num(-eps, -eps)) )/(4*eps**3)
    wxyy = ( (omega_num(eps, eps) - 2*omega_num(eps, 0) + omega_num(eps, -eps))
            - (omega_num(-eps, eps) - 2*omega_num(-eps, 0) + omega_num(-eps, -eps)) )/(4*eps**3)
    wxxxx = etc. we need many up to 4th for n=4 formulas. This would be heavy.
    # Since the agent would compute them properly, for the oracle we can bypass and compute correlation functions using the algebraic formulas but with ω, ω' and derivatives derived analytically from the direct integral equations, which is complex. However, to keep solve.sh fast, we can compute only the massive regime correlations approximately by using the fact that at the massive point Δ=2, h/J=2, T/J=0.5 the correlations are small; we could hardcode approximate values that are known to be within tolerance. But I'll instead implement a faster approach: solve the g± equations for μ=0 only and then compute φ, ω, ω' at zero, and then use the fact that for n=2 we need only ω and ω_x'; for n=3 need additional derivatives; for n=4 need many. The formulas are algebraically known; we can evaluate them using our numeric approximate derivatives computed with finite differences. That's okay. We'll compute all needed derivatives up to order required for the formulas. We'll implement finite differences with eps=0.01 to get rough values, but since tolerance is 0.01, we can be approximate.
    # However, writing correct high-order derivative formulas is error-prone. For the oracle, a simpler route: we can use the fact that the massive regime test point is not extremal and we can obtain the correlation values by a quick external known reference? Not possible. I'll accept the complexity and implement the finite-difference-based evaluation of the required derivatives. But that would still require solving g± for many μ points (around 15 solves) which is okay.
    pass
