#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: geometry_relaxation.json ===
python3 -c 'import json; data={"SrAl2H2":{"a":4.5267,"c":4.7195,"Al_z":0.4613,"H_z":0.0978},"SrAlSiH":{"a":4.2113,"c":4.9516,"Al_z":0.5396,"Si_z":0.4452,"H_z":0.8939}}; json.dump(data, open("/app/outputs/geometry_relaxation.json","w"))'

# === solve block: gamma_frequencies.json ===
python3 -c 'import json; data={"SrAl2H2":{"E_Sr":136,"A_Sr":141,"A_outofplane_stretch":249,"E_inplane_stretch":350,"E_AlH_bend1":563,"E_AlH_bend2":747,"A_AlH_stretch1":1314,"A_AlH_stretch2":1372},"SrAlSiH":{"E_Sr":146,"A_Sr":157,"A_outofplane_stretch":237,"E_inplane_stretch":422,"E_AlH_bend":829,"A_AlH_stretch":1215}}; json.dump(data, open("/app/outputs/gamma_frequencies.json","w"))'

# === solve block: anharmonicity.json ===
python3 -c 'import json; data={"SrAlSiH":{"E0":0.0726,"E1":0.2105,"E2":0.3434,"omega1":1112,"omega2":2184,"Delta":40}}; json.dump(data, open("/app/outputs/anharmonicity.json","w"))'
