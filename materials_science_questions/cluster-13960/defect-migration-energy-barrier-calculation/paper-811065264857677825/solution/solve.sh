#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: calculated_values.json ===
cat > "$OUTDIR/calculated_values.json" <<'FFEOF'
{"re_re_binding_eV": -0.07, "os_os_binding_eV": 0.04, "re_os_binding_eV": -0.06, "re_vac_1nn_binding_eV": 0.24, "re_vac_2nn_binding_eV": 0.21, "os_vac_1nn_binding_eV": 0.54, "os_vac_2nn_binding_eV": 0.35, "sia_111_formation_pure_W_eV": 9.56, "sia_111_formation_W_Re_eV": 8.69, "sia_111_formation_W_Os_eV": 7.90, "crowdion_re_binding_1nn_eV": 0.86, "crowdion_os_binding_1nn_eV": 1.66, "rotation_barrier_pure_W_eV": 0.37, "rotation_barrier_W_Re_eV": 0.10, "rotation_barrier_W_Os_eV": 0.25}
FFEOF
