#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_p4o4_band_gap.json ===
cat > "$OUTDIR/step_01_p4o4_band_gap.json" <<'FFEOF'
{"method": "DFT", "functional": "HSE06", "band_gap": 2.24, "direct": true}
FFEOF

# === solve block: step_02_p4o4_effective_mass.json ===
cat > "$OUTDIR/step_02_p4o4_effective_mass.json" <<'FFEOF'
{"method": "DFT", "functional": "LDA", "carrier_type": "electron", "effective_mass": 0.58, "reference": "free electron mass"}
FFEOF

# === solve block: step_03_p4o4_band_edges.json ===
cat > "$OUTDIR/step_03_p4o4_band_edges.json" <<'FFEOF'
{"CBM_vs_vacuum": -3.67, "VBM_vs_vacuum": -5.61, "HER_potential": -4.44, "OER_potential": -5.67, "pH": 0}
FFEOF

# === solve block: step_04_p2o3_polarization.json ===
cat > "$OUTDIR/step_04_p2o3_polarization.json" <<'FFEOF'
[
  {"structure": "P2O3-I", "polarization": 2.4e-12, "direction": "out-of-plane"},
  {"structure": "P2O3-II", "polarization": 1.2e-12, "direction": "in-plane"}
]
FFEOF
