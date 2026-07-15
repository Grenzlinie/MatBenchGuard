#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: soc_results.json ===
cat > /app/outputs/soc_results.json <<'FFEOF'
{
  "forward_1A''_to_13A''_SOC_cm-1": 480,
  "forward_13A''_to_5A'_SOC_cm-1": 373,
  "forward_13A''_to_1A'_SOC_cm-1": 266,
  "backward_5A''_to_23A''_SOC_cm-1": 271,
  "backward_5A''_to_13A''_SOC_cm-1": 9,
  "backward_23A''_to_1A'_SOC_cm-1": 796,
  "forward_crossover_preferred": true,
  "backward_crossover_preferred": true
}
FFEOF
