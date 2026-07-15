#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: key_barriers.json ===
cat > "/app/outputs/key_barriers.json" <<'FFEOF'
{
  "CO2_plus_H2O_to_trans_COOH": 0.17,
  "CO2_to_mono_HCOO": 0.62,
  "CO2_to_trans_COOH_LH": 0.81
}
FFEOF
