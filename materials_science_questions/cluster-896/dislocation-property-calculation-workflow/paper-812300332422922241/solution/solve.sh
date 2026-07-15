#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
# --- results.json ---
cat <<'PYEOF' > /tmp/compute.py
import math, json
mu = 1.0e10
b = 4.0e-10
r0 = 1.0e-9
r1 = 5.0e-6
A = b / (math.pi * (r1**2 + r0**2))
r_prime = math.sqrt(b / (2 * math.pi * A))   # mu cancels in the equality
R = r_prime / math.cos(math.pi / 4)        # since cos45° = 1/√2, R = r' * √2 ≈ r1
result = {
    "A_constant": A,
    "r_prime": r_prime,
    "domain_half_width_R": R,
    "favored_domain_type": "60°"
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF
python3 /tmp/compute.py
