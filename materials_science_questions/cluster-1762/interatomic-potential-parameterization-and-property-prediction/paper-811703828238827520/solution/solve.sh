#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: md_structural_params.csv ===
python3 /solution/write_struct.py > "$OUTDIR/md_structural_params.csv"

# === solve block: exafs_ft_180K.csv ===
python3 /solution/write_ft.py 180 > "$OUTDIR/exafs_ft_180K.csv"

# === solve block: exafs_ft_300K.csv ===
python3 /solution/write_ft.py 300 > "$OUTDIR/exafs_ft_300K.csv"

# === solve block: exafs_ft_400K.csv ===
python3 /solution/write_ft.py 400 > "$OUTDIR/exafs_ft_400K.csv"
