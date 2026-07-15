#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: diffusion_distance.json ===
python3 << 'PYEOF'
import math, json
D = 4.3e-17  # cm^2/s
tau_hours = 200
tau_s = tau_hours * 3600
X2 = 2 * D * tau_s  # cm^2
X_cm = math.sqrt(X2)  # cm
X_μm = X_cm * 1e4  # 1 cm = 10^4 μm
less_than_L = X_μm < 0.3
result = {"X_μm": X_μm, "less_than_L": less_than_L}
with open("/app/outputs/diffusion_distance.json", "w") as f:
    json.dump(result, f, indent=2)
print("Done. X_μm =", X_μm, "less_than_L =", less_than_L)
PYEOF
