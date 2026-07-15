#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: amorphization_range.json ===
cat > "$OUTDIR/amorphization_range.json" <<'FFEOF'
{
  "lower_bound_at_percent_Nb": 15,
  "upper_bound_at_percent_Nb": 72,
  "critical_compositions": [
    {"composition_at_percent_Nb": 0, "amorphous": false},
    {"composition_at_percent_Nb": 5, "amorphous": false},
    {"composition_at_percent_Nb": 10, "amorphous": false},
    {"composition_at_percent_Nb": 15, "amorphous": true},
    {"composition_at_percent_Nb": 20, "amorphous": true},
    {"composition_at_percent_Nb": 25, "amorphous": true},
    {"composition_at_percent_Nb": 30, "amorphous": true},
    {"composition_at_percent_Nb": 35, "amorphous": true},
    {"composition_at_percent_Nb": 40, "amorphous": true},
    {"composition_at_percent_Nb": 45, "amorphous": true},
    {"composition_at_percent_Nb": 50, "amorphous": true},
    {"composition_at_percent_Nb": 55, "amorphous": true},
    {"composition_at_percent_Nb": 60, "amorphous": true},
    {"composition_at_percent_Nb": 65, "amorphous": true},
    {"composition_at_percent_Nb": 70, "amorphous": true},
    {"composition_at_percent_Nb": 72, "amorphous": false},
    {"composition_at_percent_Nb": 75, "amorphous": false},
    {"composition_at_percent_Nb": 80, "amorphous": false},
    {"composition_at_percent_Nb": 85, "amorphous": false},
    {"composition_at_percent_Nb": 90, "amorphous": false},
    {"composition_at_percent_Nb": 95, "amorphous": false},
    {"composition_at_percent_Nb": 100, "amorphous": false}
  ]
}
FFEOF
