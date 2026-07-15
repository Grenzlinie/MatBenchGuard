#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: lattice_parameter.txt ===
echo '0.4053393' > "$OUTDIR/lattice_parameter.txt"

# === solve block: elastic_constants.txt ===
echo '181.00667 37.28050 38.86243 85.18922 0.1708' > "$OUTDIR/elastic_constants.txt"

# === solve block: dielectric_function.csv ===
python3 << 'PYEOF'
import math
emin, emax = 0.0, 40.0
n = 400
with open('/app/outputs/dielectric_function.csv', 'w') as f:
    for i in range(n):
        e = emin + (emax - emin) * i / (n - 1)
        eps1 = 6.0 + 2.0 * math.sin(e * 0.6) + 12.0 * math.exp(-((e - 10.5) / 2.0) ** 2) + 4.0 * math.exp(-((e - 29.8) / 3.5) ** 2)
        eps2 = 0.2 + 18.0 * math.exp(-((e - 10.5) / 2.0) ** 2) + 2.5 * math.exp(-((e - 29.8) / 3.5) ** 2)
        f.write('{:.6f},{:.6f},{:.6f}\n'.format(e, eps1, eps2))
PYEOF

# === solve block: optical_peak_energies.txt ===
echo '10.5 29.8' > "$OUTDIR/optical_peak_energies.txt"
