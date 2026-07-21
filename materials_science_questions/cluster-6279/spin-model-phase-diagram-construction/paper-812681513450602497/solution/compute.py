#!/usr/bin/env python3
"""Reference oracle for the decorated Ising lattice task.
Computes the exact thermodynamic functions from the analytic formulas.
Usage: compute.py --step {step_01,step_02,step_03} --output <path>
"""

import sys
import argparse
import numpy as np
from scipy.integrate import dblquad, quad

# ============================================================
#  Step 01: Multiple‑transition regime (general double integral)
#  Parameters: J_xd=J_yd=-1, J_x=-0.8, J_y=-3, d_x=d_y=1
#  Temperature range 0.1 – 10, ~2000 points
# ============================================================
def compute_step_01(output_file):
    Jxd = -1.0
    Jyd = -1.0
    Jx = -0.8
    Jy = -3.0
    dx = 1
    dy = 1
    N0 = 1 + dx + dy   # = 3, per unit cell

    # Temperature grid
    T_min, T_max, n_pts = 0.1, 10.0, 2000
    Ts = np.linspace(T_min, T_max, n_pts)

    # Helper functions for the double integral (one temperature)
    def D(Kd, d):
        ch = np.cosh(Kd)
        sh = np.sinh(Kd)
        return ch**(2*d+2) - sh**(2*d+2)

    def C(K, Kd, d):
        ch = np.cosh(Kd)
        sh = np.sinh(Kd)
        p = ch**(d+1) + sh**(d+1)
        m = ch**(d+1) - sh**(d+1)
        return 0.5 * np.exp(2*K) * p**2 + 0.5 * np.exp(-2*K) * m**2

    def S(K, Kd, d):
        ch = np.cosh(Kd)
        sh = np.sinh(Kd)
        p = ch**(d+1) + sh**(d+1)
        m = ch**(d+1) - sh**(d+1)
        return 0.5 * np.exp(2*K) * p**2 - 0.5 * np.exp(-2*K) * m**2

    def integrand(phi, theta, C1, C2, S1, S2, D1, D2):
        val = C1*C2 - S1*D2*np.cos(phi) - S2*D1*np.cos(theta)
        # Small positive floor to avoid log(<=0) due to numerical noise
        val = np.maximum(val, 1e-300)
        return np.log(val)

    # Pre‑compute ln_lambda for every temperature
    ln_lambda_vals = np.empty_like(Ts)
    for i, T in enumerate(Ts):
        Kx = Jx / T
        Ky = Jy / T
        Kxd = Jxd / T
        Kyd = Jyd / T

        D1 = D(Kxd, dx)
        D2 = D(Kyd, dy)
        C1 = C(Kx, Kxd, dx)
        C2 = C(Ky, Kyd, dy)
        S1 = S(Kx, Kxd, dx)
        S2 = S(Ky, Kyd, dy)

        # Double integral over [0, 2π]×[0, 2π]
        # Use scipy's dblquad; integration limits are [0,2π] for both angles.
        I, _ = dblquad(lambda t, p: integrand(p, t, C1, C2, S1, S2, D1, D2),
                       0, 2*np.pi,
                       lambda _: 0, lambda _: 2*np.pi,
                       epsabs=1e-8, epsrel=1e-8, limit=100)

        # Eq. (6): N0 * ln(λ/2) = I / (8π²)
        # => ln λ = I/(8π² N0) + ln(2)
        ln_lambda_vals[i] = I / (8 * np.pi**2 * N0) + np.log(2.0)

    # Thermodynamics: entropy S = ln λ + T * d(ln λ)/dT,
    # heat capacity C = T * dS/dT
    d_ln_dT = np.gradient(ln_lambda_vals, Ts)
    entropy = ln_lambda_vals + Ts * d_ln_dT
    heat_capacity = Ts * np.gradient(entropy, Ts)

    # Write CSV with columns: temperature, heat_capacity, entropy
    header = "temperature,heat_capacity,entropy"
    data = np.column_stack((Ts, heat_capacity, entropy))
    np.savetxt(output_file, data, delimiter=',', header=header, comments='', fmt='%.12g')
    print(f"[step_01] wrote {output_file}")


# ============================================================
#  Step 02: Isotropic singly‑decorated heat capacity
#  Parameters: J_x=J_y=0, d_x=d_y=1, J_xd=J_yd=1.0 (equal)
#  Temperature range 0.1 – 5, 2000 points
# ============================================================
def compute_step_02(output_file):
    Jd = 1.0
    N0 = 3  # single decoration => 1 + 1 + 1 = 3

    T_min, T_max, n_pts = 0.1, 5.0, 2000
    Ts = np.linspace(T_min, T_max, n_pts)

    def ln_lambda_isotropic(T):
        """ln λ per spin for the isotropic singly-decorated case, Eq. (10)."""
        Kd = Jd / T
        ch2 = np.cosh(2*Kd)
        # m parameter, Eq. (11)
        m = 2.0 * np.sinh(2*Kd) * np.sinh(4*Kd) / (ch2**2 + 1)**2

        # Integral term: (1/(6π)) * ∫₀^π ln[½(1 + √(1 - m² sin² φ))] dφ
        def integrand(phi, m_sq):
            # m_sq = m*m to avoid recomputing
            rad = 1.0 - m_sq * np.sin(phi)**2
            rad = np.maximum(rad, 0.0)   # safety for m>1 (roundoff)
            return np.log(0.5 * (1.0 + np.sqrt(rad)))

        I, _ = quad(integrand, 0, np.pi, args=(m*m,), limit=200, epsabs=1e-10, epsrel=1e-10)

        # Eq. (10): ln λ = (1/3) * [4(ch²2Kd + 1)] + I/(6π)
        result = (1.0/3.0) * (4.0 * (ch2**2 + 1.0)) + I / (6.0 * np.pi)
        return result

    # Pre‑compute ln_lambda
    ln_lambda_vals = np.array([ln_lambda_isotropic(T) for T in Ts])

    # Entropy and heat capacity via numerical differentiation
    d_ln_dT = np.gradient(ln_lambda_vals, Ts)
    entropy = ln_lambda_vals + Ts * d_ln_dT
    heat_capacity = Ts * np.gradient(entropy, Ts)

    # Write CSV: temperature, heat_capacity
    header = "temperature,heat_capacity"
    data = np.column_stack((Ts, heat_capacity))
    np.savetxt(output_file, data, delimiter=',', header=header, comments='', fmt='%.12g')
    print(f"[step_02] wrote {output_file}")


# ============================================================
#  Step 03: Isotropic critical temperature
# ============================================================
def compute_step_03(output_file):
    # Exact expression: T_c = 2 / arccosh(1+√2)
    val = 2.0 / np.arccosh(1.0 + np.sqrt(2.0))
    with open(output_file, 'w') as f:
        f.write(f"{val:.12g}\n")
    print(f"[step_03] wrote {output_file}")


# ============================================================
#  Main dispatch
# ============================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--step', required=True, choices=['step_01', 'step_02', 'step_03'])
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    if args.step == 'step_01':
        compute_step_01(args.output)
    elif args.step == 'step_02':
        compute_step_02(args.output)
    elif args.step == 'step_03':
        compute_step_03(args.output)
    else:
        raise ValueError(f"Unknown step {args.step}")
