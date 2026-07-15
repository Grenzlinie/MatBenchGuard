#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "${OUTDIR}"

# === solve block: step_04_local_equilibria.json ===
# Write local equilibrium compositions
cat > "${OUTDIR}/step_04_local_equilibria.json" <<'FFEOF'
{
  "T450_c_gamma_at_pct": 79.0,
  "T550_c_gamma_at_pct": 76.0,
  "T605_c_gamma_LE1_at_pct": 24.49,
  "T605_c_gamma_LE2_at_pct": 73.95
}
FFEOF

# === solve block: step_05_energy_barrier.json ===
# Write energy barrier
cat > "${OUTDIR}/step_05_energy_barrier.json" <<'FFEOF'
{
  "barrier_J_per_mol": 18.65
}
FFEOF
