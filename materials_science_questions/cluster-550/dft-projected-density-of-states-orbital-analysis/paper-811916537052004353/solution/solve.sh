#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: workfunction_values.json ===
echo '{
  "Nb_workfunction_eV": 7.8,
  "NbC_workfunction_eV": 6.3
}' > "$OUTDIR/workfunction_values.json"
