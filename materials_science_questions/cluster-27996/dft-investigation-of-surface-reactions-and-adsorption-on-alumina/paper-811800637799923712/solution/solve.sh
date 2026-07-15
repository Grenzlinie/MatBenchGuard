#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energies.json ===
cat > $OUTDIR/energies.json <<'JSONEOF'
{
  "A2_E_barrier": 64.4,
  "A2_E_reaction": -86.9,
  "A5_E_barrier": 68.8,
  "A5_E_reaction": 2.8,
  "B1_E_barrier": 29.1,
  "B1_E_reaction": -117.0,
  "A2_k_forward": 1.0e8,
  "A2_k_backward": 18.0,
  "A5_k_forward": 4.5e7,
  "A5_k_backward": 4.5e8,
  "B1_k_forward": 5.5e10,
  "B1_k_backward": 46.0
}
JSONEOF
