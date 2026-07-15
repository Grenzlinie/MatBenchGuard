#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: BaNi2P2_results.json ===
python3 /solution/gen_alpha2F.py 0.61 163.10 3.64 "$OUTDIR/BaNi2P2_results.json"

# === solve block: BaRh2P2_results.json ===
python3 /solution/gen_alpha2F.py 0.43 224.43 3.05 "$OUTDIR/BaRh2P2_results.json"

# === solve block: BaIr2P2_results.json ===
python3 /solution/gen_alpha2F.py 0.55 176.28 2.65 "$OUTDIR/BaIr2P2_results.json"
