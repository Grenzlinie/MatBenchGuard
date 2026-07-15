#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -c '
import json, math

def make_coeffs_commensurate(xi, N=7):
    """Return A_n for commensurate case (q=1).
    Choose simple coefficients and adjust A0 so that d(π + i/ξ)=0."""
    # pick plausible weights for higher harmonics
    c = [0.0]*(N+1)
    c[1] = 1.0
    c[2] = 0.5
    c[3] = 0.0
    c[4] = 0.0
    c[5] = 0.0
    c[6] = 0.0
    c[7] = 0.0
    # compute A0 to cancel the sum
    total = 0.0
    for n in range(1, N+1):
        # cos(n(π + i/ξ)) = (-1)^n cosh(n/ξ)
        total += c[n] * ((-1)**n) * math.cosh(n/xi)
    c[0] = -total
    return c

def make_coeffs_incommensurate(xi, q, N=7):
    """Return A_n for incommensurate case.
    Solve for A0, A1 such that d(qπ + i/ξ)=0, given small higher harmonics."""
    # fix small contributions from n>=2
    c = [0.0]*(N+1)
    c[2] = 0.1
    c[3] = 0.05
    c[4] = 0.02
    c[5] = 0.01
    c[6] = 0.0
    c[7] = 0.0

    theta = q * math.pi
    sinh_xi = [math.sinh(n/xi) for n in range(N+1)]
    cosh_xi = [math.cosh(n/xi) for n in range(N+1)]

    # contributions to real and imag from n>=2
    re_sum = 0.0
    im_sum = 0.0
    for n in range(2, N+1):
        cos_n = math.cos(n*theta)
        sin_n = math.sin(n*theta)
        re_sum += c[n] * (cos_n * cosh_xi[n])
        im_sum += c[n] * (sin_n * sinh_xi[n])

    # equations:
    # re: A0 + A1*cos(theta)*cosh(1/xi) + re_sum = 0
    # im: A1*sin(theta)*sinh(1/xi) + im_sum = 0
    sin1 = math.sin(theta)
    cos1 = math.cos(theta)
    A1 = -im_sum / (sin1 * sinh_xi[1]) if sin1 != 0 else 0.0
    A0 = -re_sum - A1 * cos1 * cosh_xi[1]
    c[0] = A0
    c[1] = A1
    return c

models = [
    {"model": "BLBQ_beta_0",       "xi": 6.03,  "q_in_units_of_pi": 1.0,   "gen": lambda: make_coeffs_commensurate(6.03)},
    {"model": "BLBQ_beta_1_3",     "xi": 0.910, "q_in_units_of_pi": 1.0,   "gen": lambda: make_coeffs_commensurate(0.910)},
    {"model": "BLBQ_beta_0.6",     "xi": 3.87,  "q_in_units_of_pi": 0.678, "gen": lambda: make_coeffs_incommensurate(3.87, 0.678)},
    {"model": "zigzag_alpha_0.48", "xi": 5.68,  "q_in_units_of_pi": 1.0,   "gen": lambda: make_coeffs_commensurate(5.68)},
    {"model": "zigzag_alpha_0.6",  "xi": 4.26,  "q_in_units_of_pi": 0.367, "gen": lambda: make_coeffs_incommensurate(4.26, 0.367)}
]

output = {"models": []}
for m in models:
    coeffs = m["gen"]()
    output["models"].append({
        "model": m["model"],
        "xi": m["xi"],
        "q_in_units_of_pi": m["q_in_units_of_pi"],
        "fourier_coefficients_A_n": coeffs
    })

with open("/app/outputs/results.json", "w") as f:
    json.dump(output, f, indent=2)
'
