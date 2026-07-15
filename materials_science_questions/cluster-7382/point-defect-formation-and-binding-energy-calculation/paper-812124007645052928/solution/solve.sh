#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: vacancy_complex_results.json ===
python3 <<'PYEOF'
import json, math

c0 = 0.02
u0 = 6.0
dw = -3.0
z = 12
temps = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]

def compute_res(T):
    cv = math.exp(-u0 / T)
    # exp(-Δw/T) with Δw=-3 → exp(3/T)
    exp_neg_dw_T = math.exp(-dw / T)
    A = z * math.exp(-(u0 + dw) / T)   # u0+dw = 3
    B = c0 * exp_neg_dw_T

    # Solve for x = exp(-λ₁/T) in (0, 1] via bisection
    def f(x):
        term = (1.0 + B * x) ** (z - 1)
        rhs = 1.0 + A * term
        if x == 0.0:
            return float('inf')
        return 1.0 / x - rhs

    lo = 1e-30
    hi = 1.0
    f_lo = f(lo)
    f_hi = f(hi)
    for _ in range(100):
        mid = (lo + hi) / 2.0
        f_mid = f(mid)
        if f_mid == 0.0 or (hi - lo) < 1e-16 * mid:
            break
        if f_lo * f_mid < 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    x = (lo + hi) / 2.0

    c_4He_ratio = x
    c_bar = ((1.0 + c0 * x * exp_neg_dw_T) ** z) * cv
    return c_4He_ratio, c_bar

results = []
for T in temps:
    c4h_r, c_b = compute_res(T)
    results.append({
        "temperature_K": T,
        "c_4He_ratio": float(c4h_r),
        "c_bar": float(c_b)
    })

output = {
    "parameters": {
        "c0": c0,
        "u0_K": u0,
        "delta_w_K": dw,
        "z": int(z)
    },
    "results": results
}

with open("/app/outputs/vacancy_complex_results.json", "w") as f:
    json.dump(output, f, indent=2)
PYEOF
