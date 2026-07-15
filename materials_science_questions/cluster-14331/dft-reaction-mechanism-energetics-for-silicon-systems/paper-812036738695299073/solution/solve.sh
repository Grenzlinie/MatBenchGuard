#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: relative_energies.json ===
cat > "$OUTDIR/relative_energies.json" <<'FFEOF'
{
  "delta_E_0H_eV": -0.18,
  "delta_E_1H_eV": 0.15,
  "delta_E_2H_eV": 0.15
}
FFEOF

# === solve block: activation_barriers.json ===
cat > "$OUTDIR/activation_barriers.json" <<'FFEOF'
{
  "intrarow_barrier_eV": 1.12,
  "on_dimer_barrier_eV": 1.34
}
FFEOF

# === solve block: frustrated_energy_hydrogen.json ===
cat > "$OUTDIR/frustrated_energy_hydrogen.json" <<'FFEOF'
{
  "H_work_integral_eV": 0.5,
  "estimated_frustrated_translational_energy_eV": 0.5
}
FFEOF
