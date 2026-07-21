#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: h_fe_defect_energies.json ===
cat > "$OUTDIR/h_fe_defect_energies.json" <<'FFEOF'
{
  "dissolution_energy_TET": 0.273,
  "dissolution_energy_OCT": 0.354,
  "surface_binding_QT": 0.241,
  "surface_binding_H": 0.191,
  "surface_binding_B": 0.222,
  "vacancy_segregation_n1": 0.319,
  "vacancy_segregation_n2": 0.330,
  "vacancy_segregation_n3": 0.263,
  "vacancy_segregation_n4": 0.160,
  "vacancy_segregation_n5": 0.144,
  "vacancy_segregation_n6": -0.033,
  "vacancy_segregation_n7": -0.474
}
FFEOF
