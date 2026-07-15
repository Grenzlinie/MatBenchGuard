#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_03_susceptibility.json ===
cat > /app/outputs/step_03_susceptibility.json <<'FFEOF'
{
  "chi_orb_100K": 4.77e-4,
  "chi_orb_300K": 4.77e-4,
  "chi_spin_100K": 3.3e-5,
  "chi_spin_300K": 3.3e-5
}
FFEOF
