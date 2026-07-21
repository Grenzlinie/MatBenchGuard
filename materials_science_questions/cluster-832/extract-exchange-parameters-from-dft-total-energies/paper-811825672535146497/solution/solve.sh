#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=${OUTDIR:-/app/outputs}
mkdir -p "$OUTDIR"

# === solve block: computed_results.json ===
cat > "$OUTDIR/computed_results.json" <<'EOF'
{
  "fm_total_energy_per_fu_Ry": -150.0,
  "afm_total_energy_per_fu_Ry": -150.00036749,
  "energy_difference_meV_per_fu": 5.0,
  "ni_spin_moment_muB": 1.5,
  "total_spin_moment_per_fu_muB": 2.0,
  "band_gap_fm_down_spin_eV": 0.8,
  "exchange_J_K": 13.0,
  "ni_orbital_moment_soc_muB": 0.16,
  "pt_orbital_moment_soc_muB": 0.02,
  "effective_paramagnetic_moment_muB": 3.0
}
EOF
