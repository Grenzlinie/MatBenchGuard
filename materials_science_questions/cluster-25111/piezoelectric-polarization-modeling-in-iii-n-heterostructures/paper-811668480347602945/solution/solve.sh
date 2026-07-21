#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_gaaln_results.json ===
cat > "$OUTDIR/step_01_gaaln_results.json" <<'JSON_EOF'
[
  {"well_width_ML": 6,  "thickness_nm": 1.554, "dE_dP_meV_per_GPa": 36, "field_0_GPa_MV_per_cm": null, "field_10_GPa_MV_per_cm": null},
  {"well_width_ML": 10, "thickness_nm": 2.590, "dE_dP_meV_per_GPa": 33, "field_0_GPa_MV_per_cm": null, "field_10_GPa_MV_per_cm": null},
  {"well_width_ML": 16, "thickness_nm": 4.144, "dE_dP_meV_per_GPa": 30, "field_0_GPa_MV_per_cm": null, "field_10_GPa_MV_per_cm": null},
  {"well_width_ML": 24, "thickness_nm": 6.216, "dE_dP_meV_per_GPa": 27, "field_0_GPa_MV_per_cm": null, "field_10_GPa_MV_per_cm": null},
  {"well_width_ML": 32, "thickness_nm": 8.288, "dE_dP_meV_per_GPa": 24, "field_0_GPa_MV_per_cm": 0.66, "field_10_GPa_MV_per_cm": 0.87}
]
JSON_EOF

# === solve block: step_02_ingan_wurtzite_results.json ===
cat > "$OUTDIR/step_02_ingan_wurtzite_results.json" <<'JSON_EOF'
[
  {"well_width_nm": 1.0, "dE_dP_meV_per_GPa": 20},
  {"well_width_nm": 2.0, "dE_dP_meV_per_GPa": 10},
  {"well_width_nm": 2.5, "dE_dP_meV_per_GPa": 0},
  {"well_width_nm": 3.5, "dE_dP_meV_per_GPa": -10},
  {"well_width_nm": 4.0, "dE_dP_meV_per_GPa": -20},
  {"well_width_nm": 5.0, "dE_dP_meV_per_GPa": -30}
]
JSON_EOF

# === solve block: step_03_ingan_cubic_results.json ===
cat > "$OUTDIR/step_03_ingan_cubic_results.json" <<'JSON_EOF'
[
  {"well_width_nm": 0.6, "dE_dP_meV_per_GPa": 28.5},
  {"well_width_nm": 1.0, "dE_dP_meV_per_GPa": 28.5},
  {"well_width_nm": 2.0, "dE_dP_meV_per_GPa": 28.5},
  {"well_width_nm": 3.0, "dE_dP_meV_per_GPa": 28.5},
  {"well_width_nm": 4.0, "dE_dP_meV_per_GPa": 28.5},
  {"well_width_nm": 5.0, "dE_dP_meV_per_GPa": 28.5}
]
JSON_EOF

# === solve finalize ===
echo "All oracle output files written successfully."
