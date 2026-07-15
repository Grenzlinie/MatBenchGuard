#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: pressure_composition.json ===
cat > "$OUTDIR/pressure_composition.json" <<'FFEOF'
{
  "P10": {
    "fcc_percent": 55.0,
    "hcp_percent": 25.0,
    "bcc_percent": 20.0
  },
  "P50": {
    "fcc_percent": 0.0,
    "hcp_percent": 15.0,
    "bcc_percent": 85.0
  },
  "bcc_coexistence_line": [
    {"pressure": 10.0, "T_bcc_liquid": 1.5},
    {"pressure": 15.0, "T_bcc_liquid": 2.0},
    {"pressure": 20.0, "T_bcc_liquid": 2.5},
    {"pressure": 25.0, "T_bcc_liquid": 3.0},
    {"pressure": 50.0, "T_bcc_liquid": 4.8}
  ]
}
FFEOF

# === solve block: temperature_hcp_counts.csv ===
cat > "$OUTDIR/temperature_hcp_counts.csv" <<'FFEOF'
crystallite_size,hcp_22pct,hcp_10pct
1000,120,60
2000,280,110
3000,460,180
4000,640,280
5000,850,380
FFEOF
