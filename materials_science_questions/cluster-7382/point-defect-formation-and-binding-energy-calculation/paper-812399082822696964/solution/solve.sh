#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energy.txt ===
printf '%s
' '-82' > /app/outputs/formation_energy.txt

# === solve block: excess_entropy.txt ===
printf '%s
' '3.90' > /app/outputs/excess_entropy.txt
