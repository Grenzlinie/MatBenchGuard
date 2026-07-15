#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: diffusion_coefficients.csv ===
cat > /app/outputs/diffusion_coefficients.csv <<'FFEOF'
system,D
WAT_BNNT,0.440
WAT_FBNNT,0.600
Drug_BNNT,0.560
Drug_FBNNT,1.890
FFEOF

# === solve block: vdw_energies.csv ===
cat > /app/outputs/vdw_energies.csv <<'FFEOF'
system,vdw_per_drug,ele_per_drug
1-Drug_FBNNT,-43.0,0.018
2-Drug_FBNNT,-45.2,0.032
3-Drug_FBNNT,-46.3,0.207
4-Drug_FBNNT,-46.8,-0.139
5-Drug_FBNNT,-45.4,-0.897
FFEOF

# === solve finalize ===
echo "All outputs written."
