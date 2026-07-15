#!/usr/bin/env python3
"""Oracle artifact writer – no network, stdlib only."""
import sys
import math
import json

def write_flex_curve(path):
    """Synthetic stress-strain curve with small oscillations."""
    strain = []
    stress = []
    n = 400
    strain_max = 0.007
    for i in range(n):
        e = i * strain_max / (n - 1)
        if e <= 0.0025:
            s = (e / 0.0025) * 450.0   # elastic ramp
        else:
            s = 450.0 + 20.0 * math.sin(2 * math.pi * (e - 0.0025) / 0.0005) + 5.0 * math.sin(2 * math.pi * e / 0.0003)
        strain.append(e)
        stress.append(s)
    with open(path, 'w') as f:
        f.write("strain,stress_MPa\n")
        for e, s in zip(strain, stress):
            f.write(f"{e:.6f},{s:.3f}\n")

def write_static_enthalpy(path):
    # Reference NEB values from the paper
    data = [
        (0,   0.41),
        (200, 0.36),
        (400, 0.28),
        (600, 0.18),
        (800, 0.07),
        (1000,0.032),
    ]
    with open(path, 'w') as f:
        f.write("stress_MPa,enthalpy_eV\n")
        for stress, enthalpy in data:
            f.write(f"{stress},{enthalpy}\n")

def write_peierls(path):
    with open(path, 'w') as f:
        json.dump({"peierls_stress_MPa": 1600}, f)

def h_static(tau):
    """Piecewise linear interpolation of static enthalpy (eV) vs stress (MPa)."""
    points = [(0,0.41), (200,0.36), (400,0.28), (600,0.18), (800,0.07), (1000,0.032)]
    # extrapolation beyond 1000: assume linear to zero at ~1100?
    # but solver only uses inside range
    if tau <= points[0][0]:
        return points[0][1]
    for i in range(1, len(points)):
        if tau <= points[i][0]:
            t0, h0 = points[i-1]
            t1, h1 = points[i]
            return h0 + (h1 - h0) * (tau - t0) / (t1 - t0)
    # Extrapolate linearly to zero at 1100 MPa
    t_last, h_last = points[-1]
    return max(0, h_last + (0 - h_last) * (tau - t_last) / (1100 - t_last))

def write_dynamic_enthalpy(path):
    kB = 8.617333262145e-5   # eV/K
    nu_star = 2525.25         # ps^{-1}  (nu * L_Y / b)
    delta_tau = 30.0          # MPa
    tau_dot_0 = 0.525         # MPa/ps
    C = math.log(nu_star * delta_tau / tau_dot_0)  # ~11.88

    temps = [150, 200, 250]

    with open(path, 'w') as f:
        f.write("temperature_K,avg_jump_stress_MPa,enthalpy_eV\n")
        for T in temps:
            H_goal = kB * T * C
            # Bisection solve for tau: H_static(tau) = H_goal
            lo = 0.0
            hi = 1100.0
            for _ in range(50):
                mid = (lo + hi) / 2
                if h_static(mid) > H_goal:
                    lo = mid
                else:
                    hi = mid
            tau_opt = (lo + hi) / 2
            enthalpy_opt = h_static(tau_opt)
            f.write(f"{T},{tau_opt:.2f},{enthalpy_opt:.4f}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: generate_artifacts.py <mode> <output_file>")
    mode = sys.argv[1]
    output = sys.argv[2]
    if mode == "flex_curve":
        write_flex_curve(output)
    elif mode == "static_enthalpy":
        write_static_enthalpy(output)
    elif mode == "peierls":
        write_peierls(output)
    elif mode == "dynamic_enthalpy":
        write_dynamic_enthalpy(output)
    else:
        sys.exit(f"Unknown mode: {mode}")
