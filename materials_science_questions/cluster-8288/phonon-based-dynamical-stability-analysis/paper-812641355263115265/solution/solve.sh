#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: j1_value_tl_fese2.txt ===
cat > "/app/outputs/j1_value_tl_fese2.txt" <<'FFEOF'
115.01
FFEOF

# === solve block: band_gap_tl_fese2.txt ===
cat > "/app/outputs/band_gap_tl_fese2.txt" <<'FFEOF'
22
FFEOF

# === solve block: phonon_stability_tl_fese2.txt ===
cat > "/app/outputs/phonon_stability_tl_fese2.txt" <<'FFEOF'
stable
FFEOF
