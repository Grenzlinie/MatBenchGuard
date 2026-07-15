#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json << 'EOF'
{
  "Li_diffusion_barrier": 0.017,
  "Na_diffusion_barrier": 0.008,
  "Li_capacity": 456,
  "Na_capacity": 1027,
  "Li_open_circuit_voltage": 0.526,
  "Na_open_circuit_voltage": 0.31
}
EOF
