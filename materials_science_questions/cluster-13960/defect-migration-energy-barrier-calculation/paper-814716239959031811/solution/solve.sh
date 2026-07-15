#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > /app/outputs/dft_results.json <<'FFEOF'
{
  "interface_single_vacancy_formation_energy": -0.30,
  "interface_double_vacancy_formation_energy": 0.22,
  "bulk_single_vacancy_formation_energy": 0.30,
  "bulk_double_vacancy_formation_energy": 0.50,
  "migration_barriers_CeO2": [0.09, 0.17]
}
FFEOF
