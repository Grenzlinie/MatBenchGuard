#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binodal_threshold.json ===
cat > /app/outputs/binodal_threshold.json <<'FFEOF'
{
  "B_min_squared": 4.5,
  "method": "Numerical evaluation of the composition conservation constraint for the periodic equilibrium solutions expressed in Jacobi elliptic functions, revealing the binodal threshold above the spinodal."
}
FFEOF
