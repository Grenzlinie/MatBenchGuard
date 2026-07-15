#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat <<'FFEOF' > /app/outputs/results.json
{
  "H_BE_n": 16.0,
  "Li_BE_n": 24.6,
  "Na_BE_n": 20.4,
  "K_BE_n": 5.1,
  "H_delta_nu": 47,
  "Li_delta_nu": 68,
  "Na_delta_nu": 43,
  "K_delta_nu": 33
}
FFEOF
