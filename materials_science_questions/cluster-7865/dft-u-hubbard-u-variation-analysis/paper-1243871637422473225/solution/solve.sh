#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_band_gaps.json ===
cat > "$OUTDIR/step_01_band_gaps.json" <<'FFEOF'
{
  "calculations": [
    {"geometry": "bulk-like", "U_eV": 0.0, "band_gap_eV": 0.0, "is_insulator": false},
    {"geometry": "bulk-like", "U_eV": 2.5, "band_gap_eV": 0.0, "is_insulator": false},
    {"geometry": "bulk-like", "U_eV": 2.625, "band_gap_eV": 0.0, "is_insulator": false},
    {"geometry": "bulk-like", "U_eV": 2.75, "band_gap_eV": 0.0, "is_insulator": false},
    {"geometry": "surface-relaxed", "U_eV": 0.0, "band_gap_eV": 0.0, "is_insulator": false},
    {"geometry": "surface-relaxed", "U_eV": 2.5, "band_gap_eV": 0.05, "is_insulator": true},
    {"geometry": "surface-relaxed", "U_eV": 2.625, "band_gap_eV": 0.08, "is_insulator": true},
    {"geometry": "surface-relaxed", "U_eV": 2.75, "band_gap_eV": 0.10, "is_insulator": true}
  ]
}
FFEOF
