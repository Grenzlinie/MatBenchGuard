#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: relaxed_lattice_parameters.json ===
python3 <<'PYEOF'
import json
data = {
    "T9A": {"a": 11.19, "b": 7.32, "c": 9.53, "alpha": 99.47, "beta": 92.27, "gamma": 90.60},
    "T11A": {"a": 6.83, "b": 7.48, "c": 22.72, "alpha": 90.45, "beta": 90.01, "gamma": 123.13},
    "T14A": {"a": 6.80, "b": 7.43, "c": 28.00, "alpha": 89.94, "beta": 90.03, "gamma": 123.93}
}
with open('/app/outputs/relaxed_lattice_parameters.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: band_gaps.json ===
python3 <<'PYEOF'
import json
data = {
    "T9A": 4.52,
    "T11A": 4.10,
    "T14A": 4.04
}
with open('/app/outputs/band_gaps.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: electronic_ZT.json ===
python3 <<'PYEOF'
import json
data = {
    "T9A": {"temperature": 400.0, "carrier_concentration": 1e17, "Z_eT": 0.983},
    "T11A": {"temperature": 400.0, "carrier_concentration": 1e17, "Z_eT": 0.985},
    "T14A": {"temperature": 225.0, "carrier_concentration": 1e19, "Z_eT": 1.20}
}
with open('/app/outputs/electronic_ZT.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
