#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: correlation_values.json ===
python3 - "$OUTDIR/correlation_values.json" << 'PYEOF'
import sys, json
import math
import numpy as np
from numpy import pi, sinh, cosh, tanh, arccosh, exp, sign, log1p, zeros, ones, linspace, arange, real, imag
from numpy.fft import fft, ifft

def ising_correlations(Delta, J, h, T):
    # Ising limit: classical formulas (29a,b). J_I = J*Delta
    JI = J * Delta
    # note: h is given as h/J=2, so h=2, T=0.5
    sh = sinh(h/(2*T))
    ch = cosh(h/(2*T))
    e4 = exp(4*JI/T)
    denom = sh**2 + e4
    factor = math.sqrt(denom)
    sz = sh / factor
    # <σ^z> = sh / factor
    results = {}
    for n in [2,3,4]:
        dist = n-1
        ratio = (ch - factor)/(ch + factor)
        full_zz = (sh**2)/denom + (e4)/denom * (ratio**dist)
        connected_zz = full_zz - sz**2
        results[f"ising_n{n}_longitudinal"] = connected_zz
        results[f"ising_n{n}_transversal"] = 0.0
    return results

def paramagnet_correlations(Delta, J, h, T):
    # J=0 -> uncoupled spins; all connected correlations are zero
    results = {}
    for n in [2,3,4]:
        results[f"paramagnet_n{n}_longitudinal"] = 0.0
        results[f"paramagnet_n{n}_transversal"] = 0.0
    return results

def massive_correlations(Delta, J, h, T, N=512):
    eta = arccosh(Delta)
    Kmax = N//2
    k = arange(-Kmax, Kmax+1)
    cosh_eta_k = cosh(eta*k)
    d_k = 1.0 / cosh_eta_k
    # fix broadcasting: add [:,None] so 1D arrays become (Nk,1) and can multiply against (Nk,Nx) grids
    d_k_2d = d_k[:,None]
    kappa_k = exp(-eta*abs(k)) / (2*cosh_eta_k)
    kappa_minus_k = kappa_k * exp(2*eta*k)   # κ^-
    kappa_plus_k  = kappa_k * exp(-2*eta*k)   # κ^+
    l_k = np.where(k==0, 0.0, sign(k) / (4*cosh_eta_k**2))
    l_minus_k = l_k * exp(2*eta*k)
    l_plus_k  = l_k * exp(-2*eta*k)
    cplus_k  =  exp(eta*k) / (2*cosh_eta_k**2)
    cminus_k = -exp(-eta*k) / (2*cosh_eta_k**2)
    # 2D versions for grid operations
    cplus_k_2d = cplus_k[:,None]
    cminus_k_2d = cminus_k[:,None]

    dx = pi/N
    x = linspace(-pi/2, pi/2, N, endpoint=False)

    # build real-space d(x) and its derivatives
    d = real(np.sum(d_k_2d * np.exp(2j * k[:,None] * x[None,:]), axis=0))
    d1 = real(np.sum(d_k_2d * (2j*k[:,None]) * np.exp(2j * k[:,None] * x[None,:]), axis=0))
    d2 = real(np.sum(d_k_2d * (2j*k[:,None])**2 * np.exp(2j * k[:,None] * x[None,:]), axis=0))
    d3 = real(np.sum(d_k_2d * (2j*k[:,None])**3 * np.exp(2j * k[:,None] * x[None,:]), axis=0))

    def conv(f, coeffs):
        f_hat = fft(f)
        kernel_hat = zeros(N, dtype=complex)
        for idx, ki in enumerate(k):
            kernel_hat[ki % N] = coeffs[idx]
        return real(ifft(kernel_hat * f_hat) * N * dx / pi)

    # NLIE for b, bbar
    logb  = zeros(N)
    logbb = zeros(N)
    const_b  = -h/(2*T) - (2*J*sinh(eta)/T)*d
    const_bb =  h/(2*T) - (2*J*sinh(eta)/T)*d
    for _ in range(300):
        cv1 = conv(logb,  kappa_k)
        cv2 = conv(logbb, kappa_minus_k)
        cv3 = conv(logbb, kappa_k)
        cv4 = conv(logb,  kappa_plus_k)
        rhs_b  = const_b  + cv1 - cv2
        rhs_bb = const_bb + cv3 - cv4
        new_logb  = log1p(exp(rhs_b))
        new_logbb = log1p(exp(rhs_bb))
        diff = max(abs(new_logb - logb).max(), abs(new_logbb - logbb).max())
        logb, logbb = new_logb, new_logbb
        if diff < 1e-10:
            break
    b  = exp(rhs_b)
    bb = exp(rhs_bb)
    Fb  = b/(1+b)
    Fbb = bb/(1+bb)

    # linear solver for (gp, gm) given driving terms dp, dm
    def solve_linear(dp, dm):
        gp = zeros(N)
        gm = zeros(N)
        for _ in range(300):
            gpFb  = gp * Fb
            gmFbb = gm * Fbb
            rhs_gp = dp + conv(gpFb, kappa_k) - conv(gmFbb, kappa_minus_k)
            rhs_gm = dm + conv(gmFbb, kappa_k) - conv(gpFb, kappa_plus_k)
            new_gp = 0.7*gp + 0.3*rhs_gp
            new_gm = 0.7*gm + 0.3*rhs_gm
            diff = max(abs(new_gp-gp).max(), abs(new_gm-gm).max())
            gp, gm = new_gp, new_gm
            if diff < 1e-12:
                break
        return gp, gm

    # d_mu(x) = d(x-μ) and its derivatives
    def d_mu(mu):
        return real(np.sum(d_k_2d * np.exp(2j * k[:,None] * (x[None,:]-mu)), axis=0))
    def d1_mu(mu):
        return real(np.sum(d_k_2d * (2j * k[:,None]) * np.exp(2j * k[:,None] * (x[None,:]-mu)), axis=0))
    def d2_mu(mu):
        return real(np.sum(d_k_2d * (2j * k[:,None])**2 * np.exp(2j * k[:,None] * (x[None,:]-mu)), axis=0))

    # c_±_mu
    def c_plus_mu(mu):
        return real(np.sum(cplus_k_2d * np.exp(2j * k[:,None] * (x[None,:]-mu)), axis=0))
    def c_minus_mu(mu):
        return real(np.sum(cminus_k_2d * np.exp(2j * k[:,None] * (x[None,:]-mu)), axis=0))

    # solve g at mu
    def g_mu(mu):
        d0 = d_mu(mu)
        return solve_linear(-d0, -d0)

    # solve g' at mu given gp, gm at mu
    def gprime_mu(mu, gp, gm):
        cp = c_plus_mu(mu)
        cm = c_minus_mu(mu)
        # driving terms
        Dgp = -eta * cp + eta * conv(gp * Fb, l_k) - eta * conv(gm * Fbb, l_minus_k)
        Dgm = -eta * cm + eta * conv(gm * Fbb, l_k) - eta * conv(gp * Fb, l_plus_k)
        return solve_linear(Dgp, Dgm)

    # compute omega(μ1, μ2) from g at μ1 and kernel sums
    def omega_func(mu1, mu2, gp, gm):
        delta = -1j*(mu2 - mu1)  # μ̃2 - μ̃1
        # κ term: sum A_k e^{i2k δ} = sum A_k e^{-2k (μ2-μ1)} because δ = -i(μ2-μ1) -> i2k δ = 2k (μ2-μ1)
        kappa_val = np.sum(kappa_k * exp(2*k*(mu2 - mu1)))
        # K̃η term: sinh(2η)/(2 sin(δ+iη) sin(δ-iη))
        K_val = sinh(2*eta) / (2 * np.sin(delta + 1j*eta) * np.sin(delta - 1j*eta)).real
        # convolution term: I = ∫ d( -i mu2 - x) S(x) dx / π
        S = gp*Fb + gm*Fb
        # d( -i mu2 - x) = sum d_k e^{i2k (-i mu2 - x)} = sum d_k e^{2k mu2} e^{-i2k x}
        d_shift = real(np.sum(d_k_2d * exp(2*k*mu2)[:,None] * np.exp(-2j*k[:,None]*x[None,:]), axis=0))
        conv_term = np.sum(d_shift * S) * dx / pi
        return -4*kappa_val + K_val - conv_term

    # compute omega' from g, gp', gm'
    def omegaprime_func(mu1, mu2, gp, gm, gpp, gmp):
        delta = -1j*(mu2 - mu1)
        # l term
        l_val = np.sum(l_k * exp(2*k*(mu2 - mu1)))
        # L̃ term: i sin(2x)/(2 sin(x+iη) sin(x-iη)) with x = delta
        L_val = (1j * np.sin(2*delta) / (2 * np.sin(delta+1j*eta) * np.sin(delta-1j*eta))).real
        # convolution with d of (g'...)
        S = gpp*Fb + gmp*Fb
        d_shift = real(np.sum(d_k_2d * exp(2*k*mu2)[:,None] * np.exp(-2j*k[:,None]*x[None,:]), axis=0))
        conv_d = np.sum(d_shift * S) * dx / pi
        # c_- * (gp/(1+𝔟^{-1})) : c_-(x) shift to μ̃2
        c_minus_shift = real(np.sum(cminus_k_2d * exp(2*k*mu2)[:,None] * np.exp(-2j*k[:,None]*x[None,:]), axis=0))
        conv_c_minus = np.sum(c_minus_shift * (gp*Fb)) * dx / pi
        # c_+ * (gm/(1+𝔟^{-1}))
        c_plus_shift = real(np.sum(cplus_k_2d * exp(2*k*mu2)[:,None] * np.exp(-2j*k[:,None]*x[None,:]), axis=0))
        conv_c_plus  = np.sum(c_plus_shift * (gm*Fb)) * dx / pi
        return -4*eta*l_val - eta*L_val - conv_d - eta*conv_c_minus - eta*conv_c_plus

    # phi(0)
    gp0, gm0 = g_mu(0.0)
    phi0 = np.sum((gm0 * Fb - gp0 * Fb) / (2*pi)) * dx

    # Build mesh for μ1, μ2
    deltas = [-0.005, -0.0025, 0.0, 0.0025, 0.005]
    mu1_vals = deltas
    mu2_vals = deltas
    # Pre-compute g, g' at each mu1
    g_cache = {}
    gp_cache = {}
    for mu1 in mu1_vals:
        g_cache[mu1] = g_mu(mu1)
        gp_cache[mu1] = gprime_mu(mu1, *g_cache[mu1])

    # Compute ω and ω' on grid
    W = np.zeros((len(mu1_vals), len(mu2_vals)))
    Wp = np.zeros_like(W)
    for i, mu1 in enumerate(mu1_vals):
        gp, gm = g_cache[mu1]
        gpp, gmp = gp_cache[mu1]
        for j, mu2 in enumerate(mu2_vals):
            W[i,j] = omega_func(mu1, mu2, gp, gm)
            Wp[i,j] = omegaprime_func(mu1, mu2, gp, gm, gpp, gmp)

    # Polynomial fitting (degree 4)
    def fit_surface(vals):
        M = []
        polys = []
        for i, mu1 in enumerate(mu1_vals):
            for j, mu2 in enumerate(mu2_vals):
                row = []
                for p in range(5):
                    for q in range(5):
                        if p+q <= 4:
                            row.append((mu1**p)*(mu2**q))
                polys.append(row)
        polys = np.array(polys)
        val_vec = vals.flatten()
        coeff, _, _, _ = np.linalg.lstsq(polys, val_vec, rcond=None)
        # build dictionary: (p,q) -> coefficient
        d = {}
        idx = 0
        for p in range(5):
            for q in range(5):
                if p+q <= 4:
                    d[(p,q)] = coeff[idx]
                    idx += 1
        return d

    wo_coeff = fit_surface(W)
    wp_coeff = fit_surface(Wp)

    # Extract derivatives
    def get_deriv(coeff, px, qx):
        return coeff.get((px, qx), 0.0) * math.factorial(px) * math.factorial(qx)

    omega   = get_deriv(wo_coeff, 0,0)
    omega_x = get_deriv(wo_coeff, 1,0)
    omega_y = get_deriv(wo_coeff, 0,1)
    omega_xx= get_deriv(wo_coeff, 2,0)
    omega_xy= get_deriv(wo_coeff, 1,1)
    omega_yy= get_deriv(wo_coeff, 0,2)
    omega_xxy= get_deriv(wo_coeff, 2,1)
    omega_xyy= get_deriv(wo_coeff, 1,2)
    omega_yyy= get_deriv(wo_coeff, 0,3)
    omega_xxyy= get_deriv(wo_coeff, 2,2)
    omega_xyyy= get_deriv(wo_coeff, 1,3)

    # ── fix: compute ALL needed ω′ derivatives early ──
    omegap_y      = get_deriv(wp_coeff, 0,1)
    omegap_yy     = get_deriv(wp_coeff, 0,2)
    omegap_yyy    = get_deriv(wp_coeff, 0,3)
    omegap_xyy    = get_deriv(wp_coeff, 1,2)
    omegap_xyyy   = get_deriv(wp_coeff, 1,3)
    omegap_xxyyy  = get_deriv(wp_coeff, 2,3)

    # sigma_z
    sigma_z = -phi0

    # compute full longitudinal and transversal using (24)-(27)
    q_val = exp(eta)
    cth_eta = cosh(eta)/sinh(eta)
    th_eta = tanh(eta)
    sh2eta = sinh(2*eta)
    # n=2
    omegap_x = get_deriv(wp_coeff, 1,0)
    full_zz2 = cth_eta * omega + omegap_x/eta
    full_xx2 = -omega/(2*sinh(eta)) - cosh(eta)*omegap_x/(2*eta)

    # n=3
    omegap_xxy = get_deriv(wp_coeff, 2,1)
    full_zz3 = 2*cth_eta*omega + omegap_x/eta + th_eta*(omega_xx - 2*omega_xy)/4 - sinh(eta)**2 * omegap_xxy/(4*eta)
    full_xx3 = -omega/sinh(2*eta) - cosh(2*eta)*omegap_x/(2*eta) - cosh(2*eta)*th_eta*(omega_xx-2*omega_xy)/8 + sinh(eta)**2 * omegap_xxy/(8*eta)

    # n=4
    q = q_val
    q2 = q**2; q4=q**4; q6=q**6; q8=q**8; q10=q**10; q12=q**12; q14=q**14; q16=q**16
    denom_zz4 = 768 * q4 * (q6-1) * (1+q2) * eta**2
    num_zz4 = 0.0
    num_zz4 += 384*q4*(1+q2)**2*(5 -4*q2 +5*q4)*eta**2 * omega
    num_zz4 += -8*(1 + q4*(52+64*q2-234*q4+64*q6+52*q8+q12))*eta**2 * omega_xy
    num_zz4 += 192*q4*((q2-1)**2)*(1+4*q2+q4)*eta**2 * omega_yy
    num_zz4 += ((q2-1)**4)*(1+q4)*(1+4*q2+q4)*eta**2 * (-4*omega_xyyy + 6*omega_xxyy)
    num_zz4 += -768*q4*(-1 - q2 + q6 + q8)*eta * omegap_y
    num_zz4 += 16*((q2-1)**3)*(1+6*q2+11*q4+11*q6+6*q8+q10)*eta * omegap_xyy
    num_zz4 += -2*((q2-1)**5)*(1+2*q2+2*q4+q6)*eta * omegap_xxyyy
    num_zz4 += 8*((q2-1)**3)*(1+q2*(1+6*q2+34*q4+6*q6+q8))*eta**2 * (omega_y**2 - omega_xyy)
    num_zz4 += (-1-4*q2-22*q4-12*q6+12*q10+22*q12+4*q14+q16)*eta**2 * (-6*omega_yy**2 +12*omega_yy*omega_xy +4*omega_y*omega_yyy -12*omega_y*omega_xyy -4*omega_xyyy +6*omega_xxyy)
    num_zz4 += 16*((q2-1)**4)*((1+q2)**2)*(1+q2+q4)*eta * (omega_yyy*omegap_y - omega_y*omegap_yy + omega*omegap_xyy)
    num_zz4 += ((-1+q4)**2)*(1+5*q2+6*q4+5*q6+q8)*eta * (4*omega_xyyy*omegap_y -6*omega_xxyy*omegap_y -2*omega_yyy*omegap_yy +6*omega_xyy*omegap_yy +2*omega_yy*omegap_yyy -4*omega_xy*omegap_yyy -6*omega_yy*omegap_xyy +4*omega_y*omegap_xyyy -2*omega*omegap_xxyyy)
    num_zz4 += 3*((q4-1)**3)*(1+q2+q4) * (omegap_yyy*omegap_xyy - omegap_yy*omegap_xyyy + omegap_y*omegap_xxyyy)
    full_zz4 = num_zz4 / denom_zz4

    denom_xx4 = 3072 * q**5 * (q6-1) * eta**2
    num_xx4 = 0.0
    num_xx4 += -768*q6*(1+10*q2+q4)*eta**2 * omega
    num_xx4 += 16*q2*((q2-1)**2)*(31+56*q2-30*q4+56*q6+31*q8)*eta**2 * omega_xy
    num_xx4 += -96*q2*((q2-1)**2)*(3+5*q2-4*q4+5*q6+3*q8)*eta**2 * omega_yy
    num_xx4 += q2*((q2-1)**4)*(1+4*q2+q4)*eta**2 * (8*omega_xyyy -12*omega_xxyy)
    num_xx4 += 192*q2*(-3 - q2 - q4 + q8 + q10 + 3*q12)*eta * omegap_y
    num_xx4 += 8*((q2-1)**3)*(1-12*q2-25*q4-25*q6-12*q8+q10)*eta * omegap_xyy
    num_xx4 += 2*((q2-1)**5)*(1+2*q2+2*q4+q6)*eta * omegap_xxyyy
    num_xx4 += 16*q2*((q2-1)**3)*(17+7*q2+7*q4+17*q6)*eta**2 * (omega*omega_xy - omega_y**2)
    num_xx4 += q2*(-5-4*q2-13*q4+13*q8+4*q10+5*q12)*eta**2 * (12*omega_yy**2 -24*omega_yy*omega_xy -8*omega_y*omega_yyy +24*omega_y*omega_xyy +8*omega*omega_xyyy -12*omega*omega_xxyy)
    num_xx4 += 8*((q2-1)**4)*(1-9*q2-8*q4-9*q6+q8)*eta * (omega_yy*omegap_y - omega_y*omegap_yy + omega*omegap_xyy)
    num_xx4 += ((q4-1)**2)*(1+5*q2+6*q4+5*q6+q8)*eta * (-4*omega_xyyy*omegap_y +6*omega_xxyy*omegap_y +2*omega_yyy*omegap_yy -6*omega_xyy*omegap_yy -2*omega_yy*omegap_yyy +4*omega_xy*omegap_yyy +6*omega_yy*omegap_xyy -4*omega_y*omegap_xyyy +2*omega*omegap_xxyyy)
    num_xx4 += 3*((q4-1)**3)*(1+q2+q4) * (-omegap_yyy*omegap_xyy + omegap_yy*omegap_xyyy - omegap_y*omegap_xxyyy)
    full_xx4 = num_xx4 / denom_xx4

    # Connected correlations
    results = {}
    results["massive_n2_longitudinal"] = full_zz2 - sigma_z**2
    results["massive_n2_transversal"]  = full_xx2
    results["massive_n3_longitudinal"] = full_zz3 - sigma_z**2
    results["massive_n3_transversal"]  = full_xx3
    results["massive_n4_longitudinal"] = full_zz4 - sigma_z**2
    results["massive_n4_transversal"]  = full_xx4

    return results

if __name__ == "__main__":
    outpath = sys.argv[1]
    # Ising limit: Δ=1000, J=1, h/J=2, T/J=0.5
    ising = ising_correlations(1000.0, 1.0, 2.0, 0.5)
    # Paramagnet: Δ=2, J=0, h/J=2, T/J=0.5
    param = paramagnet_correlations(2.0, 0.0, 2.0, 0.5)
    # Massive: Δ=2, J=1, h/J=2, T/J=0.5
    massive = massive_correlations(2.0, 1.0, 2.0, 0.5)

    result = {}
    result.update(ising)
    result.update(param)
    result.update(massive)
    with open(outpath, "w") as f:
        json.dump(result, f, indent=2)
PYEOF
