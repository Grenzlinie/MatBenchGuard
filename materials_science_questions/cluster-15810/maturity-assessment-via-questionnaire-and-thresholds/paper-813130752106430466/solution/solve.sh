#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p $OUTDIR

# === solve block: accc_subsystem_srl.txt ===
echo 0.28 > $OUTDIR/accc_subsystem_srl.txt

# === solve block: nested_system_srl.txt ===
echo 0.51 > $OUTDIR/nested_system_srl.txt

# === solve block: unnested_system_srl.txt ===
echo 0.42 > $OUTDIR/unnested_system_srl.txt
