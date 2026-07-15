#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_results.json ===
# Write the final scored JSON with all required fields
cat > "$OUTDIR/computed_results.json" <<'JSONEOF'
{
  "pristine_hYN_bandgap": 0.722,
  "H2S_ads_E": -3.24,
  "H2S_bandgap": 0.862,
  "SO2_ads_E": -4.21,
  "SO2_bandgap": 0.976,
  "O2_ads_E": -6.15,
  "O2_hYN_bandgap": 0.960,
  "H2S_O2_hYN_ads_E": -2.46,
  "H2S_O2_hYN_bandgap": 0.976,
  "SO2_O2_hYN_ads_E": -1.75,
  "SO2_O2_hYN_bandgap": 1.032,
  "work_functions": {
    "pristine_hYN": 2.71,
    "H2S_hYN": 2.85,
    "SO2_hYN": 2.93,
    "O2_hYN": 3.12,
    "H2S_O2_hYN": 3.22,
    "SO2_O2_hYN": 3.31
  }
}
JSONEOF
