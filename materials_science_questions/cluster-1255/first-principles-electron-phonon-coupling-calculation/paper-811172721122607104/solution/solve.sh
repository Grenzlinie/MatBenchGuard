#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: hyperfine_constants.json ===
mkdir -p "$OUTDIR" && echo '{"As_MHz": 33.82, "A_aniso_MHz": 7.82}' > "$OUTDIR/hyperfine_constants.json"

# === solve finalize ===
true
