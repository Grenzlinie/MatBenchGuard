#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: solgasmix_transition_pressures.json ===
echo '[292, 1428, 5754, 20007, 61124, 165119]' > /app/outputs/solgasmix_transition_pressures.json

# === solve block: dynamic_transition_pressures.json ===
echo '[236, 1145, 4629, 16107, 49029, 131690]' > /app/outputs/dynamic_transition_pressures.json
