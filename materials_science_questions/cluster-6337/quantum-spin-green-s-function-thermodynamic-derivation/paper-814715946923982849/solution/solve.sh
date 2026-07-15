#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
# The helper script is bundled as /solution/gendata.py

# === solve block: fm_magnetization_vs_T.csv ===
python3 /solution/gendata.py --type fm_mag_vs_T --output "$OUTDIR/fm_magnetization_vs_T.csv"

# === solve block: afm_magnetization_vs_T.csv ===
python3 /solution/gendata.py --type afm_mag_vs_T --output "$OUTDIR/afm_magnetization_vs_T.csv"

# === solve block: fm_hysteresis_curves.csv ===
python3 /solution/gendata.py --type fm_hysteresis --output "$OUTDIR/fm_hysteresis_curves.csv"

# === solve block: afm_hysteresis_curves.csv ===
python3 /solution/gendata.py --type afm_hysteresis --output "$OUTDIR/afm_hysteresis_curves.csv"

# === solve block: afm_hysteresis_central_T1.csv ===
python3 /solution/gendata.py --type afm_central_T1 --output "$OUTDIR/afm_hysteresis_central_T1.csv"

# === solve block: fm_extracted_values.json ===
python3 /solution/gendata.py --type fm_extracted --output "$OUTDIR/fm_extracted_values.json"

# === solve block: afm_extracted_values.json ===
python3 /solution/gendata.py --type afm_extracted --output "$OUTDIR/afm_extracted_values.json"
