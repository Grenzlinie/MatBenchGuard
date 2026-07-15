#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: hybrid_zt.json ===
python3 -c '
import json
data = {
  "SnSe-hBN": [
    {"temperature_K": 100, "ZTelec": 0.985},
    {"temperature_K": 200, "ZTelec": 0.966},
    {"temperature_K": 300, "ZTelec": 0.950},
    {"temperature_K": 400, "ZTelec": 0.933},
    {"temperature_K": 500, "ZTelec": 0.912},
    {"temperature_K": 600, "ZTelec": 0.888},
    {"temperature_K": 700, "ZTelec": 0.861},
    {"temperature_K": 800, "ZTelec": 0.832},
    {"temperature_K": 900, "ZTelec": 0.802},
    {"temperature_K": 1000, "ZTelec": 0.773}
  ],
  "SnSe-CsPbI3": [
    {"temperature_K": 100, "ZTelec": 0.991},
    {"temperature_K": 200, "ZTelec": 0.980},
    {"temperature_K": 300, "ZTelec": 0.961},
    {"temperature_K": 400, "ZTelec": 0.944},
    {"temperature_K": 500, "ZTelec": 0.930},
    {"temperature_K": 600, "ZTelec": 0.913},
    {"temperature_K": 700, "ZTelec": 0.889},
    {"temperature_K": 800, "ZTelec": 0.876},
    {"temperature_K": 900, "ZTelec": 0.865},
    {"temperature_K": 1000, "ZTelec": 0.854}
  ]
}
with open("/app/outputs/hybrid_zt.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: layered_cspbi3_zt.json ===
python3 -c '
import json
data = {
  "monolayer": {"ZTelec_max": 1.6, "temperature_K": 650},
  "bilayer": {"ZTelec_max": 1.6, "temperature_K": 200},
  "three-layer": {"ZTelec_max": 2.5, "temperature_K": 150},
  "four-layer": {"ZTelec_max": 2.49, "temperature_K": 150}
}
with open("/app/outputs/layered_cspbi3_zt.json", "w") as f:
    json.dump(data, f, indent=2)
'
