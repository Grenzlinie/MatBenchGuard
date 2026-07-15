#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transition_results.json ===
cat > /app/outputs/transition_results.json <<'FFEOF'
{
  "final_stair_rod_burgers": "1/3 a[1-00]",
  "first_transition_stress_GPa": 5.6,
  "transition_strains": [2.3, 4.8, 6.0]
}
FFEOF
