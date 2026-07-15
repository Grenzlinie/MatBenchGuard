#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: eos_parameters.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from helper import write_eos_parameters; write_eos_parameters('/app/outputs/eos_parameters.csv')"

# === solve block: elastic_constants_sc.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from helper import write_elastic_constants_sc; write_elastic_constants_sc('/app/outputs/elastic_constants_sc.csv')"

# === solve block: elastic_constants_grae1.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from helper import write_elastic_constants_grae1; write_elastic_constants_grae1('/app/outputs/elastic_constants_grae1.csv')"

# === solve block: critical_points.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from helper import write_critical_points; write_critical_points('/app/outputs/critical_points.csv')"
