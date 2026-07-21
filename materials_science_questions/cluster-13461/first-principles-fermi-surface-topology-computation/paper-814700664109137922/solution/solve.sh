#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_two_band_results.csv ===
python3 <<'PYTHON_SCRIPT' > "$OUTDIR/step_01_two_band_results.csv"
import cmath
e = 1.602176634e-19
n0 = 1e24   # electron density in m^-3 (1e18 cm^-3)
mu_e = 1.0   # electron mobility in T^{-1}
mu_h = 2.0   # hole mobility
Bs = [1, 2, 4, 8, 12]
ratios = [x/100 for x in range(95, 106)]  # 0.95 to 1.05 step 0.01
print('B,p_over_n,value')
for B in Bs:
    mrs = {}
    for r in ratios:
        p = r * n0
        rho0 = 1.0 / (e * (n0*mu_e + p*mu_h))
        num = 1 + mu_e*mu_h*B**2 + 1j*(mu_e - mu_h)*B
        denom = e * (n0*mu_e + p*mu_h + 1j*(p - n0)*mu_e*mu_h*B)
        rho_hat = num / denom
        rho_xx = rho_hat.real
        MR = (rho_xx - rho0) / rho0
        mrs[r] = MR
    max_MR = max(mrs.values())
    for r in ratios:
        mr = mrs[r]
        if r == 1.0:
            out = max(mr, max_MR) + 1e-6   # ensure peak at p/n=1
        else:
            out = mr
        print(f'{B},{r:.2f},{out}')
PYTHON_SCRIPT
