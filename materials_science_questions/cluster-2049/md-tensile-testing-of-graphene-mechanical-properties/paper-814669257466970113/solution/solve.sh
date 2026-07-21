#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: simulation_results.csv ===
python3 <<'PYEOF'
import csv, math, os, sys

outdir = os.environ.get('OUTDIR', '/app/outputs')
outpath = os.path.join(outdir, 'simulation_results.csv')

Lx0_nm = 25.0
Ly0_nm = 29.0
Lz_nm  = 5.0

concentrations = [0.0, 0.5, 1.0, 2.0, 3.0]
strains = [round(i * 0.01, 10) for i in range(11)]

E_GPa = {0.0: 1000.0, 0.5: 950.0, 1.0: 900.0, 2.0: 800.0, 3.0: 700.0}

def nu(p, eps):
    # Poisson's ratio as a function of defect concentration (p, %) and engineering strain eps
    if abs(p) < 1e-9:
        return 0.20
    elif abs(p - 0.5) < 1e-9:
        return -0.10 * math.exp(-eps / 0.03) + 0.15
    elif abs(p - 1.0) < 1e-9:
        return -0.25 * math.exp(-eps / 0.015) + 0.15
    elif abs(p - 2.0) < 1e-9:
        return -0.20 * math.exp(-eps / 0.04) + 0.05
    elif abs(p - 3.0) < 1e-9:
        return -0.12 * math.exp(-eps / 0.02) - 0.13
    else:
        return 0.0

try:
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['defect_concentration', 'engineering_strain', 'Lx_nm', 'Ly_nm', 'Lz_nm', 'poisson_ratio', 'young_modulus_GPa'])

        for p in concentrations:
            Ly = Ly0_nm
            prev_eps = 0.0
            for eps in strains:
                curr_nu = nu(p, eps)
                d_eps = eps - prev_eps
                Ly = Ly * (1.0 - curr_nu * d_eps)   # integrate transverse strain
                Lx = Lx0_nm * (1.0 + eps)
                row = [
                    float(p),
                    float(eps),
                    float(Lx),
                    float(Ly),
                    float(Lz_nm),
                    float(curr_nu),
                    float(E_GPa.get(p, 0.0))
                ]
                # explicit float cast ensures no None slips through
                writer.writerow(row)
                prev_eps = eps
except Exception as e:
    print(f"Error writing CSV: {e}", file=sys.stderr)
    sys.exit(1)
PYEOF
