#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermo_optic_coefficients.json ===
cat <<'PYEOF' | python3
import json

pts = {
    "MoO3": [(295.0, 2.1255, 0.00440), (333.0, 2.1052, 0.00518), (373.0, 2.0642, 0.00332)],
    "H0.134MoO3": [(296.0, 1.9215, 0.12940), (333.0, 1.9207, 0.12944), (373.0, 1.9164, 0.14336)],
    "Li0.42MoO3": [(296.0, 1.8485, 0.26045), (333.0, 1.8514, 0.26299), (373.0, 1.8520, 0.26404)]
}

result = []
for mat, points in pts.items():
    dndT, dkdT = [], []
    for i in range(len(points)-1):
        t1, n1, k1 = points[i]
        t2, n2, k2 = points[i+1]
        dt = t2 - t1
        dndT.append((n2-n1)/dt)
        dkdT.append((k2-k1)/dt)
    result.append({
        "material": mat,
        "temperature_range": "high",
        "cycle": "heating",
        "dn_dT_min": min(dndT),
        "dn_dT_max": max(dndT),
        "dk_dT_min": min(dkdT),
        "dk_dT_max": max(dkdT)
    })

with open("/app/outputs/thermo_optic_coefficients.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF

# === solve block: density_polarizability.json ===
cat <<'PYEOF' | python3
import json

rows = [
    ("MoO3", 295.0, 2.1255),
    ("MoO3", 333.0, 2.1052),
    ("MoO3", 373.0, 2.0642),
    ("MoO3", 333.0, 2.0251),
    ("MoO3", 297.0, 2.0365),
    ("H0.134MoO3", 296.0, 1.9215),
    ("H0.134MoO3", 333.0, 1.9207),
    ("H0.134MoO3", 373.0, 1.9164),
    ("H0.134MoO3", 298.0, 1.9093),
    ("Li0.42MoO3", 296.0, 1.8485),
    ("Li0.42MoO3", 333.0, 1.8514),
    ("Li0.42MoO3", 373.0, 1.8520),
    ("Li0.42MoO3", 296.0, 1.8524)
]

out = []
for material, T, n in rows:
    r = (n*n - 1.0) / (n*n + 2.0)
    rho = 6.96 * r
    # alpha from paper Eq.10 with physical constant 5.711e-23 (3M/(4π N_A))
    # simplifies to 5.711e-23 / 6.96 because r/rho = 1/6.96
    alpha = 5.711e-23 / 6.96
    out.append({
        "material": material,
        "temperature_K": T,
        "density_g_per_cm3": rho,
        "polarizability_cm3": alpha
    })

with open("/app/outputs/density_polarizability.json", "w") as f:
    json.dump(out, f, indent=2)
PYEOF
