#!/usr/bin/env python3
"""Compute tip deflection and blocking force for bimorph/unimorph actuators
according to the nonlinear analytical model (Yao et al.).
"""

import sys
import json
import math

def compute(actuator_type):
    # Fixed parameters (all in SI units)
    L = 0.04          # length (m)
    b = 0.007         # width (m)
    Ep = 60.6e9       # Young's modulus of PZT (Pa)
    d31 = -274e-12    # piezoelectric coefficient (C/N)
    d311 = 2.85e-17   # electroelastic coefficient (m^3/(N·V))
    m31p = -3.70e-16  # effective electrostrictive coefficient (m^2/V^2)

    # Electric field values: 0 to 1e6 V/m, step 5e4 V/m
    Ez_vals = []
    v = 0.0
    while v <= 1e6 + 1e-9:
        Ez_vals.append(v)
        v += 5e4

    results = []

    if actuator_type == 'bimorph':
        tp = 0.5e-3          # each PZT plate thickness (m)
        t = 2.0 * tp         # total thickness = 0.001 m
        factor_delta = 3.0 * L**2 / (2.0 * t)
        factor_force = 3.0 * b * t**2 * Ep / (8.0 * L)
        for Ez in Ez_vals:
            corr = 1.0 + d311 * Ez * Ep
            delta = factor_delta * corr * d31 * Ez
            fbl = factor_force * corr * d31 * Ez
            results.append({
                "electric_field": Ez,
                "tip_deflection": abs(delta),
                "blocking_force": abs(fbl)
            })

    elif actuator_type == 'unimorph':
        tp = 0.68e-3          # PZT plate thickness (m)
        tm = 0.38e-3          # stainless steel substrate thickness (m)
        t = tp + tm           # total thickness = 1.06e-3 m
        Em = 210e9            # Young's modulus of steel
        A = Em / Ep
        B = tm / tp           # thickness ratio as defined in the paper

        AB = A * B
        B2 = B ** 2
        B3 = B ** 3
        B4 = B ** 4
        A2 = A ** 2

        factor_delta_outer = 3.0 * L**2 / t
        factor_force_outer = 3.0 * b * t**2 * Ep / (4.0 * L)

        for Ez in Ez_vals:
            if Ez == 0.0:
                results.append({
                    "electric_field": 0.0,
                    "tip_deflection": 0.0,
                    "blocking_force": 0.0
                })
                continue

            common_term = d31 * Ez + 0.5 * m31p * Ez**2
            corr = 1.0 + d311 * Ez * Ep
            corr2 = corr ** 2

            # Δ (Delta) from Eq. (40)
            term1 = 1.0 + A2 * B4
            term2 = 2.0 * A * (2.0*B + 3.0*B2 + 2.0*B3) * corr
            term3 = A2 * B4 * d311 * Ez * Ep * (2.0 + d311 * Ez * Ep)
            Delta = term1 + term2 + term3

            # Tip deflection
            num_delta = AB * (1.0 + B)**2 * corr2 * common_term
            delta = factor_delta_outer * num_delta / Delta

            # Blocking force
            num_fbl = AB * (1.0 + A2 * B4 + 2.0 * A * (2.0*B + 3.0*B2 + 2.0*B3)) * corr2 * common_term
            den_fbl = (1.0 + B) * (1.0 + AB) * Delta
            fbl = factor_force_outer * num_fbl / den_fbl

            results.append({
                "electric_field": Ez,
                "tip_deflection": abs(delta),
                "blocking_force": abs(fbl)
            })
    else:
        raise ValueError("Unknown actuator type: %s" % actuator_type)

    return results

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python gen_outputs.py <bimorph|unimorph> <output_path>\n")
        sys.exit(1)
    act_type = sys.argv[1].lower()
    out_path = sys.argv[2]
    data = compute(act_type)
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2)
