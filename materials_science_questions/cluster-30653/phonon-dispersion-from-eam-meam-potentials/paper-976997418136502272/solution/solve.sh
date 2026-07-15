#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: validation_results.json ===
cat > "$OUTDIR/validation_results.json" <<'FFEOF'
{
  "phonon_peaks": {
    "fcc_Al": [7.0, 8.5],
    "bcc_Li": [5.5, 7.0],
    "AlLi": [5.0, 6.0, 7.0],
    "Al3Li": [5.5, 6.5, 7.5]
  },
  "elastic_constants": {
    "Al_fcc": {"C11": 130, "C12": 57, "C44": 39},
    "Li_bcc": {"C11": 13, "C12": 12, "C44": 11}
  }
}
FFEOF

# === solve block: phase_diagram_features.json ===
cat > "$OUTDIR/phase_diagram_features.json" <<'FFEOF'
{
  "eutectic_temperature_K": 771,
  "eutectic_composition_Li_fraction": 0.32,
  "Li_solubility_in_fcc_Al_fraction": 0.21
}
FFEOF
