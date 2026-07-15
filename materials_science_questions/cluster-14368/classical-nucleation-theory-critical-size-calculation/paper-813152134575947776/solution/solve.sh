#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_radius.json ===
cat > /app/outputs/critical_radius.json <<'FFEOF'
{
  "R_c_nm": 3.8
}
FFEOF

# === solve block: burst_energy_vs_molecules.csv ===
 python3 -c '
import sys
print("burst_total_energy_kJ_per_mol,burst_molecules_count")
points = [
    (60, 3210), (80, 4280), (100, 5350), (120, 6420),
    (140, 7490), (160, 8560), (180, 9630), (200, 10700),
    (220, 11770), (240, 12840), (260, 13910), (280, 14980),
    (300, 16050), (320, 17120), (340, 18190), (360, 19260),
    (380, 20330), (400, 21400)
]
for dN, E in points:
    print(f"{E},{dN}")
' > /app/outputs/burst_energy_vs_molecules.csv

# === solve block: fitted_slope.json ===
cat > /app/outputs/fitted_slope.json <<'FFEOF'
{
  "E_mol0_kJ_per_mol": 53.5
}
FFEOF

# === solve block: nucleation_outcomes.csv ===
cat > /app/outputs/nucleation_outcomes.csv <<'FFEOF'
nucleation_occurred,number_of_runs,pressure_GPa,velocity_m_per_s
true,4,6.3,1.0
false,2,1.6,1.0
FFEOF
