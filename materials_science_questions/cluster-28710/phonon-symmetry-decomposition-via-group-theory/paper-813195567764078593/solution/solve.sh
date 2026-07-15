#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
[
  {
    "x": 0.0,
    "a": 5.154,
    "c": 13.780,
    "volume": 317.02,
    "TO1": 200,
    "TO2": 242,
    "TO3": 348,
    "TO4": 577
  },
  {
    "x": 0.25,
    "a": 5.152,
    "c": 13.801,
    "volume": 317.27,
    "TO1": 208,
    "TO2": 242,
    "TO3": 342,
    "TO4": 582
  },
  {
    "x": 0.5,
    "a": 5.151,
    "c": 13.822,
    "volume": 317.50,
    "TO1": 214,
    "TO2": 241,
    "TO3": 335,
    "TO4": 588
  },
  {
    "x": 0.75,
    "a": 5.150,
    "c": 13.842,
    "volume": 317.86,
    "TO1": 229,
    "TO2": 244,
    "TO3": 327,
    "TO4": 598
  },
  {
    "x": 1.0,
    "a": 5.148,
    "c": 13.863,
    "volume": 318.16,
    "TO1": 235,
    "TO2": 254,
    "TO3": 323,
    "TO4": 609
  }
]
EOF
