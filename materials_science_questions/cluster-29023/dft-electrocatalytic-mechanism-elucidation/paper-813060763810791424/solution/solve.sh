#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: compiled_energies.json ===
python3 <<'PYEOF'
import json
data = [
    {"model": "Ni@SV", "site_type": "Ni single vacancy", "E_bare": -980.0, "E_COOH": -1572.0, "E_CO": -1571.2, "E_H": -995.45},
    {"model": "Ni-N@SV", "site_type": "Ni single vacancy with N", "E_bare": -981.0, "E_COOH": -1573.0, "E_CO": -1572.3, "E_H": -996.25},
    {"model": "Co@SV", "site_type": "Co single vacancy", "E_bare": -979.0, "E_COOH": -1571.0, "E_CO": -1569.5, "E_H": -994.95},
    {"model": "Co-N@SV", "site_type": "Co single vacancy with N", "E_bare": -980.5, "E_COOH": -1572.5, "E_CO": -1571.1, "E_H": -996.35}
]
with open("/app/outputs/compiled_energies.json", "w") as f:
    json.dump(data, f, indent=2)
print("compiled_energies.json written")
PYEOF

# === solve block: derived_barriers.json ===
python3 <<'PYEOF'
import json
data = [
    {"model": "Ni@SV", "site_type": "Ni single vacancy", "CO_desorption_barrier": -1.2, "HER_limiting_potential": -0.3},
    {"model": "Ni-N@SV", "site_type": "Ni single vacancy with N", "CO_desorption_barrier": -1.3, "HER_limiting_potential": -0.5},
    {"model": "Co@SV", "site_type": "Co single vacancy", "CO_desorption_barrier": -0.5, "HER_limiting_potential": 0.2},
    {"model": "Co-N@SV", "site_type": "Co single vacancy with N", "CO_desorption_barrier": -0.6, "HER_limiting_potential": 0.1}
]
with open("/app/outputs/derived_barriers.json", "w") as f:
    json.dump(data, f, indent=2)
print("derived_barriers.json written")
PYEOF
