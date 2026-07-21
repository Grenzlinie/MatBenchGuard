#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: tricritical_point.json ===
cat > /app/outputs/tricritical_point.json << 'FFEOF'
{
  "T_t": 2.1,
  "h_t": 4.2
}
FFEOF

# === solve block: critical_temperature_h0.json ===
cat > /app/outputs/critical_temperature_h0.json << 'FFEOF'
{
  "T_c": 3.45
}
FFEOF
