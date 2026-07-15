#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: activation_energies.json ===
cat > "$OUTDIR/activation_energies.json" << 'FFEOF'
{"SnS": 88, "GeSe": 43}
FFEOF

# === solve block: polarization_values.json ===
cat > "$OUTDIR/polarization_values.json" << 'FFEOF'
{"SnS": {"P": 0.6}, "GeSe": {"P": 1.7}}
FFEOF
