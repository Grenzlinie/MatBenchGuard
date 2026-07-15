#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: defect_formation_energies.json ===
cat > "$OUTDIR/defect_formation_energies.json" <<'FFEOF'
{"E_form1": 4.129, "E_form2": 5.197, "E_form3": 3.459}
FFEOF

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" <<'FFEOF'
{"pure_BG": 1.52, "Vo_BG": 1.12, "IO_BG": 0.56, "IBi_BG": 0.0}
FFEOF
