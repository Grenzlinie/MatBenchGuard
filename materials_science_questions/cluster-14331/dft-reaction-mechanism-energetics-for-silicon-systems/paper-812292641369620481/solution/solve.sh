#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: sic2h4_energies.json ===
python3 /solution/gen_energies.py sic2h4 > /app/outputs/sic2h4_energies.json

# === solve block: sic2h2_energies.json ===
python3 /solution/gen_energies.py sic2h2 > /app/outputs/sic2h2_energies.json
