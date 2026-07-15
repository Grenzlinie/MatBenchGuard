#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: spin_energies.json ===
python3 /solution/generate.py spin > /app/outputs/spin_energies.json

# === solve block: binding_energies.json ===
python3 /solution/generate.py binding > /app/outputs/binding_energies.json

# === solve block: fragmentation_energies.json ===
python3 /solution/generate.py fragmentation > /app/outputs/fragmentation_energies.json
