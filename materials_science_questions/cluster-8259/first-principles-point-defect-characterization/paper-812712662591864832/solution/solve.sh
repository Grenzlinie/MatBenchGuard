#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_qstem_results.json ===
cat > "/app/outputs/step_01_qstem_results.json" <<'FFEOF'
{
  "P_Se_intensity_ratio": 0.86,
  "V_Se_intensity_ratio": 0.66
}
FFEOF

# === solve block: step_02_dft_results.json ===
cat > "/app/outputs/step_02_dft_results.json" <<'FFEOF'
{
  "As_defect_level_above_VBM_eV": 0.10,
  "N_defect_level_above_VBM_eV": 0.66,
  "P_defect_level_above_VBM_eV": 0.30
}
FFEOF
