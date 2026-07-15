#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_barriers.csv ===
cat > /app/outputs/energy_barriers.csv <<'FFEOF'
strain,energy_barrier
-3.0,0.001
-2.0,0.04
-1.0,0.12
0.0,0.25
1.0,0.42
2.0,0.64
3.0,0.88
4.0,1.00
FFEOF
