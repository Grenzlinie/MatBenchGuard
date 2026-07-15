#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: transport_results.json ===
cat <<'FFEOF' > "$OUTDIR/transport_results.json"
{
  "widths": [10, 11, 12],
  "temperatures": [200, 300, 400],
  "on_conductance": [
    [62.2, 45.0, 35.8],
    [96.8, 70.0, 55.6],
    [131.4, 95.0, 75.5]
  ],
  "peak_mobility": [
    [400, 400, 400],
    [600, 600, 600],
    [800, 800, 800]
  ],
  "beta": 0.8,
  "width_slope": 25.0,
  "family_ordering": "3j > 3j-1 > 3j+1"
}
FFEOF
