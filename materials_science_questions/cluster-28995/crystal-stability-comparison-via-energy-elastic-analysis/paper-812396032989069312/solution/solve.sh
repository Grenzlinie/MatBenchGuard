#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: gap_results.json ===
cat > "/app/outputs/gap_results.json" <<'FFEOF'
{
  "results": [
    {
      "density_ratio": 5,
      "gap_present": false,
      "gap_lower_frequency": null,
      "gap_upper_frequency": null,
      "gap_midgap_ratio": null
    },
    {
      "density_ratio": 1,
      "gap_present": true,
      "gap_lower_frequency": 0.36,
      "gap_upper_frequency": 0.42,
      "gap_midgap_ratio": 0.15384615384615385
    },
    {
      "density_ratio": 0.06666666666666667,
      "gap_present": true,
      "gap_lower_frequency": 0.3,
      "gap_upper_frequency": 0.65,
      "gap_midgap_ratio": 0.7368421052631579
    }
  ]
}
FFEOF
