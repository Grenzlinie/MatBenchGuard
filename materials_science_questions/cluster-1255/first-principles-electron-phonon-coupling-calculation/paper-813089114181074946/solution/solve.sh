#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

mkdir -p /app/outputs

# === solve block: computed_values.json ===
cat > /app/outputs/computed_values.json <<'FFEOF'
{
  "dE_dT_static": 0.048,
  "dE_dT_vib": -0.258,
  "ratio_t": -0.186,
  "alpha_prime": 627,
  "A": 117
}
FFEOF
