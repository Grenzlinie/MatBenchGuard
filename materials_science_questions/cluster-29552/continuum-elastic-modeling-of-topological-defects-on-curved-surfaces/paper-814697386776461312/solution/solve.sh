#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
# Pure Python stdlib only; no pip install needed.

# === solve block: transition_temperatures.json ===
cat > "$OUTDIR/transition_temperatures.json" <<'EOF'
{
  "gamma_m": 69.25,
  "gamma_i": 68.25
}
EOF

# === solve block: specific_heat.csv ===
python3 /solution/write_csvs.py specific_heat "$OUTDIR"

# === solve block: defect_density.csv ===
python3 /solution/write_csvs.py defect_density "$OUTDIR"

# === solve finalize ===
# No finalization needed.
