#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_nanopores_circular.csv ===
python3 -c "
import sys
sys.path.insert(0, '/solution')
from write_outputs import write_step_01
write_step_01()
"

# === solve block: step_02_nanopores_noncircular.csv ===
python3 -c "
import sys
sys.path.insert(0, '/solution')
from write_outputs import write_step_02
write_step_02()
"

# === solve block: step_03_nanofibers.csv ===
python3 -c "
import sys
sys.path.insert(0, '/solution')
from write_outputs import write_step_03
write_step_03()
"
