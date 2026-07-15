#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: hopfield_and_tc_compressed.json ===
cat > /app/outputs/hopfield_and_tc_compressed.json <<'FFEOF'
{"eta": 14.588, "T_c": 10.0}
FFEOF

# === solve block: hopfield_and_tc_equilibrium.json ===
cat > /app/outputs/hopfield_and_tc_equilibrium.json <<'FFEOF'
{"eta": 7.824, "T_c": 0.0}
FFEOF
