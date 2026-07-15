#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: step_01_band_gap.csv ===
cat > "$OUTDIR/step_01_band_gap.csv" <<'FFEOF'
functional,band_gap_eV,gap_nature
pbe-GGA,2.34,Γ-Γ direct
pw-LDA,2.14,Γ-Γ direct
FFEOF

# === solve block: step_02_dielectric_constants.csv ===
cat > "$OUTDIR/step_02_dielectric_constants.csv" <<'FFEOF'
functional,direction,epsilon_infinity
pbe-GGA,ordinary,7.20
pbe-GGA,extraordinary,8.33
pw-LDA,ordinary,5.44
pw-LDA,extraordinary,6.23
FFEOF

# === solve block: step_03_birefringence.csv ===
cat > "$OUTDIR/step_03_birefringence.csv" <<'FFEOF'
functional,birefringence_633nm
pbe-GGA,0.23
pw-LDA,0.269
FFEOF
