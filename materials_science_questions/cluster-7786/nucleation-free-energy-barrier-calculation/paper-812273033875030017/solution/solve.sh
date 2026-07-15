#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: nucleation_barriers.json ===
python3 <<'PYEOF'
import json
data = [
  {"nucleus_type": "circular_{111}", "barrier_formula": "2*sqrt(3)*pi*phi^2/Delta_mu_a", "percentage": 100},
  {"nucleus_type": "circular_{100}", "barrier_formula": "pi*phi^2/Delta_mu_a", "percentage": 29},
  {"nucleus_type": "elliptical_trough", "barrier_formula": "(4*sqrt(3)*pi/3-3)*phi^2/Delta_mu_a", "percentage": 39},
  {"nucleus_type": "semicircular_trough", "barrier_formula": "sqrt(3)*pi*phi^2/Delta_mu_a", "percentage": 50},
  {"nucleus_type": "layer_advance_ridge", "barrier_formula": "sqrt(3)*pi*phi^2/Delta_mu_a", "percentage": 50}
]
with open("/app/outputs/nucleation_barriers.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
