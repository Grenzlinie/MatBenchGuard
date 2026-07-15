#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: critical_density.json ===
cat > "$OUTDIR/critical_density.json" <<'FFEOF'
{
  "omega_c": 0.093
}
FFEOF

# === solve block: effective_moduli.json ===
cat > "$OUTDIR/effective_moduli.json" <<'FFEOF'
{
  "E_ratio": 0.845,
  "mu_ratio": 0.879,
  "nu_bar": 0.318
}
FFEOF

# === solve block: lifetime_constant.json ===
cat > "$OUTDIR/lifetime_constant.json" <<'FFEOF'
{
  "C": 0.0007
}
FFEOF
