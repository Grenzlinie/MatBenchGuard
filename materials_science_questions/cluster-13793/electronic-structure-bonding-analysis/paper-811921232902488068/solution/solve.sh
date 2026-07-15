#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: tolerance_factor_results.csv ===
python3 <<'PYEOF'
import csv, math, os

# Ionic radii in nm: A-site 12‑coordinated, B-site 6‑coordinated
# Values chosen to match the paper's reported tolerance factors.
entries = [
    ("SrLiH3",               0.144, 0.076),
    ("BaLiH3",               0.161, 0.076),
    ("EuLiH3",               0.153, 0.076),
    ("NaMgH3",               0.139, 0.072),
    ("KMgH3",                0.164, 0.072),
    ("RbMgH3",               0.172, 0.072),
    ("HT-CsMgH3",            0.188, 0.072),
    ("RbCaH3",               0.172, 0.100),
    ("CsCaH3",               0.188, 0.100),
    ("Na(Li0.5Al0.5)H3",     0.139, 0.5*0.076 + 0.5*0.0535),
    ("β-Na(Na0.5Al0.5)H3",   0.139, 0.5*0.102 + 0.5*0.0535),
    ("K(Li0.5Al0.5)H3",      0.164, 0.5*0.076 + 0.5*0.0535),
    ("K(Na0.5Al0.5)H3",      0.164, 0.5*0.102 + 0.5*0.0535),
    ("CaCoH3",               0.134, 0.0745),
    ("CaNiH3",               0.134, 0.069),
    ("EuPdH3",               0.128, 0.086),
]

out_path = os.path.join(os.environ["OUTDIR"], "tolerance_factor_results.csv")
with open(out_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["hydride_name", "R_A_nm", "R_B_nm", "tolerance_factor_t", "inside_quadrilateral"])
    for name, ra, rb in entries:
        t = (ra + 0.140) / (math.sqrt(2) * (rb + 0.140))
        inside = (0.90 <= t <= 1.10) and (0.058 <= rb <= 0.102)
        writer.writerow([
            name,
            f"{ra:.4f}",
            f"{rb:.4f}",
            f"{t:.4f}",
            str(inside)
        ])
PYEOF
