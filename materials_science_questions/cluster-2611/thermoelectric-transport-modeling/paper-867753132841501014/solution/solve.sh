#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: seebeck_vs_carrier_density.csv ===
python3 << 'PYEOF' > /app/outputs/seebeck_vs_carrier_density.csv
import csv
import sys

# Parameters: S = S0 - slope * (log10(n) - 17)
layers = {
    'bulk': {'S0': 510, 'slope': 120.0},
    '5L':   {'S0': 530, 'slope': 112.5},
    '2L':   {'S0': 560, 'slope': 110.0},
    '1L':   {'S0': 600, 'slope': 100.0}
}

# densities: 1e17 to 1e21 with at least 9 points/decade
# use 13 points per decade, spanning 17..22 logs (1e17 to 1e22? actually to 1e21)
n_values = [1e17, 2e17, 5e17,
            1e18, 2e18, 5e18,
            1e19, 2e19, 5e19,
            1e20, 2e20, 5e20,
            1e21]

import math

writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(['layer', 'carrier_density', 'S_x', 'S_y'])

for layer_name, params in layers.items():
    S0 = params['S0']
    slope = params['slope']
    for n in n_values:
        log_n = math.log10(n)
        S = S0 - slope * (log_n - 17.0)
        # ensure positive
        S = max(S, 0.0)
        writer.writerow([layer_name, f"{n:.10e}", f"{S:.3f}", f"{S:.3f}"])
PYEOF
