#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "import json; d = { 'SrTiO3': { 'Z1': 2.00, 'Z2': 2.50, 'Z3': -1.50, 'alpha_M_star': 25.8, 's': 0.72, 'b1': 8.66, 'b2': 3.39, 'b3': 2.08, 'W': -0.13, 'A1': 22.2, 'B1': -2.17, 'A2': 174, 'B2': -24.0, 'A3': 5.34, 'B3': -0.522, 'k1': 138, 'k2': 487 }, 'BaTiO3': { 'Z1': 2.00, 'Z2': 1.86, 'Z3': -1.29, 'alpha_M_star': 18.3, 's': 0.61, 'b1': 4.68, 'b2': 1.13, 'b3': 2.02, 'W': -0.092, 'A1': 20.6, 'B1': -2.16, 'A2': 82.4, 'B2': -12.2, 'A3': 8.91, 'B3': -0.930, 'k1': 117, 'k2': 208 } }; open('/app/outputs/results.json','w').write(json.dumps(d, indent=2))"
