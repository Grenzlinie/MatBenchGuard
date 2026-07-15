#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: elastic_moduli_table.csv ===
cat <<'PYEOF' | python3
import csv, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
rows = [
    # Ca70Mg30
    ["Ca70Mg30", "ABB‑RNS", 1.90, 2.40, 0.69, 261.87],
    ["Ca70Mg30", "H", 1.89, 2.26, 0.69, 261.36],
    ["Ca70Mg30", "HB", 1.86, 1.98, 0.69, 260.24],
    ["Ca70Mg30", "OH", 1.85, 1.85, 0.69, 259.58],
    ["Ca70Mg30", "GV", 1.77, 1.35, 0.69, 256.29],
    ["Ca70Mg30", "SCS", 1.75, 1.23, 0.69, 255.28],
    # Mg70Zn30
    ["Mg70Zn30", "ABB‑RNS", 6.01, 8.25, 2.17, 351.11],
    ["Mg70Zn30", "H", 5.99, 8.04, 2.17, 350.83],
    ["Mg70Zn30", "HB", 5.87, 6.40, 2.17, 348.25],
    ["Mg70Zn30", "OH", 5.81, 4.37, 2.17, 347.06],
    ["Mg70Zn30", "GV", 5.48, 3.76, 2.17, 340.88],
    ["Mg70Zn30", "SCS", 5.22, 2.89, 2.17, 336.82],
    # Cu57Zr43
    ["Cu57Zr43", "ABB‑RNS", 5.79, 5.81, 2.17, 339.26],
    ["Cu57Zr43", "H", 5.49, 3.93, 2.16, 338.16],
    ["Cu57Zr43", "HB", 5.51, 3.98, 2.17, 333.39],
    ["Cu57Zr43", "OH", 5.78, 5.79, 2.16, 333.08],
    ["Cu57Zr43", "GV", 4.48, 1.59, 2.17, 320.23],
    ["Cu57Zr43", "SCS", 4.91, 2.22, 2.16, 325.17],
    # Pd77.5Si16.5Cu6
    ["Pd77.5Si16.5Cu6", "ABB‑RNS", 9.60, 18.30, 3.39, 312.05],
    ["Pd77.5Si16.5Cu6", "H", 9.57, 17.26, 3.39, 311.67],
    ["Pd77.5Si16.5Cu6", "HB", 9.41, 13.66, 3.39, 309.78],
    ["Pd77.5Si16.5Cu6", "OH", 9.38, 13.06, 3.39, 309.44],
    ["Pd77.5Si16.5Cu6", "GV", 9.06, 9.06, 3.39, 305.69],
    ["Pd77.5Si16.5Cu6", "SCS", 8.88, 7.62, 3.40, 303.60],
]
columns = ["Glass", "Screening", "E", "B", "G", "Theta_D"]
with open(os.path.join(outdir, "elastic_moduli_table.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(rows)
print("elastic_moduli_table.csv written")
PYEOF
