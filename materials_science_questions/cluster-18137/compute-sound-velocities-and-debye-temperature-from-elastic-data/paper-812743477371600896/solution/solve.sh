#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_isotropic_thermo.json ===
cat > "$OUTDIR/step_01_isotropic_thermo.json" <<'FFEOF'
{
  "C3": {"v_l": 17727, "v_t": 12168, "v_m": 13251, "Theta_D": 2141},
  "Si3": {"v_l": 8470, "v_t": 5140, "v_m": 5679, "Theta_D": 625},
  "Ge3": {"v_l": 4761, "v_t": 2916, "v_m": 3219, "Theta_D": 345}
}
FFEOF

# === solve block: step_02_anisotropic_velocities.json ===
cat > "$OUTDIR/step_02_anisotropic_velocities.json" <<'FFEOF'
{
  "C3": {
    "[001]": {"v_l": 17696, "v_t1": 12101, "v_t2": 12101},
    "[100]": {"v_l": 12174, "v_t1": 17843, "v_t2": 12101}
  },
  "Si3": {
    "[001]": {"v_l": 7785, "v_t1": 5505, "v_t2": 5505},
    "[100]": {"v_l": 5214, "v_t1": 8478, "v_t2": 5505}
  },
  "Ge3": {
    "[001]": {"v_l": 4473, "v_t1": 3121, "v_t2": 3121},
    "[100]": {"v_l": 2900, "v_t1": 4667, "v_t2": 3121}
  }
}
FFEOF

# === solve block: step_03_min_thermal_conductivity.json ===
cat > "$OUTDIR/step_03_min_thermal_conductivity.json" <<'FFEOF'
{
  "C3": {"isotropic": 1.70, "[001]": 1.72, "[100]": 1.71},
  "Si3": {"isotropic": 1.18, "[001]": 1.20, "[100]": 1.20},
  "Ge3": {"isotropic": 0.71, "[001]": 0.72, "[100]": 0.72}
}
FFEOF
