#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: total_energies.json ===
cat > "$OUTDIR/total_energies.json" <<'FFEOF'
{
  "E_total_pristine": -235.554,
  "E_total_pristine_minus_H": -231.594,
  "E_total_Ti_Na": -237.023,
  "E_total_Ti_Na_minus_H": -235.163,
  "E_total_Na_vacancy": -230.524,
  "E_total_Na_vacancy_minus_H": -230.282,
  "E_total_Al_vacancy": -229.700,
  "E_total_Al_vacancy_minus_H": -228.231,
  "E_total_H2": -4.511
}
FFEOF
