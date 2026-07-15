#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: mgb2_gap.json ===
cat > "$OUTDIR/mgb2_gap.json" <<'FFEOF'
{
  "sigma_gap_min_meV": 1.4,
  "sigma_gap_max_meV": 2.2,
  "pi_gap_min_meV": 8.0,
  "pi_gap_max_meV": 9.3
}
FFEOF

# === solve block: yh6_tc.json ===
cat > "$OUTDIR/yh6_tc.json" <<'FFEOF'
{
  "Tc_K": 230.98
}
FFEOF
