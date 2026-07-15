import numpy as np
from scipy.special import digamma, polygamma
from scipy.optimize import root_scalar, minimize

# Physical constants (all energies in eV, consistent with paper's unit system where hbar = kB = m = 1)
LAMBDA_EPH = 1.0
MU_STAR = 0.13
MU = 0.5
THETA_D = 0.017
EPSILON_F = 5.0

# Derived
g = LAMBDA_EPH - MU_STAR  # 0.87

# psi(1/2) = -1.963510...
PSI_HALF = digamma(0.5)

def trigamma(z):
    return polygamma(1, z)

def compute_params(epsilonFtau):
    """Return D_ratio, Tc_over_Tc0 for a given disorder parameter."""
    alpha = epsilonFtau**2
    # D/D0 ratio: Eq. (1a) paper description
    if alpha > 1e10:  # treat as infinity
        D_ratio = 1.0
    else:
        D_ratio = 1.0 - (3.0 * np.sqrt(3.0) / (4.0 * np.pi)) / alpha
    
    # Tc suppression from Eq. (1b)
    ln_epsF_tau = np.log(epsilonFtau) if epsilonFtau < 1e10 else 20.0  # large but finite
    # g*/g ratio
    num_g_star = 1.0 + MU * np.log(EPSILON_F / THETA_D)
    denom_g_star = 1.0 + MU * ln_epsF_tau
    g_star_ratio = num_g_star / denom_g_star
    
    ln_thetaD_tau = np.log(THETA_D * epsilonFtau / EPSILON_F)
    
    term1 = (1.0 / (g * g_star_ratio))**2
    term2 = 2.0 * np.pi * (1.0/g - (MU_STAR/g)**2 * ln_thetaD_tau)
    rhs = -(3.0 * np.sqrt(3.0) / (8.0 * np.pi * alpha)) * (term1 + term2)
    
    Tc_over_Tc0 = np.exp(rhs) if rhs > -30 else 0.0  # avoid underflow
    return D_ratio, Tc_over_Tc0


def fem_Hc2(t, epsilonFtau, D_ratio, Tc_over_Tc0):
    """Solve FEM Eq. (1a) for x = a0/(8 π T) and return h = π e D0 H/(4 c Tc0).
    t = T/Tc0."""
    if t <= 0 or t > Tc_over_Tc0:
        return 0.0
    alpha = epsilonFtau**2
    # Equation: ln(t / Tc_over_Tc0) = psi(1/2) - psi(1/2 + D_ratio*x) + (sqrt(3)*x)/(2*alpha)*trigamma(1/2 + x)
    # We solve for x > 0.
    ln_ratio = np.log(t / Tc_over_Tc0)
    if ln_ratio >= 0:
        return 0.0

    def f(x):
        if x <= 0:
            return -1.0
        psi_term = digamma(0.5 + D_ratio * x)
        trigamma_term = trigamma(0.5 + x)
        residual = PSI_HALF - psi_term + (np.sqrt(3.0) * x / (2.0 * alpha)) * trigamma_term - ln_ratio
        return residual

    # bracket: x in (0, some large value). At x=0, f(0) = -ln_ratio > 0 (since ln_ratio negative).
    # As x -> large, digamma(0.5 + D_ratio x) ~ ln(D_ratio x), trigamma ~ 1/x, so term ~ constant, residual -> -large?
    # We'll find a bound by increasing until f negative.
    x_lo = 1e-6
    x_hi = 1.0
    # ensure f(x_hi) < 0
    for _ in range(20):
        if f(x_hi) < 0:
            break
        x_hi *= 2.0
    else:
        return 0.0
    
    try:
        sol = root_scalar(f, bracket=[x_lo, x_hi], method='brentq')
        x = sol.root
    except Exception:
        return 0.0
    # convert to h
    h = (np.pi**2 * t * x) / 2.0
    return h


def whhm_model(t, A, B):
    """WHHM Maki reduced field h(t) for fitting parameters A=D_fit/D0, B=Tc_fit/Tc0.
    Returns h for each t; returns 0 if t > B."""
    if t <= 0 or t > B:
        return 0.0
    ln_ratio = np.log(t / B)
    if ln_ratio >= 0:
        return 0.0
    # Equation: ln(t/B) = psi(1/2) - psi(1/2 + y) where y = A * (2/(π t)) * h
    # So we solve for y first, then h = (π t)/(2 A) * y.
    def g(y):
        if y <= 0:
            return -1.0
        return PSI_HALF - digamma(0.5 + y) - ln_ratio
    # bracket y
    y_lo = 1e-6
    y_hi = 1.0
    for _ in range(20):
        if g(y_hi) < 0:
            break
        y_hi *= 2.0
    else:
        return 0.0
    try:
        sol = root_scalar(g, bracket=[y_lo, y_hi], method='brentq')
        y = sol.root
    except Exception:
        return 0.0
    h = (np.pi * t) / (2.0 * A) * y
    return h

def fit_whhm(t_array, h_fem):
    """Fit WHHM parameters A,B to the FEM h(t) data."""
    # Only fit points where h_fem > 0 (i.e., t <= Tc_over_Tc0)
    mask = h_fem > 0
    t_fit = t_array[mask]
    h_fit = h_fem[mask]
    if len(t_fit) < 2:
        return 1.0, 1.0
    
    def loss(params):
        A, B = params
        if A <= 0 or B <= 0 or B > 1.1:
            return 1e9
        h_pred = np.array([whhm_model(t, A, B) for t in t_fit])
        return np.sum((h_pred - h_fit)**2)
    
    # initial guess: A = D_ratio? but we don't have it here; use 1.0
    res = minimize(loss, [1.0, np.max(t_fit)], method='Nelder-Mead', options={'maxiter':2000, 'xatol':1e-8})
    A_opt, B_opt = res.x
    return A_opt, B_opt
