#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: puckering_critical_distances.json ===
cat > "$OUTDIR/puckering_critical_distances.json" <<'FFEOF'
{
  "d_metal_semimetal_A": 0.06,
  "d_semimetal_semiconductor_A": 0.7
}
FFEOF

# === solve block: electronic_properties.json ===
cat > "$OUTDIR/electronic_properties.json" <<'FFEOF'
{
  "As": {
    "direct_gap_no_SOI_eV": 0.99,
    "direct_gap_with_SOI_eV": 0.98,
    "SOI_gap_at_DP_eV": 0.001
  },
  "Sb": {
    "direct_gap_no_SOI_eV": 0.85,
    "direct_gap_with_SOI_eV": 0.69,
    "SOI_gap_at_DP_eV": 0.1
  },
  "Bi": {
    "direct_gap_no_SOI_eV": 0.46,
    "direct_gap_with_SOI_eV": 0.095,
    "SOI_gap_at_DP_eV": 1.0
  }
}
FFEOF

# === solve block: thermopower_summary.json ===
cat > "$OUTDIR/thermopower_summary.json" <<'FFEOF'
{
  "As": {
    "peak_p_type_Seebeck_uV_per_K": 550,
    "peak_n_type_Seebeck_uV_per_K": 300
  },
  "Sb": {
    "peak_p_type_Seebeck_uV_per_K": 550,
    "peak_n_type_Seebeck_uV_per_K": 300
  },
  "Bi": {
    "peak_p_type_Seebeck_uV_per_K": 120,
    "bipolar_suppression_observed": true
  }
}
FFEOF

# === solve finalize ===
# No further steps needed.
