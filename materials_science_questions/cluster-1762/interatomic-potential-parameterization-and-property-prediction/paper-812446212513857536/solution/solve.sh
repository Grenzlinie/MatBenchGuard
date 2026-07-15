#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: sk_parameters.json ===
cat > "$OUTDIR/sk_parameters.json" <<'FFEOF'
{
  "E_s_s_000": 0.1267,
  "E_s_s_111": -0.0111,
  "E_x_x_000": 0.4532,
  "E_x_x_111": 0.0150,
  "E_xy_xy_000": -0.0934,
  "E_xy_xy_111": 0.0003,
  "E_dz_dz_000": 0.2941,
  "E_dz_dz_111": 0.0037,
  "E_xyz_xyz_000": -0.2831,
  "E_xyz_xyz_111": -0.0009,
  "E_f4_f4_000": -0.3320,
  "E_f4_f4_111": 0.0039
}
FFEOF

# === solve block: specific_heat_gamma.json ===
cat > "$OUTDIR/specific_heat_gamma.json" <<'FFEOF'
{
  "gamma_mJ_per_molK2": 51.0
}
FFEOF
