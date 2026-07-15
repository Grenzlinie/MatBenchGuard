#!/usr/bin/env python3
"""
Compute binodal, spinodal, and density maxima curves for the 3D lattice gas
quasichemical approximation with λ=1. Prints CSV to stdout.

Methods:
- Equation of state (P*, μ*, ρ) in terms of parameter r and T*.
- Spinodal: ∂P*/∂ρ = 0 ⟺ ∂P*/∂r = 0 (numerical derivative).
- Binodal: equal P* and μ* for two densities (Maxwell construction) solved via
  fsolve for r_vap, r_liq.
- Density maxima: ∂ρ/∂T*|_P*=0, found by scanning T* for each P* and locating
  zero crossing.
"""

import sys
import argparse
import numpy as np
from scipy.optimize import fsolve, bisect

# Constants
LAMBDA = 1.0

# --- Helper functions for λ=1 ---
def x_fun(T):
    """exp(-epsilon/kT) = exp(-1/T*)"""
    return np.exp(-1.0 / T)

def rho_of_rT(r, T):
    """Density ρ from r and T* (eq 46 with λ=1)."""
    xm05 = x_fun(T) ** (-0.5)   # exp(0.5/T)
    xp15 = x_fun(T) ** (1.5)     # exp(-1.5/T)
    sqrt_r = np.sqrt(r)
    num = 1.0 + sqrt_r * (2.0 * xm05 + xp15) + 3.0 * r + xm05 * r**(1.5)
    den = (r**(-0.5) * xm05 + 4.0 + 2.0 * sqrt_r * (2.0 * xm05 + xp15) +
           4.0 * r + xm05 * r**(1.5))
    return num / den

def Pstar_of_rT(r, T):
    """Dimensionless pressure P* from r and T* (eq 39 with λ=1)."""
    rho = rho_of_rT(r, T)
    if rho >= 1.0:
        return np.nan
    t1 = (1.0 - rho)**(5.0/3.0)
    xm05 = x_fun(T) ** (-0.5)
    xp15 = x_fun(T) ** (1.5)
    x2 = x_fun(T) ** 2.0   # exp(-2/T)
    # Simplified expression: (1 + 3*sqrt(r)*x^{0.5} + r*(2 + x^2) + r^{1.5}*x^{0.5})
    inner = 1.0 + 3.0 * np.sqrt(r) * np.sqrt(x_fun(T)**(-1)) + r * (2.0 + x2) + r**(1.5) * np.sqrt(x_fun(T)**(-1))
    # Actually: inner = 1 + 3 r^{1/2} x^{1/2} + r (2 + x^2) + r^{3/2} x^{1/2}
    # Note x^{1/2} = exp(-0.5/T*) = x_fun(T)**0.5, so inverse is x_fun(T)**(-0.5)
    # So correct: 3 * sqrt(r) * x_fun(T)**(-0.5), etc.
    inner = 1.0 + 3.0 * np.sqrt(r) * x_fun(T)**(-0.5) + r * (2.0 + x_fun(T)**2.0) + r**(1.5) * x_fun(T)**(-0.5)
    prefac = 0.75 * T  # 3/4 * T*
    return prefac * np.log(t1 * inner)

def mustar_of_rT(r, T):
    """Dimensionless chemical potential μ* (eq 40 with λ=1)."""
    rho = rho_of_rT(r, T)
    if rho <= 0.0 or rho >= 1.0:
        return np.nan
    # μ* = -1.5 + T* log( r^{3/2} ((1-ρ)/ρ)^2 )
    return -1.5 + T * np.log(r**(1.5) * ((1.0 - rho) / rho)**2)

# --- Spinodal ---
def find_spinodal_for_T(T, r_range=(1e-6, 1e4), n_points=5000):
    """
    Find spinodal points (where dP*/dr = 0) for a given T.
    Returns list of (T*, P*) tuples.
    """
    # Sample r logarithmically
    rs = np.logspace(np.log10(r_range[0]), np.log10(r_range[1]), n_points)
    Ps = np.array([Pstar_of_rT(r, T) for r in rs])
    rhs = np.array([rho_of_rT(r, T) for r in rs])
    # Filter valid (finite, non-NaN)
    valid = np.isfinite(Ps) & np.isfinite(rhs) & (rhs > 0) & (rhs < 1)
    if np.sum(valid) < 50:
        return []
    rs_valid = rs[valid]
    Ps_valid = Ps[valid]
    # Compute numerical derivative
    dP_dr = np.gradient(Ps_valid, rs_valid)
    # Find sign changes
    spinodal_r = []
    for i in range(1, len(dP_dr)):
        if dP_dr[i-1] * dP_dr[i] <= 0 and abs(dP_dr[i]) > 1e-12:
            # Use bisection to refine root
            lo, hi = rs_valid[i-1], rs_valid[i]
            try:
                root = bisect(lambda r: np.gradient([Pstar_of_rT(r-lo, T) for _ in range(2)], [lo,hi])[0], lo, hi, xtol=1e-10, maxiter=50)
                # Actually better: define function f(r) = dP*/dr approx (P*(r+eps)-P*(r-eps))/(2*eps)
                # Use a small eps
            except Exception:
                continue
            # Approximate derivative with central difference
            eps = 1e-6
            f = lambda r: (Pstar_of_rT(r+eps, T) - Pstar_of_rT(r-eps, T)) / (2*eps)
            try:
                root = bisect(f, lo, hi, xtol=1e-10, maxiter=50)
            except (ValueError, RuntimeError):
                # If not bracketing, skip
                continue
            P_val = Pstar_of_rT(root, T)
            if np.isfinite(P_val) and P_val > -0.1:
                spinodal_r.append((root, P_val))
    # Deduplicate near points
    if len(spinodal_r) < 2:
        return []
    # Sort by density
    spinodal_r.sort(key=lambda x: Pstar_of_rT(x[0], T))
    # Usually two points: low-pressure (vapor spinodal) and high-pressure (liquid spinodal)
    # But for reentrant shape, there may be more; for λ=1, there is a reentrant branch.
    # Keep all.
    return [(T, P_) for _, P_ in spinodal_r]

def compute_spinodal_curve(T_min=0.05, T_max=1.2, dT=0.005):
    """Compute spinodal points over T range, return list of (T*, P*)."""
    points = []
    Ts = np.arange(T_min, T_max + dT/2, dT)
    for T in Ts[::-1]:  # descending to get critical point easily? No, just all.
        pts = find_spinodal_for_T(T)
        points.extend(pts)
    # Sort by T, then P
    points.sort()
    # Remove near duplicates
    filtered = []
    for p in points:
        if not filtered or (abs(p[0]-filtered[-1][0]) > 1e-6 or abs(p[1]-filtered[-1][1]) > 1e-5):
            filtered.append(p)
    return filtered

# --- Binodal (Maxwell construction) ---
def solve_binodal_for_T(T, r1_init, r2_init):
    """
    Solve for r1, r2 such that P*(r1) = P*(r2) and μ*(r1) = μ*(r2).
    Returns (r1, r2) or None.
    """
    def eq(vars):
        r1, r2 = vars
        P1 = Pstar_of_rT(r1, T)
        P2 = Pstar_of_rT(r2, T)
        mu1 = mustar_of_rT(r1, T)
        mu2 = mustar_of_rT(r2, T)
        return [P1 - P2, mu1 - mu2]
    try:
        sol = fsolve(eq, [r1_init, r2_init], maxfev=2000, xtol=1e-8)
    except Exception:
        return None
    r1, r2 = sol
    if r1 <= 0 or r2 <= 0 or r1 >= r2:
        return None
    # Verify equality within tolerance
    if abs(Pstar_of_rT(r1,T) - Pstar_of_rT(r2,T)) > 1e-4 or abs(mustar_of_rT(r1,T)-mustar_of_rT(r2,T)) > 1e-4:
        return None
    return r1, r2

def compute_binodal_curve(T_min=0.05, T_crit_est=1.06, dT=0.01):
    """
    Compute binodal points for T from 0.05 to near critical.
    Uses spinodal points to bracket initial guesses.
    Returns list of (T*, P*).
    """
    points = []
    Ts = np.arange(T_min, T_crit_est + dT/2, dT)
    last_r1, last_r2 = None, None
    for T in Ts[::-1]:  # start from high to low for continuation
        # Get spinodal points for this T as bounds
        spin_pts = find_spinodal_for_T(T)
        if len(spin_pts) < 2:
            continue
        # The two spinodal pressures bracket the coexistence pressure.
        # Densities: corresponding r values.
        # Get the two spinodal r values by solving for r where dP/dr=0 and taking those points.
        # But we already have them; we can approximate r from spin_pts.
        # Simpler: we can find r that gives spinodal pressures by scanning.
        # Since we are near the critical point, we can use fsolve with good guesses.
        # Use the r from the previous T as initial guess.
        if last_r1 is None or last_r2 is None:
            # initial guess: r1 small (~0.01), r2 large (~10)
            r1_g = 0.001
            r2_g = 100.0
        else:
            r1_g = last_r1 * 0.9
            r2_g = last_r2 * 1.1
        res = solve_binodal_for_T(T, r1_g, r2_g)
        if res is None:
            # Try other guesses
            for r1_g, r2_g in [(0.001, 100), (0.01, 500), (0.0001, 10)]:
                res = solve_binodal_for_T(T, r1_g, r2_g)
                if res:
                    break
        if res:
            r1, r2 = res
            P_coex = Pstar_of_rT(r1, T)
            if abs(Pstar_of_rT(r2,T) - P_coex) > 1e-4:
                continue
            points.append((T, P_coex))
            last_r1, last_r2 = r1, r2
        else:
            last_r1 = last_r2 = None
    points.sort()
    return points

# --- Density maxima ---
def find_density_max_for_P(target_P, T_range=(0.02, 0.5), T_step=0.001):
    """
    For a given pressure P*, scan T* and find points where dρ/dT* = 0.
    Returns list of (T*, P*, ρ).
    """
    # We need to solve for r given P* and T*, then compute ρ.
    def rho_from_PT(T):
        # Solve P*(r,T)=target_P for r.
        # Define function f(r) = P*(r,T) - target_P
        # Use bisection on a wide bracket.
        f = lambda r: Pstar_of_rT(r, T) - target_P
        # Find a bracketing interval
        r_lo, r_hi = 1e-6, 1e6
        f_lo = f(r_lo)
        f_hi = f(r_hi)
        if not (np.isfinite(f_lo) and np.isfinite(f_hi)):
            return None
        # Expand interval if needed
        for _ in range(30):
            if f_lo * f_hi < 0:
                break
            r_hi *= 10
            f_hi = f(r_hi)
            if not np.isfinite(f_hi):
                break
        else:
            # try contracting from low
            for _ in range(30):
                if f_lo * f_hi < 0:
                    break
                r_lo /= 10
                f_lo = f(r_lo)
                if not np.isfinite(f_lo):
                    break
        if f_lo * f_hi >= 0 or not (np.isfinite(f_lo) and np.isfinite(f_hi)):
            return None
        try:
            root = bisect(f, r_lo, r_hi, xtol=1e-6, maxiter=50)
        except Exception:
            return None
        return rho_of_rT(root, T)
    Ts = np.arange(T_range[0], T_range[1] + T_step/2, T_step)
    rhos = []
    for T in Ts:
        rho = rho_from_PT(T)
        if rho is None or not np.isfinite(rho) or rho <= 0 or rho >= 1:
            rhos.append(None)
        else:
            rhos.append(rho)
    # Find local maxima: where derivative changes sign and value is high
    maxima = []
    valid_idx = [i for i, v in enumerate(rhos) if v is not None]
    for i in range(1, len(valid_idx)-1):
        j = valid_idx[i]
        prev = rhos[valid_idx[i-1]]
        curr = rhos[j]
        nxt = rhos[valid_idx[i+1]]
        # Compute finite difference
        dT_prev = Ts[j] - Ts[valid_idx[i-1]]
        dT_nxt = Ts[valid_idx[i+1]] - Ts[j]
        if dT_prev <= 0 or dT_nxt <= 0:
            continue
        d1 = (curr - prev) / dT_prev
        d2 = (nxt - curr) / dT_nxt
        # Zero crossing of derivative: d1 > 0 and d2 < 0 (maximum)
        if d1 > 0 and d2 < 0:
            # Use refined T by linear interpolation of derivative
            # approximate zero of derivative between these points
            # Simple: take T where derivative supposedly zero
            T_zero = Ts[j] - d1 * (Ts[j] - Ts[valid_idx[i-1]]) / (d1 - d2)  # interpolation
            # recalc rho at T_zero
            rho_ref = rho_from_PT(T_zero)
            if rho_ref is not None and np.isfinite(rho_ref):
                maxima.append((T_zero, target_P, rho_ref))
    return maxima

def compute_density_maxima(P_range=(0.01, 0.3), T_max_guess=0.8):
    """Compute density maxima locus by scanning many P."""
    points = []
    Ps = np.linspace(P_range[0], P_range[1], 200)
    for P in Ps:
        max_pts = find_density_max_for_P(P, T_range=(0.005, T_max_guess), T_step=0.002)
        points.extend(max_pts)
    # Sort by T
    points.sort(key=lambda x: x[0])
    # Remove near duplicates
    filtered = []
    for t, p, rho in points:
        if filtered and abs(t - filtered[-1][0]) < 0.001 and abs(p - filtered[-1][1]) < 0.0005:
            continue
        filtered.append((t, p, rho))
    return filtered

# --- Main output ---
def generate_phase_diagram():
    print("curve_type,T_star,P_star")
    # Spinodal
    spinodal = compute_spinodal_curve()
    for T, P in spinodal:
        print(f"spinodal,{T:.6f},{P:.6f}")
    # Binodal
    binodal = compute_binodal_curve()
    for T, P in binodal:
        print(f"binodal,{T:.6f},{P:.6f}")

def generate_density_maxima():
    print("T_star,P_star,rho")
    maxima = compute_density_maxima()
    for T, P, rho in maxima:
        print(f"{T:.6f},{P:.6f},{rho:.6f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--phase-diagram", action="store_true", help="Output phase_diagram_3d.csv")
    group.add_argument("--density-maxima", action="store_true", help="Output density_maxima_3d.csv")
    args = parser.parse_args()
    if args.phase_diagram:
        generate_phase_diagram()
    elif args.density_maxima:
        generate_density_maxima()
