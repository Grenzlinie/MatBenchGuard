#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bulk_hBN_zone_center.json ===
cat > "${OUTDIR}/bulk_hBN_zone_center.json" <<'JSONEOF'
{
  "E1u_TO": 1367,
  "E1u_LO": 1612,
  "E2g_symmetric_inplane": 1366,
  "A2u_TO": 758,
  "A2u_LO": 819,
  "B1g_anti_outplane": 819,
  "B1g_sym_inphase_outplane": 100,
  "E2g_sym_inphase_inplane": 43
}
JSONEOF

# === solve block: RBM_frequencies.csv ===
python3 << 'PYEOF' > "${OUTDIR}/RBM_frequencies.csv"
import csv, math, sys

a_bn = 1.44  # B–N bond length in Angstrom
# radius R = sqrt(3*(n^2 + n*m + m^2)) * a / (2*pi)
def radius(n, m):
    return math.sqrt(3*(n*n + n*m + m*m)) * a_bn / (2*math.pi)

writer = csv.writer(sys.stdout)
writer.writerow(["radius_angstrom","rbm_freq_cm⁻¹"])
for n in range(1, 51):
    for m in range(0, n+1):
        r = radius(n, m)
        if 5.0 <= r <= 25.0:
            f = 851.0 / r
            writer.writerow([f"{r:.4f}", f"{f:.4f}"])
PYEOF

# === solve block: tube_10_10_raman_active.json ===
cat > "${OUTDIR}/tube_10_10_raman_active.json" <<'JSONEOF'
{
  "E2g_high": 1457,
  "E1_high": 1419
}
JSONEOF
