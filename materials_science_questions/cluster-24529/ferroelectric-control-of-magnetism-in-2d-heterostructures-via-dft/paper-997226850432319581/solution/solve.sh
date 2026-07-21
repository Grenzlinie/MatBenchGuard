#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_potential.csv ===
cat > /app/outputs/energy_potential.csv <<'FFEOF'
Δd (Å),ΔE_MEC (meV/UC)
0,0
0.29,-0.15
0.44,-0.20
1.0,-0.32
1.69,-0.37
FFEOF

# === solve block: charge_analysis.txt ===
cat > /app/outputs/charge_analysis.txt <<'FFEOF'
S_spin_polarization_d0: 0.135 e-/S
S_spin_polarization_d044: 0.092 e-/S
FFEOF
