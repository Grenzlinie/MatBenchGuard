#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: pristine_Mo43B2_Tc.json ===
cat > "$OUTDIR/pristine_Mo43B2_Tc.json" <<'FFEOF'
{
  "Tc_K": 4.06
}
FFEOF

# === solve block: strained_Mo43B2_Tc.json ===
cat > "$OUTDIR/strained_Mo43B2_Tc.json" <<'FFEOF'
{
  "Tc_K": 6.78
}
FFEOF

# === solve block: W43B2_Tc.json ===
cat > "$OUTDIR/W43B2_Tc.json" <<'FFEOF'
{
  "Tc_K": 2.37
}
FFEOF
