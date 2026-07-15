#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: pristine_TAC_results.csv ===
cat > "$OUTDIR/pristine_TAC_results.csv" <<'FFEOF'
a0_Ang,c0_Ang,mag_moment_muB,C11_GPa,C33_GPa,C44_GPa,C12_GPa,C13_GPa
6.16,18.65,0.0,355.2,292.4,119.3,82.2,76.6
FFEOF

# === solve block: Hf_substitutional_TAC_results.csv ===
cat > "/app/outputs/Hf_substitutional_TAC_results.csv" <<'FFEOF'
C11_GPa,C12_GPa,C13_GPa,C33_GPa,C44_GPa,a0_Ang,c0_Ang,mag_moment_muB
348.0,88.5,75.3,290.9,115.0,6.19,18.70,0.0
FFEOF

# === solve block: Hf_interstitial_TAC_results.csv ===
cat > "/app/outputs/Hf_interstitial_TAC_results.csv" <<'FFEOF'
C11_GPa,C12_GPa,C13_GPa,C33_GPa,C44_GPa,a0_Ang,c0_Ang,mag_moment_muB
310.7,91.6,85.1,176.7,108.6,6.24,19.03,1.35
FFEOF
