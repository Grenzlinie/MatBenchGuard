#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: eos_parameters.json ===
cat > "$OUTDIR/eos_parameters.json" <<'FFEOF'
{
  "V0": 46.04,
  "B0": 123,
  "Bprime": 3.43
}
FFEOF

# === solve block: metallization_pressure.json ===
cat > "$OUTDIR/metallization_pressure.json" <<'FFEOF'
{
  "metallization_pressure_GPa": 324
}
FFEOF
