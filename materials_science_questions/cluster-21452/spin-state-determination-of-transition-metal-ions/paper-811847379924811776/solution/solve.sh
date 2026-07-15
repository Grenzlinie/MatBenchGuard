#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: cfp.json ===
cat > "$OUTDIR/cfp.json" <<'FFEOF'
{
  "B_2_0": -1360.0,
  "B_2_1": 0.0,
  "B_2_-1": 0.0,
  "B_2_2": 280.0,
  "B_2_-2": 280.0,
  "B_4_0": -450.0,
  "B_4_1": 0.0,
  "B_4_-1": 0.0,
  "B_4_2": -110.0,
  "B_4_-2": -110.0,
  "B_4_3": 0.0,
  "B_4_-3": 0.0,
  "B_4_4": 300.0,
  "B_4_-4": 300.0
}
FFEOF

# === solve block: energy_levels.csv ===
cat > "$OUTDIR/energy_levels.csv" <<'FFEOF'
computed_energy_cm1,term_label
0.0,4T1g(G6+)_lower
95.5,4T1g(G8+)_1
277.5,4T1g(G8+)_2
420.5,4T1g(G6+)_upper
510.0,4T1g(G8+)_3
658.0,4T1g(G7+)
7670.0,4T2g(G5+)_1
7820.0,4T2g(G5+)_2
8050.0,4T2g(G3+)
FFEOF
