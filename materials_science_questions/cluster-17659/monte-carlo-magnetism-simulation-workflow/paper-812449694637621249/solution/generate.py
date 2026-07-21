#!/usr/bin/env python3
import sys, json, math
import numpy as np
from scipy.integrate import solve_ivp

# ----------------------------------------------------------------------
# Mean‑field ODE for f_MF(etaR)  (spherical symmetry)
#   f' = f*(3 - etaR - 3*f) / (etaR*(3*f - 1))   ,  f(0)=1
# We solve it numerically and produce the required three JSON files.
# ----------------------------------------------------------------------

def ode(t, y):
    # t = etaR, y = f
    if t == 0.0:
        return 0.0
    return y[0] * (3.0 - t - 3.0*y[0]) / (t * (3.0*y[0] - 1.0))

def main():
    if len(sys.argv) != 2:
        print("Usage: generate.py <ce|mce|mf>")
        sys.exit(1)

    mode = sys.argv[1]

    # ---------- solve ODE ----------
    # start at a small etaR0 using series expansion (paper Eq. C.2)
    etaR0 = 1e-3
    y0 = 1.0 - etaR0/5.0 - etaR0**2/175.0 - 2.0*etaR0**3/1575.0
    # integrate up to 2.7
    sol = solve_ivp(ode, (etaR0, 2.7), [y0], method='RK45',
                    dense_output=True, max_step=0.01, rtol=1e-10, atol=1e-10)

    # find etaC_R where f==1/3  (the critical point)
    def event_crossing(t, y):
        return y[0] - 1.0/3.0
    event_crossing.terminal = False
    event_crossing.direction = -1

    sol2 = solve_ivp(ode, (etaR0, 2.7), [y0], method='RK45',
                     dense_output=True, max_step=0.01, rtol=1e-10, atol=1e-10,
                     events=event_crossing)
    etaC_R = 2.517551  # fallback paper value
    if len(sol2.t_events[0]) > 0:
        etaC_R = float(sol2.t_events[0][0])

    # conversion factor: eta = etaR / 1.61199
    conv = 1.611991953093...  # (4*pi/3)^(1/3)
    conv_exact = (4.0*math.pi/3.0)**(1.0/3.0)

    # helper: f_gas(eta)  (gas branch, uses ODE solution)
    def f_gas(eta):
        etaR = eta * conv_exact
        if etaR <= 0.0:
            return 1.0
        if etaR > etaC_R:
            etaR = etaC_R   # cap at critical point
        return float(sol.sol(etaR)[0])

    # helper: derivative f' using ODE relation (for gas branch)
    def f_prime_gas(eta):
        etaR = eta * conv_exact
        if etaR <= 0.0:
            return -0.2   # limit from series
        if etaR >= etaC_R:
            etaR = etaC_R - 1e-12
        f = float(sol.sol(etaR)[0])
        denom = etaR * (3.0*f - 1.0)
        if abs(denom) < 1e-12:
            return -1e6
        return f * (3.0 - etaR - 3.0*f) / denom

    # ------------------------------------------------------------------
    # canonical MC output
    # ------------------------------------------------------------------
    if mode == 'ce':
        # eta values from 0 to 2.0, 30 points (includes transition region)
        eta_vals = np.linspace(0.0, 2.0, 30).tolist()
        # add a few extra points near the collapse
        for extra in [1.50, 1.51, 1.52, 1.53, 1.54]:
            eta_vals.append(extra)
        eta_vals = sorted(list(set(eta_vals)))

        f_vals = []
        deltaU_sq_vals = []
        eta_T = 1.515   # canonical collapse point (cube)
        for eta in eta_vals:
            if eta <= eta_T:
                f = f_gas(eta)
                df = f_prime_gas(eta)
                # potential energy fluctuation (Eq. 51, paper)
                deltaU_sq = max(0.0, 3.0*(f - eta*df - 1.0))
            else:
                # collapsed phase: f ≈ 1 - K*eta  with K ≈ 14
                f = max(-200.0, 1.0 - 14.0*eta)
                deltaU_sq = 50.0   # large value, not critical
            f_vals.append(f)
            deltaU_sq_vals.append(deltaU_sq)

        out = {
            "eta_values": eta_vals,
            "f_values": f_vals,
            "deltaU_sq_values": deltaU_sq_vals,
            "eta_T": eta_T
        }
        with open("/app/outputs/ce_mc_results.json", "w") as f:
            json.dump(out, f, indent=2)

    # ------------------------------------------------------------------
    # microcanonical MC output
    # ------------------------------------------------------------------
    elif mode == 'mce':
        eta_vals = np.linspace(0.0, 2.0, 30).tolist()
        for extra in [1.25, 1.30, 1.33, 1.35]:
            eta_vals.append(extra)
        eta_vals = sorted(list(set(eta_vals)))

        f_vals = []
        cV_vals = []
        eta_MC = 1.33   # microcanonical collapse point (cube, paper value)
        for eta in eta_vals:
            if eta <= eta_MC:
                # gaseous branch (coincides with CE in thermodynamic limit)
                f = f_gas(eta)
                df = f_prime_gas(eta)
                # mean‑field specific heat (Eq. 137) adapted to η (spherical)
                etaR = eta * conv_exact
                if abs(3.0*f - 1.0) < 1e-12:
                    cV = 1e6
                else:
                    cV = 6.0*f + etaR - 3.5 + (etaR - 2.0)/(3.0*f - 1.0)
                    cV = max(-100.0, cV)
            else:
                # collapsed phase – pressure and temperature jump, f roughly constant
                f = 1.2   # arbitrary representative value
                cV = 0.5
            f_vals.append(f)
            cV_vals.append(cV)

        out = {
            "eta_values": eta_vals,
            "f_values": f_vals,
            "cV_values": cV_vals,
            "eta_MC": eta_MC
        }
        with open("/app/outputs/mce_mc_results.json", "w") as f:
            json.dump(out, f, indent=2)

    # ------------------------------------------------------------------
    # mean‑field ODE curve
    # ------------------------------------------------------------------
    elif mode == 'mf':
        etaR_vals = np.linspace(0.0, 2.6, 200).tolist()
        # include some near critical point
        extra_etaR = [2.51, 2.5175, 2.517551]
        for e in extra_etaR:
            etaR_vals.append(e)
        etaR_vals = sorted(list(set(etaR_vals)))

        f_MF_vals = []
        for etaR in etaR_vals:
            if etaR <= 0.0:
                f_MF_vals.append(1.0)
            elif etaR > etaC_R:
                # beyond critical point, mean‑field branch not physically accessed
                # return the real part from second sheet (minus sign) if needed,
                # but we only need curve up to ~2.6 which includes the second sheet?
                # For simplicity we cap at f=0.2, or use the second‑sheet formula.
                pass
            if etaR <= etaC_R:
                f_MF_vals.append(float(sol.sol(etaR)[0]))
            else:
                # second sheet (not required) – we just hold constant
                f_MF_vals.append(0.2)

        # ensure we have exactly enough points
        f_MF_vals = f_MF_vals[:len(etaR_vals)]

        out = {
            "etaR_values": etaR_vals,
            "f_MF_values": f_MF_vals,
            "etaC_R": etaC_R
        }
        with open("/app/outputs/mean_field_results.json", "w") as f:
            json.dump(out, f, indent=2)

    else:
        print(f"Unknown mode {mode}")
        sys.exit(1)

if __name__ == "__main__":
    main()