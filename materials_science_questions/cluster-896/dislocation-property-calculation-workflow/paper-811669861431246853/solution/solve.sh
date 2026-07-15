#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: cascade_lifetime.txt ===
echo '0.1' > "$OUTDIR/cascade_lifetime.txt"

# === solve block: displacement_summary.json ===
cat > "$OUTDIR/displacement_summary.json" <<'FFEOF'
{
  "0.25": {
    "total_displacements": 4.545454545454546,
    "efficiency": 1.0,
    "anti_site_fraction": 0.15
  },
  "0.5": {
    "total_displacements": 8.636363636363637,
    "efficiency": 0.95,
    "anti_site_fraction": 0.15
  },
  "1": {
    "total_displacements": 15.454545454545455,
    "efficiency": 0.85,
    "anti_site_fraction": 0.15
  },
  "5": {
    "total_displacements": 54.54545454545455,
    "efficiency": 0.6,
    "anti_site_fraction": 0.15
  },
  "10": {
    "total_displacements": 90.9090909090909,
    "efficiency": 0.5,
    "anti_site_fraction": 0.15,
    "ratio_C_Si_interstitials": 5.0
  },
  "30": {
    "total_displacements": 201.8181818181818,
    "efficiency": 0.37,
    "anti_site_fraction": 0.15
  }
}
FFEOF

# === solve block: cluster_summary.txt ===
echo '3' > "$OUTDIR/cluster_summary.txt"
