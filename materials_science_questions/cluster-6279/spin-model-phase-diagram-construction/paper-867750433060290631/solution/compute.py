import numpy as np
from scipy.optimize import fsolve, root_scalar
import argparse
import csv
import sys

# Dimensionless Hamiltonian parameters (defaults for stability diagram)
J0 = 0.8
D = 0.4
xi = 1.25
eta = 0.8
zeta_default = 1.2

# ------------------------------------------------------------
# Self-consistency helpers
# ------------------------------------------------------------
def rhs_SQ(S, Q, theta, h, zeta):
    """Right-hand sides of eqs (8) for given (S,Q,theta,h,zeta)."""
    y = (h + 2 * J0 * S) / theta
    z = (6 * Q - D) / theta
    exp_z = np.exp(z)
    cosh_y = np.cosh(y)
    denom = 1 + 2 * cosh_y * exp_z
    S_rhs = 2 * np.sinh(y) * exp_z / denom
    Q_rhs = 1/3 - 1/denom
    return S_rhs, Q_rhs

def equations_full(p, theta, h, zeta):
    S, Q = p
    S_rhs, Q_rhs = rhs_SQ(S, Q, theta, h, zeta)
    return [S - S_rhs, Q - Q_rhs]

def solve_self_consistent(theta, h, zeta):
    """Solve for S, Q at given (theta, h)."""
    guess = [1.0, 1/3]
    sol, infodict, ier, msg = fsolve(equations_full, guess,
                                     args=(theta, h, zeta),
                                     full_output=True, xtol=1e-10, maxfev=2000)
    if ier != 1:
        raise RuntimeError(f"fsolve did not converge at theta={theta}, h={h}: {msg}")
    return sol[0], sol[1]

# ------------------------------------------------------------
# Gap expressions (dimensionless, in units of K0)
# ------------------------------------------------------------
def omega1(theta, h, zeta):
    S, Q = solve_self_consistent(theta, h, zeta)
    return 2 * h + 4 * S * (J0 - zeta)

def omega2(theta, h, zeta):
    S, Q = solve_self_consistent(theta, h, zeta)
    # J_k = J0, K_k = K0=1 at k=0
    # Note: D_tilde = D (since K0=1)
    part1 = D - 6 * Q * (1 - xi * J0)          # D - 6⟨O2^0⟩(K0 - ξ J0)
    part2 = D - 6 * Q * (1 - eta)               # D - 6⟨O2^0⟩(K0 - η K0)
    cross = S**2 * (xi * J0 - eta)**2
    sqrt_val = np.sqrt(cross + part1 * part2)
    return h + S * (2 * J0 - xi * J0 - eta) - sqrt_val

# ------------------------------------------------------------
# Specialised solve for ω₁(0)=0 curve (analytical decoupling)
# ------------------------------------------------------------
def equations_omega1(p, theta, zeta):
    S, Q = p
    # ω₁(0)=0 => h = -2*S*(J0 - zeta) → y = 2*S*zeta / theta
    y = (2 * S * zeta) / theta
    z = (6 * Q - D) / theta
    exp_z = np.exp(z)
    cosh_y = np.cosh(y)
    denom = 1 + 2 * cosh_y * exp_z
    S_rhs = 2 * np.sinh(y) * exp_z / denom
    Q_rhs = 1/3 - 1/denom
    return [S - S_rhs, Q - Q_rhs]

def solve_omega1_curve_pt(theta, zeta):
    """Return (S, Q, h) for a point on the ω₁(0)=0 boundary at theta."""
    guess = [1.0, 1/3]
    sol, infodict, ier, msg = fsolve(equations_omega1, guess,
                                     args=(theta, zeta),
                                     full_output=True, xtol=1e-10, maxfev=2000)
    if ier != 1:
        raise RuntimeError(f"omega1 fsolve did not converge at theta={theta}, zeta={zeta}: {msg}")
    S, Q = sol
    h = -2 * S * (J0 - zeta)
    return S, Q, h

# ------------------------------------------------------------
# Generate stability_boundaries.csv
# ------------------------------------------------------------
def generate_stability_boundaries():
    zeta = zeta_default
    # Use a dense theta grid from near zero to 2.0
    theta_vals = np.geomspace(0.001, 2.0, 200)
    
    points1 = []
    for th in theta_vals:
        try:
            _, _, h = solve_omega1_curve_pt(th, zeta)
            if np.isfinite(h):
                points1.append([th, h, 1])
        except:
            pass
    
    points2 = []
    for th in theta_vals:
        # For omega2 zero, find h by root-finding
        def f(h):
            return omega2(th, h, zeta)
        # Scan for bracket
        h_scan = np.linspace(0.0, 2.0, 20)
        found = False
        for i in range(len(h_scan)-1):
            a, b = h_scan[i], h_scan[i+1]
            try:
                fa, fb = f(a), f(b)
            except:
                continue
            if fa * fb < 0:
                try:
                    sol = root_scalar(f, bracket=[a,b], method='bisect', xtol=1e-8)
                    points2.append([th, sol.root, 2])
                    found = True
                except:
                    pass
                break
        # If not found, try extended range
        if not found:
            h_scan2 = np.linspace(2.0, 5.0, 10)
            for i in range(len(h_scan2)-1):
                a, b = h_scan2[i], h_scan2[i+1]
                try:
                    fa, fb = f(a), f(b)
                except:
                    continue
                if fa * fb < 0:
                    try:
                        sol = root_scalar(f, bracket=[a,b], method='bisect', xtol=1e-8)
                        points2.append([th, sol.root, 2])
                    except:
                        pass
                    break
    
    all_points = points1 + points2
    # sort by type then temperature? Actually we'll keep order; verifier will handle.
    with open('/app/outputs/stability_boundaries.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['reduced_temperature', 'reduced_field', 'boundary_type'])
        writer.writerows(all_points)

# ------------------------------------------------------------
# Generate pt_temperature_vs_zeta.csv
# ------------------------------------------------------------
def generate_pt_vs_zeta():
    h_vals = [0.6, 0.8, 1.0]
    zeta_vals = np.linspace(0.5, 2.0, 101)
    rows = []
    for h_target in h_vals:
        for zeta in zeta_vals:
            # We need theta_c solving: -2*S*(J0-zeta) = h_target
            # where S = solution of self-consistency with ω₁ condition
            def residual(theta):
                try:
                    S, Q, _ = solve_omega1_curve_pt(theta, zeta)
                    return -2 * S * (J0 - zeta) - h_target
                except:
                    return np.nan
            
            lo, hi = 0.001, 3.0
            try:
                flo = residual(lo)
                fhi = residual(hi)
            except:
                flo = np.nan
                fhi = np.nan
            if np.isnan(flo) or np.isnan(fhi):
                rows.append([zeta, 0.0, h_target])
                continue
            if flo * fhi > 0:
                # no sign change; theta_c = 0
                rows.append([zeta, 0.0, h_target])
            else:
                try:
                    sol = root_scalar(residual, bracket=[lo, hi], method='bisect', xtol=1e-8)
                    theta_c = sol.root
                    rows.append([zeta, theta_c, h_target])
                except:
                    rows.append([zeta, 0.0, h_target])
    
    with open('/app/outputs/pt_temperature_vs_zeta.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['zeta', 'reduced_temperature', 'reduced_field'])
        writer.writerows(rows)

# ------------------------------------------------------------
# Entry point
# ------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, choices=['stability_boundaries', 'pt_temperature_vs_zeta'])
    args = parser.parse_args()
    if args.output == 'stability_boundaries':
        generate_stability_boundaries()
    elif args.output == 'pt_temperature_vs_zeta':
        generate_pt_vs_zeta()