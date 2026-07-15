#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mixing_densification_results.json ===
cat > /tmp/make_json.py << 'EOF'
import json
data = {
    "unregistered_low_barrier": [
        {"time_ps": 0.1, "m_percent": 1.0, "rho": 0.9},
        {"time_ps": 2.0, "m_percent": 3.0, "rho": 1.7},
        {"time_ps": 6.0, "m_percent": 4.5, "rho": 1.8},
        {"time_ps": 12.0, "m_percent": 4.0, "rho": 1.5}
    ],
    "registered_low_barrier": [
        {"time_ps": 0.1, "m_percent": 10.0, "rho": 0.9},
        {"time_ps": 2.0, "m_percent": 13.0, "rho": 1.2},
        {"time_ps": 6.0, "m_percent": 14.5, "rho": 1.4},
        {"time_ps": 12.0, "m_percent": 15.0, "rho": 1.2}
    ]
}
with open("/app/outputs/mixing_densification_results.json", "w") as f:
    json.dump(data, f, indent=2)
EOF
python3 /tmp/make_json.py
rm /tmp/make_json.py
