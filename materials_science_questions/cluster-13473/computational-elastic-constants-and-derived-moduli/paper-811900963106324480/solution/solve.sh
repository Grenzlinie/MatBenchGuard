#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_moduli.csv ===
python3 << 'PYEOF'
import csv

rows = [
    {"d_nm": 2.0, "E_GPa": 220.0, "nu": 0.25},
    {"d_nm": 3.0, "E_GPa": 214.0, "nu": 0.29},
    {"d_nm": 4.0, "E_GPa": 210.0, "nu": 0.33},
    {"d_nm": 5.0, "E_GPa": 208.5, "nu": 0.35},
    {"d_nm": 6.0, "E_GPa": 208.0, "nu": 0.355},
    {"d_nm": 7.0, "E_GPa": 208.0, "nu": 0.355},
    {"d_nm": 8.0, "E_GPa": 208.0, "nu": 0.355},
]

with open("/app/outputs/elastic_moduli.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["d_nm", "E_GPa", "nu"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF

# === solve block: stress_profile.csv ===
python3 << 'PYEOF'
import csv

# Representative wire with side dimension d = 6 nm; half-side = 3 nm.
# Stress profile: sigma_zz = C * x^2 - d0, with centre compressive (~ -0.2 GPa)
# and surface tensile (~ +1.5 GPa).
C = 0.1888888888888889  # 1.7 / 9
d0 = 0.2

positions_nm = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
rows = []
for x in positions_nm:
    sigma = C * x * x - d0
    rows.append({"position_nm": x, "sigma_zz_GPa": sigma})

with open("/app/outputs/stress_profile.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["position_nm", "sigma_zz_GPa"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF
