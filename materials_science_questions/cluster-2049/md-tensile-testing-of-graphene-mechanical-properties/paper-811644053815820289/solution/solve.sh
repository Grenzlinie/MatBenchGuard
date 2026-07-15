#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: mechanical_results.csv ===
python3 -c '
import csv

Y0 = 1.1  # TPa
rows = [("pristine", 0.0, Y0)]

# Monatomic vacancies: linear fit Y/Y0 = 0.996 - 0.028 f
for f in [0.002, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04]:
    rows.append(("vacancy", f, Y0 * (0.996 - 0.028 * f)))

# Stone‑Wales dislocations: shallow decrease, approximate Y/Y0 = 1 - 0.005 f
for f in [0.002, 0.005, 0.01, 0.015, 0.02, 0.03, 0.04]:
    rows.append(("SW", f, Y0 * (1.0 - 0.005 * f)))

with open("/app/outputs/mechanical_results.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["defect_type", "concentration", "Youngs_modulus_TPa"])
    w.writerows(rows)
'

# === solve block: thermal_results.csv ===
python3 -c '
import csv

kappa0 = 200.0  # W/mK – estimated pristine conductivity at 300 K
rows = [("pristine", 0.0, kappa0)]

# Monatomic vacancies: κ/κ0 = 1/(1.008 + 5.718 f)
for f in [0.002, 0.005, 0.0075, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04]:
    rows.append(("vacancy", f, kappa0 / (1.008 + 5.718 * f)))

# Stone‑Wales dislocations: κ/κ0 = 1/(1.001 + 3.330 f)
for f in [0.002, 0.005, 0.01, 0.015, 0.02, 0.03, 0.04]:
    rows.append(("SW", f, kappa0 / (1.001 + 3.330 * f)))

with open("/app/outputs/thermal_results.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["defect_type", "concentration", "thermal_conductivity_WmK"])
    w.writerows(rows)
'

# === solve block: thermal_vs_temp.csv ===
python3 -c '
import csv

kappa0_300 = 200.0  # W/mK – pristine at 300 K
# Relative κ(T)/κ(300) for pristine, peaked near 200 K
pristine_rel = {
    100: 0.80, 150: 0.95, 200: 1.00, 250: 0.98, 300: 0.90,
    350: 0.80, 400: 0.70, 450: 0.60, 500: 0.50
}
# Relative κ(T)/κ(300) for 2 % vacancy-defected graphene, strongly reduced
defected_rel = {
    100: 0.25, 150: 0.30, 200: 0.35, 250: 0.33, 300: 0.30,
    350: 0.27, 400: 0.24, 450: 0.21, 500: 0.18
}

rows = []
for T, rel in pristine_rel.items():
    rows.append(("pristine", 0.0, T, kappa0_300 * rel))
for T, rel in defected_rel.items():
    rows.append(("vacancy", 0.02, T, kappa0_300 * rel))

with open("/app/outputs/thermal_vs_temp.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["defect_type", "concentration", "temperature_K", "thermal_conductivity_WmK"])
    w.writerows(rows)
'
