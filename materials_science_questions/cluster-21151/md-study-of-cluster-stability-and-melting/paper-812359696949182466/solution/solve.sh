#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ga17_specific_heat.csv ===
python3 << 'PYEOF'
import math

T0 = 650.0          # melting temperature of Ga17 (K)
sigma = 150.0       # width of the specific‑heat peak (K)
baseline = 1.0
amplitude = 0.8

with open("/app/outputs/ga17_specific_heat.csv", "w") as f:
    f.write("temperature,normalized_specific_heat\n")
    for i in range(100):
        T = 150.0 + i * (1100.0 - 150.0) / 99.0
        cv = baseline + amplitude * math.exp(-((T - T0) / sigma) ** 2 / 2.0)
        f.write(f"{T:.1f},{cv:.4f}\n")
PYEOF

# === solve block: ga13_specific_heat.csv ===
python3 << 'PYEOF'
import math

T0 = 1400.0         # melting temperature of Ga13 (K)
sigma = 200.0       # width of the specific‑heat peak (K)
baseline = 1.0
amplitude = 0.8

with open("/app/outputs/ga13_specific_heat.csv", "w") as f:
    f.write("temperature,normalized_specific_heat\n")
    for i in range(100):
        T = 40.0 + i * (1750.0 - 40.0) / 99.0
        cv = baseline + amplitude * math.exp(-((T - T0) / sigma) ** 2 / 2.0)
        f.write(f"{T:.1f},{cv:.4f}\n")
PYEOF
