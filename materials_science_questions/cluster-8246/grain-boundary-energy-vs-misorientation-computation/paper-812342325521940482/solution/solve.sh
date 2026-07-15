#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: node_angles.json ===
cat > /app/outputs/node_angles.json <<'FFEOF'
{
  "isolated_angle_2alpha_degrees": 86.0,
  "network_angle_2alpha_degrees": 91.6
}
FFEOF
