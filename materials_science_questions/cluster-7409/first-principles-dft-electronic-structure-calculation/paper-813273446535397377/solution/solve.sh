#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: rotation_angles.json ===
cat > "$OUTDIR/rotation_angles.json" <<'FFEOF'
{"V_Ra_max_theta": 13.0, "V_Rc_max_theta": 10.0, "far_theta_avg": 0.0, "V_Ra_E_gap": 0.47, "V_Rc_E_gap": 0.50}
FFEOF
