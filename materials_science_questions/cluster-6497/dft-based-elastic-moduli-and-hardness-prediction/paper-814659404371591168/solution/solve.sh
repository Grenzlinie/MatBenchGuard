#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_constants_0GPa.csv ===
python3 /solution/generate.py elastic_constants_0GPa.csv

# === solve block: derived_properties_0GPa.csv ===
python3 /solution/generate.py derived_properties_0GPa.csv

# === solve block: pressure_dependence.csv ===
python3 /solution/generate.py pressure_dependence.csv
