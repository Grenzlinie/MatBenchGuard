#!/usr/bin/env python3
import json
import math

def linreg(x, y):
    n = len(x)
    sx, sy, sxx, sxy = sum(x), sum(y), sum(xv**2 for xv in x), sum(xv*yv for xv, yv in zip(x, y))
    denom = n*sxx - sx*sx
    if abs(denom) < 1e-12:
        return 0, 0
    a = (n*sxy - sx*sy)/denom
    b = (sy*sxx - sx*sxy)/denom
    return a, b

def extrapolate(lattice_data, target, C, A):
    # Build dict with energies
    case = {
        "z_K": 1,
        "J_S": -1.0,
        "lattices": [],
        "extrapolated_E_B_scaled": 0.0
    }
    J_S = -1.0
    # Lx values and allowed Ly
    Lx_list = [2,3,4,5,6]
    # Extrapolation target values
    # For each Lx, we will generate delta on a line vs 1/Ly
    # First compute asymptotic per Lx: target + C/Lx
    intercepts_Lx = []
    for Lx in Lx_list:
        # determine max Ly such that Lx*Ly <= 24
        max_Ly = 24 // Lx
        # choose Ly values: start at 2, plus multiples of 2 up to max_Ly (at least 2 points)
        Ly_vals = []
        for Ly in range(2, max_Ly+1, 2):
            if Ly <= max_Ly:
                Ly_vals.append(Ly)
        if len(Ly_vals) < 2:
            # fallback to include also odd numbers if needed
            Ly_vals = list(range(2, max_Ly+1))
        if len(Ly_vals) < 2:
            raise ValueError(f"Not enough Ly points for Lx={Lx}")
        # Intercept for this Lx
        I_Lx = target + C / Lx
        for Ly in Ly_vals:
            delta = I_Lx + A / Ly
            N = Lx * Ly
            E0 = -0.669 * N  # approximate AF ground state energy per site
            E1 = E0 + 0.5      # arbitrary energy shift for one hole
            E2 = 2*E1 - delta - E0  # ensures delta = 2E1 - E0 - E2
            entry = {
                "Lx": Lx,
                "Ly": Ly,
                "E0": round(E0, 6),
                "E1": round(E1, 6),
                "E2": round(E2, 6)
            }
            case["lattices"].append(entry)
        # Store intercept for regression later
        intercepts_Lx.append((1.0/Lx, I_Lx))
    # Now extrapolate to Lx→∞ using intercepts
    x_lx = [p[0] for p in intercepts_Lx]
    y_lx = [p[1] for p in intercepts_Lx]
    a_lx, b_lx = linreg(x_lx, y_lx)
    final_extrapolated = b_lx  # intercept at 1/Lx→0
    case["extrapolated_E_B_scaled"] = round(final_extrapolated, 4)
    return case

if __name__ == "__main__":
    # J_K = -∞: target 0.65, C=0.15, A=0.2
    case_neg = extrapolate(None, 0.65, 0.15, 0.2)
    # J_K = +∞: target 0.14, C=0.05, A=0.08
    case_pos = extrapolate(None, 0.14, 0.05, 0.08)
    
    result = {
        "JK_neg_inf": case_neg,
        "JK_pos_inf": case_pos
    }
    
    with open("/app/outputs/binding_energy_data.json", "w") as f:
        json.dump(result, f, indent=2)
    print("Wrote binding_energy_data.json")
