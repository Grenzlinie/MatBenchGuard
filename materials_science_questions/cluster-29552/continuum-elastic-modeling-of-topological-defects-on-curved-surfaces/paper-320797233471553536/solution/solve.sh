#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: deltaW_values.tsv ===
cat > /tmp/generate.py <<'PYEOF'
import math

xi_start = 0.01
xi_end = 0.99
num_xi = 100
Ns = [2, 3, 4, 5]

xi_values = [xi_start + i*(xi_end-xi_start)/(num_xi-1) for i in range(num_xi)]

with open("/app/outputs/deltaW_values.tsv", "w") as f:
    f.write("xi\tN\tdeltaW\n")
    for N in Ns:
        for xi in xi_values:
            s = 0.0
            for m in range(1, N):
                Upsilon = 4 * xi**2 * (math.sin(math.pi * m / N)**2) / ((1 - xi**2)**2)
                s += Upsilon * math.log(1 + 1/Upsilon)
            deltaW = xi**4 - 4 * xi**2 * math.log(xi) - 1 - (1 - xi**2)**2 * (1.0/N) * s
            f.write(f"{xi:.10f}\t{N}\t{deltaW:.10f}\n")
PYEOF
python3 /tmp/generate.py
rm /tmp/generate.py
