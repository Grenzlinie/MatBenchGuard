#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json, math
A = 5.860e-4
B = 1.293e-4
temps = [100, 200, 300, 400]
result = {'A': A, 'B': B}
for T in temps:
    result[f'DeltaEg_{T}K'] = A*T - B*T*math.log(T)
with open('/app/outputs/results.json', 'w') as f:
    json.dump(result, f, indent=2)
"
