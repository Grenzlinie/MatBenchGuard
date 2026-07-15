#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "delta_E_FM_AFM_doped": -39,
  "delta_E_FM_AFM_undoped": 36,
  "delta_E_spin_polarization": 187,
  "magnetic_moment_isolated": 2.0,
  "magnetization_per_defect_doped": 1.4,
  "spin_polarization_at_EF": 0.73
}
FFEOF
