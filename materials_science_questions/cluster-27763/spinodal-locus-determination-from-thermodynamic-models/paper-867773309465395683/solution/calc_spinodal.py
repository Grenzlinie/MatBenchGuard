import sys
import numpy as np
from scipy.optimize import fsolve, root, brentq
from math import exp, sqrt, sin, cos

# ------------------------------------------------------------
# Physical constants and helpers
# ------------------------------------------------------------

THETA_STEP = 0.2
K1_LIST = [5, 10, 20, 55, 70]

# Ordered list of species: (mu, nu) pairs
SPECIES = [('z','x'), ('z','y'), ('x','z'), ('y','z'), ('x','y'), ('y','x')]
NSPEC = len(SPECIES)

def kappa2_from_theta(k1, theta):
    if abs(theta - 1) < 1e-12:
        return 1.0
    if abs(theta + 1) < 1e-12:
        return k1
    # solve k2^2 + theta*(k1-1)*k2 - k1 = 0
    b = theta * (k1 - 1.0)
    disc = b*b + 4.0*k1
    k2 = (-b + np.sqrt(disc)) / 2.0
    return k2

def compute_s_plus(u, v, k1, k2):
    return 0.5*(k1 + k2) - (k1 - 1.0)*u - (k2 - 1.0)*v

def equilibrium_residuals(vars, y, k1, k2):
    u, v = vars
    s = compute_s_plus(u, v, k1, k2)
    # xi1, xi2, xi3 (B13-B15)
    xi1 = y * (k2 * (1.0 + y*s*s) + (k2 + 1.0)*s)
    xi2 = y * (k1 * (1.0 + y*s*s) + (k1 + 1.0)*s)
    xi3 = y * (k1*k2 * (1.0 + y*s*s) + (k1 + k2)*s)
    C = 2.0 * (np.exp(-xi1) + np.exp(-xi2) + np.exp(-xi3))
    f1 = u - np.exp(-xi1) / C
    f2 = v - np.exp(-xi2) / C
    return [f1, f2]

def uniform_state_for_density(rho_star, k1, k2):
    """Solve equilibrium u+, v+ for given reduced density."""
    def func(vars):
        u, v = vars
        s = compute_s_plus(u, v, k1, k2)
        r = 0.5 - u - v
        # Psi2 from (A7) for Nu phase
        Psi2 = 2.0 * (r * k1*k2 + v * k1 + u * k2)
        if Psi2 < 0:
            return [1e10, 1e10]
        eta = rho_star * Psi2
        if eta >= 1.0:
            return [1e10, 1e10]
        y = rho_star / (1.0 - eta)
        xi1 = y * (k2 * (1.0 + y*s*s) + (k2 + 1.0)*s)
        xi2 = y * (k1 * (1.0 + y*s*s) + (k1 + 1.0)*s)
        xi3 = y * (k1*k2 * (1.0 + y*s*s) + (k1 + k2)*s)
        C = 2.0 * (np.exp(-xi1) + np.exp(-xi2) + np.exp(-xi3))
        f1 = u - np.exp(-xi1) / C
        f2 = v - np.exp(-xi2) / C
        return [f1, f2]
    # initial guess
    x0 = [0.15, 0.15]
    sol = fsolve(func, x0, maxfev=2000, xtol=1e-12)
    u, v = sol
    r = 0.5 - u - v
    s = compute_s_plus(u, v, k1, k2)
    Psi2 = 2.0 * (r * k1*k2 + v * k1 + u * k2)
    eta = rho_star * Psi2
    y = rho_star / (1.0 - eta) if eta < 1.0 else np.inf
    Psi1x = ( (u+u)*k1 + (v+v)*k2 + r+r )  # careful: gamma_zx=u, gamma_zy=u, etc.
    # Actually from (A5): Psi1x = (gamma_xy+gamma_xz)*k1 + (gamma_yx+gamma_zx)*k2 + gamma_zy+gamma_yz
    # For Nu: gamma_zx = gamma_zy = u, gamma_xz = gamma_yz = v, gamma_xy = gamma_yx = r.
    # So Psi1x = (r + v)*k1 + (r + u)*k2 + u + v
    # Let's compute explicitly:
    gamma_zx = u
    gamma_zy = u
    gamma_xz = v
    gamma_yz = v
    gamma_xy = r
    gamma_yx = r
    Psi1x = (gamma_xy + gamma_xz)*k1 + (gamma_yx + gamma_zx)*k2 + gamma_zy + gamma_yz
    Psi1y = (gamma_yx + gamma_yz)*k1 + (gamma_xy + gamma_zy)*k2 + gamma_zx + gamma_xz
    return u, v, r, y, Psi1x, Psi1y, Psi2

def run_uniform_solve_for_y(y, k1, k2):
    """Solve u,v given y using equilibrium equations (B12)."""
    func = lambda vars: equilibrium_residuals(vars, y, k1, k2)
    x0 = [0.15, 0.15]
    sol = fsolve(func, x0, maxfev=2000)
    return sol[0], sol[1]

# ------------------------------------------------------------
# Nu->Nb spinodal
# ------------------------------------------------------------

def compute_nunb_spinodal(k1, k2):
    """Solve for u+, v+, y that satisfy equilibrium and bifurcation condition (B11)."""
    def full_system(vars):
        u, v, y = vars
        # equilibrium
        f1, f2 = equilibrium_residuals([u, v], y, k1, k2)
        # spinodal condition: y^(-1) = u*(k2-1)^2 + v*(k1-1)^2 + r*(k1-k2)^2
        r = 0.5 - u - v
        cond = y**(-1) - ( u*(k2-1)**2 + v*(k1-1)**2 + r*(k1-k2)**2 )
        return [f1, f2, cond]
    # try multiple initial guesses
    guesses = [
        [0.1, 0.1, 1.0],
        [0.2, 0.1, 5.0],
        [0.15, 0.15, 10.0],
        [0.05, 0.05, 0.5],
        [0.3, 0.1, 20.0]
    ]
    for x0 in guesses:
        try:
            sol = root(full_system, x0, method='hybr', tol=1e-10)
            if sol.success:
                u, v, y = sol.x
                r = 0.5 - u - v
                # compute rho* from y and Psi2
                # Psi2 for Nu
                Psi2 = 2.0 * (r * k1*k2 + v * k1 + u * k2)
                rho_star = y / (1.0 + y * Psi2)
                if rho_star > 0:
                    return rho_star, (u, v, r)
        except Exception:
            continue
    return None

# ------------------------------------------------------------
# Non-uniform spinodal (det T = 0)
# ------------------------------------------------------------

def kappa_munu_tau(mu, nu, tau, k1, k2):
    """Compute kappa^tau_{mu nu} = 1 + (k1-1)*delta_{tau,mu} + (k2-1)*delta_{tau,nu}"""
    delta_tau_mu = 1.0 if tau == mu else 0.0
    delta_tau_nu = 1.0 if tau == nu else 0.0
    return 1.0 + (k1 - 1.0)*delta_tau_mu + (k2 - 1.0)*delta_tau_nu

def weight_functions(qx, qy, kx, ky):
    """Return w0, w1x, w1y, w2 from (C3)-(C6). kx, ky are kappa^tau."""
    # qx, qy are reduced q* = q*sigma3
    ax = qx * kx / 2.0
    ay = qy * ky / 2.0
    w0 = cos(ax) * cos(ay)
    if abs(ax) < 1e-12:
        chi1x = 1.0
    else:
        chi1x = sin(ax) / ax
    if abs(ay) < 1e-12:
        chi1y = 1.0
    else:
        chi1y = sin(ay) / ay
    w1x = kx * chi1x * cos(ay)   # (C5) includes kx factor
    w1y = ky * cos(ax) * chi1y   # (C6) includes ky factor
    w2 = kx * ky * chi1x * chi1y  # (C4)
    return w0, w1x, w1y, w2

def compute_T_determinant(gamma, k1, k2, qx, qy, y, Psi1x, Psi1y):
    """Build the 6x6 T matrix and return its determinant."""
    # Precompute weighting functions for each species
    w0 = np.zeros(NSPEC)
    w1x = np.zeros(NSPEC)
    w1y = np.zeros(NSPEC)
    w2 = np.zeros(NSPEC)
    for i, (mu, nu) in enumerate(SPECIES):
        kx = kappa_munu_tau(mu, nu, 'x', k1, k2)
        ky = kappa_munu_tau(mu, nu, 'y', k1, k2)
        w0[i], w1x[i], w1y[i], w2[i] = weight_functions(qx, qy, kx, ky)

    T = np.zeros((NSPEC, NSPEC))
    for i in range(NSPEC):
        for j in range(NSPEC):
            gi = gamma[i]
            gj = gamma[j]
            sqrt_g = np.sqrt(gi * gj) if gi>0 and gj>0 else 0.0
            # term from C8
            term = ( (w0[i]*w2[j] + w2[i]*w0[j])              # <w^(0) w^(2)>
                   + (w1x[i]*w1y[j] + w1y[i]*w1x[j]) )        # <w^(1x) w^(1y)>
            term += y * ( Psi1y * (w1x[i]*w2[j] + w2[i]*w1x[j])
                        + Psi1x * (w1y[i]*w2[j] + w2[i]*w1y[j]) )
            term += (1.0 + 2.0*y*Psi1x*Psi1y) * w2[i]*w2[j]
            T[i,j] = (1.0 if i==j else 0.0) + y * sqrt_g * term
    det = np.linalg.det(T)
    return det

def minimax_det_for_density(rho_star, k1, k2):
    """For given rho*, find min |det(T)| over q grid."""
    try:
        u, v, _, y, Psi1x, Psi1y, _ = uniform_state_for_density(rho_star, k1, k2)
    except Exception:
        return 1e20  # large
    r = 0.5 - u - v
    # build gamma array
    gamma = np.array([u, u, v, v, r, r])
    # coarse q grid
    q_vals = np.arange(0.1, 10.1, 0.3)
    min_det = 1e20
    for qx in q_vals:
        for qy in q_vals:
            det = compute_T_determinant(gamma, k1, k2, qx, qy, y, Psi1x, Psi1y)
            abs_det = abs(det)
            if abs_det < min_det:
                min_det = abs_det
                if min_det < 1e-12:
                    return 0.0  # already zero
    return min_det

def compute_nonuniform_spinodal(k1, k2):
    """Find lowest rho* where min|det|=0, using scanning + root-finding."""
    # scan for sign cross of log(det) or detect where det becomes small
    # use scanning to bracket where min_det crosses zero
    rho_start = 0.005
    rho_end = 100.0
    nstep = 200
    rho_vals = np.logspace(np.log10(rho_start), np.log10(rho_end), nstep)
    min_dets = np.array([minimax_det_for_density(rho, k1, k2) for rho in rho_vals])
    # find first index where min_det < 1e-8 (approximately zero)
    idx = np.where(min_dets < 1e-8)[0]
    if len(idx) == 0:
        # no crossing found
        return None
    first_idx = idx[0]
    if first_idx == 0:
        rho_low = rho_vals[0]
    else:
        rho_low = rho_vals[first_idx-1]
    rho_high = rho_vals[first_idx]
    # refine with root-finding
    try:
        sol = brentq(lambda r: minimax_det_for_density(r, k1, k2), rho_low, rho_high, xtol=1e-10)
        return sol
    except Exception:
        return rho_vals[first_idx]

# ------------------------------------------------------------
# Main output generation
# ------------------------------------------------------------

def main():
    header = "kappa1,theta,rho_star,transition_type"
    rows = [header]
    for k1 in K1_LIST:
        for theta in np.arange(-1.0, 1.01, THETA_STEP):
            theta = round(theta, 10)  # avoid floating errors
            k2 = kappa2_from_theta(k1, theta)
            # Nu->Nb spinodal
            nb_result = compute_nunb_spinodal(k1, k2)
            if nb_result is not None:
                rho_star, (u,v,r) = nb_result
                rows.append(f"{k1},{theta},{rho_star:.10f},NuNb")
            # Non-uniform spinodal
            nu_result = compute_nonuniform_spinodal(k1, k2)
            if nu_result is not None:
                rows.append(f"{k1},{theta},{nu_result:.10f},nonuniform")
    sys.stdout.write("\n".join(rows) + "\n")

if __name__ == "__main__":
    main()
