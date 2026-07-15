#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: critical_coefficients.json ===
python3 << 'EOF'
import json

data = {
    "203136": {"coefficient": 920.0, "critical_sigma_23_MPa": 368.0},
    "1511": {"coefficient": 1080.0, "critical_sigma_23_MPa": 540.0},
    "001": {"coefficient": 1731.707, "critical_sigma_23_MPa": 710.0},
    "S_prime_2321": -0.0202,
    "S_prime_2323": 0.0357
}

with open("/app/outputs/critical_coefficients.json", "w") as f:
    json.dump(data, f, indent=2)
EOF
