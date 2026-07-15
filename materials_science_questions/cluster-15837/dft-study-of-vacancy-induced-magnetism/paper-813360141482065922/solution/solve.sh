#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: monodoped_results.json ===
cat > /app/outputs/monodoped_results.json <<'FFEOF'
{
  "total_moment_muB": 7.50,
  "local_moment_Cr_muB": 3.84,
  "local_moment_bridging_O_muB": -0.08,
  "energy_difference_near_meV": 278,
  "energy_difference_far_meV": 26
}
FFEOF

# === solve block: codoped_results.json ===
cat > /app/outputs/codoped_results.json <<'FFEOF'
{
  "energy_difference_codoped_far_meV": 73
}
FFEOF
