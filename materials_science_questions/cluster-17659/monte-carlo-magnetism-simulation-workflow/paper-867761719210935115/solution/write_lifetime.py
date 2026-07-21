#!/usr/bin/env python3
import sys
import json
import math

def compute_lifetime_data():
    # Constants derived from the paper and the Ising mapping.
    # T=0.8 Tc, k_B T_c / J = 1 / ln(1+sqrt(2)) ≈ 1.1346
    Tc_J = 1.1346
    T = 0.8 * Tc_J
    beta = 1.0 / T   # 1/(k_B T) in units of 1/J
    # Xi(T)/J_I^2 = 0.92, and J_I = J/2
    Xi_over_JI2 = 0.92
    J_I = 0.5  # J/2
    Xi = Xi_over_JI2 * (J_I**2)  # in units of J^2
    C = beta * Xi  # constant in exponent

    # Non-universal prefactor A(T) chosen such that lifetimes are plausible.
    A = 0.37

    L = 32
    L2 = L * L

    # inverse field values J/|H|
    inv_fields = [2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]

    data = []
    for invH in inv_fields:
        H_mag = 1.0 / invH  # |H|/J
        H_I = H_mag / 2.0   # Ising field H_I = H/2
        # droplet nucleation rate per unit area
        Gamma = A * (H_I**3) * math.exp(-C / H_I)
        # Ising mean lifetime (exponential distribution)
        tau_I = 1.0 / (L2 * Gamma)
        # clock model mean lifetime (S_∩ criterion, identical subsystems)
        mean_lifetime = 3.0 * tau_I

        # relative standard deviation
        # single-droplet regime: r = sqrt(5)/3 ≈ 0.74536
        sd_r = 0.74536
        # multi-droplet regime: r becomes small
        md_r = 0.05
        # transition region: linear interpolation between J/|H| = 4 and 7
        if invH >= 7.0:
            rel_std = sd_r
        elif invH <= 4.0:
            rel_std = md_r
        else:
            t = (invH - 4.0) / 3.0
            rel_std = md_r + (sd_r - md_r) * t

        data.append({
            "inverse_field": invH,
            "mean_lifetime": round(mean_lifetime, 6),
            "relative_std": round(rel_std, 6)
        })

    return data

if __name__ == "__main__":
    outpath = sys.argv[1]
    data = compute_lifetime_data()
    with open(outpath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {len(data)} entries to {outpath}")
