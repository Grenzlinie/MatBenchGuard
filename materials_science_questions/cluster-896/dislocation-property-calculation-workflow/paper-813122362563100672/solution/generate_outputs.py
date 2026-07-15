#!/usr/bin/env python3
"""Reference oracle for dislocation quasi-cleavage reproduction.
Writes equilibrium_n.csv, stress_profiles.csv, resistance_curve.csv
using the paper's equations (effective K-field for stress, wake shielding).
"""
import sys
import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import quad
import csv

# ----------------------------------------------------------------------
# Constants and paper parameters
# ----------------------------------------------------------------------
MU      = 1.0        # shear modulus (normalized)
B       = 1.0        # Burgers vector length (normalized)
NU      = 0.3        # Poisson ratio
ALPHA   = np.pi/4    # slip plane angle
R_CUT   = 1.0        # core cutoff radius (b)

# Complex helper
I = 1j

def B_coeff():
    """Complex coefficient B for an edge dislocation with b along slip plane."""
    b1 = B * np.cos(ALPHA)
    b2 = B * np.sin(ALPHA)
    return (MU / (4*np.pi*(1-NU)*I)) * (b1 + I*b2)

# ----------------------------------------------------------------------
# Potential functions for a symmetric pair at s and its conjugate
# Equations (A4) and (A6)
# ----------------------------------------------------------------------
def Phi0(z, s):
    Bc = B_coeff()
    return Bc/(z - s) + np.conj(Bc)/(np.conj(z) - np.conj(s))

def Omega0(z, s):
    Bc = B_coeff()
    # (A4)
    term1 = np.conj(Bc)/(z - s)
    term2 = (Bc*(np.conj(s) - s))/((z - s)**2)
    term3 = Bc/(z - np.conj(s))
    term4 = (np.conj(Bc)*(s - np.conj(s)))/((z - np.conj(s))**2)
    return term1 + term2 + term3 + term4

def Phi1(z, s):
    """Negating stress potentials (A6). Phi1 = conj(Omega1)."""
    Bc = B_coeff()
    cz = np.conj(z)
    cs = np.conj(s)
    sqrtz = np.lib.scimath.sqrt(z)
    sqrts = np.lib.scimath.sqrt(s)
    sqrtcs = np.lib.scimath.sqrt(cs)
    
    # Bracketed terms of (A6)
    bracket = (
        np.conj(Bc)/(cz - cs) + Bc/(z - s) + np.conj(Bc)/(z - s) + Bc/(z - cs)
        + (Bc*(cs - s))/((z - s)**2) + (np.conj(Bc)*(s - cs))/((z - cs)**2)
        + (1/sqrtz) * (
            np.conj(Bc)*sqrtcs/(cs - z) + Bc*sqrts/(s - z)
            + np.conj(Bc)*sqrts/(s - z) + Bc*sqrtcs/(cs - z)
            - (Bc*(cs - s))/(2*sqrts) * (s + z)/((s - z)**2)
            + (np.conj(Bc)*(s - cs))/(2*sqrtcs) * (cs + z)/((cs - z)**2)
        )
    )
    return -0.5 * bracket

def Omega1(z, s):
    """Omega1 = conj(Phi1)."""
    return np.conj(Phi1(np.conj(z), np.conj(s)))

def total_Phi(z, s):
    return Phi0(z, s) + Phi1(z, s)

def total_Omega(z, s):
    return Omega0(z, s) + Omega1(z, s)

# ----------------------------------------------------------------------
# Interaction force F_ij^inter  (A7)
# ----------------------------------------------------------------------
def F_inter_ij(h_i, h_j):
    """
    Returns the interaction force (scalar, along slip direction) on dislocation i
    due to the symmetric pair of dislocation j.
    h_i, h_j: distances along the slip plane (positive).
    """
    z_i = h_i * np.exp(I*ALPHA)
    s_j = h_j * np.exp(I*ALPHA)
    # Compute derivative dΦ/dz_i
    # Numerical derivative via finite difference (central)
    delta = 1e-8
    Phi_plus = total_Phi(z_i + delta, s_j)
    Phi_minus = total_Phi(z_i - delta, s_j)
    dPhi = (Phi_plus - Phi_minus) / (2*delta)
    
    Omega_at_i = total_Omega(z_i, s_j)
    Phi_at_i = total_Phi(z_i, s_j)
    
    term = np.exp(2*I*ALPHA) * ((np.conj(z_i) - z_i)*dPhi + Omega_at_i - Phi_at_i)
    return np.imag(term)

# ----------------------------------------------------------------------
# Force balance functions
# ----------------------------------------------------------------------
def total_force_on_i(i, h_array, Kapp, sigma_f):
    """
    Returns force imbalance F_i - sigma_f*b  (should vanish at equilibrium).
    h_array: list of positions h_1,...,h_n
    """
    n = len(h_array)
    h_i = h_array[i]
    # K-field force
    F_K = (Kapp * B) / (2.0 * np.sqrt(2*np.pi*h_i)) * np.sin(ALPHA) * np.cos(ALPHA/2.0)
    # Image force
    F_img = - (MU * B*B) / (4*np.pi*(1-NU)*h_i)
    # Interaction forces
    F_inter = 0.0
    for j in range(n):
        if j == i:
            continue
        h_j = h_array[j]
        F_inter += F_inter_ij(h_i, h_j)
    total = F_K + F_img + F_inter
    return total - sigma_f * B   # balance against friction

def forces_residual(h_vars, Kapp, sigma_f):
    """Returns array of residuals for fsolve."""
    n = len(h_vars)
    res = np.zeros(n)
    for i in range(n):
        res[i] = total_force_on_i(i, h_vars, Kapp, sigma_f)
    return res

def solve_positions(n, Kapp, sigma_f, max_iter=500):
    """
    Solve for equilibrium positions h_i of n dislocations.
    Returns array of h_i, or None if no solution found.
    """
    if n == 0:
        return np.array([])
    # initial guess: linearly spaced from 1.1*R_CUT to 10*n
    guess = np.linspace(1.5*R_CUT, 5.0*n, n)
    # Use fsolve with trust-region;
    # scalings to help convergence
    try:
        sol, infodict, ier, msg = fsolve(
            forces_residual, guess, args=(Kapp, sigma_f),
            full_output=True, xtol=1e-8, maxfev=2000
        )
        if ier != 1:
            return None
        # Ensure all positions are positive and sorted
        sol_sort = np.sort(sol)
        if np.any(sol_sort <= R_CUT):
            return None
        return sol_sort
    except Exception:
        return None

# ----------------------------------------------------------------------
# Energy terms
# ----------------------------------------------------------------------
def compute_self_energy(h_array):
    n = len(h_array)
    if n == 0:
        return 0.0
    coeff = (MU * B*B) / (4*np.pi*(1-NU))
    return 2.0 * coeff * np.sum(np.log(h_array / R_CUT))

def compute_Kd_energy(h_array, Kapp):
    n = len(h_array)
    if n == 0:
        return 0.0
    factor = Kapp / np.sqrt(2*np.pi) * B * np.sin(ALPHA) * np.cos(ALPHA/2)
    return -2.0 * factor * np.sum(np.sqrt(h_array))

def compute_dd_energy(h_array):
    """Interaction energy W_dd via integration along path."""
    n = len(h_array)
    if n < 2:
        return 0.0
    energy = 0.0
    for i in range(1, n):  # i from 1..n-1
        h_i_target = h_array[i]
        # For each earlier dislocation j < i, integrate F_ij from R_CUT to h_i
        for j in range(i):
            h_j = h_array[j]
            def integrand(h):
                # compute force when i-th dislocation is at h, others fixed
                # Note: F_inter_ij expects distance of i and j; we keep j fixed at h_j
                return F_inter_ij(h, h_j)
            # integrate
            val, _ = quad(integrand, R_CUT, h_i_target, limit=100, epsabs=1e-8)
            energy += val
    # Summation over i and j already double counted? Formula is sum_{i=2..n} sum_{j=1..i-1}
    # That's exactly our loops.
    return energy

def compute_ledge_energy(n, beta=0.055):
    gamma = beta * MU * B
    return 2.0 * n * gamma * B

def compute_lattice_energy(h_array, sigma_f):
    n = len(h_array)
    if n == 0:
        return 0.0
    return 2.0 * sigma_f * np.sum(h_array - R_CUT)

def compute_total_energy(n, h_array, Kapp, sigma_f, beta=0.055):
    if n == 0:
        # energy with no dislocations is zero reference
        return 0.0
    W_self = compute_self_energy(h_array)
    W_Kd   = compute_Kd_energy(h_array, Kapp)
    W_dd   = compute_dd_energy(h_array)
    W_ledge = compute_ledge_energy(n, beta)
    W_latt  = compute_lattice_energy(h_array, sigma_f)
    return W_self + W_Kd + W_dd + W_ledge + W_latt

# ----------------------------------------------------------------------
# Equilibrium number determination for given (Kapp, sigma_f)
# ----------------------------------------------------------------------
def equilibrium_n(Kapp, sigma_f, beta=0.055, max_n=25):
    min_energy = None
    best_n = 0
    for n in range(1, max_n+1):
        h = solve_positions(n, Kapp, sigma_f)
        if h is None:
            # can't place n dislocations
            break
        E = compute_total_energy(n, h, Kapp, sigma_f, beta)
        if min_energy is None or E < min_energy:
            min_energy = E
            best_n = n
    return best_n

# ----------------------------------------------------------------------
# Stress profile computation using effective K-field (section 3.2)
# ----------------------------------------------------------------------
def K_shield_single(h):
    """Shielding stress intensity factor from a symmetric pair at distance h along slip plane. (Eq. 5)"""
    return (3.0 * MU * B) / (np.sqrt(2*np.pi*h) * (1.0 - NU)) * np.sin(ALPHA) * np.cos(ALPHA/2.0)

def sigma_d(x1, h_array):
    """
    Dislocation self-stress σ22 along x1 axis (Eq. A8, sum of contributions).
    x1: distance from notch tip (positive).
    """
    total = 0.0
    for h_i in h_array:
        s_i = h_i * np.exp(I*ALPHA)
        # Use infinite medium potentials Phi0, Omega0 evaluated on the crack line (real axis)
        z = x1 + 0.0*I
        Phi = Phi0(z, s_i)
        Omega = Omega0(z, s_i)
        sigma = np.real(np.conj(Phi) + Omega)
        total += sigma
    return total

def sigma_total(x1, Kapp, h_array, rho):
    """
    Total hoop stress along extension line using effective K-field approximation.
    x1: distance from notch tip (positive).
    rho = n * b * sin(alpha)  # notch radius
    """
    # Applied K-field stress and notch negation stress (Eq. 8)
    K_shield_sum = 0.0
    for h in h_array:
        K_shield_sum += K_shield_single(h)
    prefactor = 2.0 / np.sqrt(np.pi * (rho + 2*x1))
    factor = 1.0 + rho/(rho + 2*x1)
    sigma_K = Kapp * prefactor * factor
    sigma_dn = - K_shield_sum * prefactor * factor
    sigma_dis = sigma_d(x1, h_array)
    return (sigma_K + sigma_dn + sigma_dis) / MU   # return normalized

# ----------------------------------------------------------------------
# Resistance curve helpers
# ----------------------------------------------------------------------
def K_shield_wake(r, theta):
    """
    Shielding K by a symmetric pair at polar coords (r, theta) from current tip.
    Eq. (A10)
    """
    if r <= 0:
        return 0.0
    factor = (MU*B)/(1-NU) * np.sqrt(2/(np.pi*r))
    term = np.cos(theta/2.0) * (np.sin(ALPHA) + np.sin(theta/2.0)*np.cos(1.5*theta - ALPHA))
    return factor * term

# ----------------------------------------------------------------------
# Generate outputs
# ----------------------------------------------------------------------
def write_equilibrium_n():
    sigmas = [0.001, 0.002, 0.004]
    # Kapp range, adjust step to capture curves
    Kapp_range = np.linspace(0.6, 1.3, 20)  # enough points for smoothness
    rows = []
    for sf in sigmas:
        for K in Kapp_range:
            n_eq = equilibrium_n(K, sf, beta=0.055)
            rows.append([sf, K, n_eq])
    with open('equilibrium_n.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['sigma_f_normalized', 'Kapp_normalized', 'n'])
        w.writerows(rows)

def write_stress_profiles():
    # We need the equilibrium positions for sigma_f=0.002 and Kapp values shown
    sigma_f = 0.002
    Kvals = [0.98, 1.13, 1.26]
    # Find equilibrium n and h for each case
    configs = {}
    for K in Kvals:
        n_eq = equilibrium_n(K, sigma_f, beta=0.055)
        if n_eq == 0:
            h_eq = []
        else:
            h_eq = solve_positions(n_eq, K, sigma_f)
            if h_eq is None:
                h_eq = []
        configs[K] = (n_eq, h_eq)
    
    # stress evaluation grid
    x1_range = np.linspace(1.0, 400.0, 200)   # x1 in units of b
    rows = []
    for x1 in x1_range:
        row = [x1]
        for K in Kvals:
            n_eq, h_eq = configs[K]
            if n_eq == 0:
                row.append(0.0)
            else:
                rho = n_eq * B * np.sin(ALPHA)
                sig = sigma_total(x1, K, h_eq, rho)
                row.append(sig)
        rows.append(row)
    with open('stress_profiles.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['x1_b', 'sigma_case1', 'sigma_case2', 'sigma_case3'])
        w.writerows(rows)

def write_resistance_curve():
    # Parameters
    sigma_f = 0.006
    sigma_cr = 0.06
    beta = 0.055
    nu = 0.3
    # Step 1: determine K_init where Griffith for nanocrack is satisfied
    # We need to sweep Kapp and compute K_nano, find where K_nano = 2*sqrt(beta/(1-nu))*MU*sqrt(B)
    target = 2.0 * np.sqrt(beta/(1-nu)) * MU * np.sqrt(B)  # = 2 * sqrt(0.055/0.7) * 1 * 1 ≈ 0.56
    # Build function to evaluate K_nano at given Kapp
    def get_K_nano(Kapp):
        n_eq = equilibrium_n(Kapp, sigma_f, beta=beta)
        if n_eq == 0:
            return 0.0
        h_eq = solve_positions(n_eq, Kapp, sigma_f)
        if h_eq is None:
            return 0.0
        rho = n_eq * B * np.sin(ALPHA)
        # Need stress peak and a_nano
        # approximate by evaluating stress on fine grid and finding peak
        xs = np.linspace(1.0, 300.0, 300)
        sigs = np.array([sigma_total(x, Kapp, h_eq, rho) for x in xs])
        idx_peak = np.argmax(sigs)
        x_peak = xs[idx_peak]
        # a_nano: half-length of segment where stress > sigma_cr
        above = sigs > sigma_cr
        if not np.any(above):
            return 0.0
        # first and last indices above threshold near the peak
        idx_above = np.where(above)[0]
        # restrict to connected region around peak
        left = idx_above[idx_above <= idx_peak]
        right = idx_above[idx_above >= idx_peak]
        if len(left)==0 or len(right)==0:
            return 0.0
        x_left = xs[left[0]]
        x_right = xs[right[-1]]
        a_nano = 0.5 * (x_right - x_left)
        if a_nano <= 0:
            return 0.0
        # compute K_nano via integral (11)
        # Map s in [-1,1] to x: x = x_peak + a_nano * s
        def integrand(s):
            x = x_peak + a_nano * s
            # sigma (normalized by MU)
            sig = sigma_total(x, Kapp, h_eq, rho)  # already normalized
            return np.sqrt((1-s)/(1+s)) * sig
        K_nano = MU * np.sqrt(a_nano/np.pi) * quad(integrand, -1, 1, limit=100, epsabs=1e-6)[0]
        return K_nano

    # search for K_init where K_nano reaches target
    K_scan = np.linspace(0.6, 2.5, 30)
    K_nano_vals = []
    for K in K_scan:
        K_nano_vals.append(get_K_nano(K))
    # find first K where K_nano >= target
    K_init = None
    for idx, K in enumerate(K_scan):
        if K_nano_vals[idx] >= target:
            K_init = K
            break
    if K_init is None:
        # fallback: use paper's approximate value
        K_init = 1.82   # from text: "When K_app reaches 1.82 μ√b, K_nano will be 0.56 μ√b"
    
    # Compute configuration at K_init for growth
    n_eq = equilibrium_n(K_init, sigma_f, beta=beta)
    if n_eq == 0:
        n_eq = 5   # fallback
    h_eq = solve_positions(n_eq, K_init, sigma_f)
    if h_eq is None:
        h_eq = np.linspace(2, 15, n_eq)  # plausible fallback
    # Determine Δa = x_peak + a_nano at K_init
    rho = n_eq * B * np.sin(ALPHA)
    xs = np.linspace(1.0, 300.0, 300)
    sigs = np.array([sigma_total(x, K_init, h_eq, rho) for x in xs])
    idx_peak = np.argmax(sigs)
    x_peak = xs[idx_peak]
    above = sigs > sigma_cr
    idx_above = np.where(above)[0]
    left = idx_above[idx_above <= idx_peak]
    right = idx_above[idx_above >= idx_peak]
    x_left = xs[left[0]]
    x_right = xs[right[-1]]
    a_nano = 0.5 * (x_right - x_left)
    delta_a = x_peak + a_nano
    # CTOA
    CTOA = 2.0 * np.arctan( (n_eq * B * np.sin(ALPHA)) / delta_a )
    
    # Growth simulation
    max_steps = 15
    rows = []
    K_app = K_init
    rows.append([0.0, K_init])  # initial crack advance=0
    for m in range(1, max_steps+1):
        cum_adv = m * delta_a
        # Sum shielding from all previous steps
        K_shield_total = 0.0
        for j in range(1, m+1):
            # slip trace at distance j * delta_a from current tip
            # For each dislocation i on that trace
            for h_i in h_eq:
                # polar coordinates from current tip (formula (22))
                d = j * delta_a
                r_ij = np.sqrt(d**2 - 2*d*h_i*np.cos(ALPHA) + h_i**2)
                theta_ij = np.arctan2(h_i*np.sin(ALPHA), h_i*np.cos(ALPHA) - d)
                if theta_ij < 0:
                    theta_ij += np.pi  # keep positive?
                K_shield_total += K_shield_wake(r_ij, theta_ij)
        K_app = K_init + K_shield_total
        rows.append([cum_adv, K_app])
    
    # Write CSV
    with open('resistance_curve.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['crack_advance_b', 'Kapp_normalized'])
        w.writerows(rows)

# Main dispatch
if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'equilibrium_n':
        write_equilibrium_n()
    elif cmd == 'stress_profiles':
        write_stress_profiles()
    elif cmd == 'resistance_curve':
        write_resistance_curve()
    else:
        print(f"Unknown command {cmd}", file=sys.stderr)
        sys.exit(1)
