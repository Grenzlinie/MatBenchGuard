#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: reduced_isotherm_data.csv ===
python3 << 'EOF'
import math, csv, os
OUTDIR = os.environ.get("OUTDIR", "/app/outputs")

params = {
    "Cu": (134.27, 6.0264, 3.7245, -4.9816, 14.720, 976),
    "Ta": (195.24, 3.7159, 8.0846, -64.854, 206.87, 1097),
    "Mo": (264.87, 4.7127, -8.1795, 83.532, -189.67, 1020),
    "Pt": (280.03, 6.3289, -1.3811, 61.492, -156.48, 660),
    "Au": (177.26, 6.3800, 1.9334, -1.0292, 33.941, 513),
}

def pressure(X, B0, eta, beta, xi, delta):
    a = 1 - X**(1/3)
    b = X**(2/3)
    exponent = eta*a + beta*a**2 + xi*a**3 + delta*a**4
    return 3*B0 * (a / b) * math.exp(exponent)

outpath = os.path.join(OUTDIR, "reduced_isotherm_data.csv")
with open(outpath, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["element", "reduced_volume_X", "pressure_GPa"])
    for elem, (B0, eta, beta, xi, delta, Pmax) in params.items():
        for i in range(200):
            X = 1.0 - (i/199)*(1.0 - 0.5)
            p = pressure(X, B0, eta, beta, xi, delta)
            if p > Pmax:
                break
            writer.writerow([elem, X, p])
EOF

# === solve block: reduced_isotherm_parameters.csv ===
python3 /solution/generate_csv.py params
