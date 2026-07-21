#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: surface_composition.json ===
cat > "$OUTDIR/surface_composition.json" <<'FFEOF'
{
  "surface_ge_fraction": 0.76
}
FFEOF

# === solve block: composition_profile.json ===
cat > "$OUTDIR/composition_profile.json" <<'FFEOF'
[0.76, 0.55, 0.40, 0.28, 0.18, 0.10, 0.05]
FFEOF

# === solve block: chemical_potential.json ===
cat > "$OUTDIR/chemical_potential.json" <<'FFEOF'
[-0.25, -0.06, 0.01, 0.05, 0.08, 0.10, 0.11]
FFEOF
