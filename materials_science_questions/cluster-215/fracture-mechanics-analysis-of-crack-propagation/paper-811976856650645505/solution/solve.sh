#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: supersaturation_results.json ===
mkdir -p /app/outputs
python3 -c '
import json, math

lambda_ = 1e-7
epsilon_dot = 1e-5
eta = 2
a_b = 5.81e-20
D = 1e-9
c0 = 3.4e21
L = 1e-7
r0 = 1e-9

S_smooth_iron = (lambda_ * epsilon_dot * eta) / (2 * math.pi * a_b * D * c0) * math.log(2*L/r0)

a_b_aus = 5.77e-20
D_aus = 1e-9
c0_aus = 2e19
S_smooth_aus = (lambda_ * epsilon_dot * eta) / (2 * math.pi * a_b_aus * D_aus * c0_aus) * math.log(2*L/r0)

v = 1e-5
R = 5e-5
epsilon_dot_crack = v / (2*R)
S_crack_iron = (lambda_ * epsilon_dot_crack * eta) / (2 * math.pi * a_b * D * c0) * math.log(4*L/r0)

S_internal_iron = (lambda_ * epsilon_dot * eta) / (2 * math.pi * a_b * D * c0) * math.log(L/r0)

out = {
    "smooth_iron": {
        "S": S_smooth_iron,
        "parameters": {
            "lambda": lambda_,
            "epsilon_dot": epsilon_dot,
            "eta": eta,
            "a_times_b": a_b,
            "D": D,
            "c0": c0,
            "L": L,
            "r0": r0
        }
    },
    "smooth_austenitic": {
        "S": S_smooth_aus,
        "parameters": {
            "lambda": lambda_,
            "epsilon_dot": epsilon_dot,
            "eta": eta,
            "a_times_b": a_b_aus,
            "D": D_aus,
            "c0": c0_aus,
            "L": L,
            "r0": r0
        }
    },
    "crack_iron": {
        "S": S_crack_iron,
        "parameters": {
            "lambda": lambda_,
            "epsilon_dot": epsilon_dot_crack,
            "eta": eta,
            "a_times_b": a_b,
            "D": D,
            "c0": c0,
            "L": L,
            "r0": r0,
            "crack_velocity": v,
            "plastic_zone_size": R
        }
    },
    "internal_iron": {
        "S": S_internal_iron,
        "parameters": {
            "lambda": lambda_,
            "epsilon_dot": epsilon_dot,
            "eta": eta,
            "a_times_b": a_b,
            "D": D,
            "c0": c0,
            "L": L,
            "r0": r0
        }
    }
}

with open("/app/outputs/supersaturation_results.json", "w") as f:
    json.dump(out, f, indent=2)
'
