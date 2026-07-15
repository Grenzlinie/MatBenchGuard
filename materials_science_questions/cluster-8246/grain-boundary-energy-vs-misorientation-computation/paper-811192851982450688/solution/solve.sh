#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: local_rdf.txt ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from generate_helpers import write_local_rdf; write_local_rdf('/app/outputs/local_rdf.txt')"

# === solve block: angular_distribution.txt ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from generate_helpers import write_angular_distribution; write_angular_distribution('/app/outputs/angular_distribution.txt')"

# === solve block: gb_energy_profile.txt ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from generate_helpers import write_energy_profile; write_energy_profile('/app/outputs/gb_energy_profile.txt')"
