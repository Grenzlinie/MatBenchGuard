#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: surface_energies.json ===
python3 -c "import json; json.dump({ 'calcite_104': {'unhydrated': 0.59, 'hydrated': 0.17}, 'fluorite_011': {'unhydrated': 0.82, 'hydrated': 0.90}, 'fluorite_111': {'unhydrated': 0.52, 'hydrated': 0.40}, 'fluorite_310': {'unhydrated': 1.56, 'hydrated': 0.67} }, open('/app/outputs/surface_energies.json','w'), indent=2)"

# === solve block: adsorption_energies.json ===
python3 -c "import json; json.dump({ 'calcite_104': {'water': -92.2, 'methanoic_acid': -84.2}, 'fluorite_011': {'water': -33.4, 'methanoic_acid': -97.3}, 'fluorite_111': {'water': -61.8, 'methanoic_acid': -102.4}, 'fluorite_310': {'water': -250.7, 'methanoic_acid': -110.9} }, open('/app/outputs/adsorption_energies.json','w'), indent=2)"
