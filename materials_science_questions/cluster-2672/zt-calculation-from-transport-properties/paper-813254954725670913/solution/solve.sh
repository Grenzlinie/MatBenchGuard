#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 <<'PYEOF'
import json, math

L = 2.45e-8
T = 1000

def kappa_a(A_bar):
    return 64.0 * (A_bar ** (-1.04))

materials = [
    ("Bi2Te3", 1800, 10, 160.152),
    ("CuI", 1.0, 755, 95.225),
    ("AgI", 0.05, 500, 117.385),
]

out = []
for name, sigma_cm, alpha_uV, Abar in materials:
    sigma_SI = sigma_cm * 100   # (Ω·cm)^-1 → S/m
    kappa_e = L * sigma_SI * T
    kappa_a_val = kappa_a(Abar)
    kappa_total = kappa_e + kappa_a_val
    alpha_V = alpha_uV * 1e-6
    ZT = (alpha_V ** 2 * sigma_SI * T) / kappa_total
    out.append({
        "material": name,
        "sigma": sigma_cm,
        "alpha": alpha_uV,
        "kappa_e": round(kappa_e, 6),
        "kappa_a": round(kappa_a_val, 6),
        "kappa_total": round(kappa_total, 6),
        "ZT": round(ZT, 6)
    })

with open("/app/outputs/results.json", "w") as f:
    json.dump(out, f, indent=2)
PYEOF
